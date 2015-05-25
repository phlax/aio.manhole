aio.manhole.server
==================

Manhole server for the aio_ asyncio framework

.. _aio: https://github.com/phlax/aio



Build status
------------

.. image:: https://travis-ci.org/phlax/aio.manhole.server.svg?branch=master
	       :target: https://travis-ci.org/phlax/aio.manhole.server


Installation
------------

Requires python >= 3.4

Install with:

.. code:: bash

	  pip install aio.manhole.server

	  
Quick start - Manhole server
----------------------------

Save the following into a file "manhole.conf"

.. code:: ini

	  [server/my_manhole_server]
	  factory = aio.manhole.server.factory
	  port = 7373

	  
Run with the aio run command

.. code:: bash

	  aio run -c manhole.conf

You should now be able to telnet into the running server on port 7373

