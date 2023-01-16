<!-- PROJECT LOGO -->
<br />
  <h2 align="center">Entity Resolution on Active Businesses Beginning with the Letter 'X' from the Secretary of State of North Dakota Database</h3>

  <p align="center">
    This analysis was developed for Sayari as part of the hiring process for the role of Junior Data Engineer
    <br />
    <a href="https://github.com/AmirZahre/Sayari_Entity_Resolution_Interview_Assignment/blob/main/sayari_scraper/sayari_scraper/spiders/Sayari_Spider_X_Entity_Capture.py"><strong>Check out the Scrapy Code »</strong></a>
    <br />
<a href="https://github.com/AmirZahre/Sayari_Entity_Resolution_Interview_Assignment/blob/main/graph_generation.py"><strong>Check out the Graph Code »</strong></a>
    <br />
	<br />
    <a href="https://github.com/AmirZahre/Sayari_Entity_Resolution_Interview_Assignment/releases/tag/Sayari">Download</a>
    ·
    <a href="https://github.com/AmirZahre/Sayari_Entity_Resolution_Interview_Assignment/issues">Report Bug</a>
    ·
    <a href="https://github.com/AmirZahre/Sayari_Entity_Resolution_Interview_Assignment/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

- [About The Project](#about-the-project)
- [Notable Insights](#notable-insights)
- [Graphs](#graphs)
- [Built With](#built-with)
- [Built For](#built-for)
- [Important Files (i.e. my code)](#important-files-ie-my-code)


<!-- ABOUT THE PROJECT -->
## About The Project

The Secretary of State of North Dakota provides a business search [web app](https://firststop.sos.nd.gov/search/business) that allows users to search for businesses by name. This assignment involves conducting entity resolution on a subset of this data, followed by visualizing any connections amongst businesses, agents (both commercial and noncommercial), as well as owners.

### Notable Insights

 *  There are 108 connections (edges, at least one business name connected to one entity). Of these 108, there are only twelve connections (edges) where three of more nodes exist.
 * **Incorp Services, Inc.**, **C T Corporation System**, and **Corporation Service Company** are affiliated with the greatest number of entities when compared to their peers.


### Graphs:
**Graph 1: All Edges and Nodes, No Labels**
![Graph 1: All Edges and Nodes, No Labels](https://github.com/AmirZahre/Sayari_Entity_Resolution_Interview_Assignment/blob/main/data/entity_connections_graph_1_node_minimum_with_labels_False.png)

**Graph 2: Nodes with More than Two Edges, No Labels**
![Graph 2: Nodes with More than Two Edges, No Labels](https://github.com/AmirZahre/Sayari_Entity_Resolution_Interview_Assignment/blob/main/data/entity_connections_graph_2_node_minimum_with_labels_False.png)

**Graph 3: Nodes with More than Two Edges, With Labels**
![Graph 3: Nodes with More than Two Edges, With Labels](https://github.com/AmirZahre/Sayari_Entity_Resolution_Interview_Assignment/blob/main/data/entity_connections_graph_2_node_minimum_with_labels_True.png)


___
### Built With
* [**Scrapy**](https://docs.scrapy.org/en/latest/) to scrape the data
* [**Graphviz's Atlas Layout**](https://networkx.org/documentation/latest/auto_examples/graphviz_layout/plot_atlas.html#sphx-glr-auto-examples-graphviz-layout-plot-atlas-py) to create and visualize edges & nodes
* [**Jupyter**](https://jupyter.org/) to analyze and create graphs of the data;
* [**Python**](https://www.python.org/)

### Built For
 * [Sayari](https://sayari.com/) as part of the interview process.
  
### Important Files (i.e. my code)
 * [Scrapy Code](https://github.com/AmirZahre/Sayari_Entity_Resolution_Interview_Assignment/blob/main/sayari_scraper/sayari_scraper/spiders/main_item_method.py) using **Scrapy Item** to capture the data **(preferred choice)**
 * [networkx graph](https://github.com/AmirZahre/Sayari_Entity_Resolution_Interview_Assignment/blob/main/graph_generation.py) Code used to create the graphs based on the output data from the Scrapy Crawler.
