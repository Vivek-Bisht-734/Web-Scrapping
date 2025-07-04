# Scrapping quote, author, tags


# In txt file format
# from bs4 import BeautifulSoup as bs
# import requests as re
# import os

# page = 1
# while True:
#     if page == 1:
#         url = "https://quotes.toscrape.com/"
#     else:
#         url = f"https://quotes.toscrape.com/page/{page}/"


#     link = re.get(url).text
#     soup = bs(link, 'lxml')
#     # print(soup.prettify())

#     print(f"\n ==== Page {page} ====")

#     quote_section = soup.find_all('div', class_ = 'quote')
#     os.makedirs("quotes scrapped", exist_ok=True)
#     for quotes in quote_section:
#         quote = quotes.find('span', class_ = 'text').text.strip()
#         author = quotes.find('small', class_ = 'author').text.strip()

#         tag_list = quotes.find('div', class_ = 'tags').find_all('a', class_ = 'tag')
#         tags = [tag.text.strip() for tag in tag_list]


#         with open(f'quotes scrapped/books_scrapping.txt', 'a', encoding='utf-8') as f:
#                 f.write(f"""
# Quote : {quote}
# Author : {author}
# Tags : {', '.join(tags)}

# """)
    
#     next_button = soup.find('li', class_='next')
#     if next_button:
#         page += 1
#     else:
#         break

# print("\n\n ==== END ====")














# In Csv file format
from bs4 import BeautifulSoup as bs
import requests as re
import os
import csv

quote_to_scrape = []
page = 1
while True:
    if page == 1:
        url = "https://quotes.toscrape.com/"
    else:
        url = f"https://quotes.toscrape.com/page/{page}/"


    link = re.get(url).text
    soup = bs(link, 'lxml')
    # print(soup.prettify())

    print(f"\n ==== Page {page} ====")

    quote_section = soup.find_all('div', class_ = 'quote')
    
    for quotes in quote_section:
        quote = quotes.find('span', class_ = 'text').text.strip()
        author = quotes.find('small', class_ = 'author').text.strip()

        tag_list = quotes.find('div', class_ = 'tags').find_all('a', class_ = 'tag')
        tags = [tag.text.strip() for tag in tag_list]

        quote_to_scrape.append([quote, author, tags])
    
    next_button = soup.find('li', class_='next')
    if next_button:
        page += 1
    else:
        break
        

os.makedirs("quotes scrapped", exist_ok=True)
with open(f'quotes scrapped/books_scrapping.csv', mode = 'w', newline = '', encoding='utf-8') as f:
    write = csv.writer(f)
    write.writerow(["quotes", "author_name", "tags"])
    write.writerows(quote_to_scrape)
    

print("\n\n ==== END ====")
print(f"{len(quote_to_scrape)} Scrapped Quotes Saved.")