thonimport json
import logging
from extractors.article_parser import parse_article
from extractors.content_filter import filter_content
from outputs.exporters import export_to_json
from config.settings import get_config

logging.basicConfig(level=logging.INFO)

def main():
    config = get_config()

    # Example URL to scrape
    url = "https://example.com/news/article"

    logging.info(f"Starting to scrape the article from {url}...")

    try:
        # Parse the article
        article = parse_article(url)
        logging.info("Article parsed successfully.")

        # Filter the content based on the config
        filtered_content = filter_content(article, config["filter_keywords"])
        logging.info("Content filtered.")

        # Export the data to JSON
        export_to_json(filtered_content, config["output_path"])
        logging.info(f"Data exported successfully to {config['output_path']}.")

    except Exception as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()