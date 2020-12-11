# VRU_code
 
# Description
Problem and Solution
- Death and injuries faced by traffic safety has made up a significant portion of health issues in the US. Every year, we have 20-50 million people suffering from non-fatal traffic injuries that often result in long-term disabilities. The traffic ecosystem currently fails to provide vulnerable road users(pedestrians, bike riders, etc.) as the current automatic braking systems are far from able to guarantee the prevention of collisions. In recent years, there has been this ongoing research in finding the most optimal method to alleviate traffic accidents. At Volvo, project City Safety is implemented to minimize the damage of the collisions. This mechanism is designed to be activated as late as possible to avoid unnecessary intervention. For vehicles, the brake is released automatically after the vehicle speeds up to 28 mph for pedestrians and 30 mph for cyclists. However, it has to perform to our expectations as activities include drivers turning the steering wheel sharply, driver releases pressed brake during AEB maneuver, VRU is encountered after corner turning, and VRU don’t wear reflective clothing in dark environments. In search of a better solution, we have decided on building and maintaining a simulation server for traffic safety to visualize our data, and alert drivers of approaching VRU before cameras and the human eye. To do so, we will perform our research in two approaches: traffic accident analysis, Geolocation API. Then include our findings into a dataset which observes VRU type, VRU coordinates. In Our buildup, we hope to deploy data science techniques in search of the best mechinis, to alleviate traffic accidents. 

- We have proposed a motion classifier where it is trained by acceleration data from an accelerator & gyroscope on smartphones. In our findings, aside from speed, other factors also play a crucial role in traffic accidents. We have looked into road condition, weather, types of accidents in conjuring a more complex explanation. 

- First, we have developed a motion classifier with acceleration data. We trained our data with the KNN model and have achieved a testing accuracy of 0.946111. In addition, in terms of the traffic analysis portion, we inspected the situation with the following aspects. First, starting to see which kind of road conditions when an accident occurs, we have found out that road intersections have been a major location of traffic accidents. Thus, we would conclude that a classification of road conditions has different priorities when examining the risk of the VRU. Then we investigated the risk faced by different type of VRUs, the level of danger is described as follows: Vehicles > Cars/Pickup >  Bicycle users > Motorcycles > Bus > Trucks. In addition, to provide a better understanding of traffic understandings we also took speed and weather into consideration. We created a model where Predictor = Population / 10000000 * 0.02 + Total Average Temperature* 0.095 + RAINING * 0.34 + SNOWING * 0.50 + FOG * 0.20 + WIND * 0.16 to service as a better indicator for our alert system. 

As our project required a plethora of engineering works that required collaboration with hardware engineers, we built a simulator to reveal the specifics of our project. In our simulator, we have implemented our understanding of road users and have VRUs and vehicles interact. 

In the future, we hope to thrive for a more practical use of our research and work with cross functioning teams to deliver a better product that protect more VRU.  



# Deployment, Running
## PART I：

## converttosimdata.py

converttosimdata.py integrates VRUS from terminal input and CSV file and converts them into a JSON file. The current script parses the open data set: https://github.com/udacity/self-driving-car/tree/master/datasets

Road user types in order: BIKE, PEDESTRIAN, CAR, TRUCK, SKATER
*Argument 0 --- converttosimdata.py
*Argument 1 --- CSV file that contains two columns "lat" and "long", both in float or integer.
*Argument 2 --- The name for the JSON file. Must contain ".json". Optional.
*Argument 3 --- Number of routes. Must be a positive integer.
*Argument 4 --- List of BIKE road users. If there are no bikers but other following road users, input a list of zeros. If there are no following road users, optional. The length of the list must be equal to the number of routes. Elements in the list must be positive integers.
*Argument 5 --- List of PEDESTRIAN road users. If there are no pedestrians but other following road users, input a list of zeros. If there are no pedestrians and no following road users, no input is needed.
*Argument 6 --- List of CAR road users.
*Argument 7 --- List of TRUCK road users.
* Argument 8 --- List of SKATER road users.
* Arguments are not noted optional are required.
### TO RUN
Download converttosimdata.py.
From terminal, run for example:
1.python converttosimdata.py gps.csv output1.json 2 [2,2] [3,3] [4,4] [5,5] [6,6]
2.python converttosimdata.py gps.csv output2.json 2 [2,2] [0,0] [4,4]
3.python converttosimdata.py gps.csv output3.json 3 [0,0,0] [3,3,0] [0,0,0] [1,0,1]
 
It will create a JSON file like this format but with a much larger “gps” list. 

## PART II:

## data_analysis.ipynb

You can run data_analysis.ipynb locally or on Google Colab. We used two datasets in this part: whether_car.csv, SC_Collisions.csv(Collisions in SC county), Population.xlsx(Population of each county in California), vechicle_2019.xlsx(Number of automobiles in each counties in California),  data.xlsx(reported traffic accidents from 2002-2010), and 2349981.csv. 

We did the following analysis: 
- motion classifier
1. main purpose is to analyze how accelerantion would help us to better understand traffic accidents
2. trained the model wiht Logistics regression, KNN, Decision tree, Perceptron, XFBoost, Random Forest. 
3. KNN is our most optimal algorithm
4. Conclusion: with accelerometer data, it classifies road user type with a KNN.

- data_analysis
1. occurance of traffic accidents at different road types
2. how weather impacted collision with correlation
3. employing a predictor variable and test for accuracy
4. futher analysis of traffic accidents in the Santa Clara county



