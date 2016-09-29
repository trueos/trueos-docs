.. index:: Utilities
.. _Lumina Utilities:

Lumina® Utilities
*****************

|lumina| provides many built-in utilities, which are described in this
chapter.

.. index:: file manager
.. _Insight File Manager:

Insight File Manager
====================
  
The Insight file manager, shown in :numref:`Figure %s <lumina10a>`,
allows the user to easily browse and modify files on the local system on
a per-directory basis. To open Insight, click the start menu and select
:guilabel:`Browse Files`, right-click the desktop and select
:guilabel:`Browse Files`, or type :command:`lumina-fm` from an xterm.

.. _lumina10a:

.. figure:: images/lumina10a.png
   :scale: 100%

   Insight File Manager

It is possible to open additional directories through the tab system
using :kbd:`Ctrl-T` or by clicking :menuselection:`File --> New Browser`,
allowing the user to easily manage multiple locations on the system.
Insight also features the ability to bookmark locations on the system
for instant access via the :guilabel:`star` button. Once a location has
been bookmarked, it will be available via the :guilabel:`Bookmarks`
menu at the top of the window. Removable devices plugged into the sytem
will appear in the :guilabel:`External Devices` menu, if supported by
the operating system. When an item is selected, the icons on the left
side of the screen provide the possible actions that may be taken with
regards to that item. Possible actions include: :guilabel:`open item`,
:guilabel:`open item` (will prompt to select the application to use),
:guilabel:`add item to personal favorites`, :guilabel:`rename item`,
:guilabel:`cut items (add to the clipboard)`,
:guilabel:`copy items to the clipboard`,
:guilabel:`paste items from clipboard`, and :guilabel:`delete items`.
The action buttons are visible by default, but can be made invisible by
clicking :menuselection:`View --> Show Action Buttons`. To disable
thumbnails, uncheck :menuselection:`View --> Load Thumbnails`. Note this
option does not remove thumbnails already loaded; it only prevents
loading thumbnails in new directories. Check
:menuselection:`View --> Show Hidden Files` to display hidden files.

After right-clickin a file or directory, a number of options become
available: :guilabel:`Open`, :guilabel:`Open With` (select the
application), :guilabel:`Rename`, :guilabel:`View Checksums` (shows the
MD5 checksum), :guilabel:`Cut Selection`, :guilabel:`Copy Selection`,
:guilabel:`Paste`, :guilabel:`Delete Selection`,
:guilabel:`File Properties` (such as file type, size, permissions, and
creation date), or :guilabel:`Open Terminal here`.

A few additional options may be available at the bottom of the window,
depending on the directory being viewed and the types of files that are
in it:

* **New File:** The ability to create a new file is available if the
  user has permission to modify the contents of the current directory.

* **New Dir:** The ability to create a new directory is available if the
  user has permission to modify the contents of the current directory.

* **Slideshow:** If there are image files in the directory, this option
  will display those image files as a slideshow and provide arrows for
  going forward or back by one file or to the very beginning or end of
  the file list. Buttons are also provided for deleting the currently
  displayed image or to rotate it, and save the rotation, clockwise or
  counter-clockwise.

* **Play:** This will appear if there are supported multimedia files in
  the directory. The types of files that are supported depends on what
  multimedia plugins are installed on the system. If a particular file
  is not recognized as a multimedia file, install the associated
  multimedia codec using the operating system's application management
  software and restart the file manager.

* **Backups:** If the system is formatted with ZFS and snapshots of the
  current directory are available, this button will appear. Snapshots
  are organized from oldest to newest, with the most recent snapshot
  selected by default, and the contents of the directory at the time of
  that snapshot are displayed. To restore a file or multiple files,
  select them from the list and click :guilabel:`Restore Selection`. If
  those files still exist and need to be overwritten, make sure the
  :guilabel:`Overwrite Existing Files` option is checked first.
  Otherwise, if a file with that name exists, the restore will append a
  number to the end of the filename. For example, the first restored
  version of :file:`testfile.txt` will become :file:`testfile-1.txt`.

.. index:: Lumina File Information
.. _Lumina File Information:

Lumina® File Information
========================

The :command:`lumina-fileinfo` utility can be used to open a graphical
window summarizing the size, permissions and ownership, creation time,
and last modification time of the specified file or directory. In the
example shown in in :numref:`Figure %s <file1a>`, the user has typed
:command:`lumina-fileinfo Downloads` from a terminal
window to view the file information of their :file:`~/Downloads`
directory.

.. _file1a:

.. figure:: images/file1a.png
   :scale: 100%  

   Sample File Information

.. index:: Lumina Information
.. _Lumina Information:

Lumina® Information
===================

This utility provides information about the installed version of
|lumina|, as well as the license, acknowledgements, and project links.
To launch this utility, right-click the desktop and select
:menuselection:`Preferences --> About Lumina`, click the start menu then
the question mark icon in :guilabel:`Preferences`, or type
:command:`lumina-info` in a terminal window. An example is shown in
:numref:`Figure %s <about1c>`.

.. _about1c:

.. figure:: images/about1c.png
   :scale: 100%

   About Lumina

The :guilabel:`General` tab contains a variety of information:

* **Desktop Version:** Indicates the version of |lumina|.

* **OS Build:** Indicates the operating system used to build this
  version of |lumina|.

* **Qt Version:** Click :guilabel:`View Information` to display the QT
  version and its license.

* **Lumina Website:** Click :guilabel:`Lumina Website` to open
  `<http://lumina-desktop.org/>`_ in the default web browser.

* **Ask the Community:** Click :guilabel:`Ask the Community` to open
  `<https://webchat.freenode.net/?channels=%23lumina-desktop>`_, a
  chat channel dedicated to |lumina| with many friendly and helpful
  users.
  
* **Source Repository:** Click :guilabel:`Source Repository` to open
  `<https://github.com/trueos/lumina>`_ in the default web browser.

* **Report a Bug:** Click :guilabel:`Bug Reports` to open
  `<https://bugs.pcbsd.org/projects/pcbsd>`_ in the default web browser.
  Refer to :ref:`Report a Bug` for instructions on how to submit a bug
  report.

The :guilabel:`License` tab contains the license text for |lumina|.
|lumina| is licensed under a
`3-clause BSD license <https://github.com/trueos/lumina/blob/master/LICENSE>`_.

The :guilabel:`Acknowledgements` tab contains the following:

* **Project Lead:** The name of the Project's lead developer. Click the
  name to open his or her profile on GitHub in the default web browser.

* **Contributors:** Click :guilabel:`Open in web browser` link to open
  `<https://github.com/trueos/lumina/graphs/contributors>`_.

* **Sponsors:** lists the official sponsors of the |lumina| Project.

.. index:: application launcher
.. _Lumina Open:

Lumina® Open
============

To open a file, directory, or URL from the command line, type
:command:`lumina-open` followed by the full path to the file or the URL.
This utility will look for an appropriate application to use to open the
specified file or URL. If there is no default application registered for
the input type, a small dialog will prompt the user to select which
application to use, and optionally set it as the default application for
this file type. As seen in the example shown in
:numref:`Figure %s <lumina11b>`, this dialog organizes the available
applications into three types:

.. _lumina11b:

.. figure:: images/lumina11b.png
   :scale: 100%

   Lumina Open

* **Preferred:** These applications have registered their Mime type with
  the system and can open that type of file. Also included are any
  applications that have been used to open this type of file before as
  it keeps track of the last three applications used for that file type.

* **Available:** Displays all the applications installed on the system,
  organized by category and name.

* **Custom:** The user can manually type in the binary name or path of
  the application to use. A search button is also available for the
  user to graphically search the system for the binary. Whenever text
  is entered, a check is performed to determine if it is a valid
  binary and the icon will change between a :guilabel:`green checkmark`
  or a :guilabel:`red X` as appropriate.

.. index:: screenshot
.. _Lumina Screenshot:

Lumina® Screenshot
==================

This utility can be used to take screenshots of the desktop or selected
window and save them as PNG image files. To launch this utility, click
the start menu and select
:menuselection:`Browse Applications --> Utility --> Lumina Screenshot`,
right-click the desktop and select
:menuselection:`Applications --> Utility --> Lumina Screenshot`, type
:command:`lumina-screenshot` from a terminal window, or press :kbd:`Print Screen`.

On the :guilabel:`New Screenshot` tab, seen here in
:numref:`Figure %s <lumina25>`, options are available to fine tune the
screenshot:

.. _lumina25:

.. figure:: images/lumina25.png
   :scale: 100%

   New Screenshot Tab

* **Entire Session:** Captures the entire screen.

* **Single Screen:** In a multi-monitor setup, the screen number can be
  selected for the screenshot.

* **Single Window:** Captures a selected window. Choose
  :guilabel:`Single Window`, click :guilabel:`Take Screenshot`, and
  click the desired window. The :guilabel:`Include Borders` checkbox
  can be used to determine whether or not the utility will take a
  screenshot of the window with its border frame.
  
* **Delay:** Choose the number of seconds to delay the screenshot. This
  can be used to give more time to prepare the screenshot. For example,
  designating a five second delay on a screenshot will give the user
  time to open a temporary menu or hover over an icon, allowing the
  screenshot to include difficult elements to capture.

There are three options for taking a screenshot: clicking
:guilabel:`Take Screenshot` in the lower-right corner of |lumina|
Screenshot, pressing :kbd:`Ctrl+N`, or selecting
:menuselection:`File --> Take Screenshot`.

After capturing a screenshot, the :guilabel:`View/Edit` tab, seen here
in :numref:`Figure %s <lumina9a>`, provides additional options for
manipulating the screenshot:

.. _lumina9a:

.. figure:: images/lumina9a.png
   :scale: 100%

   View/Edit Tab

* **Image Preview:** Displays the captured screenshot. Right-click
  the image to view options for zooming in or out. Click and drag across
  the image to highlight an area which can be cropped by pressing
  :guilabel:`Crop` in the lower-right corner.
  
* **Save As:** Press :guilabel:`Save As` to open a window to specify the
  filename and location for saving the screenshot.

* **Launch Editor:** :guilabel:`Launch Editor` opens a selectable
  image manipulation program.

Additionally, click :menuselection:`File --> Quick Save` to
automatically save the screenshot to the default :file:`/Pictures`
directory and open a window to select an image manipulation program.

.. index:: search
.. _Lumina Search:

Lumina® Search
==============
  
|lumina| Search provides options to find and launch applications or to
quickly search for files and directories. The ***** wildcard can be used
in the search terms and the search will include hidden files if the
search term starts with a dot (**.**).

To start this utility, type :command:`lumina-search`, press
:kbd:`Alt + F2`, or go to the start menu and press
:menuselection:`Browse Applications --> Utility --> Lumina Search`.
:numref:`Figure %s <lumina13b>` shows a screenshot of this utility.

.. _lumina13b:

.. figure:: images/lumina13b.png
   :scale: 100%

   Search for Applications

To open an application, begin to type its name into the search field
(selected by default). The box below the selected :guilabel:`Applications`
button will display any matching application names. Select the desired
application and click :guilabel:`Launch Item` to open it.

Click :guilabel:`Files or Directories` to change the screen slightly,
as seen in :numref:`Figure %s <lumina26>`.

.. _lumina26:

.. figure:: images/lumina26.png
   :scale: 100%

   Search for Files

By default, a :guilabel:`Files or Directories` search is limited to the
user's home directory, as indicated by the :guilabel:`Search: ~` at the
bottom of the screen. :guilabel:`Smart: Off` indicates every
subdirectory is included in the search, with no exlusions. Once
subdirectories have been added to the exclusion list, :guilabel:`Smart:`
will switch to :guilabel:`On`, and the excluded subdirectories will be
shown on the :guilabel:`Search:` section of the menu. To add additional
search directories or to exclude subdirectories, click the
:guilabel:`wrench` icon to see the screen shown in
:numref:`Figure %s <lumina14a>`.

.. _lumina14a:

.. figure:: images/lumina14a.png
   :scale: 100%

   Search Configuration

Click the :guilabel:`blue folder` icon to change the starting search
directory. For example, select :guilabel:`Computer`, then
:guilabel:`/` from the :guilabel:`Select Search Directory` screen to
search the entire contents of the computer. Click :guilabel:`+` to add
directories to an exclusion list for searching. Delete an exclusion by
highlighting its entry and clicking :guilabel:`-`. The
:guilabel:`Save as Defaults` option is selected by default. Uncheck
this option to return the all customized search settings back to their
defaults after closing the menu.

.. index:: textedit
.. _Lumina Text Editor:

Lumina® Text Editor
===================

The :command:`lumina-textedit` utility is a plaintext editor with a
number of basic options. :numref:`Figure %s: <lumina23>`
shows the editor with no file opened.

.. note:: Typing :command:`lte` in the command line will also open the
   |lumina| Text Editor.

.. _lumina23:

.. figure:: images/lumina23.png
   :scale: 100%

   Lumina® Text Edit

Clicking :guilabel:`File` will present options to create **New File**,
**Open File**, **Close File**, **Save file**, **Save File As**, and
**Close**. Click :guilabel:`Edit` to open options to **Find** and
**Replace**, also usable with :kbd:`Ctrl-F` and :kbd:`Ctrl-R`,
respectively. The :guilabel:`View` tab can be used to alter
**Syntax Highlighting**, **Line Numbers**, **Wrap Lines**, and
**Customize Colors**. By default, brackets are highlighted, lines are
numbered, and words will wrap dynamically with the edge of the window.
Additionally, selecting :guilabel:`Customize "Colors` gives the option
to alter all the default text and highlight colors, seen in
:numref:`Figure %s <lumina32>`.

.. _lumina32:

.. figure:: images/lumina32.png
   :scale: 100%

   Customize Colors

.. index:: Xconfig
.. _Lumina Xconfig:

Lumina® Xconfig
===============

The :command:`lumina-xconfig` utility is a graphical front-end to the
:command:`xrandr` command line utility. It provides the ability to probe
and manage any number of attached monitors. To start this utility,
right-click the desktop and select :menuselection:`Preferences --> Display`
or type :command:`lumina-xconfig` from a terminal window. This will open
a screen similar to the one shown in :numref:`Figure %s <lumina15a>`.

.. _lumina15a:

.. figure:: images/lumina15a.png
   :scale: 100%

   Configuring Monitors

In this example, two display inputs are attached to the system and their
current screen resolutions are displayed. If the display input supports
multiple resolutions, they will appear in the :guilabel:`Resolution`
drop-down menu to select a different resolution.

If another display input is attached, the :guilabel:`Add Screen` tab is
activated so the new input's resolution can be configured. Also, the
user can select whether or not it should be the default input.