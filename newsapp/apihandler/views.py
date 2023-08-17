from django.shortcuts import render,HttpResponse
import requests
# Create your views here.
def home(request):

    if request.method == "POST":
       
        Topic = request.POST['gsearch']
        url=f'https://newsapi.org/v2/everything?q={Topic}&apiKey=a3f2e7a42aec4e42a8ab77af27695e2d'
        response = requests.get(url)
        if response.status_code == 200:
             articles1 = response.json()['articles']
             desc = []
             title = []
             img = []
             newsurl = []
             for i in range(20):
                f=articles1[i]
                title.append(f['title'])
                desc.append(f['description'])
                img.append(f['urlToImage'])
                newsurl.append(f['url'])
             mylist = zip(title,desc,img,newsurl)
             context = {'mylist':mylist}
             return render(request, 'index.html', context)
        else:
            # if the request was not successful, show an error message
            error_message = 'There was an error fetching the news. Please try again later.'
            return render(request, 'index.html', {'error_message': error_message})
        
    url='https://newsapi.org/v2/everything?q=marvel&apiKey=a3f2e7a42aec4e42a8ab77af27695e2d'
    news = requests.get(url).json()

    a=news['articles']
    desc = []
    title = []
    img = []
    newsurl = []
    for i in range(5):
        f=a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        newsurl.append(f['url'])
        

    mylist = zip(title,desc,img,newsurl)
    
    
    context = {'mylist':mylist}
    
    return render(request,'index1.html',context)
'''
    url='https://newsapi.org/v2/everything?q=&apiKey=a3f2e7a42aec4e42a8ab77af27695e2d'
    news = requests.get(url).json()

    a=news['articles']
    desc = []
    title = []
    img = []
    newsurl = []
    for i in range(3):
        f=a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        newsurl.append(f['url'])
        

    mylist = zip(title,desc,img,newsurl)
    
    
    context = {'mylist':mylist}
    '''

    


def index(request):
    
    url='https://newsapi.org/v2/everything?q={Topic}&apiKey=a3f2e7a42aec4e42a8ab77af27695e2d'

    news = requests.get(url).json()

    a=news['articles']
    desc = []
    title = []
    img = []
    newsurl = []
    
   

    for i in range(20):
        f=a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        newsurl.append(f['url'])
        

    mylist = zip(title,desc,img,newsurl)
    
    
    context = {'mylist':mylist}

    return render(request,'index.html',context)

