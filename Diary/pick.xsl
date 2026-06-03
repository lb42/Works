<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
 xmlns:xs="http://www.w3.org/2001/XMLSchema"

 xmlns:content="http://purl.org/rss/1.0/modules/content/" 
 xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:excerpt="http://wordpress.org/export/1.1/excerpt/" 
 exclude-result-prefixes="xs content"
 version="3.0">
 <xsl:template match="/">
 <body> <xsl:apply-templates select="//item"/>
</body> </xsl:template>
 
 <xsl:template match="item">
  <div>
   <head>
   <xsl:attribute name="ref"><xsl:value-of select="link"/></xsl:attribute>
    <xsl:value-of select="title"/>
   </head>
   <xsl:value-of select="content:encoded"/>
  </div>
 </xsl:template>
</xsl:stylesheet>