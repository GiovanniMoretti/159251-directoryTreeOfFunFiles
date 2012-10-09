#! /usr/bin/python

import os, os.path, sys

def makeLink(path, label):
  return '<a href="%s">%s</a>' % (path, label)


def makeImgLink(path):
  return '<img src="%s" width="100px">' % path

if len(sys.argv) != 3:
    print "Usage: makesite <indexFileName> <directory containing content>"
    sys.exit(1)
else:
    indexFile = sys.argv[1]
    contentDirectory = sys.argv[2]

# Build a list of table rows, each with two cells: 1st has filename, 2nd a download link
rows= []
for root, dirs, files in os.walk(contentDirectory):
   for file in files:
      path = os.path.join(root, file)
      xxx, ext = os.path.splitext(file)
      if ext.lower() in [".jpg", ".png"]:
         url = makeImgLink(path)
      else:
         url = makeLink(path, file)
      s = " <tr>\n  <td>%s</td>\n  <td>%s</td>\n</tr>" %(file, url)
      rows.append(s)

# Page Header
header= """<html>
<body>
<title>159251 Web Demo</title>
</body>
<html>
<h2>Lots of fun files to play with</h2>
<table border="2", width="90%">
"""

# write out the header, then the table rows
f = open (indexFile, "w")
f.write(header)
for thisrow in rows:
   f.write(thisrow + "\n")

# close the page
f.write("</table></body></html>")
f.close()
