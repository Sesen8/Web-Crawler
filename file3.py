import requests
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt
from urllib.parse import urljoin, urlparse
from requests.exceptions import RequestException
import certifi

def web_crawler(url, max_depth, current_depth=0, visited_urls=None, graph=None):
    if visited_urls is None:
        visited_urls = set()
    if graph is None:
        graph = nx.DiGraph()

    if current_depth <= max_depth and url not in visited_urls:
        try:
            response = requests.get(url, timeout=10, allow_redirects=True, verify=certifi.where())
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', href=True)

                visited_urls.add(url)

                for link in links:
                    next_url = urljoin(url, link['href'])
                    parsed_urlnext = urlparse(next_url)

                    if (
                        parsed_urlnext.netloc == urlparse(url).netloc and
                        next_url not in visited_urls and
                        link.has_attr('href') and
                        not link['href'].startswith('#') and
                        not link['href'].startswith('mailto:') and
                        not link['href'].startswith('javascript:')
                    ):
                        graph.add_edge(url, next_url)
                        web_crawler(next_url, max_depth, current_depth + 1, visited_urls, graph)

        except RequestException as e:
            print(f"Error crawling {url}: {str(e)}")

    return graph

start_url = "https://scrapeme.live/#icon-arrow-right"
web_graph = web_crawler(start_url, max_depth=3)

node_colors = ["navy" if node == start_url else "green" for node in web_graph.nodes()]
pos = nx.spring_layout(web_graph, k=0.5)
nx.draw(web_graph, pos, with_labels=True, node_color=node_colors, font_size=5, width=0.5)
plt.show()
