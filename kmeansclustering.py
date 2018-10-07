from termMatrix import get_term_term_matrix
f=open('C:\\Users\\A\\Documents\\Tencent Files\\674912850\\FileRecv\\keyword.txt','r',encoding='utf-8')
docs = f.readlines()
# print(get_top_n_words(docs))

from sklearn.cluster import KMeans
vocabulary,Xc,dist = get_term_term_matrix(docs)
id2voc = dict(zip(vocabulary.values(),vocabulary.keys()))
print(id2voc[0])
print(len(vocabulary.keys()))
clf = KMeans(n_clusters=50)
s=clf.fit(dist)
print(s)
#
# #9个中心
# print(clf.cluster_centers_)
# print(clf.inertia_)
# #每个样本所属的簇
print(len(clf.labels_))
f= open('data/keyword_cluster.txt','w',encoding='utf-8')
for i in range(len(clf.labels_)):
    f.write(str(clf.labels_[i])+'\t'+str(i)+'\t'+id2voc[i]+'\n')
f.close()
'''

for i in range(100,125,5):
    clf = KMeans(n_clusters=i)
    s = clf.fit(dist)
    print(i , clf.inertia_)
'''