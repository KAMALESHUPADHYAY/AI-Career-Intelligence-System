from flask import Flask,render_template,request
import pickle
import pdfminer.high_level
from resume_parser import extract_skills

app = Flask(__name__)

# load model
model = pickle.load(open("model.pkl","rb"))
tfidf = pickle.load(open("tfidf.pkl","rb"))

# ATS score
def ats_score(skills):
    score = len(skills)*10
    return score

# read pdf safely
def extract_text(pdf):
    try:
        text = pdfminer.high_level.extract_text(pdf)
        if text.strip()=="":
            return "No text found"
        return text
    except:
        return "Error reading PDF"

# home
@app.route("/")
def home():
    return render_template("index.html")

# dashboard page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# prediction
@app.route("/predict",methods=["POST"])
def predict():

    file = request.files["resume"]
    file.save("resume.pdf")

    text = extract_text("resume.pdf")

    # job prediction
    vector = tfidf.transform([text])
    prediction = model.predict(vector)[0]

    # skills extract
    skills = extract_skills(text)

    # ATS score
    score = ats_score(skills)

    # 🔥 REQUIRED SKILLS FOR ROLES
    required_skills = {
        "Data Science":["python","machine learning","sql","deep learning","statistics"],
        "Web Designing":["html","css","javascript","react"],
        "Java Developer":["java","spring","mysql"],
        "Python Developer":["python","django","flask","sql"]
    }

    # 🔥 Missing skills detection
    missing = []
    if prediction in required_skills:
        for s in required_skills[prediction]:
            if s.lower() not in [i.lower() for i in skills]:
                missing.append(s)

    return render_template("result.html",
                           role=prediction,
                           skills=skills,
                           score=score,
                           missing=missing)

if __name__ == "__main__":
    app.run(debug=True)
