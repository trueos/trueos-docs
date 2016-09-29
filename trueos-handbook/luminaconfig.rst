.. index:: configuration
.. _Lumina Configuration:

Lumina® Configuration
*********************

The |lumina| Configuration utility, shown in
:numref:`Figure %s <lumina3d>`, can be used to configure every aspect
of the desktop and is the recommended way to make changes. To launch
this utility, click the start menu then
:menuselection:`Preferences --> Configure Desktop`, right-click the
desktop and click :menuselection:`Preferences --> Desktop`, or type
:command:`lumina-config` from an xterm. If all those options are
unavailable, the "Desktop Configuration" application (under the
"Utilities" category) will also open the configuration utility.

.. _lumina3d:

.. figure:: images/lumina3d.png
   :scale: 100%
   
   Lumina Desktop Configuration

Under the top search bar are four options to configure different areas
of the system. Clicking a category will expand the configuration options
of that category, and clicking an option will open those configuration
options.

.. note:: If you make changes to any of the options, remember to click
   :guilabel:`Save Changes` before exiting this utility in order to save
   them.

The rest of this section describes the configurations that are available
in each category.

.. index:: appearance, wallpaper
.. _Appearance:

Appearance
==========

This category is used to change the visual appearance and functionality
of the desktop on a per-screen basis. The
:guilabel:`Change Desktop Theme` option, shown in
:numref:`Figure %s <lumina17d>`, can be used to change the default
font, font size, theme template, color scheme, icon pack, and mouse
cursors.

.. _lumina17d:

.. figure:: images/lumina17d.png
   :scale: 100%

   Modifying the Theme

It is possible to create your own **theme template** or **color scheme**
by clicking :guilabel:`Edit` next to those options and changing the
settings as necessary. :numref:`Figure %s <lumina18c>`
shows an example of clicking :guilabel:`Edit` with the
:guilabel:`Glass (System)` theme template selected. This action opened
the :guilabel:`Theme Editor` and the user has clicked the color selector
(dropper icon) in the upper right corner. Select an item in this menu to
edit the template controlling the selection by changing the values in
the theme editor box. Note the theme templates are written as
`Qt stylesheets <http://doc.qt.io/qt-5/stylesheet.html>`_, so some
scripting experience will be helpful when configuring a theme. After
making your changes, click :guilabel:`Save` to save the theme without
closing the editor, or click :guilabel:`Apply`, which saves the theme
and closes the editor.

.. _lumina18c:

.. figure:: images/lumina18c.png
   :scale: 100%
   
   Using the Theme Editor

The "Change Wallpaper" option, shown in :numref:`Figure %s <lumina27>`,
can be used to add a wallpaper with :guilabel:`+`, or remove with
:guilabel:`-`. When :guilabel:`+` is pressed, the drop-down menu can be
used to select the file(s), a single directory, a directory and all of
its subdirectories, or a solid color to use as the wallpaper. If
multiple images are selected, :guilabel:`Rotate Background` can be
selected as well as a specified time interval in minutes to move to the
next image.

.. _lumina27:

.. figure:: images/lumina27.png
   :scale: 100%
   
   |lumina| Wallpaper Settings

Click the :guilabel:`Layout` drop-down menu to change the default
layout of :guilabel:`Automatic` to one of several options:
*Full Screen*, *Fit Screen*, *Tile*, *Center*, *Top Left*, *Top Right*,
*Bottom Left*, or *Bottom Right*.

Click :menuselection:`+ --> Solid Color` to view all the wallpaper
options, shown in :numref:`Figure %s <lumina16b>`. Select a color and
click :guilabel:`OK` and it will be added as a solid color background to
the wallpaper selection drop-down menu.

.. _lumina16b:

.. figure:: images/lumina16b.png
   :scale: 100%
   
   Modifying the Wallpaper
   
:guilabel:`Window Effects`, shown in :numref:`Figure %s <lumina28>`, is
used to add or alter graphical effects or animations applied to your
windows. By default, no additional effects are added and will need to be
adjusted manually.

.. _lumina28:

.. figure:: images/lumina28.png
   :scale: 100%

   Window Effects

:guilabel:`Window Manager`, shown in :numref:`Figure %s <lumina22c>`,
contains various configuration options for the window manager.

.. _lumina22c:

.. figure:: images/lumina22c.png
   :scale: 100%

   Session Window Manager

Drop-down menus are provided for configuring all options:

* **Number of Workspaces:** A maximum of *10* workspaces can be defined,
  with a default of *2*.

* **New Window Placement:** Indicates where new windows are placed on
  the screen. Choices are *Align in a Row*, *Align in a Column*,
  *Cascade", or *Underneath Mouse*.

* **Focus Policy:** Indicates when windows receive focus. Choices are
  *Click to Focus*, *Active Mouse Focus*, or *Strict Mouse Focus*.

* **Window Theme:** Controls the appearance of the frame around
  application windows. The :guilabel:`Window Theme Preview` screen can
  be used to preview the selected theme.

The :guilabel:`Advanced Editor`, seen in
:numref:`Figure %s <lumina29>`, provides options to manually adjust
every setting related to the display of windows on the system.

.. _lumina29:

.. figure:: images/lumina29.png
   :scale: 100%

   Window Manager - Advanced

.. index:: application startup shortcuts

.. _DesktopSession Options:

Desktop Session Options
=======================

:guilabel:`Desktop Sessions Options`, seen in
:numref:`Figure %s <lumina3d>`, are used to configure which
applications automatically start upon logging in to |lumina|, the
default applications and file types, and keyboard shortcuts.

Click :guilabel:`Default Applications for File Type` to view the
:guilabel:`Basic Settings` tab, shown in
:numref:`Figure %s <lumina24a>`. This tab can be used to configure
default applications.

.. _lumina24a:

.. figure:: images/lumina24a.png
   :scale: 100%

   Lumina Default Applications - Basic

The default web browser, email client, file manager,and virtual
terminal are all configurable. Click the desired application, and a new
window will appear, allowing a new default application to be chosen. To
return to the default application, click the current application's name,
then :guilabel:`Restore Defaults`.

.. note:: Some applications, such as web browsers, keep their own
   internal lists of default applications for opening particular types
   of files. These applications, when configured to use the
   :command:`lumina-open` or :command:`xdg-open` utilities, will refer
   back to the default applications set in
   :guilabel:`Default Applications for File Type`.

The :guilabel:`Advanced` tab allows for configuring the default
application used for particular file types, as seen in
:numref:`Figure %s <lumina7e>`.

.. _lumina7e:

.. figure:: images/lumina7e.png
   :scale: 100%

   Lumina Default Applications - Advanced

To add an application, select the file type and specific group and
either click :guilabel:`Set App`, which will open a drop-down menu of
common applications, or :guilabel:`Set Binary`, which will open a file
browser for navigating the application path. Alternately, selecting only
a file type and clicking :guilabel:`Set App` or :guilabel:`Set Binary`
will register the application for all the groups within the selected
type. Selecting :guilabel:`Clear` will remove the default application
from the associated file type or group.

:guilabel:`Keyboard Shortcuts`, shown in
:numref:`Figure %s <lumina8c>`, is used to configure various keyboard
shortcuts for system or window tasks. Most of these options relate to
window and workspace management, such as moving windows between
workspaces, but there are also options for changing the system audio
volume or screen brightness.

.. _lumina8c:

.. figure:: images/lumina8c.png
   :scale: 100%

   Lumina Keyboard Shortcuts - Basic

To create a shortcut, click the desired entry, then
:guilabel:`Change Shortcut`, and define the desired key combination.
Any entry with an already defined shortcut showing in the
:guilabel:`Keyboard Shortcut` column can **not** be assigned to another
action. To free a shortcut for reuse, highlight the shortcut, click
:guilabel:`Clear Shortcut`, then :guilabel:`Save Changes`. A new
shortcut can now be created.

Click :guilabel:`Advanced Editor`, seen in :numref:`Figure %s <lumina30>`,
to manually adjust or create all keyboard shortcuts. By default, syntax
codes are shown in their own display area, but this can be hidden by
unchecking :guilabel:`View Syntax Codes`.

.. _lumina30:

.. figure:: images/lumina30.png
   :scale: 100%

   Lumina Keyboard Shortcuts - Advanced

:guilabel:`Startup Services and Applications`, displayed in
:numref:`Figure %s <lumina6e>`, provides adjustment options for what is
automatically started when logging into |lumina|.

.. _lumina6e:

.. figure:: images/lumina6e.png
   :scale: 100%

   Lumina Startup Services

To prevent an application from starting automatically, uncheck its box.
To add an application to the auto-start configuration , click
:guilabel:`Application` to select the application's name from a
drop-down menu. Alternately, click :guilabel:`Binary` or
:guilabel:`File` to browse to the location of the application or file to
open. If a file name is chosen, |lumina| will automatically open it in
an application that is capable of reading the file type.

.. index:: menu panel

.. _Interface:

Interface Configuration
=======================

:guilabel:`Interface Configuration`, as seen in
:numref:`Figure %s <lumina31>`, is used to configure the context
(right-click menu), desktop icons, and floating panels.

.. _lumina31:

.. figure:: images/lumina31.png
   :scale: 100%

   |lumina| Interface Configuration

.. note:: The options of :guilabel:`Context Menu and Plugins`,
   :guilabel:`Desktop Icons and Plugins`, and
   :guilabel:`Floating Icons and Plugins` involve modifying and
   interacting with plugins, which are described at length in the
   :ref:`Lumina Plugins` chapter of this handbook.

Click :guilabel:`Context Menu and Plugins` to adjust the appearance of
the menu which appears when right-clicking the desktop. By default, the
context menu includes the several plugins: **Terminal**,
**File Manager**, **Applications**, a **Separator**, and **Settings**.

Select :guilabel:`Desktop Icons and Plugins` to modify what appears on
the current primary desktop. By default, the :ref:`RSS Reader` plugin
will appear in the lower right corner.

Many customization options are available after right-clicking an icon on
the desktop:

* **Start Moving Item:** Click the icon to lock it in place once it is
  in the desired location.
* **Start Resizing Item:** Use the mouse to increase or decrease size.
  Click when finished adjusting the icon to save the changes.
* **Increase Desktop Icon Sizes:** Increases the size of all desktop
  icons, repeat as necessary.
* **Decrease Desktop Icon Sizes:** Decreases the size of all desktop
  icons, repeat as necessary.
* **Remove Item:** Removes the item from the desktop.

The :guilabel:`Floating Panels and Plugins` option offers the ability to
create and/or customize panels which are attached to the edges of the
screen, as seen in :numref:`Figure %s <lumina5f>`.

.. _lumina5f:

.. figure:: images/lumina5f.png
   :scale: 100%

   Lumina Panel Configuration

This screen can be used to customize the location, alignment, size,
theme, and plugins for an existing panel. The :guilabel:`+` and
:guilabel:`-` icons towards the top, next to :guilabel:`Panel 1` can be
used to add or remove additional panels. Panels must be aligned along a
screen edge, opposite screen edges in the case of two panels, and may
have any width, color, or transparency.

.. note:: When adding panels, a frame similar to :guilabel:`Panel 1`
   will be created for each panel, labeled :guilabel:`Panel 2`,
   :guilabel:`Panel 3`, and so on. This allows each panel to be
   configured separately. The configuration tabs available for a panel
   are described below. Be sure to select the tab in the desired panel.

The :guilabel:`Location` tab (4 arrow icon) contains a number of items:

* **Edge:** This drop-down menu can be used to set the location of the
  panel which can be *Top*, *Bottom*, *Left*, or *Right*.

* **Alignment:** This drop-down menu can be used to center the panel on
  the edge or pin it to one of the corners.

* **Size:** Can be used to specify the panel width in pixels and the
  panel length.

The :guilabel:`Appearance` tab (monitor icon) is shown in
:numref:`Figure %s <lumina19d>`.

.. _lumina19d:

.. figure:: images/lumina19d.png
   :scale: 100%

   Panels Appearance Tab

To hide the panel unless the mouse is hovered over it, check
:guilabel:`Auto-hide Panel`. The :guilabel:`Custom Color` option can be
used to fine-tune the panel color. Click its box, then the paint icon to
select a panel color.

The :guilabel:`Plugins` tab (puzzle icon) is shown in
:numref:`Figure %s <lumina20d>`.

.. _lumina20d:

.. figure:: images/lumina20d.png
   :scale: 100%

   Panels Plugins Tab

To add a plugin as an icon to the panel, click :guilabel:`+` below the
listed plugins and select a plugin from the list that appears. To remove
a plugin, highlight it and click :guilabel:`-`, which is below the
listed plugins. The arrow buttons can be used to move the location of
the plugin on the panel. The top of an ordered list corresponds to
either the top of a vertical panel or the left side of a horizontal
panel.

By default, |lumina| will have one panel which stretches across the
bottom of the primary screen and another auto-hiding panel centered at
the top of the screen. The bottom panel incorporates the
:ref:`Panel Start Menu`, :ref:`Task Manager Plugin (No Groups)`, a
:ref:`Spacer`, :ref:`System Tray`, :ref:`Time Date`, and
:ref:`Battery Monitor` plugins. The top panel includes the
:ref:`Desktop Bar` between two :ref:`Spacer` plugins.

.. index:: user settings

.. _User Settings:

User Settings
=============

The :guilabel:`User Settings` option governs the general settings for
the desktop session. Typically, these settings are infrequently changed.

:guilabel:`General Options`, seen in :numref:`Figure %s <lumina12f>`,
is used to govern numerous settings for the desktop experience.

.. _lumina12f:

.. figure:: images/lumina12f.png
   :scale: 100%

   |lumina| General Options

The user can choose to automatically enable numlock, play chimes when
|lumina| starts or exits, and change the icon that appears in the login
menu and the start menu button. There are also options to set the time
and date format, as well as the time display format (using a drop menu).
Additionally, a user can reset **all** their desktop settings via
:guilabel:`Return to system defaults`, which returns |lumina| to the
defaults created by the OS, while :guilabel:`Return to Lumina® defaults`
returns to the |lumina| created settings.

The :guilabel:`Localization Settings` is shown in
:numref:`Figure %s <lumina21c>`.

.. _lumina21c:

.. figure:: images/lumina21c.png
   :scale: 100%

   Session Locale Tab

The **lumina-i18n** package provides localization files. Once installed,
this allows customization of the locale used for the various items
listed in :numref:`Figure %s <lumina21c>`. To install this package on a
|trueos| or FreeBSD system, type :command:`sudo pkg install lumina-i18n`.
On other operating systems, use the default software management tool.
Since each setting has its own drop-down menu, there is flexibility to
select different locales for each item shown in this screen. If any
changes are made in the :guilabel:`Locale` tab, click
:guilabel:`Save Changes` and restart |lumina| to load the configured
locales.

Installing the **lumina-i18n** package will also add a drop-down menu to
the :guilabel:`Preferences` area of the start menu, though |lumina| will
need to be restarted after the package installation to add the locale
menu to :guilabel:`Preferences`. This drop-down menu is used to
change the locale for the current session only. This will immediately
change the localization of any translated menu items without requiring
a restart of |lumina|.

.. note:: If using |lumina| with a language other than English, any menu
          items that continue to be displayed in English have not yet
          been translated to the selected language. To assist the
          |lumina| Project in translating menu items, see
          :ref:`Interface Translation`.