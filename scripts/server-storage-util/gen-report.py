import argparse
import datetime

args=argparse.ArgumentParser()

args.add_argument("--outFile","-o",type=str,help="Output file",default="../../reports/server-storage-util/index.html")
args = args.parse_args()

fOut = open(args.outFile,"w+")

fOut.write('''
<html>
<head>
<title>Server Storage Usage</title>
</head>
<body>
<h1>Server Storage Usage</h1>
<p>This table shows the usage reports for folders that are larger than 10G on the Turing server.</p>

''')

for ss in ["kepler","turing"]:
    ff = "../../reports/server-storage-util/logs/{}-storage.log".format(ss)
    fIn = open(ff,"r")

    lines = fIn.readlines()
    fOut.write("<b>{}</b> Read on: </td><td>".format(ss)+lines[0]+"</td></tr><br><br>\n")


    fOut.write('''
    <table border="1" style="border-collapse:collapse;">
    <tr>
    <th>Usage</th>
    <th>Path</th>
    </tr>
    ''')








    for line in lines[1:]:
        fOut.write("<tr><td>" + line.split()[0] + "</td><td>" + line.split()[1] + "</td></tr>\n")

    fOut.write('''
    </table>
    <br><br>''')


fOut.write('''
<p>This page was last updated on {}.</p>

</body>
</html>
'''.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

fIn.close()
fOut.close()

print("END: gen-report.py ( -> " + args.outFile + ")")