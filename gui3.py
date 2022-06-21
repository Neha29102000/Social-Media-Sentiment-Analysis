import streamlit as st
from textblob import TextBlob


st.title("Sentiment Analysis Tool")

message = st.text_area("Please enter the Text")

if  st.button("Analyze"):
    blob=TextBlob(message)
    

    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity

    if sentiment_polarity > 0:
        sentiment_label = 1
        st.success('Positive')
        
    elif sentiment_polarity < 0:
        sentiment_label = -1
        st.success('Negative')
    else:
        sentiment_label = 0
        st.success('Neutral')
    result = {'polarity':sentiment_polarity,
              'subjectivity':sentiment_subjectivity,
              'sentiment':sentiment_label}
    st.success(result)

    
