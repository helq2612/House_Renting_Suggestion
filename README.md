# House Renting Suggestion
## Collaborated with Dapeng Li and Yifan Shen
## Introduction
In this project, we designed a approach to predict apartment renting price in Corvallis based on the infor- mation listed on Craigslist. We first used scrapy to crawl raw data on Craigslist in Corvallis, after data cleaning, we implemented MySQL queries to join and project with two schemas, and stored the data into one csv file. We used Linear Regression and Neural Network to fit the training data set. The results on the testing dataset showed that these two methods perform as well as expected.

## Data Collection
We implemented scrapy to collect apartment renting information on Craigslist in Corvallis. Scrapy is free and open source web crawling framework, written in Python, for extracting the data you need from websites. Details about it can be found on its official website: [scrapy](https://scrapy.org/).

By clonging this folder, after install scrapy (I suggest to install under venv), go the folder of "", on your terminal, type:
```python
scrapy crawl first --nolog --output=first.csv
```
Then all the data will be saved in first.csv file

