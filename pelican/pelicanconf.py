AUTHOR = "John Beers"
SITENAME = "johnbeers.xyz"
SITEURL = "https://johnbeers.xyz"

PATH = "content"

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget
SOCIAL = (
    ("Mastodon", "https://mastodon.social/@johnbeers"),
    ("Codeberg", "https://codeberg.org/jaerrib"),
    ("GitHub", "https://github.com/jaerrib/"),
    ("LinkedIn", "https://www.linkedin.com/in/john-beers9/"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

OUTPUT_PATH = "../"

THEME = "../pelican/theme/custom"

GRAVATAR_HASH = "dc88c852458e2bbb8cdd62be0cf9e26c50014cb3a593afcb04848d23801c10d6"
