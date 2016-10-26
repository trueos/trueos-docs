.. index:: help
.. _Finding Help:

Finding Help
************

The |trueos| Project strives to make using |trueos| as easy as possible
for newcomers. If help is needed, there are many ways to get in touch
with the |trueos| community. This chapter describes available resources.

As a teacher may have said, "there is no such thing as a stupid
question". However, there are ways to ensure a productive exchange for
all parties involved. The two articles below describe how and why it is
important to follow certain protocols when requesting help:

* `How to Ask Smart Questions (PDF) <http://divajutta.com/doctormo/foo/ask-smart-questions.pdf>`_

* `How To Ask Questions The Smart Way <http://catb.org/~esr/faqs/smart-questions.html>`_

.. index:: chat
.. _TrueOS® Gitter Channel:

TrueOS® Gitter Channel
======================

The |trueos| Project uses
`Gitter <https://en.wikipedia.org/wiki/Gitter>`_ to provide real-time
chat and collaboration with |trueos| users and developers. Gitter does
not require an application to use, but does require a login using
either an existing GitHub or Twitter account.

To access the Gitter channel, point a web browser to the
`TrueOS® Lobby <https://gitter.im/trueos/Lobby>`_.

Gitter is a great way to chat with other users and get answers to
questions. Here are few things to keep in mind when asking a question
on the Gitter channel:

* Most of the regular users are always logged in, even when they are
  away from their computer or are busy doing other things. If no one
  responds immediately, do not get mad, leave the channel, and never
  come back again. Stick around for a while to see if anyone responds.

* Users represent many different time zones. It is quite possible it is
  late at night or very early in the morning for some users when asking
  a question.

* Do not post large error messages in the channel. Instead, use a
  pasting service such as pastebin.com and refer to the URL on channel.

* Be polite and do not demand a response from others.

* It is considered rude to "Chat Privately" with someone who does not
  know you without first asking their permission. If no one answers
  the question, do not start chatting privately with unkown people in
  the room.

* The first time joining the channel, it is okay to say hi and introduce
  yourself. If a new person joins the channel, feel free to welcome them
  and to make them feel welcome.

.. index:: reddit
.. _TrueOS® Subreddit:

|trueos| Subreddit
==================

The |trueos| Project also has a
`Subreddit <https://www.reddit.com/r/TrueOS/>`_ for users who prefer
to use Reddit to ask questions and to search for or post how-tos. A
Reddit account is not required in order to read the Subreddit, but will
be necessary to create a login account to submit or comment on posts.

.. index:: discourse

|trueos| Discourse
==================

|trueos| also has a discourse `channel <https://discourse.trueos.org/>`_
managed concurrently with the Subreddit. Functionally similar to the
Subreddit, a new user will need to sign up with Discourse in order to
create posts, but it is possible to view the current posts without an
account.

.. index:: bug
.. _Report a bug:

Report a bug
============

One of the most effective ways to assist the |trueos| Project is by
reporting problems or bugs encountered while using |trueos|. Anyone can
report a |trueos| bug. However, a few guidelines should be followed to
ensure a speedy response:

* |trueos| uses `GitHub <https://github.com/trueos/>`_, to manage bugs.
  A GitHub account is required before bugs can be reported. Navigate
  to https://github.com, fill in the required fields, and click
  :guilabel:`Sign up for GitHub` to create a new github account.

.. note:: The GitHub issues tracker uses email to update contributors
   on the status of bugs. Please use a valid and frequently used
   email address when creating a GitHub account for the efficient
   resolution of issues.

* The |trueos| code has been organized into repositories representing
  the |lumina| desktop, the graphical utilities, |sysadm|, and various
  other applications. When reporting a bug, select the "trueos-core"
  repository. If the bug is specific to |lumina|, instead select the
  "lumina" repository.

* After clicking a repostitory name, use the :guilabel:`Search` bar on
  its page to confirm no similar bug report exists. If a similar
  report does exist, add any additional information to the report via
  a comment. While it is not required to log in to search existing bugs,
  adding a comment or creating a new report does require signing into
  the website.

* To create a new bug report, navigate to the 
  `trueos-core repository <https://github.com/trueos/trueos-core>`_ and
  press :menuselection:`Issues --> New Issue` within the repository.
  :numref:`Figure %s <bug1>` shows the creation of a new bug report.
  
.. _bug1:

.. figure:: images/bug1.png
   :scale: 100%

   : Creating a Bug Report
   
* Write a brief but descriptive title which includes the error. Ideally,
  the title is short (8 words or less) and contains key words about the
  error so the bug report is easily found with the search tool.

* In the :guilabel:`Leave a Comment` field, write about the
  circumstance of the error, including instructions how to recreate it.
  If an error message is generated, paste the error in its entirety.
  Attaching a screenshot to the report can greatly aid the developer in
  visualizing the problem. Remember to include the output of
  :command:`uname -a`.

* If the problem appears to be hardware related, attach a copy of
  :file:`/var/run/dmesg.boot` as this file shows the hardware probed the
  last time the |trueos| system booted.

* After describing the issue, click :guilabel:`Submit new issue` to
  create the issue. The bug tracker will attach a unique number to the
  report and send update messages to the the registered email address
  whenever activity occurs with the bug report.

.. index:: help
.. _Social Media:

Social Media
============

The |trueos| project maintains several social media sites to help users
keep up-to-date with what is happening and to provide venues for
developers and users to network with each other. Anyone is welcome to
join.

* `Official TrueOS® Blog <https://www.trueos.org/blog/>`_

* `TrueOS® Project on Twitter <https://twitter.com/TrueOS_Project/>`_

* `TrueOSD® Facebook Group <https://www.facebook.com/groups/4210443834/>`_

* `TrueOS® LinkedIn Group <http://www.linkedin.com/groups?gid=1942544>`_

.. index:: help
.. _FreeBSD Handbook and FAQ:

FreeBSD Handbook and FAQ
========================

|trueos| uses FreeBSD as its underlying operating system, so everything
in the
`FreeBSD Handbook <http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/>`_
and
`FreeBSD FAQ <http://www.freebsd.org/doc/en/books/faq/>`_ applies to
|trueos| as well. Both documents are comprehensive and cover nearly
every possible task to accomplish on a FreeBSD system. They are also an
excellent resource for learning how things work under the hood of a
|trueos| system.

.. note:: Some configurations described in the FreeBSD Handbook already
   "just work" on a |trueos| system as they have been pre-configured. In
   these instances, reading the FreeBSD Handbook section can help to
   learn how the system is configured and why it works.

.. index:: help
.. _Search and Portals:

Search and Portals
==================

Many BSD related search portals exist. If unable to find an answer
from the forums or mailing lists, try searching these websites:

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

Many BSD sites and resources may also contain useful information:

* `The FreeBSD Diary <http://www.freebsddiary.org/>`_

* `TrueOS® YouTube channel <https://www.youtube.com/channel/UCyd7MaPVUpa-ueUsGjUujag>`_

* `BSD YouTube channel <https://www.youtube.com/user/bsdconferences>`_

* `BSD Talk <http://bsdtalk.blogspot.com/>`_

* `BSD Now <http://www.bsdnow.tv/>`_

* `BSD Magazine <https://bsdmag.org/>`_ (free, monthly download)

* `FreeBSD Journal <http://www.freebsdjournal.com/>`_ (bi-monthly magazine)

* `BSD Hacks <http://shop.oreilly.com/product/9780596006792.do>`_ (book)

* `The Best of FreeBSD Basics <http://reedmedia.net/books/freebsd-basics/>`_ (book)

* `Definitive Guide to PC-BSD® <http://www.apress.com/9781430226413>`_ (book)
