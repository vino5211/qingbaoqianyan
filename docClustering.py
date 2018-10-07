from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances
import jieba
f=open('data/2017abs','r',encoding='utf-8')
docs = f.readlines()
f.close()
corpus=[]
for s in docs:
    corpus.append(' '.join(jieba.cut(s.replace("\n", "").strip())))
# print(corpus)
vec = TfidfVectorizer()
bag_of_words = vec.fit_transform(corpus)
# print(bag_of_words)
dist = pairwise_distances(bag_of_words,metric="cosine")
'''
for i in range(2,101,5):
    clf = KMeans(n_clusters=i)
    s = clf.fit(dist)
    print(i , clf.inertia_)

'''
clf = KMeans(n_clusters=20)
clf.fit(dist)
f= open('data/2017abs_cluster.txt','w',encoding='utf-8')
for i in range(len(clf.labels_)):
    f.write(str(clf.labels_[i])+'\t'+str(i)+'\t'+docs[i])
f.close()

