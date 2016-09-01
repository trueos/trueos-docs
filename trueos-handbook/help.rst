.. index:: help
.. _Finding Help:

Finding Help
************

The TrueOS® Project strives to make using TrueOS® as easy as possible
for newcomers. Should you need help, there are plenty of ways to get
in touch with the TrueOS® community. This chapter describes the
available resources.

As your teacher may have told you, "there is no such thing as a stupid
question". However, there are ways to ensure that you receive the
response you seek and that it will be a productive exchange for all
parties involved. The two articles below describe how and why it is
important to follow certain protocols when requesting help: 

* `How to Ask Smart Questions (PDF) <http://divajutta.com/doctormo/foo/ask-smart-questions.pdf>`_

* `How To Ask Questions The Smart Way <http://catb.org/~esr/faqs/smart-questions.html>`_

.. index:: chat
.. _TrueOS® Gitter Channel:

TrueOS® Gitter Channel
======================

The TrueOS® Project uses
`Gitter <https://en.wikipedia.org/wiki/Gitter>`_ to provide real-time
chat and collaboration with TrueOS® users and developers. Gitter does
not require an application to use, but does require a login using
either an existing GitHub or Twitter account.

To access the Gitter channel, point your web browser to the
`TrueOS® Lobby <https://gitter.im/trueos/Lobby>`_. 

Gitter is a great way to chat with other users and get answers to your
questions. A few things to keep in mind if you ask a question on the
Gitter channel:

* Most of the regular users are always logged in, even when they are
  away from their computer or are busy doing other things. If you do
  not get an answer right away, do not get mad, leave the channel, and
  never come back again. Stick around for a while to see if anyone
  responds.
    
* Users represent many different time zones. It is quite possible tha
  t it is late at night or very early in the morning for some users
  when you ask a question.

* Do not post large error messages in the channel. Instead, use a
  pasting service such as pastebin.com and refer to the URL on channel.
    
* Be polite and do not demand that others answer your question.
    
* It is considered rude to "Chat Privately" with someone who does not
  know you without first asking their permission. If no one answers
  your question, do not start chatting privately with people you do not
  know.
  
* The first time you join the channel, it is okay to say hi and
  introduce yourself. If a new person joins the channel, feel free to
  welcome them and to make them feel welcome.

.. index:: reddit
.. _TrueOS® Subreddit:

TrueOS® Subreddit
=================

The TrueOS® Project also has a
`Subreddit <https://www.reddit.com/r/TrueOS/>`_ for users who prefer
to use Reddit to ask questions and to search for or post how-tos. You
do not need a Reddit account in order to read the Subreddit, but will
need to create a login account if you wish to submit or comment on
posts.

.. index:: bug
.. _Report a bug:

Report a bug
============

One of the most effective ways to assist the TrueOS® Project is by
reporting problems or bugs encountered while using TrueOS®. Anyone can
report a TrueOS® bug. However, a few guidelines should be followed to
ensure a speedy response:

* TrueOS® uses `GitHub <https://github.com/trueos/>`_, to manage bugs.
  A GitHub account is required before bugs can be reported. Navigate
  to https://github.com, fill in the required fields, and click
  :guilabel:`Sign up for GitHub` to create a new github account.

.. note:: The GitHub issues tracker uses email to update contributors
   on the status of bugs. Please use a valid and frequently used
   email address when creating a GitHub account for the efficient
   resolution of issues.

* The TrueOS® code has been organized into repositories that represent
  the Lumina desktop, the graphical utilities, SysAdm™, and various
  other applications. Select the repository that most closely matches
  the application that has a bug. If you are in doubt, select the
  "trueos-utils-qt5" repository.
   
* Once you have clicked a repostitory name, use the "Search" bar on its
  page to confirm no similar bug report exists. If a similar report does
  exist, add any additional information to the report via a comment.
  While it is not required to log in to search existing bugs, adding a
  comment or creating a new report does require signing into the
  website.

* To create a new bug report,
  click :menuselection:`Issues --> New Issue` within the repository.
  :numref:`Figure %s: Creating a Bug Report <bug1>` shows an example
  from within the "trueos-utils-qt5" repository.

.. _bug1:

.. figure:: images/bug1.png
   :scale: 100%

* Write a brief but descriptive "Title" that includes the error.
  Ideally, the title is short (8 words or less) and contains key words
  about the error so the bug report is easily found with the search tool.

* In the "Leave a Comment" text area, write about the circumstance of
  the error, including instructions how to recreate it. If an error
  message is generated, paste the error in its entirety. Attaching a
  screenshot to the report can greatly aid the developer in visualizing
  the problem. Remember to include the output of :command:`uname -a`.

* If the problem appears to be hardware related, attach a copy of
  :file:`/var/run/dmesg.boot` as this file shows the hardware that was
  probed the last time the TrueOS® system booted.

* After describing the issue, click :guilabel:`Submit new issue` to
  create the issue. The bug tracker will attach a unique number to the
  report and send update messages to the your registered email address
  whenever activity occurs with the bug report.

.. index:: help
.. _Social Media:

Social Media
============

The TrueOS® project maintains several social media sites to help users
keep up-to-date with what is happening and to provide venues for
developers and users to network with each other. Anyone is welcome to
join.

* `Official TrueOS® Blog <https://www.trueos.org/blog/>`_

.. index:: help
.. _FreeBSD Handbook and FAQ:

FreeBSD Handbook and FAQ
========================

TrueOS® uses FreeBSD as its underlying operating system, so everything
in the
`FreeBSD Handbook <http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/>`_
and
`FreeBSD FAQ <http://www.freebsd.org/doc/en/books/faq/>`_ applies to
TrueOS® as well. Both documents are comprehensive and cover nearly
every task you can accomplish on a FreeBSD system. They are also an
excellent resource for learning how things work under the hood of your
TrueOS® system.

.. note:: Some configurations described in the FreeBSD Handbook
   already "just work" on your TrueOS® system as they have been
   pre-configured for you. In these instances, reading that FreeBSD
   Handbook section can help you to understand how your system is
   configured and why it works.

.. index:: help
.. _Search and Portals:

Search and Portals
==================

Many BSD related search portals exist. If you can not find the answer
that you are looking for in the forums or mailing lists, try searching
these websites: 

* `The OpenDirectory <http://www.dmoz.org/Computers/Software/Operating_Systems/Unix/BSD/>`_

* `FreeBSD Search <http://www.freebsd.org/search/index.html>`_
  (includes mailing list archives, man pages, and web pages) 

* `FreeBSD News <https://www.freebsdnews.com/>`_

* `About BSD <http://aboutbsd.net/>`_

* `BSD Guides <http://www.bsdguides.org/guides/>`_

* `Slashdot BSD <https://bsd.slashdot.org/>`_

* `DistroWatch <http://distrowatch.com/>`_

* `LinuxBSDos <http://linuxbsdos.com/>`_

.. index:: help
.. _Other Resources:

Other Resources
===============

The following BSD sites and resources may also contain useful
information: 

* `The FreeBSD Diary <http://www.freebsddiary.org/>`_

* `PC-BSD® YouTube channel <https://www.youtube.com/channel/UCyd7MaPVUpa-ueUsGjUujag>`_

* `BSD YouTube channel <https://www.youtube.com/user/bsdconferences>`_

* `BSD Talk <http://bsdtalk.blogspot.com/>`_

* `BSD Now <http://www.bsdnow.tv/>`_

* `BSD Magazine <https://bsdmag.org/>`_ (free, monthly download) 

* `FreeBSD Journal <http://www.freebsdjournal.com/>`_ (bi-monthly magazine) 

* `BSD Hacks <http://shop.oreilly.com/product/9780596006792.do>`_ (book) 

* `The Best of FreeBSD Basics <http://reedmedia.net/books/freebsd-basics/>`_ (book) 

* `Definitive Guide to PC-BSD® <http://www.apress.com/9781430226413>`_ (book)
