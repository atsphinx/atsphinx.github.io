=====================
Organization overview
=====================

We are many repositories on this organization.
But all repositories are not Sphinx extensions.

Overview
========

+------------------+--------------------------+-------------------+
| Category         | Published on             | Visibility        |
+==================+==========================+===================+
| Core projects    | PyPI                     | Public [#f1]_     |
+------------------+--------------------------+-------------------+
| Sub projects     | PyPI or other registries | Public [#f1]_     |
+------------------+--------------------------+-------------------+
| Support projects | Not published            | Public or Private |
+------------------+--------------------------+-------------------+

.. [#f1] Core projects and Sub projects are not always are public repositories.
    When we do prototype, we keep them as private repositories.

Categories of repositories
==========================

Core projects
-------------

These are Python projects published on PyPI using the ``atsphinx.`` namespace.
You can use them as Sphinx extensions or utility of your Sphinx extensions.

Sub projects
------------

These are published projects too, but they are different from "Core projects".

* Published on PyPI without ``atsphinx.`` namespace.
* Published on package registries of other languages.

We manage related projects on this organization as "Sub projects". [#f2]_
You will use them as dependencies of "Core projects".

.. [#f2] rst2revealjs is managed on this organization, but it is not Sphinx extension.

Support projects
----------------

These are repositories to support our organization. [#f3]_
A some projects of them are managed as private repositories.

.. [#f3] This website is Sphinx document project to describe our organization.
    So this is managed on GitHub as "Support projects".
