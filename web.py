import requests
from bs4 import BeautifulSoup
from collections import Counter

def get_hyperlinks_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        if link.startswith("http") or link.startswith("www"):
            links.append(link)
    return links

def rank_hyperlinks(links):
    link_counter = Counter(links)
    ranked_links = link_counter.most_common()
    return ranked_links

def main():
    url = 'http://www.poornima.org'  # Replace with the actual URL of Poornima College of Engineering
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
        hyperlinks = get_hyperlinks_from_html(html_content)
        ranked_hyperlinks = rank_hyperlinks(hyperlinks)
        
        print("Hyperlink Frequencies and Rankings:")
        for link, frequency in ranked_hyperlinks:
            print(f"{link}: {frequency}")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == '__main__':
    main()
