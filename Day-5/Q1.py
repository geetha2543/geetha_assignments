import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

def get_links(url):
    resp=requests.get(url)
    soup=BeautifulSoup(resp.text,"html.parser")
    urls= list(a['href'] for a in soup.find_all("a",href=True))
    url_set=set()
    for i in urls:
        if i.startswith(r'/'):
            scheme,loc,_,_,_,_=urlparse(url)
            full_url = scheme+r"://"+loc+i
            url_set.add(full_url)
        elif i.startswith('http'):
            url_set.add(i)
    return url_set


def get_all_links(main_set):
    sub_set=set()
    with ThreadPoolExecutor(max_workers=16) as executer:
        tasks=[executer.submit(get_links,url) for url in main_set]
        for task in as_completed(tasks):
            sub_set.update(task.result())
    return sub_set


def repeat_depth(n,main_set):
    if n>1:
        sub_set=get_all_links(main_set)
        main_set.update(sub_set)
        repeat_depth(n-1,main_set)
        return main_set
    else:
        pass

def download(url,directory):
    print(url)
    resp=requests.get(url)
    _,loc,path,_,_,_=urlparse(url)
    try:
        if(resp.text):
            with open(os.path.join(directory+loc+path.replace("/","_")+ '.html'), 'w', encoding='utf-8') as file:
                file.write(resp.text) 
    except Exception as e: 
        print("cannot download ",url)
        pass
                
def download_all_pages(final_set,directory):
    with ThreadPoolExecutor(max_workers=16) as executer:
        tasks=[executer.submit(download,url,directory) for url in final_set]
        for task in as_completed(tasks):
            task.result()
            

if __name__=='__main__':
    directory=r"C:\Users\Geetha\handson\assignments\day5\storage\copy"
    url=r"https://notepadfromdas.pythonanywhere.com/pad/share"
    depth=3
    if depth==1:
        final_set=get_links(url)
    else:
        final_set=repeat_depth(depth,get_links(url))
    download_all_pages(final_set,directory)
    print(len(final_set)," links have been downloaded successfully ")
    
    
