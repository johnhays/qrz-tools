#!/usr/bin/python
import sys
import getopt
import csv
import xml.etree.ElementTree as ET
import urllib

def isValid(v):
	if v == None:
		return ""
	else:
		return v.text



def lookup(key,call,ns):
	url = "http://xmldata.qrz.com/xml/current/?s=" + key + ";callsign=" + call
	calltxt = urllib.urlopen(url).read()
	callroot = ET.XML(calltxt)
	call = isValid(callroot.find('.//qrz:call',ns))
	fname = isValid(callroot.find('.//qrz:fname',ns))
	name = isValid(callroot.find('.//qrz:name',ns))
	addr1 = isValid(callroot.find('.//qrz:addr1',ns))
	addr2 = isValid(callroot.find('.//qrz:addr2',ns))
	state = isValid(callroot.find('.//qrz:state',ns))
	zipcode = isValid(callroot.find('.//qrz:zip',ns))
	country = isValid(callroot.find('.//qrz:country',ns))
	address = {'call': call,'fname':fname,'name':name,'addr1':addr1,'addr2':addr2,'state':state,'zip':zipcode,'country':country}
	return address

def main(argv):
	inputfile = ''
	outputfile = ''
	login = ''
	pwd = ''
	try:
		opts, args = getopt.getopt(argv,"hi:l:p:o:")
	except getopt.GetoptError:
		print sys.argv[0] + ' -l <qrz login> -p <qrz password> -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print sys.argv[0] + ' -l <qrz login> -p <qrz password> -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt == '-l':
			login = arg
		elif opt == '-p':
			pwd = arg
		elif opt == '-i':
			inputfile = arg
		elif opt == '-o':
			outputfile = arg
	print 'Input file is ', inputfile
	print 'Output file is ', outputfile
	target_url = "http://xmldata.qrz.com/xml/current/?username=" + login + "&password=" + pwd + ";agent=q5.0"
	sessiontxt = urllib.urlopen(target_url).read()
	root = ET.XML(sessiontxt)
	ns = {'qrz': 'http://xmldata.qrz.com'}
	Key = root.find('.//qrz:Key',ns).text

	with open(outputfile, 'w') as csvfile:
		fieldnames = ['call','fname','name','addr1','addr2','state','zip','country']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		
		writer.writeheader()
	
		with open(inputfile,'r') as callfile:
			reader = csv.DictReader(callfile);
			for crow in reader:
				print crow['CALL']
				writer.writerow(lookup(Key,crow['CALL'],ns))
	
if __name__ == "__main__":
   main(sys.argv[1:])

