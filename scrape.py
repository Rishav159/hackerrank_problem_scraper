pdfname = 'Problem.pdf'
#Enter Absolute Path of the folder here
base = ''

domain = 'https://www.hackerrank.com'
from bs4 import BeautifulSoup
import requests, zipfile, io
import os,sys

if len(sys.argv) < 2:
    print("Provide the problem URL")
    sys.exit()
link = sys.argv[1]

#Scrape the link
r = requests.get(link)
soup = BeautifulSoup(r.text, 'html.parser')

#Get all the links
problem_name = soup.find("h2",{"class" : "hr_tour-challenge-name"}).get_text().replace(' ','_')
problem_link = domain + soup.find("a",{"id":"pdf-link"})['href']
test_cases_link = domain + soup.find("a",{"id" : "test-cases-link"})['href']
folder_path = folder_path = base +'/' +problem_name

#Create the folder
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

#Save the pdf
r = requests.get(problem_link)
with open(base + '/'+ problem_name + '/problem.pdf', 'wb') as f:
    f.write(r.content)

#Download Test Case
r = requests.get(test_cases_link)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall(folder_path)
