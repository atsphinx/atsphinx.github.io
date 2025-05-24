=================
Versioning policy
=================

We use `Semantic Versioning 2.0.0 <https://semver.org/spec/v2.0.0.html>`_ for versioning,
and we define detail rules some cases.

.. important::

   This is standard rules overall atsphinx project.
   If they conflicts package specify rule, packagerules are prior to them.

"API" as Sphinx extension
=========================

  MAJOR version when you make incompatible API changes.

We define API is that "Input and output structure" as Sphinx extension.
Details, we define "input" and "output" as these:

* Input

  * Configuration definition.
  * Directive specs.

* Output

  * Output as data structure by builder.
  * Console messages.

We will update MAJOR version when it has changes them incompatibility. [#]_

.. [#] If output HTML is changed but is not difference as DOM, it is not "incompatibility changes".

Updating version of dependencies
================================

We will update MINOR version when it has only update min version of dependencies and Python runtime.

.. note::

    When it must change argument of :py:meth:`sphinx.application.Sphinx.require_sphinx` [#]_ from ``(7, 4)`` to ``(8, 0)``.
    it is not MAJOR version update if API does not change, because it has "incompatibility changes". [#]_

.. [#] This is called by ``setup`` function of extension to assert for requires min version of Sphinx.
.. [#] Ofcourse, it updates MAJOR version if it drops compatibility (e.g. drop need not configurations).

When do it updates to v1 from v0.x
==================================

We don't want to afraid updating for ``v1.x``.
Therefore, we write simple rule for that it can update ``v1.0``.

* We create issues labeled "enhancement" and marked milestone "v1.0" after first publish.
  These issues are "First goal" that we want to do by extension.
* We develop for marked issues, but it may change order to other issues.
* When we can close all marked issues, it is updated as ``v1.0.0``.
