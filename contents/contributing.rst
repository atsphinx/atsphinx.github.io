=========================
Contributing for projects
=========================

This is guideline to contribute for ``atsphinx`` packages.

Supporting languages
====================

Sources languages
-----------------

Default language of repository is English.

You must write these contents by English.

* Source code tokens (variables, functions and more)
* Comments of codes (simple comment and docstrings)
* Base documentation ( ``docs`` directory)
* README and CHANGES
* Commit logs

Documentation suports i18n.
If you want to write out documents for your language,
generate po files of language using ``sphinx-intl``.

.. warning::

   I am writing documents by English and Japanese (using i18n) [#f1]_ .
   When some package updates, I do not follow po files of other languages.

.. [#f1] These are native language and second language of attakei.

Issues ang pull-requests.
-------------------------

All projects accept English or Japanese as issues and pull-requests [#f1]_ .

When you find any troubles of specified package.
================================================

You should create new issue to repository of package.
I will check issues and work for these.

If you can write patch, please create pull-requests directly
(e.f. : you find typo in docs).

Do you have any ideas want to use on Sphinx?
============================================

If you have ideas of Sphinx-extension but difficult to implement for you,
please write it as ideas into `organization's disuccsion <https://github.com/orgs/atsphinx/discussions>`_.

I may develop it instead of you (it is not always for all ideas).
