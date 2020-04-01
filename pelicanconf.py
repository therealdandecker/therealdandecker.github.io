#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dan'
SITENAME = 'Dan Decker'
SITEURL = 'https://dandecker.us'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Anaconda Distribution', 'https://www.anaconda.com/distribution/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/dan-d-789a1ab/'),
          ('Tableau Public', 'https://public.tableau.com/profile/dan.decker#!/'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True