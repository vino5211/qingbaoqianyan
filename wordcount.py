from termMatrix import get_top_n_words
f=open('fund_keyword.txt','r',encoding='utf-8')

docs = f.readlines()
f.close()
fout = open('fund_keyword_count.txt','w',encoding='utf-8')
for k,n in get_top_n_words(docs):
    fout.write(k+'\t'+str(n)+'\n')
fout.close()