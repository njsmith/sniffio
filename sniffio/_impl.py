from contextvars import ContextVar
import sys

current_async_library_cvar = ContextVar(
    "current_async_library_cvar", default=None
)


class AsyncLibraryNotFoundError(RuntimeError):
    pass


def current_async_library():
    """Detect which async library is currently running.

    The following libraries are currently supported:

    * Trio (``"trio"``)
    * asyncio (``"asyncio"``)

    Returns:
      A string like ``"trio"``.

    Raises:
      AsyncLibraryNotFoundError: if called in synchronous context, or if the
        current async library was not recognized.

    Examples:

        .. code-block:: python3

           from sniffio import current_async_library

           async def generic_sleep(seconds):
               library = current_async_library()
               if library == "trio":
                   await trio.sleep(seconds)
               elif library == "asyncio":
                   await asyncio.sleep(seconds)
               # ... and so on ...
               else:
                   raise RuntimeError(f"Unsupported library {library!r}")

    """
    value = current_async_library_cvar.get()
    if value is not None:
        return value
    # Need to sniff for asyncio
    if "asyncio" in sys.modules:
        import asyncio
        try:
            current_task = asyncio.current_task
        except AttributeError:
            current_task = asyncio.Task.current_task
        if current_task() is not None:
            return "asyncio"
    raise AsyncLibraryNotFoundError(
        "unknown async library, or not in async context"
    )
