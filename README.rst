===============================
General Words
===============================

.. image:: https://badge.fury.io/py/generalwords.png
    :target: http://badge.fury.io/py/generalwords

.. image:: https://travis-ci.org/petrilli/generalwords.png?branch=master
        :target: https://travis-ci.org/petrilli/generalwords

.. image:: https://pypip.in/d/generalwords/badge.png
        :target: https://pypi.python.org/pypi/generalwords

Often, when building an application, I've had occasions where I need to provide
a nonce of some sort to a user.  A nonce is some thing, whether number, or
otherwise, that is used only once.


Goals
-----

The over-arching goal was for this to be simple to use,
and reasonably fast. Next, I wanted something that the average user would be
able to enter manually with minimal risk.  This ruled out a lot of the crazy
mixed-case alphanumeric strings that are often used.  Finally,
a goal was to have a reasonably large number of permutations available so
that the nonce, while not cryptographically strong, was strong enough for
uses like registration, password reset, etc.  For example, with the default
`word source`_, and a selection of three words, there are
`almost 19 billion permutations`_ available.  Presuming you're doing any form
of brute-force-attack prevention, this should be more than adequate.

.. _almost 19 billion permutations: http://www.wolframalpha.com/input/?i=number+of+3+permutations+of+2668+objects


Word Source
-----------

The list of words comes from the `New General Service List`_ v1.01. The original
list, distributed in Excel format, is covered under the
`Creative Commons Attribution 3.0 Unported License`_. More information can be
found on the website. From the base data, the following changes have been made:

#. The list was converted from Excel to a simple one-word-per-line text file
   format;
2. Only headwords were retained for clarity;
3. Supplemental words, such as months and numbers, were added;
3. Words less than 4 characters were removed.

Combined, a total of 2,668 headwords were retained.

.. _New General Service List: http://www.newgeneralservicelist.org/
.. _Creative Commons Attribution 3.0 Unported License: http://creativecommons.org/licenses/by/3.0/deed.en_US


Usage Example
-------------

The library is trivially easy to use::

    >>> from generalwords import *
    >>> get_word()
    'tire'
    >>> get_word()
    'offense'
    >>> get_words(n=3)
    ('climb', 'repair', 'force')

In the future, there may be more options, but not right now.


Not Done Yet
------------

While the library will never be massively complicated, there's a few things I'd
like to have in the future:

* Expand to other languages
* Add additional word sources
