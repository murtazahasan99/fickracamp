#here i use python 3
#iguss i solved by wrong way because i did not undersod this qustion good
#so i solved it like this

import requests

def req(url):
    fech=requests.get(url)
    return fech.json()

def get(userid,post,commint):
    ob=[]
    for i in post:
        if (i["userId"] == userid):
            for j in commint:

                if(i['id']==j['id']):
                    new={"post_name":i["title"],"post_commint":j["body"]}
                    ob.append(new)
    return (ob)



url_commint= 'https://jsonplaceholder.typicode.com/comments'
url_post="https://jsonplaceholder.typicode.com/posts"
commint=req(url_commint)
post=req(url_post)

print(get(3,post,commint))

