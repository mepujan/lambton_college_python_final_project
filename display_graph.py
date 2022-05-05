# c0842623 - Pujan Gautam
# Final Project


# Project Requirements
    # Numpy
    # Pandas
    # Matplotlib

# Output Script
# python display_graph data.csv


# importing packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import random
import sys
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()    # initializing fig and axes object
x_data, y_data = [], []     #declaring empty list for x_data and y_data

# generating two columns years and inflation
# and writing it to a file name data.csv using pandas
def generating_and_writing_data():
    years = np.array([i for i in range(1900,2023)]) #creating years array starting from 1900 to 2022
    inflation = np.array(random.rand(2023-1900))    #creating inflation array using random number function
    data_set = np.vstack((years,inflation)).T       #combining two 1D numpy arrays into 2D arrays
    data_frame = pd.DataFrame(data_set,columns=['Years','Inflation'])   # creating the dataframe of 2D arrays
    data_frame.to_csv("data.csv",index=False)  #writing the dataframe to csv file 
    
# function that plot the data into graph
def animation_frame(data):
    chunk_size = 30 #initializing chunk size of data for amount of data to be fetched 
    with pd.read_csv(sys.argv[1],chunksize=chunk_size) as data:    # reading csv file , file name is taken from command line
        for chunk in data:      #iterating over each chunk of data (i.e 1 chunk has 30 data)
                plt.clf()   #clearing entire field with all its axes
                max_inflation_year = ""
                ax.set_xlim(0,30) #setting the limit of one plot upto 30 data
                years = chunk['Years']      # getting years from the chunk
                inflation = chunk['Inflation']   # getting inflation data from the chunk
                max_inflation = str(chunk["Inflation"].max())  # getting max inflation value
                year_index = chunk["Inflation"].idxmax()       #getting id of max inflation value
                max_inflation_year = str(int(chunk["Years"][year_index]))  #fetching year value based on max inflation index value
                label = "Years: "+max_inflation_year+"   Max Inflation: "+max_inflation  #string representation for plot legend
                plt.plot(years,inflation, label = label)    #plotting the years and inflation value to graph
                plt.tight_layout()  # fitting plot within figure clearly
                plt.title("Inflation Graph")    # defining title of graph
                plt.legend(loc="upper left") # defining location of the legend
                plt.xlabel("Years ")    # xlabel name
                plt.ylabel("Inflation") # ylabel name
                plt.pause(0.1)          # pausing the animation for 0.1 second   
    generating_and_writing_data()       #calling to generate new data


#main program
if __name__ == "__main__":
    generating_and_writing_data()     #initailly generating data and saving it to a data csv file 
    animaton = FuncAnimation(fig, func=animation_frame ,interval = 1000)    #calling FuncAnimation Function
    plt.tight_layout()
    plt.show()  #showing the graph






