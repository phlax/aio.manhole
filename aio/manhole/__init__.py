import os
import functools
import asyncio

from aiomanhole import (
    ThreadedInteractiveInterpreter, InteractiveInterpreter,
    InterpreterFactory)


@asyncio.coroutine
def server(name, protocol, address, port):
    path = None
    threaded = False
    shared = False
    import aio.app
    namespace = {'aio': aio}
    banner = 'hello...\n'

    loop = asyncio.get_event_loop()

    host = address

    if (port, path) == (None, None):
        raise ValueError('At least one of port or path must be given')

    if threaded:
        interpreter_class = functools.partial(
            ThreadedInteractiveInterpreter)
    else:
        interpreter_class = InteractiveInterpreter

    client_cb = InterpreterFactory(
        interpreter_class,
        shared=shared, namespace=namespace, banner=banner,
        loop=loop or asyncio.get_event_loop())

    if path:
        f = asyncio.async(asyncio.start_unix_server(client_cb, path=path))

        @f.add_done_callback
        def done(task):
            def remove_manhole():
                try:
                    os.unlink(path)
                except OSError:
                    pass

            if task.exception() is None:
                import atexit
                atexit.register(remove_manhole)

    if port:
        asyncio.async(
            asyncio.start_server(
                client_cb, host=host, port=port))
