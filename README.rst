Nanas!!
=======

This is an online version of a game I play a lot at home.

Cluster Design
--------------

The server is made up of a couple components.

 1. **redis** holds any and all state the application needs.
 1. **engine** is a `Tornado <http://www.tornadoweb.org/en/stable/>`_ application that handles nearly all of the actual game logic. Clients connect directly to it via WebSockets.

The pages served to the client are all static and can therefore be served with any web server (my preference is `Nginx <http://wiki.nginx.org/Main>`_).


Licensing
---------

This is `Free Software <http://www.gnu.org/philosophy/free-sw.html>`_ published under the `AGPLv3 <http://www.gnu.org/licenses/agpl-3.0.html>`_.
