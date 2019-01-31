from newspaper import Article
import json
import articleDateExtractor
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True) 
rw = 1  #row no variable
f = open("news_url.txt",'r')


urls = []

for x in f:
    urls.append(x)

news = []
sheet1.write(0,0,'ID')
sheet1.write(0,1,'TITLE')
sheet1.write(0,2,'DATE')
sheet1.write(0,3,'TIME')
sheet1.write(0,4,'AUTHORS')
sheet1.write(0,5,'IMAGE URL')
sheet1.write(0,6,'VIDEO URL')
#sheet1.write(0,7,'KEYWORDS')
#sheet1.write(0,8,'SUMMARY')

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
    sheet1.write(rw, 0, rw)

    date = articleDateExtractor.extractArticlePublishedDate(url)
    date = str(date)
    print(date)
    if date != 'None':
        news[i]['date']=date.split(' ')[0]
        sheet1.write(rw, 2, news[i]['date'])
        if len(date.split(' ')):
            print("date here")
            print(date)
            time = date.split(' ')[1]
        news[i]['time']=time.split('+')[0]
        sheet1.write(rw, 3, news[i]['time'])
    try:
        article =  Article(url)
        article.download()
        article.parse()

        news[i]['title'] = article.title
        sheet1.write(rw, 1, news[i]['title'])
        news[i]['authors'] = article.authors
        sheet1.write(rw, 4, news[i]['authors'])
        news[i]['image_url'] = article.top_image
        sheet1.write(rw, 5, news[i]['image_url'])
        news[i]['video_url'] = article.movies
        sheet1.write(rw, 6, news[i]['video_url'])
        article.nlp()
        news[i]['keywords'] = article.keywords
        #sheet1.write(rw, 7, news[i]['keywords'])
        news[i]['summary'] = article.summary.split('\n')[0]
        #sheet1.write(rw, 8, news[i]['summary'])

        #for cl in range(8):
         #   sheet1.write(rw, cl, cl) 

        rw += 1
        i+=1


    except Exception as e:
        print(e)
    
print("Extraction successful")
wb.save('info2.xls')
with open('struct.json','w') as fp:
    json.dump(news,fp,indent=1)

print(urls)    
print("doneee")
