import pandas as pd
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import re
import string
import operator
import nltk
from nltk.corpus import stopwords
from app.skills_analysis import degrees, skills_type, top_skills, top_skills_by_earlier_analysis, stop_word
from app.skills_analysis import visualization_topics, v_subtopics, framework_topics, f_subtopics, bigdata_topics, bd_subtopics
from app.config import jobs_csv, jobs_req_csv
import random

def return_string(resume_loc):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(resume_loc, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    check = retstr.getvalue()
    retstr.close()
    check = str(check)
    return check

def extract_from_resume(resume):
    if resume == None:
        return [], []
    # read in resume ideally pdf format
    #text = textract.process(resume[0], method='pdfminer')
    #text = text.decode("utf-8")
    text = return_string(resume[0])
    # importing stop words

    stop_words = stop_word

    # making a list of words attached to punctuation marks
    # add the removed sections sepratly to the list
    list2 = ["ll", "t", "ve"]
    for li in list2:
        stop_words.append(li)
    #cleaning the resume
    resume = resume_cleaning(text)

    #Get the degrees of the resume holder
    resume_degree = []
    for word in resume.split(' '):
        if word in degrees.keys():
            if degrees[word] not in resume_degree:
                resume_degree.append(degrees[word])

    score, top_skills_subtopics = skill_extraction(resume)
    #sorted_topics = sorted(top_skills_by_earlier_analysis.items(), key=lambda x: x[1], reverse=True)
    sorted_vis_subtopics = sorted(v_subtopics.items(), key=lambda x: x[1], reverse=True)
    sorted_framework_subtopics = sorted(f_subtopics.items(), key=lambda x: x[1], reverse=True)
    sorted_bd_subtopics = sorted(bd_subtopics.items(), key=lambda x: x[1], reverse=True)
    suggest = {}
    for skill in top_skills:
        if skill not in score.keys():
            # Suggesting some of the top topics in the
            # Sacling up the weights of top_topics and not sub topics
            if skill == 'visualization':
                sum_3 = (sorted_vis_subtopics[0][1] + sorted_vis_subtopics[1][1] + sorted_vis_subtopics[2][1])
                for i in range(3):
                    suggest[sorted_vis_subtopics[i][0]] = sorted_vis_subtopics[i][1] * (top_skills_by_earlier_analysis[skill] / sum_3)
            if skill == 'framework':
                sum_3 = (sorted_framework_subtopics[0][1] + sorted_framework_subtopics[1][1] + sorted_framework_subtopics[2][1])
                for i in range(3):
                    suggest[sorted_framework_subtopics[i][0]] = sorted_framework_subtopics[i][1] * (top_skills_by_earlier_analysis[skill] / sum_3)
            if skill == 'big data':
                sum_3 = (sorted_bd_subtopics[0][1] + sorted_bd_subtopics[1][1] + sorted_bd_subtopics[2][1])
                for i in range(3):
                    suggest[sorted_bd_subtopics[i][0]] = sorted_bd_subtopics[i][1] * (top_skills_by_earlier_analysis[skill] / sum_3)

    # matching other skills and sorting them in order
    for skills in top_skills_by_earlier_analysis.keys():
        if skills not in top_skills:
            if skills not in score.keys():
                suggest[skills] = top_skills_by_earlier_analysis[skills]

    # Sorting different topics and subtopics based on weights
    sorted_suggestion = sorted(suggest.items(), key=lambda x: x[1], reverse=True)
    if(len(sorted_suggestion) > 10):
        sorted_suggestion = sorted_suggestion[0:10]
    #Performing a job search
    # reading job posting csv
    job = pd.read_csv(jobs_csv, sep=',')

    job_req = pd.read_csv(jobs_req_csv, sep=',')
    job_req['requirements'].fillna("No requirements", inplace=True)
    required_skill = {}
    idx = 0
    for req in job_req['requirements']:
        if req != "No requirements":
            required_skill[idx] = req.split(',')
        else:
            required_skill[idx] = []
        idx += 1

    degree = {}
    # making dictionary for degrees
    for i in range(len(required_skill)):
        ele = []
        for k in ['phd', 'masters', 'bachelor']:
            if k in set(required_skill[i]):
                ele.append(k)
        degree[i] = ele

    matching_jobs = find_job(required_skill, job, score, resume_degree, degree)
    return sorted_suggestion, matching_jobs

#cleaning resume
def resume_cleaning(text):
    stop_words = stop_word
    #lower case the entire
    text = text.lower()
    #removing \\n
    text= text.replace('\n', " ")
    #removing _ from
    text= text.replace('_', " ")
    #removing html tags
    cleanr = re.compile('<.*?>|&([a-z0-9]|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    text = re.sub(cleanr, '', text)
    #removing numbers
    text = ''.join(i for i in text if not i.isdigit())
    #removing punctuations
    punctuation = string.punctuation.replace('+', "")
    text = ''.join(c for c in text if c not in set(punctuation))
    #remove go to the next page
    text = text.replace("\x0c", "")
    text = text.replace("\x0b", "")
    #removing stop words from the tweets
    text = " ".join(i for i in text.split() if i not in stop_words)
    return text

#extracting skills from resume and compare it with most important skills and display missing skills
def skill_extraction(resume):
    #forming a dataframe for missing skills
    skills = skills_type.keys()
    score = {}
    top_skills_subtopics = []
    resume_word_list = resume.split(' ')
    for word in resume_word_list:
      if word in skills:
        #Checking if the skills is one of the top skill
        skill_score = 0
        if skills_type[word] in top_skills:
          if skills_type[word] == 'visualization':
            skill_score = v_subtopics[visualization_topics[word]]
            top_skills_subtopics.append([visualization_topics[word], skill_score])
          elif skills_type[word] == 'framework':
            skill_score = f_subtopics[framework_topics[word]]
            top_skills_subtopics.append([framework_topics[word], skill_score])
          elif skills_type[word] == 'big data':
            skill_score = bd_subtopics[bigdata_topics[word]]
            top_skills_subtopics.append([bigdata_topics[word], skill_score])

          if skills_type[word] not in score.keys():
            score[skills_type[word]] = skill_score
          elif skills_type[word] in score.keys():
            score[skills_type[word]] += skill_score

        else:
          score[skills_type[word]] = top_skills_by_earlier_analysis[skills_type[word]]

    return score, top_skills_subtopics

#Finds matching jobs
def find_job(required_skill, job, score, resume_degree, degree):

    matched_job_idx = []
    for idx in range(len(required_skill)):
        # making sure degrees are matching
        valid = 1
        if degree[idx]:
            for k in degree[idx]:
                if k not in resume_degree:
                    valid = 0

        if valid == 1:
            match = 0
            if required_skill[idx]:
                for r in required_skill[idx]:
                    if r in score.keys():
                        match += 1
                if (match / len(required_skill[idx]) > 0.9):
                    matched_job_idx.append(idx)
                    # Extracting details like company name, link of the job postings from their index
    matching_job_details = []
    for i in matched_job_idx:
        job_details = job.iloc[i, 1:7].values.tolist()
        job_details_ = job.iloc[i, 142:].values.tolist()
        del job_details_[0]
        job_details = job_details + job_details_
        job_details[0].replace('+', ' ')
        matching_job_details.append(job_details)
    if len(matching_job_details) > 5:
        return random.sample(matching_job_details, 5)
    return matching_job_details