import requests
from bs4 import BeautifulSoup
from google_search import search

headers = {

}

def google_search(query):
    # perform a google search and return results
    return search(query, num_results=10)
def extract_links_with_extensions(urls, extensions):
    valid_links = []
    for url in urls:
        if any(url.lower().endswitch(ext)for ext in extensions):
            valid_links.append(url)
    return valid_links
def fetch_url_content(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
def main(base_url):
    query = f"{base_url} RFPs, Bids and Contracts 2023 2024"
    search_results = google_search(query)
    print("Google Search Results: ")
    for link in search_results:
        print(link)
    file_extensions = ['.doc','.docx','.pdf','.xls','.xlsx']
    valid_links = extract_links_with_extensions(search_results, file_extensions)
    print("links containing word, PDF or excel documents: ")
    for link in valid_links:
        content= fetch_url_content(link)
        if content:
            snippet = BeautifulSoup(content, 'html.parser').get_text()[.300]
            print(f"link: {link}\nContent Snippet: {snippet}\n")

if __name__ == "__main__":
    base_url="https://www.worldbank.org/en/projects-operations/procurement"
    main(base_url)