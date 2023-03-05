# pelican_feed_xslt

This is a [Pelican](https://github.com/getpelican/pelican/) plug-in that adds
an XSLT processing instruction to feeds.



## Usage

In the Pelican configuration file, specify the link or relative path to the
RSS and/or Atom XSLT files by setting `XSLT_PATH_RSS` or `XSLT_PATH_ATOM`:

```python
# pelican.conf

XSLT_PATH_RSS = "rss.xsl"
XSLT_PATH_ATOM = "atom.xsl"
```
