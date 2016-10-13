.. index:: advocacy
.. _Supporting TrueOS®:

Supporting TrueOS®
******************

|trueos| is a community project which relies on involvement from its
users and supporters. This section lists some ideas for becoming
involved.

.. index:: testing
.. _Become a Beta Tester:

Become a Beta Tester
====================

If you enjoy tinkering with operating systems and have a bit of spare
time, one of the most effective ways to can assist the |trueos|
community is by reporting any encountered problems while using |trueos|.

If a spare system or virtual machine is available, you can also download
and try out the latest testing snapshots. Having as many people as
possible using |trueos| on many different hardware configurations
assists the Project in finding and fixing bugs. This makes using
|trueos| better for everyone.

If becoming a tester is tempting, join the
`TrueOS® Lobby <https://gitter.im/trueos/Lobby>`_. New testing versions,
once available, will be announced here. You will also be able to see
any problems other testers are finding and can check to see if the
problem exists on your hardware as well.

Anyone can become a beta tester. If you find a bug while testing,
accurately describe the situation when
:ref:`Reporting a bug <Report a bug>` so it can be fixed as soon as
possible.

.. index:: translations
.. _Become a Translator:

Become a Translator
===================

If interested in translating |trueos| into your native language, there
are three translation areas to become involved in: 

1. Translate the graphical menus within the |trueos| operating system.

2. Translate the documentation published with |trueos|.

3. Translate the |trueos| website.

This section describes each of these translation areas in more detail
and how to begin as a translator.

Regardless of the type of desired translation, you should first join the
`TrueOS® Lobby <https://gitter.im/trueos/Lobby>`_. The first time
joining the channel, introduce yourself and indicate which language(s)
and which type(s) of translations you can assist with. This allows you
to meet other volunteers as well as stay informed of any notices or
updates affecting translators.

.. index:: translations
.. _Interface Translation:

Interface Translation
---------------------

|trueos| uses `Weblate <https://weblate.org>`_ for managing
localization of the menu screens used by the installer and the |trueos|
utilities. Weblate makes it easy to find out if your native language
has been fully localized for |trueos|. It also makes it easy to verify
and submit translated text as it provides a web editor and commenting
system. This means translators can spend more time making and
reviewing translations rather than learning how to use a translation
tool.

To assist with a localization, open the
`TrueOS® translation website <http://weblate.trueos.org/>`_ in a web
browser. An example is seen in :numref:`Figure %s <translate1>`. 

.. _translate1:

.. figure:: images/translate1.png

   : TrueOS® Weblate Translation System

Before editing a translation, first create a a login account and verify
the activation email. Once logged in, click 
:guilabel:`Manage your languages`, shown in
:numref:`Figure %s <translate2>`.

.. _translate2:

.. figure:: images/translate2.png

   : Weblate Dashboard

In the screen shown in :numref:`Figure %s <translate3>`, use the
:guilabel:`Interface Language` drop-down menu to select the language for
the Weblate interface. Then, in :guilabel:`Translated languages`, use
the :guilabel:`arrows` to add or remove the languages you wish to
translate. Once any selections are made, click :guilabel:`Save`.

.. _translate3:

.. figure:: images/translate3.png

   : Manage Languages

.. note:: If the language you wish to translate is missing from the
   "Translated languages" menu, request its addition in the
   `TrueOS® Lobby <https://gitter.im/trueos/Lobby>`_.

Next, click :guilabel:`Projects` at the top of the screen to select
a localization project. In the example shown in
:numref:`Figure %s <translate4>`, the user has selected the
*trueos-utils-qt5* project, which represents the localization of the
|trueos| graphical interface. This screen shows the components of the
project and the current progress of each component's translation. The
green bar indicates the localization percentage. If a component is not
at 100%, this means its untranslated menus will instead appear in
English.

.. _translate4:

.. figure:: images/translate4.png

   : Project Selection

To start translating, click a component name. In the screen shown in
:numref:`Figure %s <translate5>`, select a language and click
:guilabel:`Translate`.

.. _translate5:

.. figure:: images/translate5.png  

   : Translation Languages

In the example shown in :numref:`Figure %s <translate6>`, the user has
selected to translate the *pc-installgui* component into the Spanish
language. The English text is displayed in the :guilabel:`Source` field
and the translator can type the Spanish translation into the
:guilabel:`Translation` field. Use the :guilabel:`arrows` near the
:guilabel:`Strings needing action` field to navigate between strings
to translate.

.. _translate6:

.. figure:: images/translate6.png

   : Translation Editor

If assistance is needed with either a translation or the Weblate system,
ask for help in the `TrueOS® Lobby <https://gitter.im/trueos/Lobby>`_. 

.. index:: translations
.. _Documentation Translation:

Documentation Translation
-------------------------

The source for the |trueos| Users Handbook is stored in the
`TrueOS® github repository <https://github.com/trueos/trueos-docs/tree/master/trueos-handbook>`_.
This allows the documentation and its translations to be built with
the operating system. Documentation updates are automatically pushed
to the |trueos| website and, when the system is updated using
:ref:`Update Manager`, the doc updates are installed to a local copy
named
:file:`/usr/local/share/trueos/handbook/trueos.html`. This ensures the
installed version of the Handbook always matches the operating system
and new features are documented as they are added, appearing as a local
copy on the user's system.

The |trueos| build server provides the HTML version of the |trueos|
Users Handbook. Instructions for building your own HTML, PDF, or EPUB
version can be found in this
`README.md <https://github.com/trueos/trueos-docs/blob/master/trueos-handbook/README.md>`_.

The documentation source files have been integrated into the Weblate
translation system so the |trueos| documentation can be translated
using a web browser. The process is similar to
:ref:`Interface Translation` except **trueos-guide** mus be selected
from the :guilabel:`Projects` drop-down menu shown in :ref:`translate4`.

It is important to be aware of a few elements when translating the
documentation:

At this time, some formatting tags are still displayed in raw text, as
seen in the examples in :numref:`Figure %s <translate7>` and
:numref:`Figure %s <translate8>`.

.. danger:: Do not remove the formatting as this can break the
   documentation build for that language.

In :ref:`translate7`, it is fine to translate the phrase "Using the
Text Installer", but care must be taken to avoid removing any of the
surrounding colons and backticks, or to change the text of the *ref*
tag. In :ref:`translate8`, the asterisks are used to bold the words
"bare minimum". It is fine to translate "bare minimum", but do **not**
remove the asterisks.

.. _translate7:

.. figure:: images/translate7.png

   : Formatting Characters - Do Not Remove

.. _translate8:

.. figure:: images/translate8.png

   : More Formatting Characters

To build a local HTML copy that includes the latest translations, either
for personal use or to visualize the translated Guide, type these
commands from the command line:

.. note:: These instructions are for a |trueos| system.

.. code-block:: none

 sudo pkg install trueos-toolchain
 rehash
 git clone git://github.com/trueos/trueos-docs
 cd trueos-docs/trueos-handbook
 sudo make i18n
 make html
 ls _build
 doctrees                html-es                 html-tr  		pcbsd-handbook-i18n.txz               
 html                    html-fr                 html-uk
 html-da		 html-id		 locale
 html-de                 html-pt_BR        	 locale-po     

 
This will make an HTML version of the Guide for each of the available
translations. In this example, translations are available for English
(in :file:`html`), Danish, German, Spanish, French, Indonesian,
Brazilian Portuguese, Turkish, and UK English. To update the HTML at a
later time

.. code-block:: none

 cd ~/trueos-docs
 git pull
 cd trueos-docs/trueos-handbook 
 sudo make i18n
 sudo make html

.. index:: translations
.. _Website Translation:

Website Translation
-------------------

If you are interested in translating the |trueos| website, introduce
yourself in the `TrueOS® Lobby <https://gitter.im/trueos/Lobby>`_.

Currently, the website is being translated to several languages,
including: Dutch, French, German, Polish, Spanish, Swedish, and Turkish.

.. index:: development
.. _Become a Developer:

Become a Developer
==================

If you like programming, and especially coding on FreeBSD, we would
love to see you join the |trueos| team as a |trueos| committer.
Developers who want to help improve the |trueos| codebase are always
welcome! To participate in core development, introduce yourself in the
`TrueOS® Lobby <https://gitter.im/trueos/Lobby>`_. Feel free to browse
the :guilabel:`Issues` in the 
`TrueOS® repository <https://github.com/trueos/>`_. If you see
something you want to work on, or have a proposal for a project to add
to |trueos|, mention it and someone will be happy to help you get
started.

Most of the |trueos| specific GUI tools are developed in C++ using Qt
libraries and other non-GUI development is done using standard Bourne
shell scripts. There may be cases where other languages or libraries
are needed, but those will be evaluated on a case-by-case basis.

.. index:: development
.. _Getting the Source Code:

Getting the Source Code
-----------------------

The |trueos| source code is available from
`GitHub <https://github.com/trueos/>`_. The code has been organized
into repositories which represent the |lumina| desktop, the graphical
utilities, |sysadm|, and various other applications. :command:`git`
needs to be installed in order to download the source code. When using
|trueos|, :command:`git` is included in the base install.

To download the source code, :command:`cd` to the directory to store
the source code and specify the name of the desired repository. In
this example, the user wishes to download the source for the graphical
utilities:

.. code-block:: none

 git clone git://github.com/trueos/trueos-utils-qt5

This will create a directory with the same name as the repository.

.. note:: To keep the local copy in sync with the official repository,
   periodically run :command:`git pull` within the directory.

Before compiling any source, ensure the Ports Collection is
installed as the superuser, using :command:`portsnap fetch extract`
   
Then, :command:`cd` to the directory containing the source to build and
run the :command:`mkports.sh` script. In this example, the developer
wants to compile the graphical utilities:

.. code-block:: none

 cd trueos-utils-qt5

 ./mkports /usr/ports/

This will create a port which can be installed. The name of the port
is located in :file:`mkports.sh`. This example determines the name of
the port directory, changes to it, and then builds the port. Since this
system is already running the |trueos| graphical utilities,
:command:`reinstall` is used to overwrite the current utilities:

.. code-block:: none

 grep port= mkports.sh
 port="sysutils/trueos-utils-qt5"
 cd /usr/ports/sysutils/trueos-utils-qt5
 make reinstall
 
If you plan to make source changes, several Qt IDEs are available in
:ref:`AppCafe®`. The
`QtCreator <http://wiki.qt.io/Category:Tools::QtCreator>`_ application
is a full-featured IDE designed to help new Qt users get up and
running faster while boosting the productivity of experienced Qt
developers.
`Qt Designer <http://doc.qt.io/qt-4.8/designer-manual.html>`_ is
lighter weight as it is only a :file:`.ui` file editor and does not
provide any other IDE functionality. 

If planning to submit changes to be included in |trueos|, fork the
repository using the instructions in
`fork a repo <https://help.github.com/articles/fork-a-repo>`_. Make your
changes to the fork, then submit them by issuing a
`git pull request <https://help.github.com/articles/using-pull-requests>`_.
Once your changes have been reviewed, they will be committed or sent
back with suggestions for improvement.

.. index:: development
.. _Design Guidelines:

Design Guidelines
-----------------

|trueos| is a community driven project that relies on the support of
developers in the community to help in the design and implementation
of new utilities and tools for |trueos|. The Project aims to present a
unified design so that programs feel familiar to users. As an example,
while programs could have **File**, **Main**, or **System** as their
first entry in a menu bar, **File** is used as the accepted norm for the
first category on the menu bar.

This section describes a small list of guidelines for menu and program
design in |trueos|.

Any graphical program that is a full-featured utility, such as
:ref:`Life Preserver`, should have a **File** menu. However, file menus
are not necessary for small widget programs or dialogue boxes. When
making a file menu, a good rule of thumb is keep it simple. Most
|trueos| utilities do not need more than two or three items on the file
menu.

**Configure** is our adopted standard for the category containing
settings or configuration-related settings. If additional categories
are needed, check to see what other |trueos| utilities are using.

File menu icons are taken from the KDE Oxygen theme located in
:file:`/usr/local/share/icons/oxygen`. Use these file menu icons so we
do not have many different icons used for the same function.
:numref:`Table %s <common icons>` lists the commonly used icons and
their default file names.

.. _common icons:

.. table:: Commonly Used File Menu Icons

   +-----------+-----------------+--------------------+
   | Function  | File Menu Icon  | File Name          |
   +===========+=================+====================+
   | Quit      | row 1, cell 2   | window-close.png   |
   +-----------+-----------------+--------------------+
   | Settings  | row 2, cell 2   | configure.png      |
   +-----------+-----------------+--------------------+

|trueos| utilities use these buttons:

* **Apply:** Executes settings changes and leaves the window open.

* **Close:** Exits program without applying settings.

* **OK:** Closes dialogue window and saves settings.

* **Cancel:** Closes dialog window without applying settings.

* **Save:** Keeps the current settings and closes window.

Fully functional programs like :ref:`Life Preserver` do not use close
buttons on the front of the application. Basically, whenever there is
a **File** menu, that and an :guilabel:`x` in the top right corner of
the application are used instead. Dialogues and widget programs are
exceptions to this rule.

Many users benefit from keyboard shortcuts and we aim to make them
available in every |trueos| utility. Qt makes it easy to assign
keyboard shortcuts. For instance, to configure keyboard shortcuts that
browse the **File** menu, put :command:`&File` in the text slot for the
menu entry when making the application. Whichever letter has the
:kbd:`&` symbol in front of it will become the hot key. You can also
make a shortcut key by clicking the menu or submenu entry and assigning
a shortcut key. Be careful not to duplicate hot keys or shortcut keys.
Every key in a menu and submenu should have a key assigned for ease of
use and accessibility. :numref:`Table %s <shortcuts>` and
:numref:`Table %s <hotkeys>` summarize the commonly used shortcut and
hot keys.

.. _shortcuts:

.. table:: Shortcut Keys

   +---------------+---------+
   | Shortcut Key  | Action  |
   +===============+=========+
   | CTRL + Q      | Quit    |
   +---------------+---------+
   | F1            | Help    |
   +---------------+---------+

.. _hotkeys:

.. table:: Hot Keys

   +-----------+-----------------+
   | Hot Key   | Action          |
   +===========+=================+
   | Alt + Q   | Quit            |
   +-----------+-----------------+
   | Alt + S   | Settings        |
   +-----------+-----------------+
   | Alt + I   | Import          |
   +-----------+-----------------+
   | Alt + E   | Export          |
   +-----------+-----------------+
   | ALT + F   | File Menu       |
   +-----------+-----------------+
   | ALT + C   | Configure Menu  |
   +-----------+-----------------+
   | ALT + H   | Help Menu       |
   +-----------+-----------------+

When saving an application's settings, the QSettings class should be
used if possible. There are two different *organizations*, depending
on whether the application is running with *root* permissions or user
permissions. Use **TrueOS** for the organization for applications which
run with user permissions and **TrueOS-root** for applications which are
started with root permissions via :command:`sudo`. Proper use prevents
the directory where settings files are saved from being locked down by
*root* applications, allowing user applications to save and load their
settings. Examples 1 and 2 demonstrate how to use the QSettings class
for each type of permission.

**Example 1: User Permission Settings**

.. code-block:: none

 (user application - C++ code): 
 QSettings settings("TRUEOS", "myapplication");

**Example 2: Root Permission Settings**

.. code-block:: none

 (root application - C++ code):
 QSettings settings("TRUEOS-root", "myapplication");

Developers will also find these resources helpful: 

* `Commits Mailing List <http://lists.pcbsd.org/mailman/listinfo/commits>`_

* `Qt 5.4 Documentation <http://doc.qt.io/qt-5/index.html>`_

* `C++ Tutorials <http://www.cplusplus.com/doc/tutorial/>`_

.. index:: advocacy
.. _Become an Advocate:

Become an Advocate
==================

Love |trueos|? Why not tell your family, friends, fellow students and
colleagues about it? You will not be the only one who prefers a
virus-free, feature-rich, and no-cost operating system. Here are some
suggestions for getting started:

* Burn a couple of DVDs and pass them out. If your school or user
  group has an upcoming event where you can promote |trueos|, you can
  request additional DVDs from sales@pcbsd.com.

* Consider giving a presentation about |trueos| at a local community
  event, conference, or online. Let us know about it and we will help
  you spread the word.

* Write a personal blog detailing your journey from your first |trueos|
  install experience to your most recent accomplishment. The blog
  could also be used to teach or explain how to perform tasks on
  |trueos|. A regional language blog may help build the community in
  your area and to find others with similar interests.