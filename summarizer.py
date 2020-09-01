# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:31:34 2020

@author: Admin
"""

import streamlit as st
import spacy
from PIL import Image
import pytesseract
#import cv2
import os
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

nlp=spacy.load('en_core_web_sm')


from gensim.summarization import  summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def sumy_summarizer(docx):
    parser=PlaintextParser.from_string(docx,Tokenizer("english"))
    lex_summarizer=LexRankSummarizer()
    summary=lex_summarizer(parser.document,3)
    summary_list=[str(sentence) for sentence in summary]
    result="".join(summary_list)
    return result



#@st.cache(allow_output_mutation=True)
def analyze_text(text):
    doc=nlp(text)
    list=[]
    for ent in doc.ents:
        list.append([(ent.text),(ent.label_)])
    return "".join(str(list)) 



from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_text(raw_url):
    page=urlopen(raw_url)
    soup=BeautifulSoup(page)
    
    fetch_text=" ".join(map(lambda p:p.text,soup.find_all("p")))
    return fetch_text

   

def main():
    

         
    st.title("Summary And Entity Checker ")
    activities=["Summarize","NER Checker","NER for URL","Summarize text from image"]
    choice=st.sidebar.selectbox("Select activity",activities)
    
    if choice=="Summarize":
        st.subheader("Summary With NLP")
        raw_text=st.text_area("Enter Text Here")
        #summary_choice=st.selectbox("Summary Choice ",["Gensim","Sumy Lex Rank"])
        if st.button("Summarize"):
            
            #if summary_choice=="Gensim":
            summary_result=summarize(raw_text)
            st.success(summary_result)
                
                
            #else: 
               # summary_result=sumy_summarizer(raw_text)
               # st.success(summary_result)
             
    if  choice=="NER Checker": 
        st.subheader("Entity Recognition ")
        raw_text=st.text_area("Enter Text Here")

        if st.button("Analyze"):
            doc=analyze_text(raw_text)
            st.success(doc)
            
    if choice=="NER for URL":
        st.subheader("Analyze text from URL")
        raw_url=st.text_input("Enter URL")
        x=st.slider("Summarize paragraph by what %",1,100)
        
        if st.button("Extract"):
            result=get_text(raw_url)
            len_text=len(result)
            len_summary=round((len(result)*x/100))
            r1=result[:len_summary]
            summary_result=summarize(r1)
            st.info("Length OF Paragraph From Given URL Is {}".format(len_text))
            st.info("Length OF Summary Generated Is  {}".format(len_summary))
            st.subheader("Summary Generated From URL")
            st.write(summary_result)
            doc=analyze_text(summary_result)
            st.subheader("Ner Generated From URL")
            st.success(doc)
            
    if  choice=="Summarize text from image":
        uploaded_file = st.file_uploader("Choose an image...", type="jpeg")
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', use_column_width=True)
            text=pytesseract.image_to_string(image)
            summary_result=summarize(text)
            st.subheader("Summary Generated From OCR")
            st.success(summary_result)
        
        

        # if st.button("Analyze"):
        #     doc=analyze_text(raw_text)
        #     st.success(doc)            
            
        
if __name__ == "__main__":
    main()
            