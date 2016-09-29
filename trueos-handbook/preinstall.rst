Pre-Installation Tasks
**********************

While the TrueOS® installer is very easy to use, installing a brand new
operating system can sometimes be a daunting task.

Before you begin, there are a few things you should check to ensure that
your system is ready to install TrueOS®. 

* **Are you dual-booting or installing over the entire drive?** If you
  are dual-booting you will need to ensure that you have a primary
  partition available. Refer to the section on :ref:`Dual Booting`.

* **Have you backed up your important data?** Any irreplaceable data,
  such as emails, bookmarks, or important files and documents should
  **always** be backed up to an external media, such as a removable
  drive or another system, **before** installing or upgrading any
  operating system.

If you wish to determine if your hardware is detected by TrueOS®, start
an installation and click the "Hardware Compatibility" button in the
:ref:`Language Selection Screen`.

Should you run into an issue with your installation, refer to
:ref:`Installation Troubleshooting`. 

This section discusses the TrueOS® hardware requirements, how to prepare
the system for installation, and how to obtain and prepare the
installation media.

.. index:: hardware
.. _Minimum Requirements:

Minimum Requirements
====================

TrueOS® has moderate hardware requirements and commonly uses less
resources than its commercial counterparts. Before installing TrueOS®,
make sure that your hardware or virtual machine at least meets the
minimum requirements. To get the most out of your TrueOS® experience,
use a system that meets the recommended system requirements.

At a **bare minimum** you need to meet these requirements in order to
install TrueOS®: 

* 64-bit processor

* 1 GB RAM 

* 20GB of free hard drive space on a primary partition for a
  command-line server installation 

* Network card 

The following are the minimum **recommended** requirements. More RAM and
available disk space will improve your computing experience: 

* 64-bit processor 

* 4 GB of RAM 

* 50GB of free hard drive space on a primary partition for a graphical
  desktop installation 

* Network card 

* Sound card 

* 3D-accelerated video card 

TrueOS® does not require 50GB for its installation. Instead, the
minimum recommendation is to provide sufficient room for the
installation of applications and to store local ZFS snapshots and boot
environments which can be used to retrieve earlier versions of files,
rollback the operating system to an earlier point in time, or clone
the operating system.

You can never have too much RAM, so install as much as you can afford.
To play modern video games, you should use a fast CPU. If you want to
create a collection of music and movies on your computer, you will want
sufficient disk space.

.. index:: hardware
.. _Supported Hardware:

Supported Hardware 
==================

If you wish to check your hardware before installing TrueOS®, a good
place to start is the
`FreeBSD Hardware Notes <https://www.freebsd.org/releases/11.0R/hardware.html>`_. 
Another good resource is to start the installer and click the "Hardware
Compatibility" icon.

While most hardware "just works" with TrueOS®, it is possible to run
across a piece of hardware that does not. Since TrueOS® is really
FreeBSD, any hardware that works on FreeBSD will work on TrueOS®. If you
are experiencing problems with a device, start with a web search for the
term "FreeBSD" plus the type and model of the hardware. This will let
you know if there is a known issue with the device. If there are many
search results, concentrate on the most recent ones as often hardware
that used to be problematic has since been fixed or the missing driver
will be available in an upcoming release of FreeBSD. If you experience
problems with a device that should work but does not or you can not find
any existing problem reports for your hardware, you can help improve
hardware support for all FreeBSD and TrueOS® users if you
:ref:`Report a bug` so that it can be addressed by the developers.

The rest of this section provides an overview of the various hardware
that is supported.

Processor
---------

TrueOS® should install on any system containing a 64-bit (also called 
*amd64*) processor. Despite the name, a 64-bit processor does
**not need** to be manufactured by AMD in order to be supported. The
`FreeBSD Hardware Notes - amd64 <https://www.freebsd.org/releases/11.0R/hardware.html#proc-amd64>`_ 
lists the *amd64* processors known to work.

Graphics
--------

Like many open source operating systems, TrueOS® uses
`X.org <https://www.x.org/wiki/>`_ drivers for graphics support.
TrueOS® will automatically detect the optimal video settings for
supported video drivers. You can verify that your graphics hardware is
supported by clicking the "Hardware Compatibility" icon within the
installer.

Support for the major graphic vendors is as follows: 

**NVIDIA:** 3D acceleration on NVIDIA is provided by native FreeBSD
drivers. If an NVIDIA video card is detected, an "nVidia settings" icon will be added to "Browse Applications" for managing NVIDIA settings.

**Intel:** 3D acceleration on most Intel graphics is supported. This
includes Skylake, Haswell, Broadwell, and ValleyView.

**ATI/Radeon:** 3D acceleration on most ATI and Radeon cards is
supported.

**Optimus:** at this time there is no switching support between the two graphics adapters provided by Optimus. Optimus implementations vary, so
TrueOS® may or may not be able to successfully load a graphics driver on
your hardware. If you get a blank screen after installation, check your
BIOS to see if it has an option to disable one of the graphics adapters
or to set "discrete" mode. If the BIOS does not provide a discrete mode,
TrueOS® will default to the 3D Intel driver and disable NVIDIA. This
will change in the future when the NVIDIA driver supports Optimus.

Wireless
--------

TrueOS® has built-in support for most wireless networking cards.
TrueOS® will automatically detect available wireless networks for
supported wireless devices. You can verify that your device is supported
by clicking the "Hardware Compatibility" icon within the installer. If
it an external wireless device, insert it before running the installer.

Certain Broadcom devices, typically found in cheap laptops, are buggy
and can have lockups when in DMA mode. If the device freezes, try
switching to "PIO" mode in the BIOS. Alternately, add the line
*hw.bwn.usedma=0* to :file:`/boot/loader.conf` and reboot to see if that
makes a difference. 

.. index:: laptops
.. _Laptops:

Laptops
-------

Many TrueOS® users successfully run TrueOS® on their laptops. However,
depending upon the model of laptop, you may run across some issues.
These typically
deal with: 

* **Sleep/suspend:** unfortunately, 
  :wikipedia:`Advanced Configuration and Power Interface` (ACPI) is not
  an exact science, meaning that you may have to experiment with various
  :command:`sysctl` variables in order to achieve successful sleep and
  suspend states on your particular laptop model. If your laptop is a
  ThinkPad, `ThinkWiki <http://www.thinkwiki.org/wiki/ThinkWiki>`_ is an
  excellent resource. For other types of laptops, try reading the
  "SYSCTL VARIABLES" section of :command:`man 4 acpi` and check to see
  if there is an ACPI man page specific to your vendor by typing
  :command:`apropos acpi.` The
  `Tuning with sysctl(8) <http://www.freebsd.org/doc/en/books/handbook/configtuning-sysctl.html>`_ 
  section of the FreeBSD Handbook demonstrates how to determine your
  current :command:`sysctl` values, modify a value, and make a modified
  value persist after a reboot. If the battery reading is incorrect, try
  the workaround in this
  `PR <https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=160838>`_.

* **Synaptics:** depending upon the hardware, you may or may not be able
  to disable the system's touchpad. This
  `forum post <https://forums.freebsd.org/threads/17370/#post-100670>`_ 
  describes how to enable Synaptics and some of the :command:`sysctl`
  options that this feature provides.

If you wish to test your laptop's hardware, use the "Hardware
Compatibility" icon in the :ref:`Language Selection Screen` before
continuing with the installation.

If you would like to install TrueOS® onto an Asus Eee PC, review the
`FreeBSD Eee page <https://wiki.FreeBSD.org/AsusEee>`_ first.

The 
`FreeBSD Tuning Power Consumption page <https://wiki.FreeBSD.org/TuningPowerConsumption>`_ 
has some tips for reducing power consumption.

.. index:: thinkpad

With regards to specific hardware, the ThinkPad T420 may panic during
install. If it does, go into the BIOS and set the video mode to
"discrete" which should allow you to complete an installation. Some
Thinkpads have a BIOS bug that prevents them from booting from
GPT-labeled disks. If you are unable to boot into a new installation,
restart the installer and go into "Advanced Mode" in the
:ref:`Disk Selection Screen`. Make sure that the  “GPT (Best for new
hardware)” box is unchecked. If it was checked previously, redo the
installation with that box unchecked.

.. index:: partition
.. _Creating Free Space:

Creating Free Space
===================

If you wish to dual-boot TrueOS® with an existing operating system, you
must first make sure that there is either a free partition or an area of
free space to use. For example, if you are currently running a
Windows operating system, it usually occupies the entire hard drive.
You will need to first shrink the partition that contains the current
operating system to make room to install TrueOS®. Shrinking is
an operation that retains the current operating system while reducing
the size of its partition. This section demonstrates how to create free
space within Windows 10.

.. warning:: **Before** shrinking a partition, make sure that you first
  back up your valuable data to an external media such as a removable
  USB drive!

To shrink the drive, right-click the "Start" menu and click
"Disk Management". In the example shown in
:numref:`Figure %s: Viewing Disk Layout in Disk Management <partition1>`, 
the Windows system has three partitions: a 450MB recovery partition, a
237.93GB data partition, and a 100MB system partition.

.. _partition1:

.. figure:: images/partition1.png

Since the three Windows partitions fill the entire disk, the data
partition must be shrunk to create space to install TrueOS®. Right-click
the data partition (in this example, the *(C:)* partition),
and select "Shrink Volume" as shown in
:numref:`Figure %s: Shrink Volume Menu Selection <partition2>`.

.. _partition2:

.. figure:: images/partition2.png

Wait a
moment as the volume is queried for available shrink space. The results
are shown in
:numref:`Figure %s: Available Shrink Space <shrink1>`. 

.. _shrink1:

.. figure:: images/shrink1.png

Here, 119307MB of space is available. This is the maximum amount
Windows can shrink this particular partition. Accept that number, or
choose a smaller number for a smaller TrueOS® partition.  Click the
"Shrink" button to begin the shrinking process.  This procedure can
take several minutes to complete. When finished, the newly created
free space will be displayed as seen in
:numref:`Figure %s: Disk Now Has Free Space <shrink2>`.

.. _shrink2: 

.. figure:: images/shrink2.png

.. warning:: It is important that you **do not** choose to install
   TrueOS® into any of the three Windows partitions when you get to the
   :ref:`Disk Selection Screen` of the installer. It is a good idea to
   write down the sizes of all of the partitions so that you will
   recognize the free space when the TrueOS® installer displays your
   current partitions.

.. _Obtaining TrueOS®:

Obtaining TrueOS®
==================

TrueOS® uses a rolling release model rather than versioned releases.
This model...

Around the 1st of each month, :ref:`Update Manager` will  provide a patch which will update the operating system to include all
  of the new features and drivers. If you wish to have or test the
  latest features and drivers as they become available and can tolerate
  possible breakage caused by new features being available before the
  next RELEASE, use the STABLE version.

Installation files can be downloaded from the
`TrueOS® website <https://www.trueos.org/downloads/>`_ or the `PC-BSD® CDN <http://iso.cdn.pcbsd.org/>`_. 

Several types of files are available for download. Before downloading
a file, review the following descriptions to see which one best suits
your needs: 

* Files beginning with :file:`TrueOS-Desktop` contain all of the
  information needed to install either a graphical desktop or
  command-line server using a graphical installer. If the file has an 
  :file:`.iso`  extension, it should be burned to a DVD media. If it
  has a :file:`img` extension, it should be burned to a USB stick.
  There will also be associated files with the same name but ending in
  an :file:`.md5` or :file:`.sha256` extension. Depending upon your
  current operating system and its tools, you can use the value in
  either one of those files to determine the integrity of the
  download, as described in :ref:`Data Integrity Check`. If a torrent
  is available, there will also be a file with the same name and a
  :file:`.torrent` extension.

* Files beginning with :file:`TrueOS-Server` contain a command-line
  installer and are used to install a command-line version of a
  server. If the file has an  :file:`.iso`  extension, it should be
  burned to a CD media. If it has a :file:`img` extension, it should
  be burned to a USB stick. There will also be associated files with
  the same name but ending in an :file:`.md5` or :file:`.sha256`
  extension. Depending upon your current operating system and its
  tools, you can use the value in either one of those files to
  determine the integrity of the download, as described in
  :ref:`Data Integrity Check`. If a torrent is available, there will
  also be a file with the same name and a :file:`.torrent` extension.

If you plan to install a graphical desktop, download the file with
:file:`TrueOS-Desktop` in its name and either burn it to a DVD media
or write it to a removable USB device.

If you prefer to install a command-line only server, you can either
download a file beginning with :file:`TrueOS-Desktop` (to use the
graphical installer) or :file:`TrueOS-Server` (to use the command-line
installer). The :file:`TrueOS-Server` files are smaller and can fit on
CD.

Refer to :ref:`Burning the Installation Media` for instructions on how
to burn the downloaded file to bootable media.

Members of the TrueOS® project attend many IT conferences across the
globe and give out TrueOS® DVDs at the FreeBSD booth. Visiting a
FreeBSD booth is an excellent way to meet other TrueOS® and FreeBSD
users and to get your questions answered. Check the
`TrueOS® Blog <https://www.trueos.org/blog/>`_ to see if any events
are happening near you. If you are organizing a TrueOS® booth, contact
us `on Gitter <https://gitter.im/trueos/Lobby>`_ to arrange for DVDs.

.. index:: checksum
.. _Data Integrity Check:

Data Integrity Check 
---------------------

After downloading the desired file, it is a good idea to check that the
file is exactly the same as the one on the TrueOS® download server.
While downloading, a portion of the file may get damaged or lost, making
the installation file unusable. Each TrueOS® installation file has an
associated MD5 and SHA256 checksum. If a checksum of the file you
downloaded matches, your download was successful. If a checksum does not
match, try downloading the file again. In order to verify a checksum, 
use a checksum verification utility.

.. note:: You only need to verify one of the checksums. The
   `PC-BSD® website <http://www.pcbsd.org/download/>`_  lists the
   SHA256 while the `PC-BSD® CDN <http://iso.cdn.pcbsd.org/>`_ lists
   both the :file:`.md5` and the :file:`.sha256` checksum files. This
   section demonstrates how to verify an SHA256 checksum.

If you are currently using a Windows system, you can download and
install a utility such as
`Raymond's MD5 & SHA Checksum Utility <http://download.cnet.com/MD5-SHA-Checksum-Utility/3000-2092_4-10911445.html>`_.
This utility can be used to simultaneously check the MD5, SHA-1,
SHA-256, and SHA-512 checksums of any file. Once installed, launch the
program and use the "Browse" button, shown in
:numref:`Figure %s: Verifying a Checksum <fastsum1>`, to browse to the
location of your downloaded file.

.. _fastsum1:

.. figure:: images/checksum.png

Once the file is selected, click the "Open" button to calculate the
checksums. It may take a minute or so, depending upon the size of the
downloaded file.

On Linux and BSD systems you can use the built-in :command:`md5` or
:command:`md5sum` command line tool to check the MD5 checksum. In this
example, the file is located in the :file:`Downloads` directory. You
should substitute the name and location of the file that you
downloaded::

 md5 Downloads/TrueOS-Desktop-2016-08-11-x64-DVD.iso.md5

.. index:: burn
.. _Burning the Installation Media:

Burning the Installation Media
==============================

Once you have downloaded the installation file and verified its
checksum, you are ready to burn it to a media. Which media depends
upon the file you downloaded:

* Files beginning with :file:`TrueOS-Desktop` and ending with
  :file:`.iso` must be burned to a DVD. 
  
* Files beginning with :file:`TrueOS-Server` and ending with
  :file:`.iso` should be burned to a CD. 
  
* Files ending in :file:`img` must be burned to a USB stick.

To burn to a CD or DVD, use either a burning utility that came with
the operating system on the system with the burner or a burning
application. Table 2.5a lists some freely available burning utilities.

**Table 2.5a: Free Burning Utilities**

+-------------------------+-------------------------------------------------------------------------------------------------+
| **Operating System**    | **Utility**                                                                                     |
+=========================+=================================================================================================+
| Windows                 | `InfraRecorder utility <http://infrarecorder.org/>`_                                            |
+-------------------------+-------------------------------------------------------------------------------------------------+
| Windows                 | `Disk Burner <http://windows.microsoft.com/en-US/windows7/Burn-a-CD-or-DVD-from-an-ISO-file>`_  |
+-------------------------+-------------------------------------------------------------------------------------------------+
| Linux or \*BSD          | `K3B <https://www.kde.org/applications/multimedia/k3b/>`_                                       |
+-------------------------+-------------------------------------------------------------------------------------------------+
| Linux or \*BSD          | `Brasero <https://wiki.gnome.org/Apps/Brasero>`_                                                |
+-------------------------+-------------------------------------------------------------------------------------------------+
| FreeBSD/PC-BSD/TrueOS   | `growisofs <https://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/creating-dvds.html>`_    |
+-------------------------+-------------------------------------------------------------------------------------------------+
| Mac OS X                | `Disk Utility <https://support.apple.com/kb/PH20577?locale=en_US>`_                             |
+-------------------------+-------------------------------------------------------------------------------------------------+


.. index:: burn
.. _Writing to a USB Device:

Writing to a USB Device
-----------------------

To write the :file:`img` file to a USB device, you will need the
following: 

* a utility that can write the image to a USB media; the utility that
  you use will depend upon your operating system 

* a USB thumb drive or hard drive large enough to hold the image 

.. note:: If there is a card reader on the system or the USB drive is
   connected using a USB dongle, device enumeration may be affected. For
   example, with the USB card reader dongle as the destination, the
   device name could be :file:`/dev/da1` instead of :file:`/dev/da0`.

To write the :file:`.img` file to a flash card or removable USB drive on
a BSD or Linux system, use the :command:`dd` command line utility. On a
FreeBSD system, the superuser can use this command to write the file to
the first plugged in USB device:

.. code-block:: none

 dd if=TrueOS-Desktop-2016-08-11-x64.img of=/dev/da0 bs=1M
 1415+1 records in
 1415+1 records out
 1483990016 bytes transferred in 238.552250 secs (6220818 bytes/sec)

When using the :command:`dd` command: 

* **if=** refers to the input file to be written

* **of=** refers to the output file (the device name of the flash card
  or removable USB drive); increment the number in the name if it is not
  the first USB device 

* **bs=** refers to the block size 

.. note:: On Linux, if you type :command:`mount` with the USB stick
   inserted, you will see two or more device nodes corresponding to the
   USB stick. For example, :file:`/dev/sdc` and :file:`/dev/sdc1`, where
   :file:`/dev/sdc1` corresponds to the primary partition of the USB
   stick. Before using the :command:`dd` command, ensure that the USB
   stick is first unmounted. Then, remember to use :file:`/dev/sdc` (the
   device node without the number) as the option for the output file
   **of=**. Once the :command:`dd` completes, you might not be able to
   mount the USB stick on Linux as Linux has very limited support for
   UFS, the BSD filesystem that gets created on the USB stick.

To burn the image file on a Windows system, you can use
`win32-image-writer <https://sourceforge.net/projects/win32diskimager/>`_.
When downloading win32-image-writer, download the latest version that
ends in :file:`-binary.zip` and use a utility such as Windows Explorer
or 7zip to unzip the executable.

If you launch :command:`win32-image-writer.exe`, it will start the Win32 Disk Imager utility, shown in :numref:`Figure %s: Using Win32 Disk Imager to Write the Image <writer1>`. Use the
"browse" button to browse to the location of the :file:`.iso` file. Insert a USB thumb drive and select its drive letter (in this example, drive D). Click the "Write" button and the image
will be written to the USB thumb drive.

.. _writer1:

.. figure:: images/writer1.png

To burn the :file:`.iso` file on Mac OS X, insert a USB stick and open
Terminal. Run the :command:`diskutil list` command to find out the
device name of the USB disk, unmount the USB disk, then use
:command:`dd` to write the image to the raw disk (:file:`rdisk`). In the
following example, an 8GB USB stick has a device name of
:file:`/dev/disk1` and a raw device name of :file:`/dev/rdisk1`.:

.. code-block:: none

 diskutil list 
 /dev/disk0
 #: TYPE NAME SIZE IDENTIFIER
 0: GUID_partition_scheme *500.1 GB disk0
 1: EFI 209.7 MB disk0s1
 2: Apple_HFS Macintosh HD 499.2 GB disk0s2
 3: Apple_Boot Recovery HD 650.0 MB disk0s3 
 /dev/disk1
 #: TYPE NAME SIZE IDENTIFIER
 0: FDisk_partition_scheme *8.0 GB disk1
 1: DOS_FAT_32 UNTITLED 8.0 GB disk1s1

 diskutil unmountDisk /dev/disk1
 Unmount of all volumes on disk1 was successful

 sudo dd if=/Users/dru/Downloads/TrueOS-Desktop-2016-08-11-x64.img of=/dev/rdisk1 bs=4m
 Password:
 1415+1 records in
 1415+1 records out
 1483990016 bytes transferred in 238.552250 secs (6220818 bytes/sec)

.. index:: virtualization
.. _Virtualization:

Virtualization
==============

A virtualized environment allows you to test drive an operating system
without overwriting your current operating system. This is an excellent
way to practice installation, determine whether all of your hardware is
supported, or to try multiple versions of different operating systems.
Virtualization software effectively creates windows (known as virtual
machines) into which you can install and use an operating system. The
only limitation to virtualization is your hardware as each virtual
machine uses CPU and RAM. Depending upon the amount of CPU and RAM in
your computer, you may find that the operating system you install using
virtualization software runs slowly. If your computer slows down, try
closing other applications running on your computer to free up some RAM.

If you would like to run virtualization software on a TrueOS® system,
search for "virtualbox" within :ref:`AppCafe®` and install the
`VirtualBox <https://www.virtualbox.org/>`_ open source virtualization
program and the
`VirtualBox Guest Additions <http://www.virtualbox.org/manual/ch04.html>`_ . 
The guest additions add mouse pointer integration, shared folders
between the host and guest, better video support, and a shared
clipboard.

.. note:: The first time you run VirtualBox on a TrueOS® system, a
   background script will automatically give your user account the 
   permissions required to run this application. This might break any
   existing shortcuts to VirtualBox. To fix the shortcut, logout and back in.

If your computer is running another operating system, download the
binary for your operating system from the
`VirtualBox Downloads page <https://www.virtualbox.org/wiki/Downloads>`_. 
VirtualBox runs on Windows, Linux, Macintosh, and OpenSolaris and
supports a large number of operating systems that can be installed into
a virtual machine.

This section describes how to prepare VirtualBox for an installation of
TrueOS® using an :file:`.iso` file.

.. index:: virtualization
.. _Creating a Virtual Machine for an ISO File:

Creating a Virtual Machine for an ISO File
------------------------------------------

Once you have downloaded the TrueOS® ISO and installed VirtualBox on the
current system, create a virtual machine and use the ISO to install
TrueOS® into the virtual machine. The virtual machine must meet the
following minimum requirements and this section will demonstrate how to
configure these:

* 1024 MB base memory size 

* a virtual disk **at least 20 GB in size** for a server installation or
  **at least 50 GB in size** for a desktop installation 

* a bridged adapter 

To create the virtual machine, start VirtualBox to see the screen shown
in :numref:`Figure %s: Initial VirtualBox Screen <vbox1>`. 

.. _vbox1:

.. figure:: images/vbox1.png

Click the "New" button to start the new virtual machine wizard and
display the screen in
:numref:`Figure %s: Type in a Name and Select the Operating System for the New Virtual Machine <vbox2>`.

.. _vbox2:

.. figure:: images/vbox2.png

Enter a name for your virtual machine, which can be anything that makes
sense to you. Click the "Operating System" drop-down menu and select
"BSD". In the "Version" drop-down menu, select "FreeBSD (64 bit)". Click
"Next" to see the screen in
:numref:`Figure %s: Select the Amount of Memory Reserved for the Virtual Machine <vbox3>`.

.. _vbox3:

.. figure:: images/vbox3.png

The base memory size must be changed to **at least 1024 MB.** If your
system has a lot of RAM, use more. Any number within the green area is
considered a safe value by VirtualBox, meaning it should not slow down
your computer too much. When finished, click Next to see the screen in
:numref:`Figure %s: Select Whether to Use an Existing or Create a New Virtual Hard Drive <vbox4>`.

.. _vbox4:

.. figure:: images/vbox4.png

This screen is used to create the virtual hard drive, or the amount of
disk space that will be available to the virtual machine. If this is your
first virtual machine, keep the default of "Create a virtual hard drive
now" and click "Create" to go to the screen shown in
:numref:`Figure %s: Select the Hard Drive Type <vbox5>`. If you have
created a virtual machine in the past and wish to reuse its disk space,
select "Use an existing virtual hard drive file" from the drop-down
menu. You can create as many virtual machines as you wish. However, if
your computer is getting low on disk space, you should consider reusing
existing virtual hard drives to prevent your physical hard drive from
being used up by old virtual machines.

.. _vbox5:

.. figure:: images/vbox5.png

Select "VDI" and click the "Next" button to see the screen in
:numref:`Figure %s: Select the Storage Type <vbox6>`.

.. _vbox6:

.. figure:: images/vbox6.png

You can now choose whether you want "Dynamically allocated" or "Fixed
size" storage. The first option uses disk space as needed until it
reaches the maximum size that you will set in the next screen. The
second option creates a disk the same size as that specified amount of
disk space, whether it is used or not. Choose the first option if you
are worried about disk space; otherwise choose the second option as it
allows VirtualBox to run slightly faster. Once you select "Next", you
will see the screen in
:numref:`Figure %s: Select the File Name and Size of the Virtual Disk <vbox7>`.

.. _vbox7:

.. figure:: images/vbox7.png

This screen is used to set the size (or upper limit) of the virtual
machine. If you plan to install TrueOS® into the virtual machine,
**increase the size to at least 20 GB** or you will receive an error
during the TrueOS® installation. If you plan to install KDE, GNOME,
multiple desktop managers, or applications within the virtual machine,
you will probably want to choose at least 50GB. Whatever size you set,
make sure that your computer has enough free disk space to support it.
Use the folder icon to browse to a directory on disk with sufficient
space to hold your virtual machine.

Once you make your selection, press "Create" to finish using the wizard.
Your virtual machine will now show up in the left box, as seen in the
example in :numref:`Figure %s: The New Virtual Machine <vbox8>`.

.. _vbox8:

.. figure:: images/vbox8.png

In order to use your network card, configure bridging on your virtual
machine. To do this, go to :menuselection:`Settings --> Network`. In
the "Attached to" drop-down menu select "Bridged Adapter" then select
the name of the physical interface from the "Name" drop-down menu. In
the example shown in
:numref:`Figure %s: Configuring a Bridged Adapter in VirtualBox <vbox9>`, 
the Intel Pro/1000 Ethernet card is attached to the network and has a
device name of :file:`re0`.

.. _vbox9:

.. figure:: images/vbox9.png

Before starting your virtual machine, configure it to use your
installation media. Click the "Storage" hyperlink in the right frame to
access the storage screen seen in
:numref:`Figure %s: The Storage Settings of the Virtual Machine <vbox10>`.

.. _vbox10:

.. figure:: images/vbox10.png

Double-click the word "Empty", which represents your DVD reader. If you
wish to access the TrueOS® installer from your DVD reader, double-check 
that the "Slot" is pointing to the correct location (e.g. "IDE Secondary
Master") and use the drop-down menu to change it if the location is
incorrect.

If you prefer to use an ISO that is stored on your hard disk, click the
DVD icon then "Choose a virtual CD/DVD disk file" to open a browser menu
where you can navigate to the location of the ISO. Highlight the desired
ISO and click "Open". The name of the ISO will now appear in the
"Storage Tree" section.

You are now ready to install TrueOS® into your virtual machine.
Highlight the virtual machine and click on the green "Start" icon. A
window will open indicating that the virtual machine is starting. If you
have a DVD inserted, you should hear it spin and it should start to boot
into the installation program. If it does not or if you are using an ISO
stored on the hard disk, press "F12" to select the boot device when you
see the message to do so, then press "c" to boot from CD-ROM. You can
then proceed through the installation as described in :ref:`Installing TrueOS®`.
