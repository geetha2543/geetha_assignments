from bs4 import BeautifulSoup
from urllib.parse import urlparse
import asyncio,os,aiohttp

async def get_links(url):
    url_set = set()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                html = await resp.text()
                soup=BeautifulSoup(html,"html.parser")
                urls = list(a['href'] for a in soup.find_all("a",href=True))
                for i in urls:
                    if i.startswith(r'/'):
                        scheme,loc,_,_,_,_ = urlparse(url)
                        full_url = scheme+r"://"+loc+i
                        url_set.add(full_url)
                    elif i.startswith('http'):
                        url_set.add(i)
    except Exception as e:
        print(f"error in getting the sub links from {url} -->{e}")
    return url_set


async def get_all_links(final_set):
    tasks = [asyncio.create_task(get_links(url)) for url in final_set]
    sub_set = set()
    res = await asyncio.gather(*tasks)
    for i in res:
        sub_set.update(i)
    return sub_set


async def repeat_depth(n,main_set):
    if n>1:
        sub_set = await get_all_links(main_set)
        main_set.update(sub_set)
        await repeat_depth(n-1,main_set)
        return main_set
    else:
        pass


async def download(url,directory):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                print(url)
                html = await resp.text()
                _,loc,path,_,_,_ = urlparse(url)
                try:
                    if(resp.text):
                        with open(os.path.join(directory+loc+path.replace("/","_")+ '.html'), 'w', encoding='utf-8') as file:
                            file.write(html) 
                except Exception as e: 
                    pass
    except Exception as e:
        print(f"error in downloading the link {url}--> {e}")
    
            
async def download_all_pages(final_set,directory):
    tasks = [asyncio.create_task(download(url,directory)) for url in final_set]
    for e in asyncio.as_completed(tasks):
        res = await e


directory=r"C:\Users\Geetha\handson\assignments\day6\storage\copy"
url=r"https://notepadfromdas.pythonanywhere.com/pad/share"
depth=2
with asyncio.Runner() as r:
    if depth==1:
        final_set=r.run(get_links(url))
    else:
        first_set = r.run(get_links(url))
        final_set=r.run(repeat_depth(depth,first_set))
r.run(download_all_pages(final_set,directory))
print(len(final_set)," links have been downloaded successfully ")
    
    
