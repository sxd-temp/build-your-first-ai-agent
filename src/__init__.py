"""Source package for the Startup Idea Validator workshop project.

It also holds the small guards that PAUSE the app until you finish each lab.

✅ PROVIDED — you don't edit this file.

The guards stop the app with a clear, friendly message whenever a lab's TODO is
still unfinished, so you always know exactly what to fill in next (and where).
The moment you replace a TODO with your own text, the guard steps aside and the
app runs.
"""
from __future__ import annotations


class LabTODO(Exception):
    """Raised when a lab exercise still has an unfinished TODO.

    The Streamlit apps catch this and show your message as a gentle prompt
    instead of a scary red traceback.
    """


def todo_guard(*values: object, message: str) -> None:
    """Stop the app if any value still contains the placeholder word ``TODO``.

    Pass in the strings you're supposed to fill in (e.g. role / goal / backstory).
    As soon as none of them say ``TODO`` anymore, this does nothing.
    """
    if any("TODO" in str(v) for v in values):
        raise LabTODO(message)


def fan_in_guard(context_tasks: list, *, message: str) -> list:
    """Stop the app until the memo task is given its fan-in context.

    Returns the list unchanged once it's non-empty, so you can use it inline.
    """
    if not context_tasks:
        raise LabTODO(message)
    return context_tasks
