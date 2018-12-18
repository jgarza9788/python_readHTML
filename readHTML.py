import urllib3

http = urllib3.PoolManager()


def getHTML(url):
    response = http.request('GET', url)
    return response.data


if __name__ == "__main__":
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(getHTML("www.google.com"))
    print(getHTML("www.google.com"))