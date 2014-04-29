import xml.etree.ElementTree as ET
import codecs, urllib2




xmlSource = "qald-4_multilingual_train.xml"
lang = "en"
resultFile = codecs.open("qald4-questions-"+lang, "w", "utf-8")
dump = ET.parse(xmlSource)
root = dump.getroot() 
questEN = root.findall(".//question/string[@lang='" + lang + "']")   
# write questions to file
S = ""
for q in questEN:
	resultFile.write(q.text + "\n")
	S = S + q.text + " "
resultFile.close()


# add all questions up to one string S and push the enire thing to the SRL service:
# call SRL service for each sentence and write reponse to file
endpoint = 'http://141.52.218.56:9090/axis2/services/analysis_en/analyze'
DATA = '<analyze><text>{SENTENCE}</text><target>relations</target></analyze>'.format(SENTENCE=S)
HEADER = {'Content-type' : 'text/xml'}

request = urllib2.Request(endpoint, data=DATA, headers=HEADER)
response = urllib2.urlopen(request).read()


"""
sample SRL request via curl:
-----------------------------
curl -H 'Content-type:text/xml' -d '<analyze><text>Cave Story is a freeware platform-adventure video game released in 2004 for the PC.</text><target>relations</target></analyze>' 'http://141.52.218.56:9090/axis2/services/analysis_en/analyze'
"""
