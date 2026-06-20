"""Utilities for piping CrewAI's verbose output into the Streamlit UI.

✅ PROVIDED — you don't need to edit this file.
"""
from __future__ import annotations

import io
import sys
import threading
from contextlib import contextmanager


class StreamCapture(io.TextIOBase):
    """A file-like object that mirrors writes to the original stream and a buffer.

    CrewAI prints its agent reasoning to stdout when `verbose=True`. We capture
    that stream so the Streamlit app can render it live, while still letting it
    flow to the terminal for debugging.
    """

    def __init__(self, original):
        self._original = original
        self._buffer: list[str] = []
        self._lock = threading.Lock()
        self._listeners: list = []

    def write(self, s) -> int:  # type: ignore[override]
        if not s:
            return 0
        if isinstance(s, bytes):
            try:
                s = s.decode("utf-8", errors="replace")
            except Exception:
                s = repr(s)
        if not isinstance(s, str):
            s = str(s)
        with self._lock:
            self._buffer.append(s)
            for cb in list(self._listeners):
                try:
                    cb(s)
                except Exception:
                    pass
        try:
            return self._original.write(s)
        except Exception:
            return len(s)

    def flush(self):  # type: ignore[override]
        try:
            self._original.flush()
        except Exception:
            pass

    def getvalue(self) -> str:
        with self._lock:
            return "".join(self._buffer)

    def subscribe(self, callback) -> None:
        with self._lock:
            self._listeners.append(callback)


@contextmanager
def capture_stdout_stderr():
    """Context manager that captures stdout & stderr into a single StreamCapture."""
    cap = StreamCapture(sys.__stdout__)
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout = cap
    sys.stderr = cap
    try:
        yield cap
    finally:
        sys.stdout = old_out
        sys.stderr = old_err


def make_step_callback(on_step):
    """Wrap a UI updater so CrewAI's step_callback can call it safely."""

    def _cb(step):
        try:
            on_step(step)
        except Exception:
            pass

    return _cb
