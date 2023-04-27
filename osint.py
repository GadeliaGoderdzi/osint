from summary import spy
from search import collector


# input from user
query1 = input("Who? and What?")
query2 = input("When?")
query3 = input("Where?")
query4 = input("Why?")
query5 = input("So What?")

query = query1 + query2 + query3 + query4 + query5

# send my collector to look for links
list_links = collector(query)
print(list_links)


#Send my scrapper to get information
for link in list_links:
    information = spy(link)



