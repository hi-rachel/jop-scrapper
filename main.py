from flask import Flask, render_template, request
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.wanted import extract_wanted_jobs

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    indeed = extract_indeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    wanted = extract_wanted_jobs(keyword)
    jobs = indeed + wwr + wanted
    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("0.0.0.0")

"""
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.wanted import extract_wanted_jobs
from file import save_to_file

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)

wwr = extract_wwr_jobs(keyword)

wanted = extract_wanted_jobs(keyword)

jobs = indeed + wwr + wanted

save_to_file(keyword, jobs)
"""