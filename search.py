try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
list_links = []
def collector(source):
    for j in search(source, tld="co.in", num=20, stop=20, pause=2):
        list_links.append(j)
    return list_links
    
