from sklearn.feature_extraction.text import CountVectorizer
f=open('data/author.txt','r',encoding='utf-8')
docs = f.readlines()
f.close()
corpus=[]
for s in docs:
    corpus.append(s.replace("\n", "").strip())
count_model = CountVectorizer(ngram_range=(1,1),token_pattern=r"(?u)\b[^;]+\b") # default unigram model
X = count_model.fit_transform(corpus)
sum_author = X.sum(axis=0)
author_freq = [(word, sum_author[0, idx]) for word, idx in count_model.vocabulary_.items()]
author_freq = sorted(author_freq, key=lambda x: x[1], reverse=True)
Xc = (X.T * X) # this is co-occurrence matrix in sparse csr format
'''
print(count_model.vocabulary_)
f=open('data/author_count'
       '.txt','w',encoding='utf-8')
for a,c in author_freq:
    f.write(a+'\t'+str(c)+'\t'+str(count_model.vocabulary_[a])+'\n')
f.close()
'''
# print(author_freq)
# list = [((i, j), Xc[i,j]) for i, j in zip(*Xc.nonzero())]
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
for i, j in zip(*Xc.nonzero()):
    if Xc[i,j]>=0:
        G.add_edge(i,j, weight=Xc[i,j])
pos = nx.kamada_kawai_layout(G)  # positions for all nodes
#nodes
d = nx.degree(G)
nx.draw_networkx_nodes(G, pos, node_size=[v * 10 for (k,v) in d],node_color='y')
#edges
nx.draw_networkx_edges(G, pos)
# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
plt.figure(1, figsize=(100, 50))
plt.axis('off')
plt.show()