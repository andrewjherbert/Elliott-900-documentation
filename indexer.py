# INDEXER - program to insert HTML index files in Elliott Archive "Manuals"
# directory tree
# Andrew Herbert 23/07/2020

import os.path
import sys

mb        = 1000000
hundredmb = 100 * mb

def fullName (path, name):
    return path + '/' + name

def ignore (path):
#	print('Ignoring', path)
	return

def indexPath (path, name, depth):

    filenames = os.listdir (path)
    filenames.sort ()

    if depth == 1:
        for n in filenames:
            pn = fullName (path, n)
            if os.path.isdir (pn):
                if  n.startswith('.'):
                    ignore (pn)
                else:
                    indexPath (pn, n, depth+1)
        return

    parent = '../' * (depth-1)

    outfile = open (path + '/index.htm', 'w')
    outfile.write ('<html>\n')
    outfile.write ('<body>\n')
    outfile.write ('<IMG alt="Elliott 900 Banner" src="' + parent +
                   ('Elliott%20900%20banner.jpg"'
                    ' width=631 height=239>'))
    outfile.write ('<H1>Contents of ' + name + '</H1>')
    outfile.write ('<table>\n')

    count = 0

    for n in filenames:

        pn = fullName (path, n)
        nl = n.lower()

        if n.startswith ('.'):
            ignore (pn)
            continue

#        if nl == 'index.htm.old':
#            print('Deleting', pn)
#            os.remove (pn)
#            continue

        if nl == 'index.htm' or nl == 'index.html' or nl == 'indexer.py':
            continue

        size = os.path.getsize (pn)
        if size >= hundredmb:
            print(pn, 'is larger than 100mb', size / mb, 'mb')

        if count % 3 == 0:
            outfile.write ('<tr>\n')

        if os.path.isfile (pn):
            outfile.write ('<td style="padding:10px"><a href="' +
                               n + '">' + n + '</a></td>\n')

        elif os.path.isdir (pn):
            outfile.write ('<td style="padding:10px"><a href="' +
                               n + '/index.htm">' + n + '</a></td>\n')
            indexPath (pn, n, depth+1)

        else:
            continue

        if count % 3 == 2:
            outfile.write ('</tr>\n')

        count = count + 1

    if count % 3 != 2:
        outfile.write ('</tr>\n')

    outfile.write ('</table>\n')
    outfile.write (('<br><br><br><a href="..">BACK TO PARENT</a>'
                   '&nbsp&nbsp&nbsp<a href="') + parent + '">BACK TO TOP</a>')
    outfile.write ('</body>\n')
    outfile.write ('</html>\n')
    outfile.close ()

# Main program
indexPath ('.', 'Elliott Documents', 1)

