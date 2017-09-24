.. towers

Towers of Hanoi for Python
==========================

.. image:: https://img.shields.io/badge/Author:%20francis%20horsman-Available-brightgreen.svg?style=plastic
    :target: https://www.linkedin.com/in/francishorsman
    :alt: Author
.. image:: https://travis-ci.org/sys-git/towers.svg?branch=master
    :target: https://travis-ci.org/sys-git/towers
.. image:: https://coveralls.io/repos/github/sys-git/towers/badge.svg
    :target: https://coveralls.io/github/sys-git/towers
.. image:: https://readthedocs.org/projects/towers/badge/?version=latest
    :target: http://towers.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://badge.fury.io/py/towers.svg
    :target: https://badge.fury.io/py/towers
.. image:: https://img.shields.io/pypi/l/towers.svg
    :target: https://img.shields.io/pypi/l/towers.svg
.. image:: https://img.shields.io/pypi/wheel/towers.svg
    :target: https://img.shields.io/pypi/wheel/towers.svg
.. image:: https://img.shields.io/pypi/pyversions/towers.svg
    :target: https://img.shields.io/pypi/pyversions/towers.svg
.. image:: https://img.shields.io/pypi/status/towers.svg
    :target: https://img.shields.io/pypi/status/towers.svg
.. image:: https://pyup.io/repos/github/sys-git/towers/shield.svg
    :target: https://pyup.io/repos/github/sys-git/towers/
    :alt: Updates
.. image:: https://pyup.io/repos/github/sys-git/towers/python-3-shield.svg
    :target: https://pyup.io/repos/github/sys-git/towers/
    :alt: Python 3

The **`Towers of Hanoi`** algorithm.

.. toctree::
    :maxdepth: 1
    :caption: Main modules:

    towers
    rods
    rod
    disk
    errors
    validation
    moves


Example
-------

.. code-block:: python

    >>> tower = Towers(height=3)
    >>> print(tower)
    Towers(Rods(3 - start([***, **, *]), end([]), tmp([])))

    >>> print('moves required: {moves}'.format(moves=tower.moves_for_height(height)))
    moves required: 7

    >>> with tower:
    ...    for i in tower:
    ...        print(i)
    Move(disk=*, start=Rod(name='start', disks=[***, **, *], height=3), end=Rod(name='end', disks=[], height=3), moves=0)
    Move(disk=**, start=Rod(name='start', disks=[***, **], height=3), end=Rod(name='tmp', disks=[], height=3), moves=1)
    Move(disk=*, start=Rod(name='end', disks=[*], height=3), end=Rod(name='tmp', disks=[**], height=3), moves=2)
    Move(disk=***, start=Rod(name='start', disks=[***], height=3), end=Rod(name='end', disks=[], height=3), moves=3)
    Move(disk=*, start=Rod(name='tmp', disks=[**, *], height=3), end=Rod(name='start', disks=[], height=3), moves=4)
    Move(disk=**, start=Rod(name='tmp', disks=[**], height=3), end=Rod(name='end', disks=[***], height=3), moves=5)
    Move(disk=*, start=Rod(name='start', disks=[*], height=3), end=Rod(name='end', disks=[***, **], height=3), moves=6)

    >>> print(tower)
    Towers(Rods(3 - start([]), end([***, **, *]), tmp([])))

    >>> print('moves taken: {moves}'.format(moves=tower.moves))
    moves taken: 7

Installation
------------

Instructions can be found :ref:`here <installation>`


Contributions
-------------

Guidelines can be found :ref:`here <contributing>`

Authors can be found :ref:`here <authors>`


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
