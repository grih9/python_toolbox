# Copyright 2009-2011 Ram Rachum.
# This program is distributed under the LGPL2.1 license.

"""
"Almost" import the entire Python 2.6 standard library.

This is so py2exe will think we're actually using all of it, and bundle it for
our app.

Todo: This currently doesn't import submodules which aren't imported by the
package itself. (For example `email`.)
"""

if False:
    import AutoComplete
    import AutoCompleteWindow
    import AutoExpand
    import BaseHTTPServer
    import Bastion
    import Bindings
    import CGIHTTPServer
    import CallTipWindow
    import CallTips
    import Canvas
    import ClassBrowser
    import CodeContext
    import ColorDelegator
    import ConfigParser
    import Cookie
    import Debugger
    import Delegator
    import Dialog
    import DocXMLRPCServer
    import EditorWindow
    import FileDialog
    import FileList
    import FixTk
    import FormatParagraph
    import GrepDialog
    import HTMLParser
    import HyperParser
    import IOBinding
    import IdleHistory
    import MimeWriter
    import MultiCall
    import MultiStatusBar
    import ObjectBrowser
    import OutputWindow
    import ParenMatch
    import PathBrowser
    import Percolator
    import PyParse
    import PyShell
    import Queue
    import RemoteDebugger
    import RemoteObjectBrowser
    import ReplaceDialog
    import ScriptBinding
    import ScrolledList
    import ScrolledText
    import SearchDialog
    import SearchDialogBase
    import SearchEngine
    import SimpleDialog
    import SimpleHTTPServer
    import SimpleXMLRPCServer
    import SocketServer
    import StackViewer
    import StringIO
    import Tix
    import Tkconstants
    import Tkdnd
    import Tkinter
    import ToolTip
    import TreeWidget
    import UndoDelegator
    import UserDict
    import UserList
    import UserString
    import WidgetRedirector
    import WindowList
    import ZoomHeight
    import _LWPCookieJar
    import _MozillaCookieJar
    import __future__
    import _abcoll
    import _bsddb
    import _ctypes
    import _ctypes_test
    import _elementtree
    import _hashlib
    import _msi
    import _multiprocessing
    import _socket
    import _sqlite3
    import _ssl
    import _strptime
    import _testcapi
    import _threading_local
    import _tkinter
    import abc
    import aboutDialog
    import aifc
    import anydbm
    import ast
    import asynchat
    import asyncore
    import atexit
    import audiodev
    import base64
    import bdb
    import binhex
    import bisect
    import bsddb
    import bz2
    import cProfile
    import calendar
    import cgi
    import cgitb
    import chunk
    import cmd
    import code
    import codecs
    import codeop
    import collections
    import colorsys
    import commands
    import compileall
    import compiler
    import configDialog
    import configHandler
    import configHelpSourceEdit
    import configSectionNameDialog
    import contextlib
    import cookielib
    import copy
    import copy_reg
    import csv
    import ctypes
    import curses
    import dbhash
    import decimal
    import difflib
    import dircache
    import dis
    import distutils
    import doctest
    import dumbdbm
    import dummy_thread
    import dummy_threading
    import dynOptionMenuWidget
    import email
    import encodings
    import filecmp
    import fileinput
    import fnmatch
    import formatter
    import fpformat
    import fractions
    import ftplib
    import functools
    import genericpath
    import getopt
    import getpass
    import gettext
    import glob
    import gzip
    import hashlib
    import heapq
    import hmac
    import hotshot
    import htmlentitydefs
    import htmllib
    import httplib
    import idle
    import idlelib
    import idlever
    import ihooks
    import imaplib
    import imghdr
    import imputil
    import inspect
    import io
    import json
    import keybindingDialog
    import keyword
    import lib2to3
    import linecache
    import locale
    import logging
    import macosxSupport
    import macpath
    import macurl2path
    import mailbox
    import mailcap
    import markupbase
    import md5
    import mhlib
    import mimetools
    import mimetypes
    import mimify
    import modulefinder
    import msilib
    import multifile
    import multiprocessing
    import mutex
    import netrc
    import new
    import nntplib
    import ntpath
    import nturl2path
    import numbers
    import opcode
    import optparse
    import os
    import os2emxpath
    import pdb
    import pickle
    import pickletools
    import pipes
    import pkgutil
    import platform
    import plistlib
    import popen2
    import poplib
    import posixfile
    import posixpath
    import pprint
    import profile
    import pstats
    import pty
    import py_compile
    import pyclbr
    import pydoc
    import pydoc_topics
    import pyexpat
    import quopri
    import random
    import re
    import repr
    import rexec
    import rfc822
    import rlcompleter
    import robotparser
    import rpc
    import run
    import runpy
    import sched
    import select
    import sets
    import sgmllib
    import sha
    import shelve
    import shlex
    import shutil
    import site
    import smtpd
    import smtplib
    import sndhdr
    import socket
    import sqlite3
    import sre
    import sre_compile
    import sre_constants
    import sre_parse
    import ssl
    import stat
    import statvfs
    import string
    import stringold
    import stringprep
    import struct
    import subprocess
    import sunau
    import sunaudio
    import symbol
    import symtable
    import tabbedpages
    import tabnanny
    import tarfile
    import telnetlib
    import tempfile
    import test
    import testcode
    import textView
    import textwrap
    import this
    import threading
    import timeit
    import tkColorChooser
    import tkCommonDialog
    import tkFileDialog
    import tkFont
    import tkMessageBox
    import tkSimpleDialog
    import toaiff
    import token
    import tokenize
    import trace
    import traceback
    import tty
    import turtle
    import types
    import unicodedata
    import unittest
    import urllib
    import urllib2
    import urlparse
    import user
    import uu
    import uuid
    import warnings
    import wave
    import weakref
    import webbrowser
    import whichdb
    import winsound
    import wsgiref
    import xdrlib
    import xml
    import xmllib
    import xmlrpclib
    import zipfile