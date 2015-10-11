import scipy.linalg as sl
import scipy as sp
import scipy.spatial as spl


wordRank = sp.loadtxt('term_by_doc.txt',int)

U,s,V = sl.svd(wordRank)


U = U[:,0:4]
S = sp.diag(s)[0:4,0:4]
V = V[0:4,:]

nwordRank = sp.dot(U,sp.dot(S,V))

execfile('make_term_by_doc.py')

for x,y in zip(word_list,range(len(word_list))):
    print(y,x)


print('Distance(cosine) between {0} and {1}: {2}'.format(word_list[0],word_list[1],sp.spatial.distance.cosine(nwordRank[0],nwordRank[1])))
print('Distance(cosine) between {0} and {1}: {2}'.format(word_list[0],word_list[5],sp.spatial.distance.cosine(nwordRank[0],nwordRank[5])))
print('Distance(cosine) between {0} and {1}: {2}'.format(word_list[6374],word_list[6380],sp.spatial.distance.cosine(nwordRank[6374],nwordRank[6380])))
print('Distance(cosine) between {0} and {1}: {2}'.format(word_list[6374],word_list[700],sp.spatial.distance.cosine(nwordRank[6374],nwordRank[700])))