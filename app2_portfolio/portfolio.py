
# create a multi column webpage

import streamlit as st
import pandas as pd

st.set_page_config(layout= 'wide')

col1,col2 = st.columns(2)

with col1:
    st.image('images/photo1.jpeg')

with col2:
    st.title('Suman Kumar')
    content = '''I am Suman Kumar and I am interested in Machine learning , Deep learning , AI and Generative AI,
    I am going to learn NLP and computer vision'''

    content1 = '''
                I have done MCA with 73% in 2004 , I have worked as a Software Test Analyst for 7 years 2004-2011 and afterwards I came out of IT in 2011 ,  So there is a 11 years career gap from IT and I am so interested in getting back into IT with your course
                
                ----------------
                
                I’m an Ex Software Engineer in Testing | I had 7 Years Experience as a Testing engineer and Software Test Analyst | I’m currently trying to get back to Software Job Again as a programmer | I’m currently learning Data Science | Technical Skills - beginner level on HTML , CSS , Javascript , C Programming | Certifications - Cisco CCNA , Redhat RHCSA and RHCE
                
                I have done MCA with 73% in 2001-2004 in Tirunvanamalai - Tamilnadu The place was good and the college was also good
                
                I have worked as a Software Test Analyst for 7 years 2004-2011 and afterwards I came out of IT in 2011 The company is good and i had lot of work in System Testing and Database Testing as i was in a Product Qualifying Team
                
                I have done projects while i was working as a test analyst but i did not build my own projects and hopefully i will do my own projects in Data Science
                
                '''

    st.info(content)
    st.info(content1)

df = pd.read_csv('data.csv', sep=';')

col3 , col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        # st.write(index,row)

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
