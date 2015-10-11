% let's run svd and make the lsa "model"

txd = load('term_by_doc.txt'); % if the file is all #'s carefully delimited, it's easy!
size(txd) % check the size
word_list = textread('words.txt','%s','headerlines',1); % if strings, then we need textread, skip the header row
doc_list = textread('docs.txt','%s','headerlines',1); 

% see links on site to read up on this
[u,s,v] = svd(txd);
word_vects = u(:,1:10);

%% check cosine between the following vectors

%energy
%power
%wind
%pollution
%spears
%timberlake
%rollins
%federline

energy_index = find(strcmp(word_list,'energy')); % find index / location of word 'energy' in word list
energy_vect = word_vects(energy_index,:); % energy_indexth row, all columns -- ':'

power_index = find(strcmp(word_list,'power'));
power_vect = word_vects(power_index,:); 


% cosine = dot(x,y)/ [norm(x)*norm(y)]
dot(energy_vect,power_vect) / ( norm(energy_vect) * norm(power_vect))

