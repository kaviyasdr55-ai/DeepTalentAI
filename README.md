# DeepTalent AI
### An Explainable AI-Based Talent Assessment and Career Recommendation System

## Overview
DeepTalent AI is a resume-based talent assessment and career recommendation web application designed to help candidates understand their skills, identify skill gaps, and explore suitable career opportunities.

The system extracts information from uploaded resumes, analyzes technical and interpersonal skills, calculates skill-match scores, and recommends relevant job roles.

## Problem Statement
Candidates often struggle to identify whether their skills match industry job requirements. Traditional resume screening methods may not clearly explain missing skills or suggest suitable career paths.

DeepTalent AI aims to simplify this process through automated resume analysis and transparent skill matching.

## Key Features
- **Resume Upload:** Supports PDF, DOCX, and TXT formats.
- **Resume Parsing:** Extracts text from uploaded resumes.
- **Skill Extraction:** Identifies technical and interpersonal skills.
- **Talent Assessment:** Calculates skill-match percentages against selected job roles.
- **Skill Gap Analysis:** Highlights missing skills.
- **Career Recommendations:** Suggests suitable job roles based on identified skills.
- **Web Dashboard:** Displays assessment results in an accessible interface.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript |
| Resume Parsing | PyPDF2, python-docx |
| Data Processing | NumPy, Pandas |
| Machine Learning Libraries | Scikit-learn |
| Database | SQLite |

## System Workflow

1. Candidate uploads a resume.
2. The system extracts resume text.
3. Skills are identified using a predefined skill dictionary.
4. Extracted skills are compared with the selected job role requirements.
5. The system calculates a skill-match score.
6. Missing skills are identified.
7. Suitable career roles are recommended.
8. Results are displayed through the web dashboard.

## Project Structure

```text
DeepTalentAI/
│
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
│
├── modules/
│   ├── resume_parser.py
│   ├── skill_analyzer.py
│   ├── talent_scorer.py
│   ├── skill_gap.py
│   └── career_recommender.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── data/
    └── job_roles.json
```

## Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/kaviyasdr55-ai/DeepTalentAI.git
```

### 2. Navigate to the project

```bash
cd DeepTalentAI
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Initialize the database

```bash
python database.py
```

### 7. Run the application

```bash
python app.py
```

Open the application in your browser:

`http://127.0.0.1:5000`

## Future Enhancements
- Semantic skill extraction using NLP and transformer models.
- Explainable AI techniques for assessment transparency.
- Personalized learning paths based on identified skill gaps.
- Advanced candidate profiling and multi-dimensional assessment.
- Candidate history and analytics dashboard.
- More comprehensive job-role recommendations.

## Project Scope and Limitations
The current implementation uses dictionary-based skill extraction and rule-based skill matching. The match percentage indicates overlap with predefined job requirements; it should not be interpreted as a validated measurement of a candidate's actual ability.

Advanced NLP, explainability methods, and personalized learning features are proposed future enhancements.

## Author
**Kaviya Tharani K.**

Artificial Intelligence and Data Science Student

GitHub: [@kaviyasdr55-ai](https://github.com/kaviyasdr55-ai)

---

*DeepTalent AI — Turning Resume Insights into Career Direction.*
