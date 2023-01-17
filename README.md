<!-- PROJECT LOGO -->
<br />
  <h2 align="center">Entity Resolution on Active Businesses Beginning with the Letter 'X' from the Secretary of State of North Dakota Database</h3>

  <p align="center">
    This analysis was developed for Sayari as part of the hiring process for the role of Junior Data Engineer
      </p>
</p>
    <br />
    <a href="https://github.com/AmirZahre/Sayari_Entity_Resolution_Interview_Assignment/blob/main/sayari_scraper/sayari_scraper/spiders/Sayari_Spider_X_Entity_Capture.py"><strong>Scrapy Crawler Code »</strong></a>
    <br />
<a href="https://github.com/AmirZahre/Sayari_Entity_Resolution_Interview_Assignment/blob/main/graph_generation.py"><strong>Graph Code »</strong></a>
    <br />


<!-- TABLE OF CONTENTS -->
## Table of Contents

- [About The Project](#about-the-project)
	- [How to Run](#how-to-run)
	- [Process](#process)
	- [Notable Insights](#notable-insights)
	- [Potential Future Enhancements](#potential-future-enhancements)
	- [Graphs](#graphs)
- [Built With](#built-with)
- [Built For](#built-for)
- [Important Files (i.e. my code)](#important-files-ie-my-code)
- [Known Issues](#known-issues)


<!-- ABOUT THE PROJECT -->
## About The Project

The Secretary of State of North Dakota provides a business search [web app](https://firststop.sos.nd.gov/search/business) that allows users to search for businesses by name. This assignment involves conducting entity resolution on a subset of this data, followed by visualizing any connections amongst businesses, agents (both commercial and noncommercial), as well as owners.

### How to Run:
1. Create a Python virtual environment by executing `python -m venv venv`. Activate the virtual environment with the command `source venv/bin/activate`.
2. Download the required packages by executing the command `pip install -r requirements.txt`.

3. Finally, to run the script, invoke `main.py` from the top-level of the folder by executing the command `python main.py`.

### Process:

1. `main.py` will invoke the scraper, located in `sayari_scraper/sayari_scraper/spiders/Sayari_Spider_X_Entity_Capture.py`, via. subprocess. It will then save the collected data in the folder `/data` as `crawler_results.json`.
2. `main.py` will then invoke the file `graph_generation.py`, which will then use `crawler_results.json` to create the graphs shown below. These graphs will also be saved within the `/data` folder.


### Notable Insights:

 *  There are 108 connections (edges, at least one business name connected to one entity). Of these 108, there are only 12 connections (edges) where three or more nodes exist.
 * **Incorp Services, Inc.**, **C T Corporation System**, and **Corporation Service Company** are affiliated with the greatest number of entities when compared to their peers.
 
### Potential Future Enhancements:

* Incorporate Airflow with this process to schedule frequent scrapes and graph generations on a regular interval.
* Capture (1) the scrapy results by either pointing the BusinessResults() Item feed to an [S3 bucket](https://docs.scrapy.org/en/latest/topics/feed-exports.html#s3) or using Airflow's [LocalFilesystemToS3Operator](https://airflow.apache.org/docs/apache-airflow-providers-amazon/3.3.0/operators/transfer/local_to_s3.html), and (2) capture the generated graphs using [LocalFilesystemToS3Operator](https://airflow.apache.org/docs/apache-airflow-providers-amazon/3.3.0/operators/transfer/local_to_s3.html).



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
 * [Scrapy Code](https://github.com/AmirZahre/Sayari_Entity_Resolution_Interview_Assignment/blob/main/sayari_scraper/sayari_scraper/spiders/Sayari_Spider_X_Entity_Capture.py) using **Scrapy Item** to capture the data **(preferred choice)**
 * [networkx graph](https://github.com/AmirZahre/Sayari_Entity_Resolution_Interview_Assignment/blob/main/graph_generation.py) Code used to create the graphs based on the output data from the Scrapy Crawler.
 
 ### Known Issues:
- graphviz on Mac M1: Follow [this guide](https://github.com/pygraphviz/pygraphviz/issues/398) on installing graphviz if you're experiencing issues and are 
using an M1 computer.

```
brew install graphviz
python -m pip install \
    --global-option=build_ext \
    --global-option="-I$(brew --prefix graphviz)/include/" \
    --global-option="-L$(brew --prefix graphviz)/lib/" \
    pygraphviz
```

- Issues with Scrapy Items() pathing can be solved via [this guide](https://www.youtube.com/watch?v=V8lUh8mY-UI). This fix has also been implimented.
