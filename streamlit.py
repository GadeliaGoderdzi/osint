import streamlit as st
#from TextBlob import textblob
from NLTK import nltk

header = st.container()
input = st.container()

with header:
    st.header('Hello this is my OSINT tool')

try:
    from googlesearch.search import search
except ImportError:
    print("No module named 'google' found")
list_links = []
def collector(source):
    for j in search(source, tld="co.in", num=20, stop=20, pause=2):
        list_links.append(j)
    return list_links

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
links = collector(query)
links_output = st.container()
with links_output:
    for link in links:
        st.write(link)





    
