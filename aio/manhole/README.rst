aio.web.server usage
--------------------


Configuration
-------------

Lets create a manhole configuration
  
>>> config = """
... [aio]
... log_level = ERROR
... 
... [server/server_name]
... factory = aio.manhole.factory
... port = 7373
... 
... """  

>>> import sys
>>> import io
>>> import aiomanhole

>>> import aio.testing
>>> import aio.app
>>> from aio.app.runner import runner

When we run the manhole server, its accessible as "server_name" from aio.app.servers

>>> @aio.testing.run_forever(sleep=1)
... def run_manhole_server(config):
...     yield from runner(['run'], config_string=config)
... 
...     def call_manhole():
...         print(aio.app.servers["server_name"])
...         aio.app.clear()
...          
...     return call_manhole

>>> run_manhole_server(config)
<Server sockets=[<socket.socket ...laddr=('0.0.0.0', 7373)...>

Lets try calling the manhole server

>>> import asyncio
>>> import telnetlib3

>>> @aio.testing.run_forever(sleep=1)
... def run_manhole_server(config):
...     yield from runner(['run'], config_string=config)
...     
...     class TestTelnetClient(telnetlib3.TelnetClient):
... 
...         def data_received(self, data):
...             print(data)
... 
...     def call_manhole():
...         loop = asyncio.get_event_loop()
...         transport, protocol = yield from loop.create_connection(
...             TestTelnetClient, "127.0.0.1", 7373)
...         aio.app.clear()
...          
...     return call_manhole

>>> run_manhole_server(config)
b'hello...\n>>> '
