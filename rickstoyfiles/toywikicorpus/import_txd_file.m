% let's import the term-by-document file
asdf
%%
txd = load('term_by_doc.txt'); % if the file is all #'s carefully delimited, it's easy!
size(txd) % check the size
word_list = textread('words.txt','%s','headerlines',1); % if strings, then we need textread, skip the header row
doc_list = textread('docs.txt','%s','headerlines',1); 
size(word_list) % let's look at their sizes!
size(txd)

% wanna find the most frequent words?
freqs = sum(txd,2); % take sum down the rows, across columns
[val index] = max(freqs); % what is the MOST frequent?
[val index] = min(freqs); % what is the LEAST frequent?
[vals indices] = sort(freqs,'descend'); % let's just sort it man

hist(freqs); % histogram of all frequencies
hist(txd(:)); % histogram of word-document frequencies...


