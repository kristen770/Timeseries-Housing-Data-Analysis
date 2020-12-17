# Phase-4-Final-Project 
By: Kristen Davis   

<p align="center">
  <img width="600" height="250" src="/Images/photo-1491357492920-d2979986a84e.jpeg">
</p>
 
 [](/Images/photo-1491357492920-d2979986a84e.jpeg)   

# Overview  
For the Phase 4 Final Project I chose to model Time Series Data from [Zillow Research](https://www.zillow.com/research/data/) data. The task was to act as consultant advising an investor on the "5 best zipcodes" to invest in. The data from Zillow included the average price of single family home sales each month from from 1996 - 2018 accross the US. This project showcases technical skills such as Pandas, proficiency with Time Series, and ARIMA modeling as well as soft skills such as domain knowledge, data driven insights and strong analysis. 

# Project Senario 

InvesTex is a real estate investment firm looking to make value buys in the Dallas/ Fort Worth Metroplex. Looking to buy low sell high the client is targeting a  18-36 month turn around on investment. They have asked for the 5 best zipcode to invest in. Using domain knowledge in conjunction with the data 'best' will be defined using the following metrics:  

1. Homes in the Dallas/ Fort Worth Metroplex
2. Zipcodes location within or near a high preforming school disctrict 
2. Postitive Predicted Earnings 18 - 36 months from the home buy 
3. Highest ROIs

# Data Processing   

There are 207 zipcodes in the Dallas/ Fort Worth Metroplex, to filter the data further I applied the first metric of best- grouping zipcode by school district and then looking at the school district [grade](https://www.niche.com/k12/search/best-school-districts/m/dallas-fort-worth-metro-area/) of each district.

71 of these zipcodes fall into high preforming (A-, A, A+) school districts. The majority of these zipcodes fall outside of Dallas proper, in suburbs in and around highways. These are the zipcode I modeled, looking for family homes that will produce a return within 18 - 36 months for the investor.  

Looking at the overall trend of this data we can see that housing prices were relatively turmultous during the late 1990 with a small but steady rise in prices between 2000 & 2008. While not a dramatic dip in prices in this housing data set the 2008 housing bubble burst did affect housing prices overall. There is about 4 years of stagnant growth in the market. Starting in 2012 there is a dramatic rise in prices over all. Since my client is looking to receive return on investment in the relatively short term (18-36 months) the housing prices pre bubble & during the recovery are not directly indicative of the current housing market and this client assumes there will be no second bubble in the short term that would need to be accounted for. Thus I am going to segment my data to include only home value prices after 2015 to build a model on.

# ARIMA Modeling   

Using ARIMA Modeling I predicted home value prices for each of the zipcodes considered. This modeling looked at housing prices up to 36 months from a 'buy' date of April 2018. The ARIMA modeling provided a predicted value, a high and low for each zipcode and I added additional calcualtions of ROI (return on investment) based on a predicted value sell in October 2019 (18 months) and April 2021 (36 months). I then filtered zipcodes to identify the 5 with the highest ROI, while the ROI was different at each interval it is interesting to note that the top 5 highest ROIs were in the same zipcodes for 2019 and 2021 further strengthening the recommendation. 

# Conclusion    

The 5 zipcodes that I would recommend the client buy are: 

 * 75205 - Highland Park, Texas - 18 Month ROI = 59,301.00 / 36 Month ROI = 119,147.00
 
 * 75094 - Wylie, Texas - 18 Month ROI = 50,704.15 / 36 Month ROI = 105,634.49 
 
 * 75009 - Celina, Texas - 18 Month ROI = 57,106.34 / 36 Month ROI = 121,411.43 
 
 * 75167 - Waxahachie, Texas - 18 Month ROI = 58,555.76 / 36 Month ROI = 118,947.10  
 
 * 75182 - Sunnyvale, Texas - 18 Month ROI = 62,362.45/ 36 Month ROI = 132,092.47

# Future Work:   
With greater time and scope I would pursue the following additions to the project: 
1. Extend the scope of the data to zipcodes outside of Dallas/Fort Worth 
2. Look at additional features to prefilter the data - largest lot size, fastest growing ect. 
3. Consider different windows to base my ROI calculations on 
4. Build and interactive dash for a potential client to explore the data with 
5. Functionize my workflow to build a class

# Resources: 
* Flatiron School Curriculum 
* Zillow 
* Unsplash 

# [Blog Post](https://kristendavis27.medium.com/stationarity-check-16701ddbe963)    
# [Executive Summary](https://docs.google.com/presentation/d/138AyPTbIbCXHykpWUnBVU1TmxnDSZWSHfv4QhCyUleQ/edit#slide=id.ga5da48c167_0_193)
