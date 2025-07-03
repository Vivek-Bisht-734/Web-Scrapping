# Scrapping book titles, prices, availability and star ratings which are 4 and 5 stars



# Saving file in txt format
# from bs4 import BeautifulSoup as bs
# import requests as re
# import os

# page = 1
# while True:
#     if page == 1:
#         url = "https://books.toscrape.com"
#     else:
#         url = f"https://books.toscrape.com/catalogue/page-{page}.html"

#     link = re.get(url).text
#     soup = bs(link, 'lxml')
#     # print(soup.prettify())

#     print(f"\n ==== Page {page} ====")

#     book_details = soup.find_all('li', class_ = 'col-xs-6')
#     for books in book_details:
#         book_title = books.find('h3').a['title']
#         price_section = books.find('div', class_ = 'product_price')
#         book_price = price_section.find('p', class_ = 'price_color').text.replace('Â', '')
#         book_availability = books.find('p', class_ = 'instock availability').text.strip()
#         rating_section = books.find('p', class_ = 'star-rating')
#         book_rating = rating_section.get('class')
#         not_rated = ['Four', 'Five']
#         star_rating = book_rating[1] if len(book_rating) > 1 else 'Not Rated'
          
#         os.makedirs("posts", exist_ok=True)
#         if star_rating in not_rated:
#             with open(f'posts/books_details.txt', 'a', encoding='utf-8') as f:
#                 f.write(f"""
# Book Name: {book_title}
# Book Price: {book_price}
# Book Availability: {book_availability}
# Star Rating: {star_rating}
# """)
    
#     next_button = soup.find('li', class_='next')
#     if next_button:
#         page += 1
#     else:
#         break

# print("\n\n ==== END ====")







# Saving file in csv format
from bs4 import BeautifulSoup as bs
import requests as re
import os
import csv

all_books = []
page = 1
while True:
    if page == 1:
        url = "https://books.toscrape.com"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    link = re.get(url).text
    soup = bs(link, 'lxml')

    print(f"\n ==== Page {page} ====")

    book_details = soup.find_all('li', class_ = 'col-xs-6')
    for books in book_details:
        book_title = books.find('h3').a['title']
        price_section = books.find('div', class_ = 'product_price')
        book_price = price_section.find('p', class_ = 'price_color').text.replace('Â', '')
        book_availability = books.find('p', class_ = 'instock availability').text.strip()
        rating_section = books.find('p', class_ = 'star-rating')
        book_rating = rating_section.get('class')
        star_rating = book_rating[1] if len(book_rating) > 1 else 'Not Rated'

        not_rated = ['Four', 'Five']
        if star_rating in not_rated: 
            all_books.append([book_title, book_price, book_availability, star_rating])

    next_button = soup.find('li', class_='next')
    if next_button:
        page += 1
    else:
        break
 

os.makedirs('posts', exist_ok = True)        
with open('posts/book_details.csv', mode = 'w', newline = '', encoding = 'utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["book_name", "book_price", "book_availability", 'star_rating'])
    writer.writerows(all_books)

print("\n\n ==== END ====")
print(f"{len(all_books)} books saved to posts/books_details.csv")

