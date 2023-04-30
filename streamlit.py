import streamlit as st
#from TextBlob import textblob
from NLTK import nltk

header = st.container()
input = st.container()

with header:
    st.header('Hello this is my OSINT tool')

# try:
#     from googlesearch.searcher import search
# except ImportError:
#     print("No module named 'google' found")
# list_links = []
# def collector(source):
#     for j in search(source,num_results=1,stop=10, pause=2):   #tld="co.in" , stop=10, pause=2
#         list_links.append(j)
#     return list_links

#-------------end of functions--------------------------------

with st.form("my_form", clear_on_submit = True):
    query1 = st.text_input("What are you interested in?")
    query2 = st.text_input("Do you know what locations we can look for?")
    query3 = st.text_input("Are there any key people you are interested in?")
    query4 = st.text_input("What time intervals should we look for?")
    query5 = st.text_input("Why is this information important for you?")
    submitted = st.form_submit_button("Submit your information")
    

query = query1 + query2 + query3 + query4 + query5
st.write(query)
#Output
# links = collector(query)
num_searches = 10
while num_searches>0:
    try:
        from googlesearch.searcher import search
    except ImportError:
        print("No module named 'google' found")
    list_links = []
    for j in search(query,tld="co.in", num_results=10,stop=10, pause=2):   #tld="co.in" , stop=10, pause=2
            list_links.append(j)
    num_searches = num_searches - 1
# links_output = st.container()
with list_links:
    for link in list_links:
        st.write(link)





    
