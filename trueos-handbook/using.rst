.. _Using TrueOS®:

Using TrueOS®
**************

This section discusses how to perform common tasks that were not
discussed in the :ref:`SysAdm™ Client` section.

.. index:: configuration
.. _Java and Flash:

Java and Flash
==============

IcedTea-Web provides an open source Java browser plugin which
automatically works with the FireFox, Chromium, and Opera web browsers
without any additional configuration. To install this software, search
for "icedtea" within :ref:`AppCafe®`. 

Version 11 of the Adobe Flash player is available for installation
through :ref:`AppCafe®`. To install flash as a browser plugin search
for and install both the "flashplugin" and "nspluginwrapper" packages.
Once installed, flash should "just work" when browsing the web. If
Adobe Flash does not seem to be working, running the following command
as your regular user account should fix the problem::

 flashpluginctl on

The Adobe Flash Player preferences utility can be used to modify how websites interact with your browser using Adobe Flash. Many of the
same configurations can be done via right-click within an active flash object in a web browser.

To access the utility shown in :numref:`Figure %s: Flash Player Configuration Utility <flash>`, use :menuselection:`Browse Applications --> Adobe Flash Player preferences` or type
:command:`flash-player-properties`.

.. _flash:

.. figure:: images/flash.png

The options available in each tab and when to use them are described at the Adobe website: 

* `Storage <http://help.adobe.com/en_US/FlashPlayer/LSM/WS6aa5ec234ff3f285139dc56112e3786b68c-7fff.html>`_ describes private browsing support and the privacy issues associated with
  local storage of flash information.

* `Camera and Mic <http://help.adobe.com/en_US/FlashPlayer/LSM/WS6aa5ec234ff3f285139dc56112e3786b68c-7ff8.html>`_ controls how websites can use your computer's camera and microphone.

* `Playback <http://help.adobe.com/en_US/FlashPlayer/LSM/WS6aa5ec234ff3f285139dc56112e3786b68c-7ff5.html>`_ describes how to configure peer-assisted networking to improve bandwidth.

* `Advanced <http://help.adobe.com/en_US/FlashPlayer/LSM/WS6aa5ec234ff3f285139dc56112e3786b68c-7ff0.html>`_ controls how Flash Player handles browsing data, updates, trusted locations,
  and protected content.

.. index:: fonts
.. _Fonts:

Fonts 
=====

TrueOS® installs with `Google Noto <http://www.google.com/get/noto/>`_
which provides multi-lingual Sans and Serif fonts. Many other fonts
are available from :ref:`AppCafe®`. Any font installed using AppCafe®
should not require any additional configuration to "just work". 

If you have a collection of fonts that you have downloaded or
purchased, you can configure your TrueOS® system to also use those
fonts. Become the superuser and copy the downloaded font to the
:file:`/usr/local/share/fonts/` directory. Then, run this command to
refresh the fonts cache::

 fc-cache -f -v /usr/local/share/fonts/name_of_font
 
.. index:: sound
.. _Sound Mixer Tray:

Sound Mixer Tray
=================

TrueOS® includes a graphical utility for managing the sound card's
mixer settings. The utility can be accessed using the speaker icon in
the system tray.

:numref:`Figure %s: Mixer Icon <sound1>` shows an example of
clicking the mixer icon in the system tray on a system with
multiple audio outputs. If the system only has one audio output, the
"Outputs" submenu will not be displayed. To change the default audio
output, click its entry in the "Output" menu.

.. _sound1:

.. figure:: images/sound1.png

:numref:`Figure %s: Mixer Controls <sound2>` shows the menu which
opens when you instead click the "Mixer" button shown in
:numref:`Figure %s: Mixer Icon <sound1>`.

.. _sound2:

.. figure:: images/sound2.png

The "Mixer Controls" screen provides sliders to modify the left and
right channels that control volume, pcm (the sound driver), the
speaker, the microphone, the recording level, the input level, and the
output level. Each control can be muted/unmuted individually by
clicking its "Mute" or"Unmute" button, depending upon its current mute
state.

:numref:`Figure %s: System Sound Configuration <sound3>` shows the "System Configuration" tab.

.. _sound3:

.. figure:: images/sound3.png

This tab contains the following options: 

* **Recording Device:** use the drop-down menu to select the device to
  use for recording sound.

* **Default Tray Device:** use the drop-down menu to set the default
  slider to display in the system tray.

* **Audio Output Channel:** use the drop-down menu to change the sound
  device and use the "Test" button to determine that sound is working.
  This is sometimes necessary when you change audio devices. For
  example, if you connect a USB headset, TrueOS® will detect the new
  device and will automatically change the audio device to the USB
  input. However, if you insert a headset into an audio jack, the
  system may not detect the new input so you will have to manually
  change the default device.

The "File" menu can be used to quit this mixer screen or to close both
this screen and remove the icon from the system tray.

.. note:: To re-add the mixer icon after removing it, type
   :command:`pc-mixer &`. Alternately, to open this application
   without adding it back to the system tray, type
   :command:`pc-mixer -notray`.

The "Configuration" menu provides options for accessing the "PulseAudio Mixer" and "PulseAudio Settings" utilities as well as for restarting PulseAudio.
TrueOS® provides full `PulseAudio <https://www.freedesktop.org/wiki/Software/PulseAudio/>`_ support and these utilities can be used to configure discoverable
network sound devices and mixer levels.

.. index:: troubleshooting
.. _Troubleshooting Sound:

Troubleshooting Sound 
----------------------

Type :command:`mixer` from the command line to see the current sound
settings::

 mixer
 Mixer vol      is currently set to   0:0
 Mixer pcm      is currently set to 100:100
 Mixer speaker  is currently set to 100:100
 Mixer mic      is currently set to  50:50
 Mixer rec      is currently set to   1:1
 Mixer monitor  is currently set to  42:42
 Recording source: monitor

If any of these settings are set to *0*, set them to a higher value,
by specifying the name of the mixer setting and a percentage value up
to *100*::

 mixer vol 100
 Setting the mixer vol from 0:0 to 100:100.

You can make that change permanent by creating a file named
:file:`.xprofile` in your home directory that contains the corrected
mixer setting.

If you only get one or two mixer settings, you need to change the
default mixer channel. As the superuser, try this command::

 sysctl -w hw.snd.default_unit=1

To see if that changed to the correct channel, type :command:`mixer`
again. If you still only have one or two mixer settings, try setting
the :command:`sysctl` value to *2*, and if necessary, to *3*.

Once you have all of the mixer settings and none are set to *0*, your
sound should work. If it still doesn't, these resources may help you
to pinpoint the problem: 

* `Sound Section of FreeBSD Handbook <http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/sound-setup.html>`_

* `FreeBSD Sound Wiki <https://wiki.FreeBSD.org/Sound>`_

If you still have problems with sound, see the section on
:ref:`Finding Help` to determine which help resources are available.
When reporting your problem, include your version of TrueOS® and the
name of your sound card. 

.. index:: multimedia
.. _Multimedia:

Multimedia
==========

TrueOS® has been pre-configured to support most multimedia formats and
makes it easy to install most open source media applications using
:ref:`AppCafe®`.

If you install a web browser using AppCafe®, you should be able to
play most media formats, including YouTube videos, Internet radio, and
many trailer and movie sites.

If people are blue in YouTube videos, this is due to a known issue in
flash which Adobe hasn't fixed for open source players. To resolve
this issue, right-click an area in the video, select "Settings", then
uncheck the box "Enable hardware acceleration". Alternately, install
`Minitube <http://flavio.tordini.org/minitube>`_ using :ref:`AppCafe®`
and use it to watch YouTube.

.. note:: if you happen to come across a file that you can not play in
   a web browser or media player, it is probably because it is in a
   proprietary format that requires a licensing fee or restricts
   distribution of the codec that is required to play that media
   format.

AppCafe® contains several dozen applications for playing and editing
multimedia. It includes these popular applications (click the links to
view screenshots): 

* `aTunes <http://www.atunes.org/?page_id=5>`_: full-featured audio
  player and manager that can play mp3, ogg, wma, wav, flac, mp4 and
  radio streaming, allowing users to easily edit tags, organize music
  and rip audio CDs.

* `Audacity <https://sourceforge.net/projects/audacity/?lang=en>`_:
  multilingual audio editor and recorder.

* `DeaDBeeF <http://deadbeef.sourceforge.net/screenshots.html>`_:
  music player that supports most audio formats.

* `Decibel <http://decibel.silent-blade.org/index.php?n=Main.Screenshots>`_:
  audio player built around a highly modular structure that lets the
  user disable completely the features he does not need. Able to play
  CDs directly.

* `gtkpod <http://www.gtkpod.org/index.php?title=Screenshots>`_:
  graphical user interface for the Apple iPod.

* `Miro <http://www.getmiro.com/download/screenshots/>`_: HD video
  player that can play almost any video file and offers over 6,000
  free Internet TV shows and video podcasts.

* `SMPlayer <http://smplayer.sourceforge.net/>`_: universal media
  player that can handle any media format and play audio CDs, DVDs,
  (S)VCDs, TV/radio cards, YouTube™ and SHOUTcast™ streams. This is
  the default player used by :ref:`Mount Tray`.

.. index:: multimedia
.. _Kodi:

Kodi
----

`Kodi, formerly known as XBMC, <https://kodi.tv/>`_ is a GPL-licensed
software media player and entertainment hub for digital media. It can
play most audio and video formats, CDs and DVDs from a disk or image
file, and even files inside ZIP and RAR archives. It can scan all of
your media and automatically create a personalized library with album
covers, descriptions, and fan art. 

Kodi can be installed using :ref:`AppCafe®`. Once installed, an entry
for "Kodi media center" will be added to "Browse Applications". You
can also start Kodi by typing :command:`kodi` from a command prompt. 

If you have never used Kodi before, take some time to skim through the
`Kodi Wiki Manual <http://kodi.wiki/>`_. The
`Turn PC-BSD into a home theater forum post <https://forums.pcbsd.org/thread-19799.html>`_
contains a quick how-to for configuring Kodi.

.. index:: multimedia
.. _PlexHome Theater:

PlexHome Theater
----------------

`Plex Home Theater <https://plex.tv/>`_ is a centralized media
playback system. The central Plex Media Server streams media to many
Plex player Apps which are used to view your media library and watch
shows. 

To install PlexHome Theater, use AppCafe®. Once installed, an entry should be added to the "Multimedia" section of the application menu
of your desktop. You can also start this application by typing :command:`plexhometheater` from a command prompt. 

Once installed, an entry for "Plex Home Theater" will also be added to the login manager so that you can login directly to the home theater instead of a desktop.

The first time you run or log into Plex Home Theater, a wizard will check your audio settings and sign into your Plex account. If you do not have a Plex account yet,
create one at `plex.tv <https://plex.tv/>`_. The wizard will give you a PIN code and an URL to enter the code. Once you enter the PIN, the wizard will connect and sign you in.
You can now search for and watch media. To exit Plex, click the "<" then "Quit".

.. index:: files
.. _Files and File Sharing:

Files and File Sharing
======================

Depending upon which desktops you have installed, different graphical file manager utilities may already be installed for you. You do not need to be
logged into a specific window manager to use an installed file manager. For example, if KDE is installed, you can run its file manager from any window manager
by typing :command:`dolphin`. KDE, GNOME, LXDE, and XFCE install their own file managers while most of the other desktops assume that you will install your
favorite file manager. Table 9.4a summarizes the available file managers and indicates which desktop they are installed with. Some file managers can be
installed independent of a desktop using :ref:`AppCafe®`. Once a file manager is installed, type its name if you wish to run it from another desktop.

**Table 9.4a: Available File Managers**

+---------------+------------------+--------------------------------------------------------------------+
| File Manager  | Desktop/AppCafe  | Screenshots                                                        |
+===============+==================+====================================================================+
| dolphin       | KDE              | `<https://userbase.kde.org/Dolphin>`_                              |
+---------------+------------------+--------------------------------------------------------------------+
| emelfm2       | AppCafe          | `<http://emelfm2.net/wiki/ScreenShots>`_                           |
+---------------+------------------+--------------------------------------------------------------------+
| caja          | MATE             | `<http://mate-desktop.org/gallery/1.6/>`_                          |
+---------------+------------------+--------------------------------------------------------------------+
| mucommander   | AppCafe          | `<http://www.mucommander.com/screenshots.php>`_                    |
+---------------+------------------+--------------------------------------------------------------------+
| nautilus      | GNOME, AppCafe   | `<https://projects.gnome.org/nautilus/screenshots.html>`_          |
+---------------+------------------+--------------------------------------------------------------------+
| pcmanfm       | LXDE, AppCafe    | `<http://lxde.org/easy_fast_file_management_pcmanfm>`_             |
+---------------+------------------+--------------------------------------------------------------------+
| thunar        | XFCE, AppCafe    | `<http://docs.xfce.org/xfce/thunar/start>`_                        |
+---------------+------------------+--------------------------------------------------------------------+
| xfe           | AppCafe          | `<http://roland65.free.fr/xfe/index.php?page=screenshots>`_        |
+---------------+------------------+--------------------------------------------------------------------+

When working with files on your TrueOS® system, save your own files to your home directory. Since most of the files outside of your home directory are used
by the operating system and applications, you should not delete or modify any files outside of your home directory, unless you know what you are doing.

Table 9.4b summarizes the directory structure found on a TrueOS® system. :command:`man hier` explains this directory structure in more detail.

**Table 9.4b: TrueOS Directory Structure**

+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Directory                | Contents                                                                                                                        |
+==========================+=================================================================================================================================+
| /                        | pronounced as "root" and represents the beginning of the directory structure                                                    |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /bin/                    | applications (binaries) that were installed with the operating system                                                           |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /boot/                   | stores the startup code, including kernel modules (such as hardware drivers)                                                    |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /compat/linux/           | Linux software compatibility files                                                                                              |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /dev/                    | files which are used by the operating system to access devices                                                                  |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /etc/                    | operating system configuration files                                                                                            |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /etc/X11/                | the :file:`xorg.conf` configuration file                                                                                        |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /etc/rc.d/               | operating system startup scripts                                                                                                |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /home/                   | subdirectories for each user account; each user should store their files in their own home directory                            |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /lib/                    | operating system libraries needed for applications                                                                              |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /libexec/                | operating system libraries and binaries                                                                                         |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /media/                  | mount point for storage media such as DVDs and USB drives                                                                       |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /mnt/                    | another mount point                                                                                                             |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /proc/                   | the proc filesystem required by some Linux applications                                                                         |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /rescue/                 | necessary programs for emergency recovery                                                                                       |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /root/                   | administrative account's home directory                                                                                         |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /sbin/                   | operating system applications; typically only the superuser can run these applications                                          |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /tmp/                    | temporary file storage; files stored here may disappear when the system reboots                                                 |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /usr/bin/                | contains most of the command line programs available to users                                                                   |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /usr/local/              | contains the binaries, libraries, startup scripts, documentation, and configuration files used by applications installed from   |
|                          | ports or packages                                                                                                               |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /usr/local/share/fonts/  | system wide fonts for graphical applications                                                                                    |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /usr/local/share/icons/  | system wide icons                                                                                                               |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /usr/ports/              | location of system ports tree (if installed)                                                                                    |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /usr/share/              | system documentation and man pages                                                                                              |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /usr/sbin/               | command line programs for the superuser                                                                                         |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /usr/src/                | location of system source code (if installed)                                                                                   |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| /var/                    | files that change (vary), such as log files and print jobs                                                                      |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+

TrueOS® provides built-in support for accessing Windows shares, meaning you only have to decide which utility you prefer to access existing Windows shares on
your network. If a desktop is installed, you do not have to be logged into that desktop in order to use that utility.

Table 9.4c summarizes the available utilities (type a utility's name to launch it in any desktop), which desktop it installs with, whether or not it can be installed
separately using :ref:`AppCafe®`, and a short description of how to access the available shares using that utility.

**Table 9.4c: Utilities that Support Windows Shares**

+--------------+----------------------+--------------------------------------------------------------------------------------------------------------------------+
| **Utility**  | **Desktop/AppCafe**  | **How to Access Existing Shares**                                                                                        |
+==============+======================+==========================================================================================================================+
| dolphin      | KDE                  | in the left frame, click on :menuselection:`Network --> Samba Shares`, then the Workgroup name; if the network requires  |
|              |                      | a username and password to browse for shares, set this in :menuselection:`System Settings --> Sharing`                   |
|              |                      | while in KDE or type :command:`systemsettings` and click "Sharing" while in another desktop                              |
+--------------+----------------------+--------------------------------------------------------------------------------------------------------------------------+
| konqueror    | KDE                  | in the location bar, type *smb:/*                                                                                        |
+--------------+----------------------+--------------------------------------------------------------------------------------------------------------------------+
| mucommander  | AppCafe              | click on :menuselection:`Go --> Connect to server --> SMB`; input the NETBIOS name of server, name of share, name of     |
|              |                      | domain (or workgroup), and the share's username and password                                                             |
+--------------+----------------------+--------------------------------------------------------------------------------------------------------------------------+
| nautilus     | GNOME, AppCafe       | click on :menuselection:`Browse Network --> Windows Network`                                                             |
+--------------+----------------------+--------------------------------------------------------------------------------------------------------------------------+
| thunar       | XFCE, AppCafe        | in the left frame, click on :menuselection:`Network --> Windows Network`                                                 |
+--------------+----------------------+--------------------------------------------------------------------------------------------------------------------------+

.. index:: windows
.. _Windows Emulation:

Windows Emulation
=================

`Wine <https://wiki.winehq.org/Main_Page>`_ is an application that allows you to create a Windows environment for installing Windows software. This can be useful if your
favorite Windows game or productivity application has not been ported to Linux or BSD.

Wine is not guaranteed to work with every Windows application. If you are unsure if the application that you require is supported, search for it in the
"Browse Apps" section of the `Wine application database <https://appdb.winehq.org/>`_. The  `Wine wiki <http://wiki.winehq.org/>`_ contains many resources to
get you started and to refer to if you encounter problems with your Windows application.

Wine can be installed during installation or from :ref:`AppCafe®`. Once installed, it can be started by clicking the entry for "Wine Configuration" from the
desktop's application menu or by typing :command:`winecfg` at the command line. The initial Wine configuration menu shown in :numref:`Figure %s: Wine Configuration Menu <wine1>`.

.. _wine1:

.. figure:: images/wine1.jpg

Click the "Add application" button to browse to the application's installer file. By default, the contents of your hard drive will be listed under "drive_c".
If the installer is on a CD/DVD, use the drop-down menu to browse to your :menuselection:`home directory --> *.wine --> dosdevices` folder. The contents of
the CD/DVD should be listed under *d:*. If they are not, the most likely reason is that your CD/DVD was not automatically mounted by the desktop. To mount the
media, type the following as the superuser::

 mount -t cd9660 /dev/cd0 /cdrom

You should hear the media spin and be able to select the installer file. Once selected, press "Apply" then "OK" to exit the configuration utility.

To install the application, click the Winefile desktop icon or type :command:`winefile` to see the screen shown in :numref:`Figure %s: Installing the Application Using winefile <wine2>`.

.. _wine2: 

.. figure:: images/wine2.jpg

Click the button representing the drive containing the installer and double-click on the installation file (e.g. :file:`setup.exe`).
The installer should launch and you can proceed to install the application as you would on a Windows system.

.. note:: if you had to manually mount the CD/DVD, you will need to unmount it before it will eject. As the superuser, use the command :command:`umount /mnt`.

Once the installation is complete, browse to the application's location. :numref:`Figure %s: Running the Installed Application <wine3>` shows an example of running Internet Explorer within
:command:`winefile`.

.. _wine3:

.. figure:: images/wine3.jpg

.. index:: games
.. _Running Steam:

Running Steam
-------------

Wine can be configured to install and run `Steam games <http://store.steampowered.com/about/>`_. Video instructions can be found
at `Steam on PC-BSD - How to Get Wine Running 3D Games <https://www.youtube.com/watch?v=B04EuZ9hpAI>`_ and at
`Steam on PCBSD 2 - Using Wine as a Streaming Client <http://blog.pcbsd.org/2014/12/steam-on-pcbsd-2-using-wine-as-a-streaming-client/>`_.

.. index:: security
.. _Security:

Security
========

Your TrueOS® system is secure by default. This section provides an overview of the built-in security features and additional resources should you like to
learn more about increasing the security of your system beyond its current level.

The security features built into TrueOS® include: 

* **Naturally immune to viruses and other malware:** most viruses are written to exploit Windows systems and do not understand the binaries or paths found on
  a TrueOS® system. Antivirus software is still available in the Security section of :ref:`AppCafe®` as this can be useful if you send or forward email
  attachments to users running other operating systems.

* **Potential for serious damage is limited:** file and directory ownership and permissions along with separate user and group functions mean that as an
  ordinary user any program executed will only be granted the abilities and access of that user. A user that is not a member of the *wheel* group can not
  switch to administrative access and can not enter or list the contents of a directory that has not been set for universal access.

* **Built-in firewall:** the default firewall ruleset allows you to access the Internet and the shares available on your network but does not allow
  any inbound connections to your computer. In addition, `Fail2ban <http://www.fail2ban.org/wiki/index.php/Main_Page>`_ is installed. This service can be
  configured to identify possible break-in attempts and to respond with an action such as creating a firewall rule to ban the intruder. Instructions for
  configuring fail2ban can be found on the `fail2ban wiki <http://www.fail2ban.org/wiki/index.php/MANUAL_0_8#Usage>`_. 

* **Very few services are enabled by default:** you can easily view which services are started at boot time by reading through
  :file:`/etc/rc.conf`. You can disable the services that you do not use by commenting the line for that service
  with a *#* in :file:`/etc/rc.conf`.

* **SSH is disabled by default:** and can only be enabled by the superuser. This setting prevents bots and other users from trying to access your system. If
  you do need to use SSH, add the line *sshd_enable=YES* to :file:`/etc/rc.conf`. You can then start the service by typing
  :command:`service sshd start`. You will need to add a firewall rule using :ref:`Firewall Manager` to allow SSH connections over TCP port 22.

* **SSH root logins are disabled by default:** if you enable SSH, you must login as a regular user and use :command:`su` or :command:`sudo` when you need
  to perform administrative actions. You should not change this default as this prevents an unwanted user from having complete access to your system.

* **sudo is installed:** and configured to allow users in the *wheel* group permission to run an administrative command after typing their password. By
  default, the first user you create during installation is added to the *wheel* group. You can use :ref:`User Manager` to add other users to this group. You
  can change the default :command:`sudo` configuration using the :command:`visudo` command as the superuser.

* :wikipedia:`AES instruction set` (AESNI) support is loaded by default for the Intel Core i5/i7 processors that support this
  encryption set. This support speeds up AES encryption and decryption.

* **Automatic notification of security advisories:** :ref:`Update Manager` will automatically notify you if an update is available as the result of a
  `security advisory <http://www.freebsd.org/security/advisories.html>`_ that affects TrueOS®. This allows you to keep your operating system fully patched
  with just the click of a mouse.

* TrueOS® packages are built with `LibreSSL <http://www.libressl.org/>`_ which has fewer vulnerabilities than OpenSSL.

* :ref:`PersonaCrypt` allows a user to use a removable, encrypted device as their home directory.

* Logging into a stealth session creates an encrypted zvol as a temporary home directory for that login session.
  When the user logs out of a stealth session, the zvol is destroyed, along with the contents of the temporary home directory. 

If you would like to learn more about security on FreeBSD/TrueOS® systems, :command:`man security` is a good place to start. These resources provide more
information about security on FreeBSD-based operating systems: 

* `FreeBSD Security Information <http://www.freebsd.org/security/>`_

* `Security Section of FreeBSD Handbook <http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/security.html>`_

* `Hardening FreeBSD <http://www.bsdguides.org/2005/hardening-freebsd/>`_
  
.. index:: printing
.. _Printing:

Printing and Scanning
=====================

Like many open source operating systems, TrueOS® uses the Common Unix
Printing System (`CUPS <http://cups.org/>`_) to manage printing.

CUPS provides an easy-to-use utility for adding and managing printers.
Whether or not it automatically detects your printer depends upon how
well your printer is supported by an open source print driver. This
section will walk you through a sample configuration for a HP DeskJet
36xx series printer. Your printer may "just work", allowing you to
breeze through the configuration screens. If your printer
configuration does not work, read this section more closely for hints
on how to locate the correct driver for your printer.

.. index:: printing
.. _Researching Your Printer:

Researching your Printer 
-------------------------

Before configuring your printer, it is worth the time to see if a
print driver exists for your particular model, and if so, which driver
is recommended. If you are planning to purchase a printer, this is
definitely good information to know beforehand. You can look up the
vendor and model of the printer in the
`Open Printing Database <http://www.openprinting.org/printers>`_ which
will indicate if the model is supported and if there are any known
caveats with the print driver. Once the model is selected, click the
"Show this printer" button to see the results.

For the example HP DeskJet model, the HPLIP driver is recommended. In
TrueOS®, the HPLIP driver is available as an optional package called
"hplip". You can search if the driver is installed, and install it if
it is not, using :ref:`AppCafe®`.

.. index:: printing
.. _Adding a Printer:

Adding a Printer 
-----------------

Once you know that your printer is supported, make sure that the
printer is plugged into your computer or, if the printer is a network
printer, that both your computer and the printer are connected to the
network. Then, open a web browser and enter the address
"127.00.1:631/admin". This will open the CUPS configuration shown in
:numref:`Figure %s: Printer Configuration <print4a>`. 

.. _print4a: 

.. figure:: images/print4a.png

To add a new printer, click the "Add Printer" button. CUPS will pause
for a few seconds as it searches for available printers. When it is
finished, you should see a screen similar to
:numref:`Figure %s: Select a Print Device <print5a>`. 

.. _print5a: 

.. figure:: images/print5a.png

In this example, the wizard has found the HP DeskJet 3630 printer on
both the USB port (first entry) and the wireless network (second
entry). Click the desired connection method then click "Continue".
CUPS will attempt to load the correct driver for the device. If it is
successful, it will display the screen shown in
:numref:`Figure %s: Describe Printer Screen <print6a>`. 

.. _print6a:

.. figure:: images/print6a.png

This screen automatically fills out the printer model series, a
description, and the type of connection. If you wish, you can add a
descriptive "Location". If you will be sharing the printer on the
network, check the "Sharing" box. 

Once you click the "Continue" button, the next screen, shown in
:numref:`Figure %s: Viewing the Default Driver <print7a>`,
will show a summary of the selected options and offer the ability to
select another driver. For now, leave the driver that was detected and
click "Add Printer". If the printer does not work using the default
driver, read the section on :ref:`Printer Troubleshooting` which
describes how to use this screen in more detail.

.. _print7a:

.. figure:: images/print7a.png

The next screen, shown in
:numref:`Figure %s: Modify Print Properties <print8a>`, can be used to
modify the properties of the printer. 

.. _print8a:

.. figure:: images/print8a.png

You may wish to take a few minutes to review the settings in the
"General", "Banners", and "Policies" tabs as these allow you to
configure options such as print banners, permissions, the default
paper size, and double-sided printing. The available settings will
vary, depending upon the capabilities of the print driver. When
finished, click the "Set Default Options" button to save the options.
This will open the Printers tab, with the new printer displayed. An
example is shown in :numref:`Figure %s: Manage Printer <print9a>`.

.. _print9a:

.. figure:: images/print9a.png

You should print a test page to ensure that the printer is working.
Ensure the printer has paper and click
:menuselection:`Maintenance -> Print Test Page`. If you can not print
a successful test page, refer to :ref:`Printer Troubleshooting`.

.. index:: printing
.. _Manually Adding a Driver:

Manually Adding a Driver 
-------------------------

If the print configuration fails, double-check that the printer is
supported as described in :ref:`Researching your Printer` and that
HPLIP is installed if it is a HP printer. Also check that the printer
is plugged in and powered on.

If the wizard is unable to even detect the device, try to manually add
the information for the print device. In the "Select Device" screen 
(:numref:`Figure %s: Select a Print Device <print5a>`), select the type
of connection to the printer and input the following information. The
type of information depends upon the type of connection:

**USB:** this entry will only appear if a printer is plugged into a
USB port and the number of entries will vary depending upon the number
of USB ports on the system. If there are multiple USB entries,
highlight the one that represents the USB port your printer is plugged
into.

**IPP:** select this option if you are connecting to a printer cabled
to another computer (typically running a Microsoft operating system)
that is sharing the printer using IPP. You will need to input the IP
address of the printer and the name of the print queue. To use IPP
over an encrypted connection, select "ipps" instead.

**HTTP:** this option allows you to manually type in the URI to the
printer. A list of possible URIs is available on the
`cups site <http://www.cups.org/documentation.php/network.html>`_. To
use HTTP over an encrypted connection, select "https" instead.

**AppSocket/HP JetDirect:** select this option if you are connecting
to an HP network printer. You will need to input the IP address of the
printer. Only change the port number if the printer is using a port
other than the default of 9100. 

**LPD/LPR:** select this option if you are connecting to a printer
which is cabled to a Unix computer that is using LPD to share the
printer. You will need to input the hostname and queue name of the
Unix system.

After inputting the connection information, continue to add the
printer and test the connection by printing a test page as described
in :ref:`Adding a Printer`.

If the default driver is not working, try readding the printer. When
you get to the
:numref:`Figure %s: Viewing the Default Driver <print7a>` screen, try
selecting a different driver.

Alternately, if you have a PPD driver from the manufacturer's website
or on the CD that came with the printer, click "Choose File" to browse
to the location of the PPD file. PPD (PostScript Printer Description)
is a driver created by the manufacturer that ends in a :file:`.ppd`
extension. Sometimes the file will end with a :file:`.ppd.gz`
extension, indicating that it has been compressed. 

.. index:: printing
.. _Printer Troubleshooting:

Printer Troubleshooting
-----------------------

Here are some solutions to common printing problems: 

* **A test page prints but it is all garbled:** this typically means
  that you are using the wrong driver. If your specific model was not
  listed, click :menuselection:`Adminstration --> Modify Printer` for
  the printer in the "Printers" tab. In the screen shown in
  :numref:`Figure %s: Viewing the Default Driver <print7a>`, try
  choosing another driver that is close to your model number. If trial
  and error does not fix the problem, see if there are any suggestions
  for your model in the
  `Open Printing database <http://www.openprinting.org/printers>`_. A
  web search for the word "freebsd" followed by the printer model name
  may also help you to find the correct driver to use.

* **Nothing happens when you try to print:** in this case, type
  :command:`tail -f /var/log/cups/error_log` in a console and then try
  to print a test page. The error messages should appear in the
  console. If the solution is not obvious from the error messages, try
  a web search for the error message. If you are still stuck, post th
  e error, the model of your printer, and your version of TrueOS® as
  you :ref:`Report a Bug`.

.. index:: scanner
.. _Scanner:

Scanning
--------

TrueOS® includes `XSane <http://www.xsane.org/>`_, a graphical utility for managing scanners.

To use your scanner, make sure the device is plugged into the TrueOS® system and click :menuselection:`Browse Applications --> Scanner` or type :command:`xsane` from the
command line. A pop-up message will indicate that XSane is detecting devices and will prompt you to accept the XSane license if a device is detected.
If a device is not detected, search for your device at the `list of supported scanners <http://www.sane-project.org/sane-backends.html>`_. 

.. note:: if the scanner is part of an HP All-in-One device, make sure that the "hplip" package is installed. You can see if the driver is
   installed, and install it if it is not, using :ref:`AppCafe®`.

:numref:`Figure %s: XSane Interface <sane>` shows the XSane interface running on a TrueOS® system attached to an HP OfficeJet.

.. _sane:

.. figure:: images/sane.png

The `XSane documentation <http://www.xsane.org/doc/sane-xsane-doc.html>`_ contains details on how to perform common tasks such as saving an image to a file,
photocopying an image, and creating a fax. It also describes all of the icons in the interface and how to use them.

By default, XSane uses the default browser when you click :kbd:`F1` to access its built-in documentation. How to configure the default browser varies by
window manager so you may need to do an Internet search if you need to set that configuration setting and can not find it. 