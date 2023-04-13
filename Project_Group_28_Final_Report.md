# Final Report - Sustainable Development (Group 28)

## Introduction
Our group is excited to explore the umbrella topic "Sustainable Development". Development has always been and will be the goal of humanity. However, in today's time where the environment is engendered, and as we experience its adverse effects such as climate change, the question arises what can be done to make this development sustainable? Hence, through this exploration, we aim to explore the three main factors of sustainable development. First, money through the target variable GDP. Second, health through the target variable life expectancy. Thirst, the environment through the target variable carbon dioxide emissions. All in all, we are interested in exploring how these three facts are influenced by the various other factors in the dataset.

## Exploratory Data analysis

We explored our dataset using various numpy and pandas functions like shape, describe and nunique. As part of the EDA we explored the missing values in dataset using, using the missing values matrix which can be seen below:

<img src ="images/msn.png" width="500px">

Looking at the graph above we can see there are a signficant number of missing values for the variable people practicing open defecation, which is understandable because this might be difficult to record.

Additionally, to understand the spread of variables, we made a violin plot for each of the variables. 

<img src ="images/vplots.png" width="100px">

Looking at the graph above we can see that the variable Beer Consumption has the smallest spread, whereas, the variable GDP Per Capita has the biggest spread.

Next, we look at the relation between all the variables at a glance using the pairplot:

<img src ="images/pairplot.png" width="100px">

To understand the relation between all the variables better we then plotted a correlation matrix for the dataframe:

<img src ="images/corr.png" width="100px">

In the above correlation matrix we can see the correlation coefficiant of the all the variables in the dataframe.

## Research Topic 1: A Roadmap to a Greener Future: Understanding Factors Driving CO<sub>2</sub> Emissions
**Global warming is a big issue that humanity is facing today and poses a great threat to our future. The adverse effects of which we have experienced firsthand here in Kelowna, with temperatures hitting the extremes, with all-time highs and lows. Last year's heatwave was definitely a strong reminder to many of us about the great risks global warming can pose. Carbon dioxide emissions are the leading causes of human-induced climate change, henceforth, I wish to explore what factors influence CO<sub>2</sub> emissions which eventually cause climate change. The end goal is to find out the correlation between CO2 emissions and other variables.

I was first curious to know if there is a trend between the continents and carbon dioxide emissions. Is there continent that particularly stands out in terms of carbon dioxide emissions. 

<img src ="images/ridgeline.png" width="100px">

In the above ridgeline plot, we have grouped the entries by continent, and we can observe that there are certainly some continents that have the higher carbon dioxide emissions than other. On one hand we can observe that on an average the continent of Oceania is one with highest carbon dioxide emissions, but that is becuase in the dataset there is only one country in the continent of Oceania. On the other hand, we can observe that the continent of Africa has the lowest carbon dioxide emissions.

Saying so, we must also note that what we discussed is averages, but continents like Asia display some anomalous behaviour as they have outliers. Even though, on an average, Asia is not the continent with the highest carbon dioxide emissions, one of the countries in Asia has the highest carbon dioxide emissions in the world.

We can see a more visually appealing presentation of the same through geo maps in tableau as presented below:

<img src ="images/continent.png" width="100px">

To understand the impact of geography on CO<sub>2</sub> emmissions, we can see the CO<sub>2</sub> emissions by country:

<img src ="images/country.png" width="100px">

Another important factor that significantly impacts CO<sub>2</sub> emissions is Electric Power Consumption

<img src ="images/scatter1.png" width="100px">

Here we can see positive correlation between the two factors - both electric power consumption and carbon dioxide emissions move in the same direction. 

The last factors that significantly impacts CO<sub>2</sub> emisssions is GDP per capita:

<img src ="images/scatter2.png" width="100px">

Through the regression plot we can see that the relaiton between the two variable is close to a linear relation. Looking at the correlation matrix displayed earlier we can see the correlation coefficient is 0.828 which suggests a strong positive correlation between the two variables GDP per capita and carbon dioxide emissions.

#### Conclusion:
Based on the exploratory data analysis conducted we can conclude that that are numerous factors that influence carbon dioxide emissions. According to the analysis, there is a correlation between carbon dioxide emissions and continent, a country's level of development, how much electricity is used, and GDP per capita. The continent of Oceania stands out as having the largest carbon dioxide emissions, whilst Africa has the lowest emissions. Additionally, Carbon dioxide emissions are often higher in nations with higher levels of economic development and electric power usage. The investigation also revealed a strong positive association between GDP per capita and carbon dioxide emissions, which shows that carbon dioxide emissions increase with GDP per capita. Overall, the analysis suggests that countries' economic development and power consumption play the most crucial role in their carbon dioxide emissions.
