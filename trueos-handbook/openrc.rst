.. index:: init
.. _OpenRC:

OpenRC and |trueos|
*******************

|trueos| now uses OpenRC as an integral component of the operating
system. This is a major point of difference between |trueos| and
FreeBSD, and this section is intended to provide detailed information
about the |trueos| implementation for more advanced users.

Location of RC scripts for starting and stopping services:

* |trueos| base system new rc script location is :file:`/etc/init.d/`.

* FreeBSD base system legacy rc script location is :file:`/etc/rc.d/`.

* |trueos| ports rc script location is :file:`/usr/local/etc/init.d/`.

* FreeBSD ports rc script location is :file:`/usr/local/etc/rc.d/`.

.. warning:: The user may find leftover RC files during the |trueos|
   migration to OpenRC. These files do not work with OpenRC and are
   intended to be removed both from the source tree and via
   :command:`pc-updatemanager` when all functionality is successfully
   migrated. If discovered, **do not** attempt to use these leftover
   files.

.. index:: init, bootservices
.. _Managing Bootup Services:

Managing Bootup Services
========================
   
OpenRC has a variety of options to *start*, *stop*, *add*, or *remove*
services from bootup, seen in :numref:`Table %s <rcbootserv>`. Most of
these actions can be accomplished using the :ref:`Service Manager` built
into |sysadm|. Individuals familiar with the FreeBSD :command:`service`
command may notice some similarities between some of these commands:

.. _rcbootserv:

.. table:: : Bootup Service Commands

   +--------------------------------+------------------------------------------------------------+
   | Command                        | Description                                                |
   +================================+============================================================+
   | service nginx start            | Start nginx from :file:`usr/local/etc/init.d/nginx`.       |
   +--------------------------------+------------------------------------------------------------+
   | service nginx restart          | Restart nginx from :file:`/usr/local/etc/init.d/nginx`.    |
   +--------------------------------+------------------------------------------------------------+
   | service nginx stop             | Stop nginx from :file:`/usr/local/etc/init.d/nginx`.       |
   +--------------------------------+------------------------------------------------------------+
   | service nginx status           | View the status of the nginx service.                      |
   +--------------------------------+------------------------------------------------------------+
   | rc-status                      | View the status of all running services.                   |
   +--------------------------------+------------------------------------------------------------+
   | rc-update                      | Views all runlevels. Used in conjunction with service      |
   |                                | names to add or remove services from the default runlevel. |
   +--------------------------------+------------------------------------------------------------+
   | rc-update add nginx default    | Adds the nginx service to the default runlevel.            |
   +--------------------------------+------------------------------------------------------------+
   | rc-update remove nginx default | Removes the nginx service from the default runlevel.       |
   +--------------------------------+------------------------------------------------------------+

:command:`rc-update` displays all runlevels. The full list of available
runlevels is seen here in :numref:`Table %s <rcuprnlvl>`

.. _rcuprnlvl:

.. table:: : Services and runlevels

   +-------------+-------------------+
   | Service     | Runlevel          |
   +=============+===================+
   | abi         | boot              |
   +-------------+-------------------+
   | adjkerntz   | boot              |
   +-------------+-------------------+
   | automount   | default           |
   +-------------+-------------------+
   | bootmisc    | boot              |
   +-------------+-------------------+
   | bridge      | boot              |
   +-------------+-------------------+
   | cron        | boot              |
   +-------------+-------------------+
   | cupsd       | default           |
   +-------------+-------------------+
   | dbus        | default           |
   +-------------+-------------------+
   | devd        | boot              |
   +-------------+-------------------+
   | dumpon      | boot              |
   +-------------+-------------------+
   | fsck        | boot              |
   +-------------+-------------------+
   | hostid      | boot              |
   +-------------+-------------------+
   | hostname    | boot              |
   +-------------+-------------------+
   | ipfw        | boot              |
   +-------------+-------------------+
   | local       | default nonetwork |
   +-------------+-------------------+
   | localmount  | boot              |
   +-------------+-------------------+
   | lockd       | default           |
   +-------------+-------------------+
   | loopback    | boot              |
   +-------------+-------------------+
   | modules     | boot              |
   +-------------+-------------------+
   | motd        | boot              |
   +-------------+-------------------+
   | moused      | default           |
   +-------------+-------------------+
   | netmount    | default           |
   +-------------+-------------------+
   | network     | boot              |
   +-------------+-------------------+
   | newsyslog   | boot              |
   +-------------+-------------------+
   | openntpd    | default           |
   +-------------+-------------------+
   | pcdm        | default           |
   +-------------+-------------------+
   | root        | boot              |
   +-------------+-------------------+
   | rpcbind     | default           |
   +-------------+-------------------+
   | savecache   | shutdown          |
   +-------------+-------------------+
   | savecore    | boot              |
   +-------------+-------------------+
   | statd       | default           |
   +-------------+-------------------+
   | staticroute | boot              |
   +-------------+-------------------+
   | swap        | boot              |
   +-------------+-------------------+
   | sysadm      | default           |
   +-------------+-------------------+
   | syscons     | boot              |
   +-------------+-------------------+
   | sysctl      | boot              |
   +-------------+-------------------+
   | syslogd     | boot              |
   +-------------+-------------------+
   | trueosinit  | default           |
   +-------------+-------------------+
   | urandom     | boot              |
   +-------------+-------------------+
   | zfs         | boot              |
   +-------------+-------------------+
   | zvol        | boot              |
   +-------------+-------------------+

OpenRC has a few ordered runlevels in |trueos|. First is the *sysinit*
runlevel which is used for OpenRC to initialize itself. Second is the
*boot* runlevel, which starts most base services from
:file:`/etc/init.d/`. Third is the *default* runlevel, which is where
services started by ports are added.

.. note:: Services added by ports cannot be added to *boot* or
   *sysinit*.

OpenRC allows users to add a service in the prefix location to the
*boot* runlevel, which happens before the :file:`/usr` filesystem is
mounted. Finally, there is a *shutdown* runlevel reserved for a few
services like :command:`savecore` or :command:`pc-updatemanager`
installing updates at shutdown.

When a service is added to a runlevel a symlink is created in
:file:`/etc/runlevels`. When a service is started, stopped, or changed
to another state a symlink is added to :file:`/libexec/rc/init.d/`, as
seen in this example:

.. code-block:: none

   [tmoore@Observer] ~% ls /libexec/rc/init.d/
   daemons exclusive inactive scheduled starting wasinactive
   depconfig failed options softlevel stopping
   deptree hotplugged prefix.lock started tmp

Also under :file:`/libexec/rc` exists a cache directory which keeps a
dependancies cache that is only updated when dependencies change.
Additionally, several directories exist for other binaries and special
binaries used by OpenRC functions.

OpenRC has a dependency based init system. As an example, let’s examine
a service which needs *network* such as SysAdm. Here are the contents of
the :file:`/usr/local/etc/init.d/sysadm` *depend* section:

.. code-block:: none

   depend() {
   need net
   after bootmisc
   keyword -shutdown
   }

We can define that SysAdm needs *network*, which is the nickname of the
:file:`/etc/init.d/network` service defined by *provide in network*. We
also see that it starts after *bootmisc*. If we don’t want restarting
*network* to restart SysAdm then we don’t need *net* for SysAdm. If we
just want SysAdm to start after network then we add *network* the actual
name of the script in *after bootmisc*.

Here are the contents of :file:`/etc/init.d/network`:

.. code-block:: none

   depend()
   {
   provide net
   need localmount
   after bootmisc modules
   keyword -jail -prefix -vserver -stop
   }

The *provide* option will set the service nickname to *net*. *Need*
indicates restarting *localmount* will restart *network*. *After*
defines that we start after *bootmisc* and *modules*. For example, the
keyword *-jail* option says this service doesn't run in a jail, prefix,
any of the other options shown.

.. index:: init, rcdefault
.. _RC Defaults:

RC Defaults
===========

|trueos| and FreeBSD now have very different rc defaults.

**TrueOS OpenRC Defaults**

The entire
`TrueOS rc.conf file <https://github.com/trueos/freebsd/blob/drm-next-4.7/etc/defaults/rc.conf>`_
is viewable on GitHub.

.. code-block:: none

   # Global OpenRC configuration settings

   # Set to "YES" if you want the rc system to try and start services
   # in parallel for a slight speed improvement. When running in parallel we
   # prefix the service output with its name as the output will get
   # jumbled up.
   # WARNING: whilst we have improved parallel, it can still potentially lock
   # the boot process. Don't file bugs about this unless you can supply
   # patches that fix it without breaking other things!
   #rc_parallel="NO"

   # Set rc_interactive to "YES" and you'll be able to press the I key during
   # boot so you can choose to start specific services. Set to "NO" to disable
   # this feature. This feature is automatically disabled if rc_parallel is
   # set to YES.
   #rc_interactive="YES"

   # If we need to drop to a shell, you can specify it here.
   # If not specified we use $SHELL, otherwise the one specified in /etc/passwd,
   # otherwise /bin/sh

**FreeBSD RC Defaults**

The entire
`FreeBSD rc.conf file <https://github.com/freebsd/freebsd/blob/master/etc/defaults/rc.conf>`_
is available online.

.. code-block:: none

   #!/bin/sh

   # This is rc.conf - a file full of useful variables that you can set
   # to change the default startup behavior of your system.  You should
   # not edit this file!  Put any overrides into one of the ${rc_conf_files}
   # instead and you will be able to update these defaults later without
   # spamming your local configuration information.
   #
   # The ${rc_conf_files} files should only contain values which override
   # values set in this file.  This eases the upgrade path when defaults
   # are changed and new features are added.
   #
   # All arguments must be in double or single quotes.
   #
   # For a more detailed explanation of all the rc.conf variables, please
   # refer to the rc.conf(5) manual page.
   #
   # $FreeBSD$

   ##############################################################

The |trueos| :file:`rc.conf` file is much smaller because
:file:`rc.conf` is now primarily used for tuning OpenRC behavior. By
default, |trueos| uses 3 elements, documented in
:numref:`Table %s <orcpritun>`

.. _orcpritun:
.. table:: : OpenRC Primary Tunables

   +-------------------------------+-------------------------------------+
   | Tunable                       | Description                         |
   +===============================+=====================================+
   | rc_parallel="YES"             | Starts all services in parallel     |
   +-------------------------------+-------------------------------------+
   | rc_logger="YES"               | Enables logging                     |
   +-------------------------------+-------------------------------------+
   | rc_log_path="/var/log/rc.log" | Defines the location for logging rc |
   |                               | activity                            |
   +-------------------------------+-------------------------------------+
  
:numref:`Table %s <orcalltun>` shows all other tunables enabled on a 
clean |trueos| installation. Many of these tunables continue to work in
:file:`/etc/rc.conf` to ensure a smoother migration for existing users
to upgrade. The eventual target locations for these services are also
listed.

.. note:: These migration targets are estimates and subject to change.

.. TODO fill gaps in table with Joe's input.

.. _orcalltun:
.. table:: : OpenRC Other Tunables

   +------------------------------------------+-------------------------------------+------------------------------+
   | Tunable                                  | Description                         | Migration Target             |
   +==========================================+=====================================+==============================+
   | linux_enable="YES"                       | Notifies :file:`/etc/init.d/abi`    | :file:`/etc/conf.d/abi`      |
   |                                          | service to enable the Linux         |                              |
   |                                          | compatability during boot           |                              |
   +------------------------------------------+-------------------------------------+------------------------------+
   | ifconfig_re0="DHCP"                      | TBD                                 | :file:`/etc/conf.d/network`  |
   +------------------------------------------+-------------------------------------+------------------------------+
   | ifconfig_re0_ipv6="inet6 accept_rtadv"   | TBD                                 | :file:`/etc/conf.d/network`  |
   |                                          |                                     |                              |
   +------------------------------------------+-------------------------------------+------------------------------+
   | hostname="trueos-4843"                   | TBD                                 | :file:`/etc/conf.d/hostname` |
   +------------------------------------------+-------------------------------------+------------------------------+
   | kldload_i915kms="i915kms"                | TrueOS specific. Allows loading an  | :file:`etc/conf.d/modules`   |
   |                                          | individual module via the installer |                              |
   |                                          | post installation.                  |                              |
   +------------------------------------------+-------------------------------------+------------------------------+
   | zfs_enable="YES"                         | Obsolete, marked for removal        | None                         |
   +------------------------------------------+-------------------------------------+------------------------------+
   | wlans_iwm0="wlan0"                       | TBD                                 | :file:`/etc.conf.d.network`  |
   +------------------------------------------+-------------------------------------+------------------------------+
   | wlans_iwm0="wlan 0 DHCP"                 | TBD                                 | :file:`/etc.conf.d.network`  |
   +------------------------------------------+-------------------------------------+------------------------------+
   | ifconfig_wlan0_ipv6="inet6 accept_rtadv" | TBD                                 | :file:`/etc.conf.d.network`  |
   +------------------------------------------+-------------------------------------+------------------------------+

.. index:: init, script
.. _OpenRC Install Scripts:

OpenRC Install Scripts
======================

There are number of scripts used for older |trueos| systems and new
installations, listed below.

.. index:: init, scripts, onetime
.. _One time migration:

One-time Migration Script
-------------------------

A one time migration script is available for |trueos| installations 
dated 10-28-16 or older that are still using the legacy FreeBSD rc
system:

.. note:: This block is truncated from the
   `original file <https://github.com/trueos/trueos-core/blob/master/xtrafiles/local/bin/migrate_rc_openrc>`_

.. code-block:: none

   #!/bin/sh

   if [ ! -e /etc/rc.conf ] ; then
     exit 0
   fi

   . /etc/rc.conf

   for var in `set | grep "_enable="`
   do
     key=`echo $var | cut -d '=' -f 1 | sed 's|_enable||g'`
     val=`echo $var | cut -d '=' -f 2`
     if [ "$val" != "YES" ] && [ "$val" != "NO" ] ; then continue; fi
     if [ "$val" = "NO" ] && [ -e "/etc/runlevels/default/$key" ] ; then
         echo "Deleting OpenRC service for $key to default runlevel..."
         rc-update delete $key default
     fi
     if [ -e "/etc/init.d/$key" -o -e "/usr/local/etc/init.d/$key" ] ; then
       if [ -e "/etc/runlevels/default/$key" ] ; then
         echo "OpenRC service for $key already enabled, skipping.."

With this migration, :file:`rc.conf.trueos`, located in :file:`/etc/`,
has been phased out of |trueos| and is automatically removed from legacy
installs dated 10-28-16 and older by :command:`pc-updatemanger`:

This script is used to define a list of services such as *PCDM*
designated to boot by default on a desktop. It also defines what drivers
to load on a desktop. This is now accomplished when the
*trueos-desktop* or *trueos-server* package is installed using
:command:`sysrc` or other methods. Now there is no need to keep an extra
overlay file to accomplish this behaviour.

.. index:: init, scripts, desktop pkginstall
.. _TrueOS desktop pkginstall script:

|trueos| Desktop pkg-install Script
-----------------------------------

.. note:: This is an excerpt from the |trueos| Desktop
   :file:`pkg-install` file, available online:
   https://github.com/trueos/trueos-desktop/blob/master/port-files/pkg-install

.. code-block:: none

   #!/bin/sh
   # Script to install preload.conf

   PREFIX=${PKG_PREFIX-/usr/local}

   if [ "$2" != "POST-INSTALL" ] ; then
      exit 0
   fi

   # If this is during staging, we can skip for now
   echo $PREFIX | grep -q '/stage/'
   if [ $? -eq 0 ] ; then
      exit 0
   fi

   # REMOVEME - Temp fix to ensure i915kms is loaded on upgraded systems
   # 8-29-2016
   if [ -e "/etc/rc.conf.trueos" ] ; then
     set +e
     grep -q "i915kms" /etc/rc.conf.trueos

.. index:: init, scripts, server pkginstall
.. _TrueOS server pkginstall script:

TrueOS Server pkg-install script
--------------------------------

.. note:: This is an excerpt from the |trueos| Server
   :file:`pkg-install` file, available online:
   https://github.com/trueos/trueos-server/blob/master/port-files/pkg-install

.. code-block:: none

   #!/bin/sh
   # Script to install preload.conf

   PREFIX=${PKG_PREFIX-/usr/local}

   if [ "$2" != "POST-INSTALL" ] ; then
      exit 0
   fi

   # If this is during staging, we can skip for now
   echo $PREFIX | grep -q '/stage/'
   if [ $? -eq 0 ] ; then
      exit 0
   fi

   # Copy over customizations for TrueOS
     install -m 644 ${PREFIX}/share/trueos/conf/loader.conf.trueos /boot/loader.conf.trueos
     install -m 644 ${PREFIX}/share/trueos/conf/brand-trueos.4th /boot/brand-trueos.4th
     install -m 644 ${PREFIX}/share/trueos/server-defaults/etc/conf.d/modules /etc/conf.d/modules/

The typical :command:`nginx_enable=”YES”` is no longer used to enable
services. Instead, :command:`rc-update` is used to add or remove
services from runlevels. The one time migration script automatically
adds previously defined user services to the OpenRC default runlevel.
Leftover lines can be removed after migration.

.. index:: init, update makefile
.. _Update Port Makefile:

Updating a Port's Makefile
==========================

There is still quite a bit of work to do updating each port's
:file:`Makefile` to the new format, :command:`USE_OPENRC_SUBR=`.
However, these are to be changed only when each service file has the new
OpenRC ready format:

.. note:: This is an excerpt from the |trueos| :file:`dbus.in` file,
   which is available online:
   https://github.com/trueos/freebsd-ports/blob/xserver-next/devel/dbus/files/dbus.in

.. code-block:: none

   #!/sbin/openrc-run
   # Copyright (c) 2007-2015 The OpenRC Authors.
   # See the Authors file at the top-level directory of this distribution and
   # https://github.com/OpenRC/openrc/blob/master/AUTHORS
   #
   # This file is part of OpenRC. It is subject to the license terms in
   # the LICENSE file found in the top-level directory of this
   # distribution and at https://github.com/OpenRC/openrc/blob/master/LICENSE
   # This file may not be copied, modified, propagated, or distributed
   # except according to the terms contained in the LICENSE file.

   command=/usr/local/bin/dbus-daemon
   pidfile=/var/run/dbus/dbus.pid
   command_args="${dbusd_args---system}"
   name="Message Bus Daemon"

   depend()
   {
           need localmount
           after bootmisc


Here is an example from FreeBSD of *dbus* using the legacy rc script
format:

.. note:: This is an excerpt from the legacy FreeBSD :file:`dbus.in`
   file, which is available online:
   https://github.com/freebsd/freebsd-ports/blob/master/devel/dbus/files/dbus.in

.. code-block:: none

   #!/bin/sh
   #
   # $FreeBSD$
   #
   # PROVIDE: dbus
   # REQUIRE: DAEMON ldconfig
   #
   # Add the following lines to /etc/rc.conf to enable the D-BUS messaging system:
   #
   # dbus_enable="YES"
   #

   . /etc/rc.subr
   . %%GNOME_SUBR%%

   dbus_enable=${dbus_enable-${gnome_enable}}
   dbus_flags=${dbus_flags-"--system"}

   name=dbus
   rcvar=dbus_enable

Several developers are working on the thousands of instances as quickly
as possible. Anyone can begin transitioning to defining all service
configurations in :file:`/etc/conf.d/`, if desired. All configuration
files should reside in that directory with the name of the service for
the configuration file itself. For example, *nginx* is
:file:`/etc/conf.d/nginx`.

Generally, usage of :file:`/etc/rc.conf` is minimized. Tweaking the
default OpenRC configuration parameters is recommended only for advanced
users. It is still possible to use service configurations through
:file:`/etc/rc.conf`, but this file is unusable for enabling or disabling
services for startup.
