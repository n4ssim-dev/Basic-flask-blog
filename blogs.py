import requests

URL = "https://api.npoint.io/c790b4d5cab58020d391"

def get_all_blog_post():
    response = requests.get(url=URL)
    if response.status_code == requests.codes.ok:
        all_blogs = response.json()
        return all_blogs
    else:
        print(f'There seems to be an error : {response.status_code}, {response.text}')
        return None

def get_blog_post(num):
    all_blogs = get_all_blog_post()
    blog = all_blogs[num]
    return blog