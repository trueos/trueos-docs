.. index:: pico
.. _trueos pico:

|trueos| Pico
*************

|trueos| Pico is an initiative to connect multiple small ARM device
thin clients to a single |trueos| system. Similar to the |sysadm|
project, Pico utilizes two primary pieces of software: Pico Server and
Pico Client.

The goal for the |trueos| Pico is to provide a low-cost solution for
users who wish to have a central server provide resources to multiple
low-cost, low-power systems. In effect, Pico allows one system to
provide all the processing power and graphical "muscle" for as many
computers the user wishes to add on the network. For example, three or
four users can log into their thin clients and open utilities, browse
the Internet, or even play games while one central server dynamically
provides the needed resources for each of these tasks.

Pico Server is available both
`online <https://www.trueos.org/downloads/>`_ and in |appcafe|. The
Server software will need to be configured before downloading the client
software or initializing the Pico client device.

Pico Client is available to download from the |trueos|
`download page <https://www.trueos.org/downloads>`_. A separate computer
will be required to unpack and transfer the :file:`.img` file to a
microSD card for insertion into the thin client device.

Currently, the Pico software is functional for |trueos| and the
Raspberry Pi 2 model B v1.1. The bulk of development efforts are being
directed toward ensuring graphics and sound functionality. Future
development goals include supporting a wider variety of ARM Devices
and building the server software to be cross-platform.

.. _picoinit:

Pico Initialization
===================

To create a Pico network, several elements will be required:

* A |trueos| system with both an internet and local network connection
  to download the necessary files and be used as the Pico server. It is
  recommended this system have strong hardware to provide the smoothest
  experience for each connected client.

.. tip:: For best performance, it is recommended to have wired
   network connections from the Pico server to all connected clients.

* An ARM device to act as the thin client (as many as the user wants or
  the server can support). Currently, only the Raspberry Pi 2 model B
  v1.1 is supported.
* A microSD card for each thin client.

.. note:: Using a microSD card larger than 4 GB in size is largely
   unnecessary, as the server will store almost all created data.

* Adapter or connector for microSD cards to connect to the Pico server
  (Ex. a USB to microSD card reader).
  
Each thin client will need:

* HDMI monitor. Currently, 1920x1080 is the maximum supported
  resolution and the monitor should have integrated speakers for audio
  to function properly.
* Network cable.
* USB Mouse.
* USB Keyboard.
* Power Adapter.

Once all these components are assembled, it's time to configure the Pico
Server.

.. _picoserver:

Pico Server
===========

Installing and configuring a Pico server is done via the command prompt,
with superuser permissions (:command:`su` or
:command:`sudo <rest of command>`).
Begin opening a terminal and downloading the Pico Server package with
:command:`sudo pkg install picoserver` (also available in |appcafe|).
Next, enable the Pico server using
:command:`sysrc -f /etc/rc.conf picoserver_enable=yes`. Finally,
the Pico server is started with :command:`service picoserver start`.

Once the Pico server is started, a new :file:`picoserver.ini` file will
be created on the system, found in :file:`usr/local/etc`. This
:file:`.ini` file holds the initialization settings for the Pico server
and has three sections, seen in :numref:`Table %s <inisett>`. The table
will expand as additional elements are added to :file:`picoserver.ini`.

.. _inisett:

.. table:: : Pico Server Initialization Settings

   +-------------------+----------------+------------------+
   | SSH               | Video          | Audio            |
   +===================+================+==================+
   | cipher            | enablevgl=true | enablesound=true |
   +-------------------+----------------+------------------+
   | compression=<1-9> |                |                  |
   +-------------------+----------------+------------------+

The *compression* setting can be any number from 1 to 9. The default
setting is recommended as turning up the compression can introduce
performance issues on the clients.

Pico uses *Virtual GL* (vgl) for graphics hardware acceleration. VGL
will work with any *OpenGL* supported graphics card, but Nvidia cards
are generally recommended at this time.

.. warning:: Turning on VGL may introduce security vulnerabilities on a
   network with untrusted clients.

If the server does not support video acceleration or you wish to avoid
any security vulnerabilities on the Pico network, edit
:file:`picoserver.ini` and change :command:`enablevgl=` to **false**.

Currently, audio only functions over the HDMI connection port on the
Raspberry Pi, meaning audio will only work on monitors with built-in
audio capabilities. Change **true** to **false** to disable all audio.

Once satisfied with the settings in :file:`picoserver.ini`, new user
accounts/logins need to be created for the client systems. See
:ref:`User Manager` for detailed instructions on creating new users on
a |trueos| system.

After any new accounts are created, it is time to initialize the client.

.. _startpicoclient:

Starting the Pico Client
========================

The process of initializing a Pico Client begins on a separate |trueos|
system. On this system, navigate to the |trueos| website's
`download page <https://www.trueos.org/downloads>`_ and download the
latest :file:`<pico>.img.xz` file. This file is compressed with **xz**
and will need to be decompressed prior to burning the file to a microSD
card. Open a terminal and navigate to the file's location to use
:command:`unxz` to unpack the file:

.. code-block:: none

 [tmoore@Observer] ~% cd Downloads/
 [tmoore@Observer] ~/Downloads% unxz TrueOS-pico-rpi2-2016-10-29.img.xz

Please be patient as it may take a few moments for the system to
decompress the file.

Once the file is decompressed to a :file:`.img` file, insert a microSD
card into the system. An adapter may be necessary if the system
has no microSD card slots. As the superuser, use the :command:`dd`
command line utility to write the :file:`.img` file to the card:

.. code-block:: none

 [tmoore@Observer] ~/Downloads% dd if=TrueOS-pico-rpi2-2016-10-29.img of=/dev/da0 bs=4m
 512+0 records in
 512+0 records out
 2147483648 bytes transferred in 426.140554 secs (5039379 bytes/sec)

Again, please be patient as this command may take some time to process.

.. warning:: Be sure the :command:`dd if=` command points to right
   storage device if there are multiple storage devices inserted in the
   system. In the example above, the microSD card is connected to a USB
   adapter (da0) attached to the system.

Now the :file:`.img` file is written to the microSD card; it is time
to connect the Pico client to the Pico server:

* Insert the microSD card into the thin client.
* Attach the network cable. Be sure the client is wired into the same
  network as the Pico Server.
* Plug in the USB Mouse and Keyboard.
* Attach the monitor's HDMI cable.
* Plug in the ARM device's power cable. This should always be the **last** step.

Inserting the power cable will generally turn on the client device. The
Pico client then searches for and connects to any Pico Server on the
network, bringing the user to the |trueos| login screen. The Pico client
should now be fully configured and ready to use.

.. _usepicoclient:

Using the Pico Client
=====================

There are a few differences in |trueos| when using a Pico client.

If the server uses the |lumina| Desktop Environment, hovering over the
:guilabel:`Network Status Icon` in the System Tray displays the client's
IP address, the server's IP address, and the client's unique
:command:`pico_auth` number, seen in :numref:`Image %s <piip>`. This is
intended to efficiently provide relevant network information for
simplified server administration.

.. _piip:

.. figure:: images/picoip.png

    : Pico Client IP display

When logging out with the Pico client, several processes are begun. The
client clears the session, then completely restarts the discovery and
connection processes. The server will destroy the previous user's
:file:`temp` file, along with the previously assigned **pico_auth #**.
These processes prepare the server for a brand new connection and user
login from the same Pico client.

.. _vglaccel:

VGL Graphics Acceleration
-------------------------

VirtualGL (VGL) is the toolkit used by the |trueos| Pico to provide 3D
hardware acceleration to the Pico Clients. VGL redirects OpenGL commands
and data to the GPU in the Pico Server, then pulls back the rendered 3D
images to the client. For further information about this open-source
project, please refer to the `VirtualGL website <virtualgl.org>`_

VirtualGL also has a fully featured
`user guide <http://www.virtualgl.org/Documentation/Documentation>`_ to
help guide new users through the various features of this useful toolkit.

On a Pico client, test VGL functionality by opening the command line
and typing :command:`/usr/local/VirtualGL/bin/vglrun glxgears`. A
window will popup, displaying several moving gears, as seen in
:numref:`Image %s <vgltest>`. The terminal will also display the framerate
of the gears, updating periodically.

.. _vgltest:

.. figure:: images/picovglgears.png

    : VirtualGL Gears Test

.. _pulseaud:

Pulse Audio
-----------

`Pulse Audio <https://www.freedesktop.org/wiki/Software/PulseAudio>`_
is the preferred audio solution for Pico clients. Pulse Audio allows
Pico clients play audio sent from the server. The Pulse Audio user
`documentation <https://www.freedesktop.org/wiki/Software/PulseAudio/Documentation/User/>`_
provides a wealth of information on configuring Pulse Audio, including
streaming audio over the network. Advanced controls for Pulse Audio are
available in |appcafe| with the :command:`pavucontrol` multimedia
application.
   
.. _Pico Server Administration:

Pico Server Administration
==========================

Once the Pico server and clients are installed and ready to use, there
are a number of administrative commands available to use, seen in
:numref:`Table %s <picoadmin>`. This table will expand as new commands
are added:

.. _picoadmin:

.. Table:: : Pico Server Administration Commands

   +---------------------+-------------------------------------------+
   | Command             | Description                               |
   +=====================+===========================================+
   | pico-server         | Primary Pico command. All commands begin  |
   |                     | with :command:`pico-server` and a space.  |
   +---------------------+-------------------------------------------+
   | -list               | Displays all connected clients, as either |
   |                     | "pico_auth <#>" or the specific logins    |
   |                     | ("testuser_pico")                         |
   +---------------------+-------------------------------------------+
   | -kill pico_auth <#> | Immediately reboots the specified client. |
   +---------------------+-------------------------------------------+

.. _Pico Current Issues:

Pico Current Issues
===================

This section lists the currently known bugs with Pico use:

* **Audio:** Pulse Audio has a random issue with freezing upon
  *client* initialization. A bugfix is forthcoming.
