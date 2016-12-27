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

.. _Managing Bootup Services:

Managing Bootup Services
========================
   
OpenRC has a variety of options to *start*, *stop*, *add*, or *remove*
services from bootup. Most of these actions can be accomplished using
the :ref:`` <service manager utility> built into |sysadm|. Users
familiar with the FreeBSD service command will notice the similarities
between some of these commands:

<Build table here to doc all commands and descriptions>
service nginx start – to start nginx from /usr/local/etc/init.d/nginx
service nginx restart – to restart nginx from /usr/local/etc/init.d/nginx
service nginx stop – to stop nginx from /usr/local/etc/init.d/nginx
service nginx status – to see the status of the nginx service

rc-status – to see the status of all running services
rc-update – to add or remove a service from the default runlevel

rc-update add nginx default – add a service to the default runlevel
rc-update remove nginx default – remove a service from the default runlevel

**gitter copy/pastes**

Scroll down a little, it was followed by the mention of upstream where
upstream = OpenRC.
Also (for newcomers to OpenRC) note that with OpenRC-enabled TrueOS, a
request for the manual page for service(8) presents the manual page for
rc-service(8). This is normal.
Jeffrey Baitis
@baitisj
Dec 16 15:11
that seems the desired behaviour... would you kindly elaborate regarding
why this is noteworthy?
Guillermo García Rojas C.
@SoloBSD
Dec 16 15:12
Ok now I am getting new packages on "stable"
Ira T Taylor
@itaylor57
Dec 16 15:13
yes stable has been updated
glad you finally work up hehe
Guillermo García Rojas C.
@SoloBSD
Dec 16 15:14
Let's see how it goes
_
Graham Perrin
@grahamperrin
Dec 16 15:16
@baitisj I should probably say something like, "newcomers with a FreeBSD
background" who might assume, from habit (without reference to a manual
page) that service is as documented at
https://www.freebsd.org/cgi/man.cgi?query=service&sektion=8&manpath=FreeBSD

$ service --version
service (OpenRC) 0.23.83
$ rc-service --version
rc-service (OpenRC) 0.23.83
$ ls -l /sbin/*service
-r-xr-xr-x  2 root  wheel  20368 14 Dec 21:47 /sbin/rc-service
-r-xr-xr-x  2 root  wheel  20368 14 Dec 21:47 /sbin/service
$

– and the two binaries share the same sha256 checksum. (Previously, I
wondered whether we would find a symlink at one of the two paths.)
@SoloBSD I'm curious, what address do you get from host pkg.cdn.trueos.org?

I read clarification (from someone at iXsystems?) that OpenRC-enabled
TrueOS does, and will contnue to, use rc.conf. Not to be confused with
rc.conf.trueos.

Ken Moore
@beanpole135
Dec 16 14:30
rc.conf is still used - but not for the <service>_enable=YES stuff anymore

Ken Moore
@beanpole135
Dec 16 14:31
so the rc.conf.trueos file was now unneeded
since that was primarily just for setting up the default services needed
for a system

**copy/paste from https://discourse.trueos.org/t/openrc-differences-from-freebsd-rc/389**

Hello everyone. This is my first attempt at a very rough draft of a
brain dump needed for future handbook additions in relation to OpenRC.
Please let me know if I have drastically overlooked something you may be
curious about, or if I have stated something incorrectly. I hope it is
helpful to answer some of the ongoing questions during the migration to
OpenRC.

TrueOS now uses OpenRC. This replaces traditional behavior of FreeBSD RC
in a few ways. Let’s start with the location of rc scripts for starting,
and stopping services.

TrueOS base system new rc script location:
/etc/init.d/

FreeBSD base system legacy rc script location:
/etc/rc.d/

TrueOS ports rc script location:
/usr/local/etc/init.d/

FreeBSD ports rc script location:
/usr/local/etc/rc.d/

While we are still going through the migration it may be noticeable that
leftovers may exist on the system. They should not be used as they most
will not work at all with OpenRC. They will be likely removed from the
source tree altogether, and by pc-updatemanager in the future when all
functionality has been migrated, and there is no longer a reason to keep
them in our tree for ports compatibility.

Before we get into the more technical stuff. Let’s just start with how
to start, stop, add, or remove services from bootup. Most of the actions
can also be accomplished using the service manager utility built into
sysadm also known as Control Panel in TrueOS. Most of you familiar with
the FreeBSD service command should feel right at home for the first
couple of examples.

service nginx start – to start nginx from /usr/local/etc/init.d/nginx
service nginx restart – to restart nginx from /usr/local/etc/init.d/nginx
service nginx stop – to stop nginx from /usr/local/etc/init.d/nginx
service nginx status – to see the status of the nginx service

rc-status – to see the status of all running services
rc-update – to add or remove a service from the default runlevel

rc-update add nginx default – add a service to the default runlevel
rc-update remove nginx default – remove a service from the default runlevel

What is a runlevel? Let’s run rc-update by itself to show all of the runlevels.

              abi | boot                                   
        adjkerntz | boot                                   
        automount |      default                           
         bootmisc | boot                                   
           bridge | boot                                   
             cron | boot                                   
            cupsd |      default                           
             dbus |      default                           
             devd | boot                                   
           dumpon | boot                                   
             fsck | boot                                   
           hostid | boot                                   
         hostname | boot                                   
             ipfw | boot                                   
            local |      default nonetwork                 
       localmount | boot                                   
            lockd |      default                           
         loopback | boot                                   
          modules | boot                                   
             motd | boot                                   
           moused |      default                           
         netmount |      default                           
          network | boot                                   
        newsyslog | boot                                   
         openntpd |      default                           
             pcdm |      default                           
             root | boot                                   
          rpcbind |      default                           
        savecache |                        shutdown        
         savecore | boot                                   
            statd |      default                           
      staticroute | boot                                   
             swap | boot                                   
           sysadm |      default                           
          syscons | boot                                   
           sysctl | boot                                   
          syslogd | boot                                   
       trueosinit |      default                           
          urandom | boot                                   
              zfs | boot                                   
             zvol | boot

With OpenRC there are a few runlevels that happen in order in TrueOS. First is the sysinit runlevel which we start nothing in as it’s just to allow OpenRC to initialize itself. Second is the boot runevel which we start most base services in from /etc/init.d/. Third is the default runlevel which is where services start by ports should be added. In fact services added by ports cannot be added to boot, or sysinit. OpenRC will now allow you to add a service in the prefix location to the runlevel boot which happens before the /usr filesystem is mounted. Lastly there is a shutdown runlevel which only things like savecore should run in, or the in the future perhaps pc-updatemanager installing updates at shutdown.

When a service is added to a runlevel a symlink is created in /etc/runlevels. When a service is started, stopped, or changed to another state a symlink is added into /libexec/rc/init.d/.

daemons exclusive inactive scheduled starting wasinactive
depconfig failed options softlevel stopping
deptree hotplugged prefix.lock started tmp

Also under /libexec/rc exists a cache directory which keeps a dependancies cache only updated when dependencies change. In addition several directories exist for other binaries, and special binaries used by OpenRC functions.

With OpenRC we also have a dependency based init system. Let’s look at a service which needs network such as sysadm.

Contents of /usr/local/etc/init.d/sysadm depend section:

depend() {
need net
after bootmisc
keyword -shutdown
}

We can define that sysadm needs network which is the nickname of the /etc/init.d/network service defined by provide in network. We also see that it starts after bootmisc. If we don’t want restarting network to restart sysadm then we don’t need net for sysadm. If we just want sysadm to start after network then we add network the actually name of the script in after bootmisc.

Now let’s look at /etc/init.d/network

depend()
{
provide net
need localmount
after bootmisc modules
keyword -jail -prefix -vserver -stop
}

The provide option will set the service nickname to net. Need says that restarting localmount will restart network. After defines that we start after bootmisc, and modules. The keyword -jail option for example says we do not run this service in a jail, prefix, or the other options shown.

We have a drastically different rc defaults file from FreeBSD
TrueOS rc defaults
github.com2
trueos/freebsd/blob/drm-next-4.7/etc/defaults/rc.conf

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

This file has been truncated. show original

FreeBSD rc defaults
github.com2
freebsd/freebsd/blob/master/etc/defaults/rc.conf

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

This file has been truncated. show original

The reason ours is so much smaller is the fact that rc.conf is now primarily used for tuning OpenRC behavior. In particular we currently use 3 knobs by default:

rc_parallel="YES"
rc_logger="YES"
rc_log_path="/var/log/rc.log"

The rc_parrallel is just to inform that we want to start all services in parallel. The rc_logger is just to inform that we want to enable logging. The rc_log_path is just to define the location we want to use for logging rc activity.

Let’s look at some of the other knobs we have enabled on a clean install to work for the TrueOS OpenRC migration. We have ensured that many of these knobs would continue to work in /etc/rc.conf to ensure a smoother migration for existing users to upgrade. We do plan to migrate them, and I will outline where they should likely going in the future.

linux_enable="YES"
ifconfig_re0="DHCP"
ifconfig_re0_ipv6="inet6 accept_rtadv"
hostname="trueos-4843"
kldload_i915kms="i915kms"
zfs_enable="YES"
wlans_iwm0="wlan0"
kldload_i915kms="i915kms"
ifconfig_wlan0_ipv6="inet6 accept_rtadv"

The linux_enable=”YES” parameter is to tell the /etc/init.d/abi service that we want to enable the Linux compat during boot. This may be migrated in the future to /etc/conf.d/abi or something more OpenRC style.

The ifconfig_re0=”DHCP”, and ifconfig_re0_ipv6="inet6 accept_rtadv" will likely be migrated to /etc/conf.d/network where it is more appropriate.

The hostname="trueos-4843" parameter would typically go under /etc/conf.d/hostname.

The zfs_enable parameter is no longer in use, and needs to to removed.

The three wlans lines would also typically belong in /etc/conf.d.network.

The kldload_i915kms="i915kms" is a TrueOS specific function not normally part of FreeBSD to allow the installer to enable an individual module loading post install. Normally all modules are defined together in /etc/rc.conf with kldlist=””. This should eventually belong in /etc/conf.d/modules.

This would be something which many of you may see leftover from upgrades. The SYNCDHCP parameter was to tell dhclient to wait in the foreground until, and IP address could be obtained. This is undesirable for a laptop, and unfortunately has not worked reliably with for us to use DHCP on wireless devices with dhclient.

wlans_iwm0="wlan0 SYNCDHCP"

This is one of the reasons we are now shipping with dhcpcd as the default dhcp client. For dhcp to work properly SYNCDHCP will not work, and should not be used. Instead it should be:

wlans_iwm0="wlan0 DHCP"

We have a one time migration script which will run for 10-28-16, and older installs still using the legacy FreeBSD rc system.
github.com1
trueos/trueos-core/blob/master/xtrafiles/local/bin/migrate_rc_openrc

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

This file has been truncated. show original

With the migration rc.conf.trueos has been phased out of TrueOS, and is removed from legacy installs 10-28-16, and older by pc-updatemanger:

Legacy rc.conf.trueos location:
/etc/rc.conf.trueos

This script was used to define a list of services such as PCDM that we want to boot by default on a desktop. It also defined what drivers we would want to load on a desktop. We now do this when the trueos-desktop, or trueos-server package is installed instead using sysrc, and other methods. There is no longer a need for us to have an extra overlay file to accomplish this behaviour.

TrueOS Desktop pkg-install script:
github.com1
trueos/trueos-desktop/blob/master/port-files/pkg-install

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

This file has been truncated. show original

TrueOS Server pkg-install script:
github.com
trueos/trueos-server/blob/master/port-files/pkg-install

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

This file has been truncated. show original

As one may have guessed the typical nginx_enable=”YES” is no longer used to enable services. Instead the rc-update command is used to add, or remove services from runlevels. The one time migration script should take care of auto adding previously defined user services to the OpenRC default runlevel. Leftover lines can be removed after migration.

We still have quite a bit of work to do updating each ports Makefile currently using:

USE_RC_SUBR=

To use the new format:

USE_OPENRC_SUBR=

This should only be changed when each service file has the new OpenRC ready format:
github.com1
trueos/freebsd-ports/blob/xserver-next/devel/dbus/files/dbus.in

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

This file has been truncated. show original

FreeBSD example of dbus using the legacy rc script format:
github.com
freebsd/freebsd-ports/blob/master/devel/dbus/files/dbus.in

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

This file has been truncated. show original

Several developers are working on the thousands of instances as quickly as possible. Going forward anyone can begin transitioning to defining all service configuration in /etc/conf.d/ if desired. All configuration files should reside in that directory with the name of the service for the configuration file itself.

For nginx this would be:
/etc/conf.d/nginx

In general usage of /etc/rc.conf should be kept to a minimum, and you should only tweak the default OpenRC configuration parameters if you really know what you are doing. Service configuration can still be used in /etc/rc.conf. It's simply no longer used for enabling, or disabling services for startup.