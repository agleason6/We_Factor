# We_Factor
Simple script to calculate We Factor

WE Factor is a metric I invented to compare different housing scenarios (R Spaces) to apartments.

Breaks down WE Factor and compares working from home and working from office

We connect through magnetic fields, and magnetic fields fall off with distance. The script assumes that the fields fall off at a factor of 1/r^a, where "a" is 1.5 (conviently between 1 and 2); would need to really do a full characterization, however it doesn't really matter much because ratios are being taken (results do shift a little, but quality still shows and proves R Spaces).

The analysis factors out the R characterstic (B fields cancel out in ratio, R's don't)

The base formula calculates Nox Ratio = (1-E)*RMS(1/rh^a) + E*RMS(1/re^a)
rh = vector of distances to neighbors at home
re = vector of distances to people in public (during public time)
E is ratio of public to home time

run python3 we_factor.py
Follow prompts to input your housing situation

Feel free to modify the code to adjust the standard apartment vector and public social distancing based off your country's housing standard


example operation and output:
>> python3 we_factor.py
----------------------------------------------------------
How many hours do you sleep at night (at home)? 8
----------------------------------------------------------
How many hours do you spend working?: 8
----------------------------------------------------------
After work, how many hours do you typically spend in public (shopping, religous, sports, picking up kids from school, etc., ex: 2.5): 1
The rest of the time spent at home after work has been calculated as the following:
7.0
----------------------------------------------------------
Now we will input all your surrounding neighbors and how far you live from them
For each neighbor, try to estimate the distance in meters (1 meter ~ 3ft), approximate best you can
Estimate distance from the center of your house (or apartment) to the center of their home
If your neighbors have multiple people living in the home, input a distance for each person, ie if your neighboring house 30m away has a family of 3, type 30m 3 times for a more accurate estimate
Maximum number of neighbors is 40, to keep comparison to standard equal
Distance to neighbor 1 in meters (type done if done): 30
Distance to neighbor 2 in meters (type done if done): 30
Distance to neighbor 3 in meters (type done if done): 30
Distance to neighbor 4 in meters (type done if done): 40
Distance to neighbor 5 in meters (type done if done): 40
Distance to neighbor 6 in meters (type done if done): 40
Distance to neighbor 7 in meters (type done if done): 50
Distance to neighbor 8 in meters (type done if done): 50
Distance to neighbor 9 in meters (type done if done): 50
Distance to neighbor 10 in meters (type done if done): 60
Distance to neighbor 11 in meters (type done if done): 60
Distance to neighbor 12 in meters (type done if done): 60
Distance to neighbor 13 in meters (type done if done): done
----------------------------------------------------------
This is what the array of neighbors looks like based off your input: 
[30.0, 30.0, 30.0, 40.0, 40.0, 40.0, 50.0, 50.0, 50.0, 60.0, 60.0, 60.0]
----------------------------------------------------------
Assuming you work frome office
This means an office connected to the public, meaning you work close to grocery stores, food, gas, stores, and any other places that the general public frequents
----------------------------------------------------------
Your WE Factor compared to people living in an aparment and working from home (quartine, COVID) is: 
1 / 4.06
24.63% WE
----------------------------------------------------------
Your WE Factor compared to people living in an aparmtnet and working from an office (normal life) is: 
1 / 3.52
28.43% WE
----------------------------------------------------------
Assuming you work frome home
This could also be an office that isn't connected to the public, such as an office in the desert, jungle, or farm (lab, power plant, factory, ...
----------------------------------------------------------
Your WE Factor compared to people living in an aparment and working from home (quartine, COVID) is: 
1 / 20.37
4.91% WE
----------------------------------------------------------
Your WE Factor compared to people living in an aparmtnet and working from an office (normal life) is: 
1 / 17.65
5.67% WE
----------------------------------------------------------
Thank you for taking the time to get to know your WE Factor! Consider this in your actions and thoughts about other people in life
