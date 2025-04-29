
# Web Crawler
A web crawler application that creates a web-link graphs and finds the Closeness Centrality for each node



## Introduction	
<pre>
    In our digital age, information can be found in all corners of the internet. From news 
    articles, to social media posts, the information online is ever-expanding and 
    everlasting. However accessing and organizing all this data and intel can be a tedious 
    task, as the internet is very much interconnected. Bringing in our solution to this 
    very query, a Web Crawler!
</pre>



## Description
<pre>
    This web crawling project includes the creation of a program that is designed to 
    explore and navigate websites through a provided link, with the purpose of gathering 
    information from them. This program functions by scanning numerous web pages and 
    links that can be found on the initial website. From here it will create a beautiful 
    graph displaying the nodes which resemble the pages found. As well as the edges 
    that are the links found from the website, which show the connection between each node
    node and how they interconnected through each website. As seen through the graph all of 
    the edges have the same weight, and we did not use weight as the depth. Once the graph 
    is created, the program will continue to calculate the closeness centrality of each 
    node(webpage) which is the proximity of node based on the shortest path to the rest of 
    the nodes in the graph. With this web crawling program and its visial represention, one
    can gain a deeper understanding of a websites interconnectivity as well as its organization.  
</pre>


## Requirements	
<pre>
    Before you begin you are going to need to download some packeages.  

    1. Install Python3 Enviroment 
        - type: python3 -m venv venv
        - i.e: sesenyonas@Sesens-MacBook-Pro web-crawler-tearm-and-graph-2 % python3 -m venv venv
    
    2. Install Python3 Enviroment Activator
        - type: source venv/bin/activate
        - i.e: sesenyonas@Sesens-MacBook-Pro web-crawler-tearm-and-graph-2 % source venv/bin/activate

    3. Install Requests
        - type: pip3 install requests
        - i.e: pinkshukie@Shukras-Air web-crawler-tearm-and-graph-2 % pip3 install requests

    4. Install beautifulsoup4
        - type: pip3 install bs4 
        - i.e:  pinkshukie@Shukras-Air web-crawler-tearm-and-graph-2 % pip3 install bs4

    5. Install networkx as nx
        - type: pip3 install networkx
        - i.e: pinkshukie@Shukras-Air web-crawler-tearm-and-graph-2 % pip3 install networkx

    6. Install matplotlip
        - type: pip3 install matplotlib
        - i.e : pinkshukie@Shukras-Air web-crawler-tearm-and-graph-2 % pip3 install matplotlib

    7. Install scripy
        - type: pip3 install scripy 
        - i.e: sesenyonas@Sesens-MacBook-Pro web-crawler-tearm-and-graph-2 % pip3 install scripy  


</pre>


## User Manual 

### Setting up the Program
<pre>
    1. Begin by cloning or downlaoding the program repository to a local folder on your computer
    2. Then start your VS Code, simular code editor, or Terminal/CommandLine 
    3. Open the folder containing the project folder
    4. Begin the program by activating the virtual enviroment it runs on 
        - source venv/bin/activate 
    5. Install the required packages
        - python3 -m venv venv
        - pip3 install requests
        - pip3 install bs4
        - pip3 install networkx
        - pip3 install matplotlib
    6. Congrats you've successfully downloaded the required installations, see part next part
</pre>

### Running the Program
<pre>
    1. Open project folder in code editor
    2. Activate virtual enviroment to begin
        - source venv/bin/activate 
    3. Run the program
        - python3 file.py 
    4. Enter a URL that you want to the program to analyze 
    5. Now sit back and watch the Web Crawler do its thing!

</pre>


## Reflection
<pre>
    During the production of the web crawling project, my partner and I gained a comprehensive 
    understanding when it came to small and large details surrounding the process of traversing 
    the internet. From the beginning part of the project, we learned the importance of parssing 
    html content to properly retrieve the information needed for our graphs. Additionally we 
    understood how to handle different types of content and navigate through various website 
    structures effectively. 
    
    As for challenges, the first one we faced was getting the graphs to show up, as nothing was 
    being displayed after we got the program to run, so we had to download so many libraries
    and packages. The second challenge we faced was about the depth and closeness centrality. 
    We were trying a large domain such as SPU.edu, the program “looked” like it worked, but 
    when running smaller domains, the graphs looked off. This was either because we were not 
    keeping track of the visited URLs properly or we warrant keeping track of depth well. There 
    were a lot of days with trials and errors such maybe using queues, removing a loop, etc. to 
    figure out the solution.With the calculation of Dijkstra and closeness centrality, first, 
    the code was not reading any code after the graph was printed. And to use the print 
    statement to debug and figure out why it was not calculating the closeness centrality 
    much less entering the dijkstratas function. Turns out they were just in the wrong place 
    in the code.  

    Now when we got to read the rest of the functions, we were having trouble matching. 
    Meaning the Dijkstra function we had used before, was outputting dictionaries instead of 
    values, eg it was outputting something similar to an adjacent list(url edge and its 
    weight). Yet closeness centrality was using the Dijkstra output to calculate arithmetic 
    closeness. For this too we had to rely on several print statements to see what was 
    going on. At first we thought it was something with the closeness centrality algorithm
    and switched back and forth between the two equations. We tried getting around this 
    issue using lambda but didn't work.

    Then after solving the issue, we faced trouble with crawling pages. We no longer were 
    able to crawl the SPU and other websites suddenly. We have this Error “Error crawling 
    https://spu.edu/ugcatalog/interdisciplinaryinformation-studies: HTTPSConnectionPool
    (host='spu.edu', port=443): Maxretries exceeded with url: /ugcatalog/interdisciplinary
    /information-studie (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection 
    objectat 0x11closeness centrality87590>: Failed to resolve 'spu.edu'([Errno 8] 
    nodenam nor servname provided, or not known)"))” 
    
    After seeing this, we didn't even know where to start but we had also realized SPU was 
    such a large domain which made us decide to explore smaller links. As a result we used 
    the GitHub.io link our professor provided us to fix the graph, make some edits to the 
    codes, and correct the centrality algorithm. Proceeding this, it now seemed like the program 
    was only working with that link. Other URLs were either giving us 0.0 centrality or the graphs 
    were off or even had the same connection error like spu. However we fixed all that and we
    were able to run spu.edu and find closeness centrality

    As for time complexity of our program, if we were to break it down we'd begin with the web 
    crawling function which would have a complexity of O(V+E), with V for number of pages and E 
    for number of links. Then with the addition of Dijkstra's algorithm logV, and with the
    closeness centrality calculation the overall time complexity would be O(V(V+E)logV). 


    Here is the link to the google drive with our videos 
    https://drive.google.com/drive/folders/1VMRyph6od9DmXyrpdeMKReP3cmF598oi?usp=drive_link

</pre>

## Results
<pre>
    
    spu.edu example graph
    <img width="1393" alt="Screenshot 2024-03-14 at 10 21 52 PM" src="https://github.com/csc3430-winter2024/web-crawler-tearm-and-graph-2/assets/96497659/1f13adf2-19ed-4c79-988b-c313167c363d">


    spu.github example
    <img width="1393" alt="Screenshot 2024-03-14 at 10 21 52 PM" src="https://github.com/csc3430-winter2024/web-crawler-tearm-and-graph-2/assets/96497659/aa4e5a6e-0b02-4f75-9096-ac949e67121d">

</pre>

















    
