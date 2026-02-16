# simple skill extraction 

skills_list = [
    "python","machine learning","data science","sql",
    "java","c++","excel","html","css","javascript",
    "flask","pandas","numpy","deep learning"
]

def extract_skills(text):
    text = text.lower()
    found = []

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return list(set(found))
