# Resseract 1.0

### Description
A simple rule based resume/cv parser web application built on django|Python. Browse the [live site](http://40.114.65.200/)

### Requirements
1. Python 3.7.0 or later Version
2. pip installer 
3. Dependencies listed in requirements.txt (Follow Installation steps)

### Installation
1. Get the dependencies
Use pip to invoke the following command and get the dependencies listed in requirements.txt
	`pip install -r requirements.txt`
	
2. NLTK Corpora
	- Get a python shell using `py` or `python`
	- Import NLTK Module with `import nltk`
	- Download Corpora listed in nltk.txt with following syntax
		`nltk.download(<corpora_name>)`
		
3. Create Static content
In the root directory of project, fire the command
	`py manage.py collectstatic`
	
4. Execution Time 
Run the local Django Server with
	`py manage.py runserver`
	
5. Now Browse it
Web Application will run at 127.0.0.1:8000

### Features
1. Accepts Resume/CV in .pdf and .docx formats only.
2. Extracts following information from Resume
	- Name,Email Address, Phone Number
	- LinkedIn profile Link
	- Total no. of text characters, lines and pages
	- Fonts and Font Sizes
	- Total no. of Tables and Images
3. View Live Results or Download in .csv or .xlsx format

\*Drag & Drop Facility included

**Note**: Application is still in developmental phases. Report the bugs to pagalprogrammer@protonmail.com
