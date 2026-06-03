import glob
import os
import sys
import pathlib
import re

# useful strings

repoRoot='/home/lou/Public/Works/Diary/'
proxyRoot='/home/lou/Public/lb42.github.io/Diary/'

from datetime import date
today = str(date.today())

string1='''<!DOCTYPE html>
<html>  <head>   <meta charset="utf-8"/>   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <meta http-equiv="X-UA-Compatible" content="ie=edge"> 
    <link rel="stylesheet" href="../css/diary.css" media="screen" title="no title"/>  
    <script src="../js/CETEI.js"></script>
    <script>
      (new CETEI).getHTML5('https://raw.githubusercontent.com/lb42/Works/master/Diary/'''
string2='''', function(data) {
        document.getElementsByTagName("body")[0].appendChild(data);
      });
    </script>
    <title>'''
string3='''</title>  </head>  <body>
 <img alt="Built with CETEICEAN" src="https://raw.githubusercontent.com/lb42/Works/master/Diary/media/builtWithCeteicean.png" style="width:200px; height:auto; float:right;"/>
   </body></html>'''

teiString='''<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
 <teiHeader>
  <fileDesc>
   <titleStmt>
    <title>Blogging</title>
   </titleStmt>
   <publicationStmt>
    <p>Unpublished draft</p>
   </publicationStmt>
   <sourceDesc>
    <p>AMOW</p> 
   </sourceDesc>
  </fileDesc>
  <revisionDesc>
   <change when="'''+today+'''">Written by diarize.py</change>
  </revisionDesc>
 </teiHeader>
 <text>
<body>
 <div><head>Summary</head>
'''

# Script to process Diary files

if (len(sys.argv) != 2) :
    print(len(sys.argv))
    print("Usage: python diarize.py [year] ")
    print("  [year] identifies subdirectory containing files")
else :
    YEAR=sys.argv[1]
    fileName=YEAR+'-summary.xml'
    fileTitle='The '+YEAR+' summary'
    proxyFile=proxyRoot+YEAR+'-summary.html'
# first create summary file and its proxy
    with open(fileName, "a") as iF:
        iF.write(teiString)
        string=string1+YEAR+'/'+fileName+string2+fileTitle+string3
        with open(proxyFile, "w") as f:
            f.write(string)
# now loop round individual files
            FILES=sorted(glob.glob(YEAR+'/'+'*.xml'))
            print(str(len(FILES))+' files found')
            for FILE in FILES:
# read the file to get its title
                txt = pathlib.Path(FILE).read_text()
                result=re.search('<title>(.+)<\/title>',txt)
                fileTitle=result.group(1)
# create a proxy
                proxyFile2=proxyRoot+pathlib.Path(FILE).stem+'.html'
                print(FILE+' has proxy '+proxyFile2)
                with open(proxyFile2, "w") as f:
                   string=string1+FILE+string2+fileTitle+string3
                   f.write(string)
                   f.close()
# add info to summary file        
                link='<ref target="'+proxyFile2+'">'+fileTitle+'</ref>'
                print(link)
                iF.write(link)


