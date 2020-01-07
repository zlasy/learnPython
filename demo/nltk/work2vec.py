#使用以下命令初始化模型
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
 
path = get_tmpfile("word2vec.model") #创建临时文件
 
model = Word2Vec(common_texts, size=100, window=5, min_count=1, workers=4)
model.save("word2vec.model")
#加载模型
model = Word2Vec.load("word2vec.model")
#获取每个词的词向量
model['computer']  # raw numpy vector of a word
#输出array([-0.00449447, -0.00310097,  0.02421786, ...], dtype=float32)
# 支持词语的加减运算。（实际中可能只有少数例子比较符合）
model.most_similar(positive=['woman', 'king'], negative=['man'])
#输出[('queen', 0.50882536), ...]
#计算两个词之间的余弦距离
model.similarity("好", "还行")
model.most_similar("人民")#计算余弦距离最接近“滋润”的10个词
for i in model.most_similar("人民"):
    print(i[0],i[1])
#model.similar_by_word('人民',topn=100) 输出与“人民”相似的前100个词
for key in model.similar_by_word('人民',topn=10):
        print(key)
for key in model.wv.similar_by_word('人民', topn =10):
    print(key)
#计算两个集合之间的余弦似度,当出现某个词语不在这个训练集合中的时候，会报错
list1 = [u'今天', u'我', u'很', u'开心']
list2 = [u'空气',u'清新', u'善良', u'开心']
list3 = [u'国家电网', u'再次', u'宣告', u'破产', u'重新']
list_sim1 =  model.n_similarity(list1, list2)
print (list_sim1)
list_sim2 = model.n_similarity(list1, list3)
print( list_sim2) 
0.541874230659
0.13056320154
#选出集合中不同类的词语
model.doesnt_match("breakfast cereal dinner lunch".split())
#输出'cereal'
list = ['纽约', '北京', '上海', '西安']
print( model.doesnt_match(list))
list = ['纽约', '北京', '上海', '西瓜']
print(model.doesnt_match(list))