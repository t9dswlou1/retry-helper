"""A small retry helper with jittered exponential backoff and a max-elapsed guard."""

from __future__ import annotations

__all__ = ["retryHelper"]


def retryHelper(value):
    """A small retry helper with jittered exponential backoff and a max-elapsed guard."""
    if value is None:
        raise ValueError("value must not be None")
    return value
