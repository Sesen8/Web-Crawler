#imported libraries
import requests
from bs4 import BeautifulSoup # only impaorting BeautifulSoup class in bs4 into our program
import networkx as nx 
import matplotlib.pyplot as plt
from urllib.parse import urljoin, urlparse, urlunparse
from requests.exceptions import RequestException

def web_crawler(url, max_depth=3):
    visited_urls= set()  #keeps track of the Urls visted 
    graph = nx.DiGraph()# create undfirected graph

    def crawl(current_url, depth):
        current_depth= depth -1
        if depth > max_depth or current_url in visited_urls:
            return
            #current url and next url are nodes 

        try:
            parsed_url = urlparse(current_url)

            if not parsed_url.scheme:
                current_url = urljoin("http://", current_url).replace('//', '/')
            response= requests.get(current_url) #checking validity of the current url

            if parsed_url.scheme not in ['http', 'https']: #handling phones etc
                visited_urls.add(current_url)
                return

            response = requests.get(current_url, timeout= 10)
                
            if response.status_code == 200: #request grante
                soup= BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', href =True) #find all the hrefs 

                for link in links:
                    next_url = link['href']#extract the hrefs

                    if '#' in next_url:
                        next_url= urljoin(current_url, next_url)
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



def web_crawler(url, max_depth = 3 ,current_depth =None, visited_urls=None, graph=None):
    current_depth = 0 if current_depth is None else current_depth
    #print(f"Processing URL: {url}, Depth: {current_depth}")
    #queue = deque([(url, 0)]) 
    visited_urls= set()  #keeps track of the Urls visted 
    graph = nx.DiGraph() if graph is None else graph# create undfirected graph
    
    if current_depth < max_depth and url not in visited_urls:
        try:
            parsed_url = urlparse(url)
            if not parsed_url.scheme:
                url = urljoin("http://", url).replace('//', '/')
            #checking validity of the current url
            response = requests.get(url, allow_redirects=False, timeout=30, verify=None)

            if response.status_code == 200: #request grante
                soup= BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', href =True) #find all the hrefs
                #print(f"URL: {url}, Links found: {len(links)}")

                visited_urls.add(url) 

                for link in links:
                    next_url= urljoin(url, link['href'])#extract the hrefs

                    parsed_urlnext = urlparse(next_url)

                    if (
                        parsed_urlnext.netloc == parsed_url.netloc and next_url not in visited_urls and not link['href'].startswith('mailto:')
                    ): #preventing the codes from poting back to each other 
                        graph.add_edge(url, next_url, weight = current_depth ) #creating an edge
                        web_crawler(next_url, max_depth, current_depth + 1, visited_urls, graph)

                # Mark the current URL as visite

        except requests.RequestException as e:
            print(f"Error crawling {url}: {str(e)}")
    return graph

test_graph = {
    'A': {'B': {'weight': 1}, 'C': {'weight': 3}},
    'B': {'C': {'weight': 1}, 'D': {'weight': 2}},
    'C': {'D': {'weight': 1}},
    'D': {}
}

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



def closeness_centrality(web_graph, start_url):
    start_dis = dijkstra(web_graph, start_url)
    dist = 1 / sum(start_dis.values())
    return dist

start_url = input("Enter a Url ")
web_graph = web_crawler(start_url) #initializing the drwing

centralities= {node : closeness_centrality(web_graph, start_url) for node in web_graph.nodes()}

for node, closeness in centralities.items():
    print(f"{node}: {closeness}")

distances = dijkstra(test_graph, 'A')  # Corrected function call

# Expected shortest distances from source node 'A'
# Verify the computed distances
for node, distance in distances.items():
    assert distance == expected_distances[node], f"Distance to node {node} is incorrect: {distance}"
print("All distances are correct!")

node_colors = ["navy" if node == start_url else "green" for node in web_graph.nodes()]
pos = nx.spring_layout(web_graph, k=0.5) #positon of the nodes
nx.draw(web_graph, pos, with_labels=False, node_color= node_colors, font_size=5, width = 0.5)



plt.show()





# https://spu-csc.github.io/index.html



#print("Nodes:", web_graph.nodes())
#print("Edges:", web_graph.edges())


#pos = nx.drawing.nx_agraph.pygraphviz_layout(web_graph, prog='dot')








                    else:
                        next_url = urljoin(current_url, next_url).replace('http://', '').replace('https://', '')
                    
                    parsed_urlnext = urlparse(next_url)
                    
                    
                    if parsed_urlnext.netloc == parsed_url.netloc not in visited_urls:#preventing the codes from poting back to each other 
                        graph.add_edge(current_url, next_url) #creating an edge
                        visited_urls.add(next_url)
                        crawl(next_url, depth + 1)

                #visited_urls.add(current_url) #keep track of the urls

        except RequestException as e:
            print(f"Error crawling {current_url}: {str(e)}")


    crawl(url, 0)
    return graph

start_url = "https://spu.edu/"
web_graph = web_crawler(start_url) #initializing the drwing

#print("Nodes:", web_graph.nodes())
#print("Edges:", web_graph.edges())


#pos = nx.drawing.nx_agraph.pygraphviz_layout(web_graph, prog='dot')

#nx.draw(web_graph, pop=pos,  with_labels=True)
#plt.show()
node_colors = ["navy" if node == start_url else "green" for node in web_graph.nodes()]
pos = nx.spring_layout(web_graph, k=0.5) #positon of the nodes
nx.draw(web_graph, pos, with_labels=False, node_color= node_colors, font_size=5, width = 1.0)
plt.show()