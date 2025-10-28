#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    temp=pd.read_csv("src/kumpula-weather-2017.csv")
    # print(temp.head())
    # print(temp.columns)
    july= temp["m"]==7
    temp2= temp[july]["Air temperature (degC)"].mean()
    return temp2
def main():
    
    result = average_temperature()
    print(f"Average temperature in July: {result}")
    # print(f"Average temperature in July: {result:.1f}")
    
if __name__ == "__main__":
    main()
