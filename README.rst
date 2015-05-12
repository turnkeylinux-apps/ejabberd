ejabberd - XMPP and Web Chat
============================

An instant messaging server that combines `ejabberd`_ with `Speeqe`_ to
create a live chat server that supports strong encryption and works with
any web browser or dedicated XMPP client (e.g., Pidgin). ejabberd is a
powerful XMPP server that supports clustering, live upgrades, shared
roster groups and provides support for virtual hosts.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- ejabberd (chat server) configurations:
   
   - Installed from package management.
   - Includes custom ejabberd-config script to change domain and set
     admin password (configured on first boot).
   - Enabled in-band user registration (usability, convenience).
   - Enabled legacy SSL connection method (still required by some
     clients).
   - Set erlang node: ejabberd@localhost (workaround mnesia hostname
     changes).
   - Binded admin console to port 12322 - uses SSL.

- Speeqe (web chat application) configurations:
   
   - Installed from upstream source code to /var/www/django/speeqeweb
   - Installed and configured to provide web chat interface.
   - Configured ejabberd with anonymous access for speeqe to connect.
   - Created ejabberd robot XMPP user for speeqe to list active rooms.
   - Includes local JQuery library (internal deployment).

- SSL support out of the box.
- Postfix MTA (bound to localhost) to allow sending of email from
  speeqe.
- Webmin modules for configuring Apache2 and Postfix.

- Includes custom ejabberd-config script to change domain,
  administrative password and regenerate related secrets::

    /usr/lib/inithooks/bin/ejabberd.sh XMPP_DOMAIN ADMIN_PASS
    # ejabberd admin interface user will be: admin@XMPP_DOMAIN

- XMPP DNS records example::

    _jabber._tcp.example.com.      0 5269 example.com.    SRV
    _xmpp-client._tcp.example.com. 0 5222 example.com.    SRV
    _xmpp-server._tcp.example.com. 0 5269 example.com.    SRV

- Example hosts file when testing in demo mode::

    /etc/hosts : appliance_ip example.com

- Recommended XMPP chat clients:
   
   - `Gajim`_ - a full featured and easy to use Jabber client
   - `Pidgin`_ - the universal chat client
      
      - Add XMPP account
         
         - username: newuser
         - domain: example.com
         - resource: Pidgin
         - password: \*\*\*\*\*\*\*
         - [v] create this account on server


Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, Webshell, SSH: username **root**
-  ejabberd:
   
   - Admin interface: username **admin@example.com**
   - Regular login: username **admin**
   - robot user is configured with a random password and regenerated as
     part of secrets regeneration.


.. _ejabberd: http://www.ejabberd.im
.. _Speeqe: https://github.com/thepug/speeqe/wiki
.. _TurnKey Core: http://www.turnkeylinux.org/core
.. _Gajim: http://www.gajim.org/
.. _Pidgin: http://www.pidgin.im/
