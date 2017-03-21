# House Renting Suggestion
## Collaborated with Dapeng Li and Yifan Shen
## Introduction
In this project, we designed a approach to predict apartment renting price in Corvallis based on the infor- mation listed on Craigslist. We first used scrapy to crawl raw data on Craigslist in Corvallis, after data cleaning, we implemented MySQL queries to join and project with two schemas, and stored the data into one csv file. We used Linear Regression and Neural Network to fit the training data set. The results on the testing dataset showed that these two methods perform as well as expected.

## Data Collection
We implemented scrapy to collect apartment renting information on Craigslist in Corvallis. Scrapy is free and open source web crawling framework, written in Python, for extracting the data you need from websites. Details about it can be found on its official website: [scrapy](https://scrapy.org/).

By clonging this folder, after install scrapy (I suggest to install under venv), on your terminal, to call the "first" spider, just type:
```python
scrapy crawl first --nolog --output=first.csv
```
Then all the data will be saved in first.csv file.

In this csv file, the 4th column contains all the url links of each poster. Then by using spider "second", we can obtain all the information, such as latitude, longitude, bedroom number, and bath room number. Then store them in second.csv file, as shown below:
```python
scrapy crawl second --nolog --output=second.csv
```
**Warning 1 :** There are some white spaces and line breaks in the data (use _clean.py_ to clean).;  
**Warning 2 :** Some data are missing, such as bedroom number, bathroom number, etc. Remove them;  
**Warning 3 :** Some duplications might be exist. Use Excel commend to remove.  

## Data Collection
### Add Safety Rate
Since safety rate is reasonable factor impacting house renting price, we introduced this attribute into our model. The safety rate of Corvallis is available on [Neighbourhoodscout](https://www.neighborhoodscout.com/or/corvallis).  
However, as we can see, the shape of each zone is regular. One duable method is deviding big zone into small parts, and map the latitude and longitude value with the apartment location.  
Here we chose an easy and approximate method:
* Divide each zone to small part, 
* Find the center point of each part(shown by red point), 
* Calculate the distance (Euler distance) between the apartment and all center points,
* Get the center point with minimum distance,
* Label the safety rate of this apartment with the safety rate of that center. 
### MySQL Queries
After data clean, and add safety rate, we got two csv files, first.csv and second.csv. Import them into MySQL workbench, and simply using following queries:  
```python
select first.pid, price, area, safety, latitude, longitude
from first, second
where first.pid = second.pid  and safety <> ""
```
Then we got total 656 data entries.

## Data Analysis
We divided data into two parts: 606 as training examples and 50 as testing examples.  
For the linear regression model, we got the weight as shown below:  
Area | Longitude | Latitude | Safety Rate
------------ | ------------- | ------------- | ------------- 
494.331 | -144.024 | -108.401 | -14.388

And its score is 69.9%.

For the Neural Network model, the score is 73.3%, which is better than the linear regression model(69.9%).


<img src="https://github.com/helq2612/House_Renting_Suggestion/blob/master/images/Figure9.png" alt="Drawing" style="width: 100px;"/>

Above figure shows part of our result of the predicted data. The left column shows the pre- dicted price of the linear regression model, the right column shows the predicted price of the neural network regression model and the middle column shows the true predicated price. This table clearly demonstrates the more accuracy neural network models achieved in predicating the price compared to the linear regression model. Therefore, there might be some features not linearly related to the target and neural network can apply in high-dimension and learn a better fix on X and Y.
<!---
![alt text](https://github.com/helq2612/House_Renting_Suggestion/blob/master/images/Figure9.png =100x120)
-->
