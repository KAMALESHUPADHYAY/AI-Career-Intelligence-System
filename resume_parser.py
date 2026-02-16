import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

skills_list = ["python","machine learning","data science","sql","java","c++","excel"]

def extract_skills(text):
    doc = nlp(text.lower())
    found = []

    for token in doc:
        if token.text in skills_list:
            found.append(token.text)

    return list(set(found))
