=================================================================
sniffio: Sniff out which async library your code is running under
=================================================================

You're writing a library. You've decided to be ambitious, and support
multiple async I/O packages, like [Trio](https://trio.readthedocs.io),
and [asyncio](https://docs.python.org/3/library/asyncio.html), and ...
You've written a bunch of clever code to handle all the differences.
But... how do you know *which* piece of clever code to run?

This is a tiny package whose only purpose is to let you detect which
async library your code is running under.

* Documentation: https://sniffio.readthedocs.io

* Bug tracker and source code: https://github.com/python-trio/sniffio

* License: MIT or Apache License 2.0, your choice

* Contributor guide: https://trio.readthedocs.io/en/latest/contributing.html

* Code of conduct: Contributors are requested to follow our `code of
  conduct
  <https://trio.readthedocs.io/en/latest/code-of-conduct.html>`_
  in all project spaces.

This library is maintained by the Trio project, as a service to the
async Python community as a whole.


Quickstart
----------

.. code-block:: python3

   from sniffio import current_async_library
   import trio
   import asyncio

   async def print_library():
       library = current_async_library()
       print("This is:", library)

   # Prints "This is trio"
   trio.run(print_library)

   # Prints "This is asyncio"
   asyncio.run(print_library())

For more details, including how to add support to new async libraries,
`please peruse our find manual <https://sniffio.readthedocs.io>`__.
