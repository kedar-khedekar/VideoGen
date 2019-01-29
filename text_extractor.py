from newspaper import Article
import json
import articleDateExtractor

f = open("news_url.txt",'r')

urls = []

for x in f:
    urls.append(x)

news = []

for i in range(0,len(urls)):
    news.append({
        'id': i+1,
        'title':'',
        'date':'',
        'authors':[],
        'keywords':[],
        'summary':'',
        'image_url':'',
        'video_url':'',
        'time':''
    }) 

print(news)
i=0
for url in urls:
    date = articleDateExtractor.extractArticlePublishedDate(url)
    date = str(date)
    print(date)
    if date != None:
        news[i]['date']=date.split(' ')[0]
        if len(date.split(' ')):
            time = date.split(' ')[1]
        news[i]['time']=time.split('+')[0]
    article =  Article(url)
    article.download()
    article.parse()
    news[i]['title'] = article.title
    news[i]['authors'] = article.authors
    news[i]['image_url'] = article.top_image
    news[i]['video_url'] = article.movies
    article.nlp()
    news[i]['keywords'] = article.keywords
    news[i]['summary'] = article.summary.split('\n')[0]
    i+=1

print("Extraction successful")
with open('struct.json','w') as fp:
    json.dump(news,fp,indent=1)

print(urls)    