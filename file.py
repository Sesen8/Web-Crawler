#imported libraries
import requests
from bs4 import BeautifulSoup # only impaorting BeautifulSoup class in bs4 into our program
import networkx as nx 
import matplotlib.pyplot as plt
from urllib.parse import urljoin, urlparse, urlunparse
from requests.exceptions import RequestException
from collections import deque  # Correct import of deque
import certifi
import heapq



def web_crawler(url, max_depth=3, current_depth=0, visited_urls=None, graph=None):
    visited_urls = set() if visited_urls is None else visited_urls  # keeps track of the Urls visted
    graph = nx.DiGraph() if graph is None else graph  # create undfirected graph

    if current_depth < max_depth and url not in visited_urls:
        try:
            parsed_url = urlparse(url)
            if not parsed_url.scheme:
                url = urljoin("http://", url).replace('//', '/')
            # checking validity of the current url
            response = requests.get(url, allow_redirects=False, verify=None)

            if response.status_code == 200:  # request grante
                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', href=True)  # find all the hrefs

                visited_urls.add(url)

                for link in links:
                    next_url = urljoin(url, link['href'])  # extract the hrefs

                    parsed_urlnext = urlparse(next_url)

                    if (
                        parsed_urlnext.netloc == parsed_url.netloc and next_url not in visited_urls and not link[
                            'href'].startswith('mailto:')
                    ):  # preventing the codes from poting back to each other
                        graph.add_edge(url, next_url, weight=1)  # creating an edge
                        web_crawler(next_url, max_depth, current_depth=current_depth + 1, visited_urls=visited_urls,
                                     graph=graph)

        except requests.RequestException as e:
            print(f"Error crawling {url}: {str(e)}")
    return graph


def dijkstra(graph, s_node):
    distances = {node: float('inf') for node in graph}
    distances[s_node] = 0
    priority_q = [(0, s_node)]

    while priority_q:
        d_current, vertex_c = heapq.heappop(priority_q)

        if d_current > distances[vertex_c]:
            continue

        for neighbor, weight in graph[vertex_c].items():
            distance = d_current + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_q, (distance, neighbor))
    return distances




def closeness_centrality(web_graph, start_node):
    start_dis = dijkstra(web_graph, start_node)
    #print(f"dis :{start_dis}")
    dist = 1 / sum(start_dis.values())
    return dist

start_node = input("Enter a Url: ")
web_graph = web_crawler(start_node) # initializing the drawing

centralities = {node: closeness_centrality(web_graph, node) for node in web_graph.nodes()}

for node, closeness in centralities.items():
    print(f"Closeness Centrality: {closeness}")

node_colors = ["navy" if node == start_node else "green" for node in web_graph.nodes()]
pos = nx.spring_layout(web_graph, k=0.5) # position of the nodes
nx.draw(web_graph, pos, with_labels=True, node_color=node_colors, font_size=5, width=0.5)

plt.show()





# def closeness_centrality(web_graph, start_url):
#     start_dis = dijkstra(web_graph, start_url)
#     print(f"dis :{start_dis}")
#     dist = 1 / sum(start_dis.values())
#     return dist

# start_url = input("Enter a Url ")
# web_graph = web_crawler(start_url) #initializing the drwing

# centralities= {node : closeness_centrality(web_graph, start_url) for node in web_graph.nodes()}

# for node, closeness in centralities.items():
#     print(f"{node}: {closeness}")

# node_colors = ["navy" if node == start_url else "green" for node in web_graph.nodes()]
# pos = nx.spring_layout(web_graph, k=0.5) #positon of the nodes
# nx.draw(web_graph, pos, with_labels=True, node_color= node_colors, font_size=5, width = 0.5)



# plt.show()





# https://spu-csc.github.io/index.html



#print("Nodes:", web_graph.nodes())
#print("Edges:", web_graph.edges())


#pos = nx.drawing.nx_agraph.pygraphviz_layout(web_graph, prog='dot')







