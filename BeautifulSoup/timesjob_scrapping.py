from bs4 import BeautifulSoup as bs
import requests as re
import time

base_url = "https://m.timesjobs.com/mobile/jobs-search-result.html?compCluster=amazon+india+pvt+ltd"
params_template = {
    "sequence": 1,
    "startPage": 1
}

print('Skill that you are not familiar with to filter it out: ')
unfamliar_skill = input("Enter the skills you don't know >> ")
print(f'Filtering Out {unfamliar_skill}')

def find_jobs():
    page = 1
    while True:
        print(f"\n--- Scraping Page {page} ---\n")
        params_template["sequence"] = page
        params_template["startPage"] = page

        response = re.get(base_url, params=params_template)
        soup = bs(response.text, 'lxml')

        job_lists = soup.find_all('li')
        if not job_lists or len(job_lists) < 2:
            print("No more job listings found. Stopping.")
            break

        for index, job_list in enumerate(job_lists):
            a = job_list.find('div', class_='srp-job-heading')
            b = job_list.find('div', class_='srp-keyskills')
            exp_req = job_list.find('div', class_='srp-exp')
            location = job_list.find('div', class_='srp-loc')
            c = job_list.find('div', class_ = 'srp-listing')

            if not all([a, b, exp_req, location, c]):
                continue

            job_role = a.find('a').text.split(',')[0].strip()
            company = a.find('span', class_="srp-comp-name").text.strip()
            skills_list = b.find_all('a', class_='srphglt')
            skills = [skill.text.strip() for skill in skills_list]
            exp_req = exp_req.text.strip()
            location = location.text.strip()
            more_info = c.find('a', class_ = 'srp-apply-new')['href']


            if unfamliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"""
Company Name: {company}
Job Role: {job_role}
Skills Required: {', '.join(skills)}
Experience Required: {exp_req}
Job Location: {location}
More Info: {more_info}""")
                    f.write('')
                print(f'File Saved: {index}')

        page += 1



if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)