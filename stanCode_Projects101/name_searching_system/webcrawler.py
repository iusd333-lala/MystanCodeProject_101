"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
"""

from bs4 import BeautifulSoup
from selenium import webdriver


def main():
    # # for year in ['2010s', '2000s', '1990s']:
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)

        # ----- Write your code below this line ----- #
        with webdriver.Chrome() as driver:
            url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'
            driver.get(url)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            tag = soup.find('table', {'class': 't-stripe'})
            if tag:
                tokens = tag.find('tbody').text.split()
                total_man = 0
                total_woman = 0
                count = 0
                for token in tokens:
                    if ',' in token:
                        num_ppl = int(token.replace(',', ''))
                        if count % 2 == 0:
                            total_man += num_ppl
                        else:
                            total_woman += num_ppl
                        count += 1
                print(f"Male Number:{total_man}")
                print(f"female_number:{total_woman}")
            else:
                print('Timed out waiting for page to load or table missing')
            # driver.quit()



if __name__ == '__main__':
    main()
