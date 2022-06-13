# we_factor.py
# This script calculates your WE Factors based on given conditions and compares
# to a standard (made up) apartment reference vector and public social distancing vector
# Simple analysis doesn't integrate over time nor consider gate effect experienced for
# people living in apartments with out gates (block out bad people from coupling to building, stealing ME)
# Gate effect is assumed only for apartments, as if someone rolls up and hangs out in someone's
# house driveway they're assume to be a criminal and tresspassing (cops will come)
# Add input and expand formula to incorporate frequency of visitations and model homeless
# Author Mx. Aistheta Error (Adam J) Gleason
# 6/13/2022
import math as m

# Distance RMS function
# Calculates the RMS of the R vector characteristic
# def RMS_R(R_vec, a)
# R_vec: vector of distances (in meters)
# a: power of R used in computing RMS (on top of 2)
def RMS_R(R_vec, a):
    rsum = 0
    for r in R_vec:
        rsum += 1/(r**(2*a))
    return m.sqrt(rsum)

# Nox Ratio function vectorized
# This is the formula to compute Nox Ratio, which is the basis of comparison to compute WE Factor
# Duty cycle calculation weighting home and public times with corresponding RMS R
# def NR_calc_vec(RH_vec, RE_vec, E, a)
# RH_vec: vector of distances for housing scenario (in meters)
# RE_vec: vector of distances for equal public interaction (in meters)
# a: power of R used in computing RMS (on top of 2)
def NR_calc_vec(RH_vec, RE_vec, E, a):
    return ((1-E)*(RMS_R(RH_vec,a)) + E*RMS_R(RE_vec,a))

# Times of life (hours)
# total hours in a day
Tday = 24

# Time sleeping
print("----------------------------------------------------------")
Tsleep = float(input("How many hours do you sleep at night (at home)? "))
print("----------------------------------------------------------")
# Time working
Twork = float(input("How many hours do you spend working?: "))
print("----------------------------------------------------------")
# Public time
Tpub = float(input("After work, how many hours do you typically spend in public (shopping, religous, sports, picking up kids from school, etc., ex: 2.5): "))
# the other time spent at home (breakfast, dinner, after work...)
Thome = Tday - Tsleep - Twork - Tpub
print("The rest of the time spent at home after work has been calculated as the following:")
print(Thome)
print("----------------------------------------------------------")
# Input neighbor distances (build R vector)
print("Now we will input all your surrounding neighbors and how far you live from them")
print("For each neighbor, try to estimate the distance in meters (1 meter ~ 3ft), approximate best you can")
print("Estimate distance from the center of your house (or apartment) to the center of their home")
print("If your neighbors have multiple people living in the home, input a distance for each person, ie if your neighboring house 30m away has a family of 3, type 30m 3 times for a more accurate estimate")
print("Maximum number of neighbors is 40, to keep comparison to standard equal")
R_input_vec = []
done = 0
count = 1
while(done == 0):
    rin = input("Distance to neighbor "+str(count)+" in meters (type done if done): ")
    if (rin == "done" or count == 40):
        done = 1
    else:
        R_l = float(rin)
        R_input_vec.append(R_l)
    count = count + 1
print("----------------------------------------------------------")
print("This is what the array of neighbors looks like based off your input: ")
print(R_input_vec)
print("----------------------------------------------------------")

# a the power of R, assume 1.5, between 1 and 2
a = 1.5

# Equality coeff, time spent in public or "body sharing"
# E work from home
E_wfh_in = Tpub/Tday
# E work from office
E_wfo_in = (Tpub + Twork)/Tday

# Standard times for reference
# assumes working at public office
Tsleep_std = 8
Twork_std = 8
Tpub_std = 1
E_wfh_std = (Tpub_std)/Tday
E_wfo_std = (Tpub_std + Twork)/Tday

# Number of people and distance (average) in public situations
# Equal body sharing time
# Social Distancing standard vector (public)
# This means while you're in public, you're always surrounded by a person 3m away, another person 3m away, 4m, 5m, 6m, ...
# a total of 10 people
# This is an estimate of what I consider going to the grocery store, modify to fit your life
RE_vec = [3, 3, 4, 5, 6, 5, 6, 6, 7, 8]

# Apartment standard vector (for reference)
# multiple 3's incorporate multiple people living in the apartments surrounding you (not just a single person)
R_apt_vec = [3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 9, 9, 10, 10, 10, 10, 10, 10, 12, 12, 17, 17, 19, 19, 21, 21, 25, 25, 27, 27, 27, 27, 30, 30, 33, 33, 35, 35, 38, 38]
# RH_vec: vector of distances (in meters)

# Nox ratio for apartment working from home
NR_apt_wfh_std = NR_calc_vec(R_apt_vec, RE_vec, E_wfh_std, a)
# Nox ratio for apartment working from office
NR_apt_wfo_std = NR_calc_vec(R_apt_vec, RE_vec, E_wfo_std, a)

# Calculate the inputed NR
# Input nox ratio for working from office
NR_input_wfo = NR_calc_vec(R_input_vec, RE_vec, E_wfo_in, a)
# Input nox ratio for working from home
NR_input_wfh = NR_calc_vec(R_input_vec, RE_vec, E_wfh_in, a)

# Calculate WE Factor
print("Assuming you work frome office")
print("This means an office connected to the public, meaning you work close to grocery stores, food, gas, stores, and any other places that the general public frequents")
print("----------------------------------------------------------")
print("Your WE Factor compared to people living in an aparment and working from home (quartine, COVID) is: ")
print("1 / " +str(round(NR_apt_wfh_std/NR_input_wfo,2)))
print(str(round(100/(NR_apt_wfh_std/NR_input_wfo),2))+"% WE")
print("----------------------------------------------------------")
print("Your WE Factor compared to people living in an aparmtnet and working from an office (normal life) is: ")
print("1 / " +str(round(NR_apt_wfo_std/NR_input_wfo,2)))
print(str(round(100/(NR_apt_wfo_std/NR_input_wfo),2))+"% WE")
print("----------------------------------------------------------")
print("Assuming you work frome home")
print("This could also be an office that isn't connected to the public, such as an office in the desert, jungle, or farm (lab, power plant, factory, ...")
print("----------------------------------------------------------")
print("Your WE Factor compared to people living in an aparment and working from home (quartine, COVID) is: ")
print("1 / " +str(round(NR_apt_wfh_std/NR_input_wfh,2)))
print(str(round(100/(NR_apt_wfh_std/NR_input_wfh),2))+"% WE")
print("----------------------------------------------------------")
print("Your WE Factor compared to people living in an aparmtnet and working from an office (normal life) is: ")
print("1 / " +str(round(NR_apt_wfo_std/NR_input_wfh,2)))
print(str(round(100/(NR_apt_wfo_std/NR_input_wfh),2))+"% WE")
print("----------------------------------------------------------")
print("Thank you for taking the time to get to know your WE Factor! Consider this in your actions and thoughts about other people in life")


