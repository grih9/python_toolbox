# Copyright 2009-2010 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

'''
This module defines the ProcessCruncher class.

See its documentation for more information.

This module requires the multiprocessing package to be installed. It is part of
the standard library for Python 2.6 and above, but not for earlier versions.
Backports of it for Python 2.4 and 2.5 are available on the internet.
'''

try:
    import multiprocessing # tododoc: import_if_exists
except ImportError:
    raise ImportError('The backported multiprocessing package is needed. '
                      'Search for it online and install it.')

from .process_cruncher import ProcessCruncher
