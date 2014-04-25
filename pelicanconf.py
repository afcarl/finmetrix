#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Stanislav Khrapov'
SITENAME = u'Pythonic FinMetrix'
SITEURL = 'http://khrapovs.github.io/finmetrix'

GITHUB_URL = 'http://github.com/khrapovs/'
GITHUB_USER = 'khrapovs'

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DIRECT_TEMPLATES = ('index', 'archives', 'tags')

# Paths
STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.ico']
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plugins
THEME = '../pelican-octopress-theme/'
#THEME = '../pelican-themes/plumage/'
#THEME = '../pelican-themes/blueidea/'
# Plugins
PLUGIN_PATH = '../pelican-plugins/'
PLUGINS = ['summary', 'sitemap', 'render_math',
		   'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']


TRACKING_CODE = "<script>\n\
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){\n\
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n\
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n\
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');\n\
\n\
  ga('create', 'UA-17393493-6', 'google.com');\n\
  ga('send', 'pageview');\n\
</script>\n"

# The theme file should be updated so that the base header contains the line:
#
#  {% if EXTRA_HEADER %}
#    {{ EXTRA_HEADER }}
#  {% endif %}
# 
# This header file is automatically generated by the notebook plugin
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = TRACKING_CODE + open('_nb_header.html').read().decode('utf-8')

# Title menu options
MENUITEMS = (('About', 'https://sites.google.com/site/khrapovs'),
             ('Contact', 'mailto:khrapovs@gmail.com'),
             ('Archives', '/archives.html'))

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('LinkedIn', 'http://www.linkedin.com/in/khrapovs'),
		  ('Twitter', 'https://twitter.com/khrapovs'),
          ('Google+', 'https://www.google.com/+StanislavKhrapov'),)

# Sharing
GOOGLE_PLUS_USER = 'StanislavKhrapov'
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = False
TWITTER_USER = 'khrapovs'
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = False
TWITTER_FOLLOW_BUTTON = False
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
#TWITTER_SHOW_FOLLOWER_COUNT = False

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = False

# Delete the output directory, and all of its contents, before generating new files.
# This can be useful in preventing older, unnecessary files from persisting in your output.
DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# RSS/Atom feeds
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

GOOGLE_ANALYTICS = "UA-17393493-7"
DISQUS_SITENAME = "pythonicfinmetrix"

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}