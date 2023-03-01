import argparse
import datetime

args=argparse.ArgumentParser()
args.add_argument("--inFile","-i",type=str,help="Input file",default="temp.txt")
args.add_argument("--outFile","-o",type=str,help="Output file",default="../../reports/turing-storage-usage/index.html")
args = args.parse_args()

fIn = open(args.inFile,"r")
fOut = open(args.outFile,"w+")

fOut.write('''
<html>
<head>
<title>Turing Storage Usage</title>
</head>
<body>
<h1>Turing Storage Usage</h1>
<p>This table shows the usage reports for folders that are larger than 10G on the Turing server.</p>

<table border="1" style="border-collapse:collapse;">
<tr>
<th>Usage</th>
<th>Path</th>
</tr>
''')
lines = fIn.readlines()
for line in lines:
    fOut.write("<tr><td>" + line.split()[0] + "</td><td>" + line.split()[1] + "</td></tr>\n")
fOut.write('''
</table>
<p>This page was last updated on {}.</p>

</body>
</html>
'''.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

fIn.close()
fOut.close()

print("END: gen-report.py (" + args.inFile + " -> " + args.outFile + ")")