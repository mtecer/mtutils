mtutils
========================

This is a structure template for Python command line applications, ready to be released and distributed via setuptools/PyPI/pip for Python 2 and 3.

Usage
-----

Clone this repository and adopt the mtutils structure for your own project. This is just a starting point, but I hope a good one. From there on, you should read and follow <http://python-packaging-user-guide.readthedocs.org/en/latest/>, the definite resource on Python packaging.

Behavior
--------

### Flexible invocation

The application can be run right from the source directory, in two different ways:

1.  Treating the mtutils directory as a package *and* as the main script:

        $ python -m mtutils arg1 arg2
        Executing mtutils version 0.2.0.
        List of argument strings: ['arg1', 'arg2']
        Stuff and Boo():
        <class 'mtutils.stuff.Stuff'>
        <mtutils.mtutils.Boo object at 0x7f43d9f65a90>

2.  Using the mtutils-runner.py wrapper:

        $ ./mtutils-runner.py arg1 arg2
        Executing mtutils version 0.2.0.
        List of argument strings: ['arg1', 'arg2']
        Stuff and Boo():
        <class 'mtutils.stuff.Stuff'>
        <mtutils.mtutils.Boo object at 0x7f149554ead0>

### Installation sets up mtutils command

Situation before installation:

    $ mtutils
    bash: mtutils: command not found

Installation right from the source tree (or via pip from PyPI):

    $ python setup.py install

Now, the `mtutils` command is available:

    $ mtutils arg1 arg2
    Executing mtutils version 0.2.0.
    List of argument strings: ['arg1', 'arg2']
    Stuff and Boo():
    <class 'mtutils.stuff.Stuff'>
    <mtutils.mtutils.Boo object at 0x7f366749a190>

On Unix-like systems, the installation places a `mtutils` script into a centralized `bin` directory, which should be in your `PATH`. On Windows, `mtutils.exe` is placed into a centralized `Scripts` directory which should also be in your `PATH`.

