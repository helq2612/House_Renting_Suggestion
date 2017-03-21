#!/usr/bin/env python
from tempfile import NamedTemporaryFile
import csv
import re
import shutil
def clean():
	filename = 'first.csv'
	tempfile = NamedTemporaryFile(delete=False)
	with open(filename, "rU") as csvFile, tempfile:

		rows = csv.reader(csvFile)
		writer = csv.writer(tempfile)
		idx = 0
		for row in rows:
			if row == "":
				continue
			s = row[0]
			
			#print "idx =", idx, "len = ", len(s)
			#print "row =", s#, "row type =", type(row[0])
			s = s.replace("\n", "")
			s = s.replace(" ", "")
			s = s.replace(",", "")
			s = s.replace("-", "")
			#print "row =", s#, "row type =", type(row[0])
			#print type(s), len(s)
			#print "*******************"
			s = "".join(s.split())
			pattern = re.compile(r'r*.*?ft')
			
			try:
				m = re.search('(.\d+)ft', str(s)).group()
			except AttributeError:
				m = ""


			m = m.replace("r","")
			m = m.replace("ft","")
			m = m.replace(" ","")

			try:
				mm = re.search('(\d+)br', str(s)).group()
			except AttributeError:
				mm = ""
			mm = mm.replace("r","")
			mm = mm.replace("b","")
			mm = mm.replace("ft","")
			mm = mm.replace(" ","")
			
			#else:
			#	print "not found, m =", m
			#print "idx =", idx,"M=",m, "pid=",row[5],"price=", row[4]
			if idx != 0:
				if m != "":
					row[0] = m 
					
				else:
					row[0] = ""
				if mm != "":
					row[1] = mm
				else:
					row[1] = ""
				#print "len=", len(row)
				#dd = [str(m), str(row[5]),str(row[4])]
				writer.writerow(row)

			writer.writerow(row)
			idx += 1
			#if idx == 10:
			#	break
	shutil.move(tempfile.name, filename)
	pass




if __name__ == '__main__':
	clean()
	