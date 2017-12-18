# qrz-tools
Tools for generating data out of QRZ.com

## getaddresses.py

A python script to take in a CSV file which contains callsigns under the header **CALL** and create a CSV that can be used with a mail merge package to create mailing labels to send out QSL cards.

You must have a QRZ.com account with [XML Data](https://www.qrz.com/page/xml_data.html) permissions.

Execution:
**./getaddresses.py -l <qrz login> -p <qrz password> -i <inputfile> -o <outputfile>**

If you log your contacts on QRZ.com, you can pull down your log as an adif, then use an [ADIF to CSV](http://software.ad1c.us/ADIF_to_CSV/index.html) to create a CSV for input to this script.

