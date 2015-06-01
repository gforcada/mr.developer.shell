.. -*- coding: utf-8 -*-

==================
mr.developer.shell
==================
Run shell commands on all your `mr.developer <https://pypi.python.org/pypi/mr.developer>`_ controlled repositories!

Motivation
==========
I got tired of::

    cd src
    for f in *; do echo $f; cd $f; DO SOMETHING; cd .. ; done

So I created a mr.developer extension to do **exactly** the sambe but nicer::

    ./bin/develop shell "git grep hidden stuff"
