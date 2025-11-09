thondef filter_content(article, keywords):
    """Filter the content of the article based on the provided keywords."""
    if not keywords:
        return article
    
    filtered_text = " ".join([word for word in article["articleText"].split() if word.lower() in keywords])
    
    article["articleText"] = filtered_text
    return article