<xsl:stylesheet
  version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
>
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="no"/>
  <xsl:template match="/rss/channel">
    <html xmlns="http://www.w3.org/1999/xhtml">
      <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title>RSS feed - <xsl:value-of select="title"/></title>
        <style type="text/css">
          body { font: 1em sans-serif; margin: 0 auto 2em; width: 800px; }
          h2 { margin: 0 0 1rem; }
          .post { border: 1px solid #000; padding: 1em; margin: 1em 0; }
        </style>
      </head>
      <body>
        <h1>
          <a href="{link}">
            <xsl:value-of select="title"/>
          </a>
        </h1>
        <xsl:apply-templates select="item"/>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="item">
    <div class="post">
      <h2>
        <a href="{link}">
          <xsl:value-of select="title"/>
        </a>
      </h2>
      <p>
        <time>
          Published: <xsl:value-of select="pubDate"/>
        </time>
      </p>
      <xsl:value-of select="description" disable-output-escaping="yes"/>
    </div>
  </xsl:template>
</xsl:stylesheet>
