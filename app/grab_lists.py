from requests import get
from os import environ

with open('blocklists.txt') as blocklistsFile:
    blocklists = [x for x in blocklistsFile.read().splitlines() if x.startswith('http')]

URLs = set()

for list in blocklists:
    response = get(list)

    if response.ok:
        print(f"Downloaded {list}")
        tmpURLs = [y.decode("utf-8").split(" ")[-1] for y in response.content.splitlines() if not y.decode("utf-8").startswith('#') and not y.decode("utf-8").startswith('|') and y.decode("utf-8").strip()]
        URLs.update(tmpURLs)
    else:
        print(f"Error downloading list: {response.status_code}")

with open(environ['OutputPath'], 'w') as outFile:
    for URL in URLs:
        outFile.write(f"{URL}\n")