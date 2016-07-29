.. index:: plugins   
.. _Lumina Plugins:

Lumina Plugins
**************

Lumina offers a wide variety of plugins which allow the user to 
customize their desktop experience. Plugins are divided between context 
menu, desktop, and floating panel plugins.

.. index:: contextmenu plugins
.. _Context Menu Plugins:

Context Menu Plugins
====================

Menu plugins are the options which appear when the user right-clicks on 
the desktop screen in Lumina. You can customize these options by 
clicking on the Start Menu, then 
:menuselection:`Preferences --> Configure Desktop --> Interface Configuration --> Context Menu and Plugins`.

.. _luminamenupluginmenu1:

.. figure:: images/luminamenupluginmenu1.png

:numref:`Figure %s: Lumina Menu Plugins <luminamenupluginmenu1>`

Add or remove plugins by clicking the green "plus" or red "minus" 
buttons in the bottom left corner of the window. The arrow buttons in 
the bottom right allow the user to move plugins up or down in the 
Quick-Access Menu field, which will alter their display order when the 
desktop is right-clicked. Click the Save button to immediately implement 
any changes to the menu.

Two elements the right-click menu will always display are the name of 
the current virtual desktop at the top of the menu and the shutdown 
options on the bottom, as pictured in :numref:`Figure %s: Default Menu <luminamenuplugin1>`.

.. _luminamenuplugin1:

.. figure:: images/luminamenuplugin1.png

The user can customize what appears between these two elements of the 
menu however they wish.

.. _Menu Applications:

Applications
------------

.. _luminamenuplugin2:

.. figure:: images/luminamenuplugin2.png

:numref:`Figure %s: Applications <luminamenuplugin2>`

This plugin adds an application menu which can be navigated to open any 
installed application. The Control Panel and Application Management 
options will always be shown at the top, while the categories of 
applications are shown underneath.

.. _Custom App:

Custom App
----------

.. _luminamenuplugin3:

.. figure:: images/luminamenuplugin3.png

:numref:`Figure %s: Custom Application <luminamenuplugin3>`

Adds a specific quickstart icon for a single application to the 
right-click menu. Pictured is the icon for the "About" application, 
which is displaying current TrueOS® system information.

.. _File Manager:

File Manager
------------

.. _luminamenuplugin4:

.. figure:: images/luminamenuplugin4.png

:numref:`Figure %s: File Manager <luminamenuplugin4>`

Opens the user's home directory within the default file manager.

.. _JSON Menu:

JSON Menu
---------

The JSON Menu plugin give a more advanced user the flexibility to create
their own entries into the right-click menu. Selecting the JSON Menu 
plugin immediately brings up the menu configuration window, seen in 
:numref:`Figure %s: JSON Menu Configuration Window <luminamenuplugin5>`.

.. _luminamenuplugin5:

.. figure:: images/luminamenuplugin5.png

This window has three fields: Visible Name, Executable, and Icon. The 
Visible Name field will define the name of the right-click menu entry. 
Executable is the path to the custom script that is to be run for the 
entry. The Icon field is optional, but is used to assign a specific 
icon to the custom script.

.. _luminamenuplugin6:

.. figure:: images/luminamenuplugin6.png

:numref:`Figure %s: JSON Menu Example <luminamenuplugin6>`

After completing the configuration window, the resultant display shows 
the custom script in action. The Visible Name appears under "Workspace 2",
while the executable script has generated the menu of files and folders.

.. _Separator:

Separator
---------

:numref:`Figure %s: Separator <luminamenuplugin1>`

A Separator is simply a horizontal line which can be used to divide 
entries in the right-click menu. When added to the menu, use the up and
down arrows in the plugin selection menu to place the Separator plugin 
between the plugins you wish to place a line between.

.. _Settings:

Preferences
-----------

.. _luminamenuplugin7:

.. figure:: images/luminamenuplugin7.png

:numref:`Figure %s: Preferences <luminamenuplugin7>`

This plugin adds a shortcut to the right-click menu which opens a new 
menu of configuration quicklinks.

.. _Terminal:

Terminal
--------

.. _luminamenuplugin8:

.. figure:: images/luminamenuplugin8.png

:numref:`Figure %s: Terminal <luminamenuplugin8>`

A shortcut to the default system terminal.

.. _Window List:

Window List
-----------

.. _luminamenuplugin9:

.. figure:: images/luminamenuplugin9.png

:numref:`Figure %s: Window List <luminamenuplugin9>`

This plugin adds an entry to the right-click menu which, when hovered 
over with the mouse, will list all open application windows. This plugin 
is comparable to a task manager plugin for panels.

.. index:: desktop plugins
.. _desktop plugins:

Desktop Plugins
===============

Desktop plugins will add icons or widgets for display on the main screen
of the Lumina Desktop Environment. Click on default start menu in the 
lower left of the main desktop screen, then click 
:menuselection:`Preferences --> Configure Desktop --> Interface Configuration --> Desktop Icons and Plugins`.

.. _luminadesktoppluginmenu1:

.. figure:: images/luminadesktoppluginmenu1.png

:numref:`Figure %s: Desktop Plugin Menu <luminadesktoppluginmenu1>` This 
is the primary menu for configuring desktop plugins. Clicking the green 
"plus" button will open a "Select Plugin" window. The user can choose 
between the available plugins by opening the drop-down menu and clicking
the desired plugin. Once a plugin has been selected, your choice will 
appear in the "Embedded Utilities" window. 

The “Display Desktop Folder Contents” option is used to display each 
item stored in ~/Desktop as an icon on the desktop. By default, this 
option is selected as its box is black. If you de-select this option and
click “Save Changes”, the icons for the contents of ~/Desktop will be 
removed from the desktop. To define a smaller area on the desktop for 
displaying icons, use the :ref:`Desktop Icons View` plugin.

Once all the desired plugins have been added, click the "Save" button 
that appears in the upper right section. The menu will automatically 
save and implement any changes to the desktop plugins.
 
There are numerous plugins in the desktop category, listed in
alphabetical order.

.. _Application Launcher:

Application Launcher
--------------------

.. _luminadesktopplugin1:

.. figure:: images/luminadesktopplugin1.png

Choosing the Application Launcher plugin opens the window seen in 
:numref:`Figure %s: Application Launcher <luminadesktopplugin1>`. This 
drop down menu allows the user to choose a specific application to add 
to the desktop.

.. _Audio Player:

Audio Player
------------

.. _luminadesktopplugin2:

.. figure:: images/luminadesktopplugin2.png

:numref:`Figure %s: Audio Player <luminadesktopplugin2>` 

The Audio Player plugin will play user added lists of audio files. 
Pressing the wrench icon in the upper left corner will open an options 
menu to clear or shuffle the playlist. 

The green plus icon gives the user options to add files, a directory, or
URL to the playlist. Toggle the play button in the lower left corner of 
the plugin in order to start/stop an audio file. The forward and back 
buttons in the upper right corner allow the user to skip to the next 
song or return to the previous one. Click the currently playing file to
open a drop down menu of all added audio files.

.. _calendar:

Calendar
--------

.. _luminadesktopplugin3:

.. figure:: images/luminadesktopplugin3.png

:numref:`Figure %s: Calendar <luminadesktopplugin3>` 

This is a calendar plugin which will display a calendar set to the 
current month and day. The arrows in the upper left and right of the 
plugin allow the user to view previous or upcoming months. If available,
the user can also use their mouse to hover over the calendar and then 
scroll up or down through the calendar.

.. _Desktop Icons View:

Desktop Icons View
------------------

.. _luminadesktopplugin4:

.. figure:: images/luminadesktopplugin4.png

:numref:`Figure %s: Desktop Icons <luminadesktopplugin4>` 

This plugin will define an area on the desktop to display icons. If 
enough icons are added to the plugin, a scroll bar will appear for the 
user to scroll through all available icons.

.. _Note Pad:

Note Pad
--------

.. _luminadesktopplugin5:

.. figure:: images/luminadesktopplugin5.png

:numref:`Figure %s: Note Pad <luminadesktopplugin5>` 

A plugin which adds a simple text editor widget to the desktop. The 
user needs to create or open a note before they can type a message. 
Notes default to the .note text format and are saved in 
/usr/home/<username>/Notes. Clicking the down arrow in the upper-right 
corner displays a number of options:

	* **Open Text File** - Allows the user to browse through their 
	  directories to open a .note or other text file.
	* **Create a Note** - Creates a new note; a unique name is required.
	* **Rename Note** - Renames the currently open note.
	* **Delete Note** - Immediately deletes the displayed note.

.. _RSS Reader:

RSS Reader
----------

.. _luminadesktopplugin6:

.. figure:: images/luminadesktopplugin6.png

:numref:`Figure %s: RSS Reader <luminadesktopplugin6>` 

Displays connected RSS feeds. The user can add their own custom RSS 
feeds to the plugin, but the default feed displayed is the Lumina 
Desktop Environment blog. Click the dropdown menu to choose which RSS 
feed to display. The down arrow in the upper right corner opens a list 
of options:

	* **Add RSS Feed** - An option to allow the user to type in their 
	  own RSS URL or load a preset RSS Feed.
	* **View Feed Details** - Displays current feed data, including URL, 
	  feed description and website address, and the previous build date
	  and synchronization settings. Also included is an option to remove
	  the feed.
	* **Settings** - Options for syncing the feed. You can choose to 
	  synchronize manually, or instead define the sync interval. 
	  Remember to save any changes in feed settings.
	* **Update Feeds Now** - Click to immediately update all feeds.
	
.. note:: An active Internet connection is required for the RSS Reader 
          plugin to function properly.
          
Click the blue globe to open the default web browser at the feed's 
associated website. 

.. _System Monitor:

System Monitor
--------------

.. _luminadesktopplugin7:

.. figure:: images/luminadesktopplugin7.png

:numref:`Figure %s: System Monitor Display <luminadesktopplugin7>` 

The "Summary" tab of the System Monitor plugin. CPU Temperature (in 
Celsius), CPU Usage, and Memory Usage are displayed. Currently, there 
are no other options to display in the system monitor aside from these 
statistics and the read/write speed monitor, shown next.

.. _luminadesktopplugin8:

.. figure:: images/luminadesktopplugin8.png

:numref:`Figure %s: System Monitor I/O <luminadesktopplugin8>` 

The "Disk I/O" tab of the System Monitor plugin. Displayed are the 
current read and write speeds of the connected hardware, which in this 
case is a hard drive and cd player. 

.. index:: float panel plugins
.. _floating panel plugins:

Floating Panel Plugins
======================

Panels are a completely customizable option for Lumina users. By default,
Lumina users will have one panel stretched across the bottom of the 
primary screen and one smaller pop-up panel in the top middle of the 
primary screen. To adjust the default panels and add plugins, click the 
start menu and navigate :menuselection:`Preferences --> Configure Desktop --> Interface Configuration --> Floating Panels and Plugins`.
For demonstration purposes, a simple panel centered at the top of a 
secondary screen was utilized to show the various plugins listed below.
The settings for this panel are pictured in :numref:`Figure %s: Panel Settings <luminapanelpluginmenu1>`.

.. _luminapanelpluginmenu1:

.. figure:: images/luminapanelpluginmenu1.png

As you can see, Panel 1 is configured to the top center of Monitor 1 
(plugged into DVI-I-0). To add or adjust plugins for this panel, click 
on the green puzzle piece icon to open the :numref:`Figure %s: Panel Plugins Menu <luminapanelpluginmenu2>`.

.. _luminapanelpluginmenu2:

.. figure:: images/luminapanelpluginmenu2.png

The large field shows currently active plugins. Click the red minus or 
green plus buttons to add or remove plugins to the panel. Use the arrow 
keys to alter the display order of attached plugins. By default, plugins
will populate horizontal panels from left to right, and vertical panels 
from top to bottom. All the plugins available for panel plugins are 
listed below.

.. _panel application launcher:

Panel Application Launcher
--------------------------

.. _luminapanelplugin1:

.. figure:: images/luminapanelplugin1.png

:numref:`Figure %s: Panel Application Launcher <luminapanelplugin1>`

When you select this plugin, it will prompt you to select the 
application to launch. This will add a shortcut for launching the 
selected application to the panel.

.. _Application Menu:

Application Menu
----------------

.. _luminapanelplugin2:

.. figure:: images/luminapanelplugin2.png

:numref:`Figure %s: Application Menu <luminapanelplugin2>`

Adds an application menu that contains a shortcut to your home directory,
a shortcut to the operating system’s graphical software management 
utility (if there is one), a shortcut to the operating system’s Control 
Panel (if it provides one), and a list of installed software sorted by 
categories. This plugin is also considered a primary menu, like the 
start button, and will open when the :kbd:`Windows` key is pressed.

.. _Battery Monitor:

Battery Monitor
---------------

Hover over this icon (not pictured) to view the current charge status of
the battery. When the charge reaches 15% or below, the low battery icon 
will flash intermittently and will change to a low battery icon when 
there is less than 5% charge left.

.. _Desktop Bar:

Desktop Bar
-----------

.. _luminapanelplugin3:

.. figure:: images/luminapanelplugin3.png

:numref:`Figure %s: Desktop Bar <luminapanelplugin3>` :guilabel:`Favorite Applications` 
is pressed.

This plugin adds shortcuts to the panel for applications or files 
contained within the ~/Desktop folder or favorited by the user. The 
“star” button displays applications, the "folder" button displays 
folders, and the "file" button shows favorite files.

.. _Line:

Line
----

.. _luminapanelplugin4:

.. figure:: images/luminapanelplugin4.png

:numref:`Figure %s: Line <luminapanelplugin4>` The line is highlighted 
in red.

Adds a separator line to the panel to provide visual separation between 
plugins. When adding a line plugin in the :numref:`Figure %s: Panel Plugins Menu <luminapanelpluginmenu2>`,
be sure to use the arrow buttons in the bottom-right corner of the 
window to place the line entry between the two other plugins you wish to 
separate.

.. _Show Desktop:

Show Desktop
------------

.. _luminapanelplugin5:

.. figure:: images/luminapanelplugin5.png

:numref:`Figure %s: Show Desktop Button <luminapanelplugin5>`

This button will immediately hide all open windows on all active 
monitors so that only the desktop is visible. This is useful for touch 
screens or small devices. 

.. _Spacer:

Spacer
------

.. _luminapanelplugin6:

.. figure:: images/luminapanelplugin6.png

:numref:`Figure %s: Spacer <luminapanelplugin6>`

Adds a blank area to the panel. Similar to lines, spacers need to be 
positioned between plugins in the :numref:`Figure %s: Panel Plugins Menu <luminapanelpluginmenu2>`
in order to achieve the desired separation.

.. _Panel Start Menu:

Start Menu
----------

.. _luminapanelplugin7:

.. figure:: images/luminapanelplugin7.png

:numref:`Figure %s: Start Menu <luminapanelplugin7>`

Adds a classic start menu as seen on other operating systems. This is 
added by default to the primary desktop panel in the lower left corner.

.. _System Dashboard:

System Dashboard
----------------

.. _luminapanelplugin8:

.. figure:: images/luminapanelplugin8.png

:numref:`Figure %s: System Dashboard <luminapanelplugin8>` with the 
button pressed.

The System Dashboard plugin is a convenient shortcut to view or modify 
a number of basic settings. The system volume and screen brightness can 
be manually adjusted higher or lower, and you can also toggle between 
virtual workspaces with the left and right arrows. A "Log Out" button 
has also been added for additional convenience. If your system has a 
battery, its current charge will also be displayed.

.. note:: Adjusting the screen brightness on a multi-monitor system will 
          affect both monitors.

.. _System Tray:

System Tray
-----------

.. _luminapanelplugin9:

.. figure:: images/luminapanelplugin9.png

:numref:`Figure %s: System Tray <luminapanelplugin9>` with several 
docked applications (Quassel IRC, PC Mixer, etc.). 

Provides an area on the panel for dockable applications. Applications 
can be sent to this area on a per-application basis, but only one system
tray plugin can be active at a time. By default, the active system tray 
will be the one on the **lowest number** monitor and panel. For example,
when adding the system tray plugin to monitor zero, panel one and again 
to monitor one, panel one, only the system tray on monitor zero will 
be active. Disabling the system tray on monitor zero will activate the 
tray on monitor one, automatically migrating any docked applications to 
the other panel.

.. _Task Manager (No Groups):

Task Manager (No Groups)
------------------------

.. _luminapanelplugin10:

.. figure:: images/luminapanelplugin10.png

:numref:`Figure %s: Task Manager (No Groups) <luminapanelplugin10>`

Ensures that every window gets its own button on the panel. This plugin 
will use a large amount of space on the panel, as every window will 
need to display a part of its title. This plugin is added to the default
panel for Lumina.

.. _Task Manager:

Task Manager
------------

.. _luminapanelplugin11:

.. figure:: images/luminapanelplugin11.png

:numref:`Figure %s: Task Manager <luminapanelplugin11>` Pictured are 
three open terminal windows grouped into one minimal panel entry with 
"(3)" displayed next to the terminal icon. 

The grouping task manager displays windows in the panel as well. Its 
primary function is to group windows by application, saving more space 
on the panel. This manager also does not typically display window titles
on the panel, a further space savings.

.. _Time Date:

Time/Date
---------

.. _luminapanelplugin12:

.. figure:: images/luminapanelplugin12.png

:numref:`Figure %s: Time/Date <luminapanelplugin12>` The clock has been 
selected, opening the larger calendar and time zone settings.

Displays the current time and date. A basic clock is added to the panel; 
clicking it will open the calendar, which will highlight the current 
date. Clicking the arrows in the top corners will allow you to look back 
or ahead in the calendar, while clicking the "Time Zone" will allow you 
to adjust the displayed time.

.. _User Button:

User Menu
---------

The User Menu is a more complicated plugin that provides an array of 
shortcuts to files and applications on the system, essentially as an 
alternative to the Start Menu.

.. _luminapanelplugin13:

.. figure:: images/luminapanelplugin13.png

:numref:`Figure %s: User Favorites <luminapanelplugin13>` Shows the
default view after clicking the user button. On the sidebar, the 
"Favorites" folder is highlighted, with the top tab showing 
"Applications". You can also view favorite folders and files by clicking
the "Places" and "Files" tabs, respectively.

Clicking the "gear" icon in the left sidebar will open the "Applications"
section of the menu, seen in :numref:`Figure %s: User Applications <luminapanelplugin14>`.

.. _luminapanelplugin14:

.. figure:: images/luminapanelplugin14.png

This section displays all applications by default, with the drop down 
menu at the top allowing you to view applications by category. The 
"AppCafe" button in the top right will open the SysAdm AppCafe®, allowing
you to quickly search for and download more applications.

.. _luminapanelplugin15:

.. figure:: images/luminapanelplugin15.png

:numref:`Figure %s: Home Directory <luminapanelplugin15>`

The "folder" icon on the left sidebar opens the Home directory, giving 
you the option to quickly browse through system directories. Clicking 
the file/folder button in the upper right launches the Insight File 
Manager at the home directory. Clicking the binoculars and gear icon 
will launch the search utility. 

Finally, selecting the screwdriver and wrench icon on the sidebar will 
open the "Desktop Preferences" section, seen in :numref:`Figure %s: Desktop Preferences <luminapanelplugin16>`

.. _luminapanelplugin16:

.. figure:: images/luminapanelplugin16.png

This panel displays shortcuts to all the settings and configuration 
utilities, as well as the system information window. 

.. _Workspace Switcher:

Workspace Switcher
------------------

.. _luminapanelplugin17:

.. figure:: images/luminapanelplugin17.png

:numref:`Figure %s: Workspace Switcher <luminapanelplugin17>`

Used to switch between virtual desktops. Click the monitor icon to show 
a drop down menu of all workspaces. The active workspace will have 
asterisks (*) before and after its name.