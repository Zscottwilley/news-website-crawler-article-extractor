thonimport requests
from bs4 import BeautifulSoup

def parse_article(url):
    """Parse the article from the given URL."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve article, status code {response.status_code}")
    
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find("h1").get_text()
    article_text = " ".join([p.get_text() for p in soup.find_all("p")])
    authors = soup.find("meta", {"name": "author"})["content"] if soup.find("meta", {"name": "author"}) else "Unknown"
    publish_date = soup.find("time")["datetime"] if soup.find("time") else "Unknown"
    language = soup.html["lang"] if soup.html.has_attr("lang") else "Unknown"
    
    article = {
        "articleURL": url,
        "articleTitle": title,
        "articleText": article_text,
        "articleAuthors": authors,
        "articlePublishDate": publish_date,
        "articleLanguage": language,
        "articleWordCount": len(article_text.split()),
        "articleKeywords": [],  # Placeholder for keyword extraction
        "articleSummary": "",   # Placeholder for AI summary
        "articleTopImage": "",  # Placeholder for image URL
        "scrapeSuccess": True
    }

    return article