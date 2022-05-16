import requests

username = "ctiller"
allLanguages = {}
url = f"https://api.github.com/users/{username}/repos"

try:
    user_data = requests.get(url)

    if user_data.status_code != 200:
       raise Exception (f'Oops! Something went wrong {user_data.status_code}')
    user_data = user_data.json()  
     
    for repo in user_data:
        if repo["language"] in allLanguages:
            allLanguages[repo["language"]] +=1
        else:
            allLanguages[repo["language"]] = 1

    for key in allLanguages:
        if key is None:
            continue
        print(key, '->', allLanguages[key])

except Exception as e:
    print(e)
  
