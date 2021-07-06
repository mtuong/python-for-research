import requests
from bs4 import BeautifulSoup
import smtplib, ssl

def sendEmail(message):
    port = 587  # For SSL
    smtp_server = "mail.smtp2go.com"
    sender_email = "itlab@oucru.org"  # Enter your address
    receiver_email = "mtuong@eocru.org"  # Enter receiver address
    username = 'alarm@oucru.org'
    password = input("Type your password and press enter: ")
    subject = 'Finding Job of Accountant'

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()

#https://realpython.com/python-send-email/
#https://www.analyticsvidhya.com/blog/2021/04/automate-web-scraping-using-python-autoscraper-library/
realpython = 'https://realpython.com/beautiful-soup-web-scraper-python/'
URL = "https://realpython.github.io/fake-jobs/"
oucru = 'http://www.oucru.org/work-with-us/'
page = requests.get(oucru)
#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find('ul', class_='wwu-items')
#results = soup.find(id="ResultsContainer")
#print(results.prettify())

#job_elements = results.find_all("div", class_="card-content")
acc_jobs = results.find_all(
    "a", string=lambda text: "accountant" in text.lower()
)
print('Find result: ',len(acc_jobs))

job_elements = results.find_all("a")

for job_element in job_elements:
    job = job_element.text

    if ("accountant" in job.lower()):
        link = job_element['href']
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find('div', class_='page-content')

        print(job)
        print(link)

        SUBJECT = 'Accountant Job of OUCRU-VN'
        TEXT = job + '\n' + link
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        sendEmail(message)




