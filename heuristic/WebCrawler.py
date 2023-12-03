# Word wide web (www) can be represented as a directed graph
# vertices: domains/ URLs/ websites
# edges: connections btw websites via links

import requests
import re

class WebCrawler:
    def __init__(self):
        self.discovered_websites = []

    def crawl(self, start_url):
        queue = [start_url]
        self.discovered_websites.append(start_url)

        while queue:
            url = queue.pop(0)
            print(url)

            url_html = self.read_raw_html(url)

            for new_url in self.get_links_from_html(url_html):
                if new_url not in self.discovered_websites:
                    self.discovered_websites.append(new_url)
                    queue.append(new_url)

    def read_raw_html(self, url):
        raw_html = ''

        try:
            raw_html = requests.get(url).text
        except Exception as e:
            pass
        return raw_html

    def get_links_from_html(self, raw_html):
        # regex expression
        return re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", raw_html)

if __name__ == "__main__":
    crawler = WebCrawler()
    crawler.crawl("https://www.cnn.com")
