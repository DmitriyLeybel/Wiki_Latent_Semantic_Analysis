# requires os and re to be imported

import os, re

#file_list = os.listdir('test_corpus') # get list of files
file_list = os.listdir('toywikicorpus') # get list of files

word_freq = {} # create a new "dictionary" -- special kind of list
				# check out: http://www.tutorialspoint.com/python/python_dictionary.htm
word_list = []
docs = []

X = 40 # what size chunk of text will define a "document" (to get multi-docs from 1 transcript)
		
for fname in file_list: # loop thru file names (string variables)
	#if len(re.findall('^P',fname)): # only find chat files (start with P)
	if len(re.findall('.txt$',fname)): # only find chat files (start with P)
		#print(fname)
		#fpath = 'test_corpus/' + fname # get path to the file 
		fpath = 'toywikicorpus/' + fname # get path to the file 
		fl = open(fpath,'r') 
		flc = fl.read()
		lines = flc.split('\n') # if you look at flc, you'll see this is the line separator
		lines_by_X = 1
		line_count = 0 # reset line count
		for line in lines:
			line_count = line_count + 1 # keep track of line count
			if len(line)>0:
				# check inside the file using flc: this character delimits the content, so let's split
				#items = line.split('\xa0') 
				#said = items[1]
				said = line
				# print said # for debugging purposes, earlier
				said = said.lower() # lowercase everything
				said = re.sub('\,','',said) # remove the comma ,
				said = re.sub('\.','',said) # remove periods .
				said = re.sub('\?','',said) # remove the ?
				said = re.sub('\"','',said) # remove the "
				said = re.sub('  ',' ',said) # remove any double spaces
				words = said.split() # let's get a list of words!
				for word in words: # loop through each of them
					if len(word):
						# will give us a key like 'dog,filename-1' where 1 is first block of X, etc.					
						word_doc_key = word+","+fname+"-"+str(lines_by_X) 
						if word_doc_key in word_freq.keys(): # is the current word already in the dictionary
							word_freq[word_doc_key] +=1  # if so increment its occurrence
						else:
							word_freq[word_doc_key] = 1 # if not let's add it!
						if word not in word_list:
							word_list.append(word) # append this word so we keep track of it in a list
						if fname+"-"+str(lines_by_X) not in docs: # see if our document code is saved in the list
							docs.append(fname+"-"+str(lines_by_X))
				if line_count%X==0: # if it is a factor of our X (lines_by_X) let's increase to create a new "document"
					lines_by_X = lines_by_X + 1
		#break # for debugging; break early
		
flo = open("docs.txt","w") # create a new file to save the list of docs
strout = "Documents defining columns in term_by_doc.txt:"
for doc in docs: 
	strout = strout + "\n" + doc
flo.write(strout)
flo.close()

flo = open("words.txt","w") # create a new file to save the list of words
strout = "Unique word strings found in documents:"
for word in word_list: 
	strout = strout + "\n" + word
flo.write(strout)
flo.close()

flo = open("term_by_doc.txt","w") # create a new file to save it
for word in word_list: # loop through all the words we tracked in the last loop
	strout = "" # start over
	for doc in docs: # all the docs we identified
		if word+","+doc in word_freq:
			strout = strout + "\t" + str(word_freq[word+","+doc]) # is it in our frequency count? if so, append
		else:
			strout = strout + "\t0" # if not, then the frequency is 0
	flo.write(strout+"\n") # spit out that string variable
flo.close()



	