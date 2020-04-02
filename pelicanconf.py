#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dan'
SITENAME = 'Dan Decker'
SITESUBTITLE = 'A semi-pro blog'
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

#HOME_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'

AUTHORS_BIO = {
  "zutrinken": {
    "name": "Dan Decker",
    "cover": "https://casper.ghost.org/v1.0.0/images/team.jpg",
    #"image": "assets/images/avatar.png",
    "website": "https://dandecker.us",
    "linkedin": "https://www.linkedin.com/in/dan-d-789a1ab/",
    "github": "https://github.com/therealdandecker",
    "location": "USA",
    "bio": "Dan Decker is not a pulizer winning writer, but anyone wiht Python skills can make a website these days."
  }
}