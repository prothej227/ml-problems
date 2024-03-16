from tensorflow.keras.models import load_model
from typing import Any
from numpy import ravel
from pandas import DataFrame
import pickle
import argparse
import os

def __dependency_load(base_path : str) -> Any:
    mdl = load_model(base_path + "model.h5")
    with open(base_path + "ct.pickle", "rb") as f:
        ct = pickle.load(f)
    return mdl, ct
    
def main(model, ct, **kwargs) -> None:
    arr_input = []
    print("\nInput features:")
    for k, v in kwargs.items():
        if v is not None: 
            v = int(v) if v.isdigit() else None
            arr_input.append(v)
            print(f"{k} -> {v}")
        else:
            print(f"Missing args: {k}")
    
    if len(arr_input) == 4:

        input_data = DataFrame(
            [arr_input],
            columns=['size_ft', 'bedroom', 'bathroom', 'age_yr']
        )
        normal_data = ct.transform(input_data)
        print(f"\n\nPredicted Price: {ravel(model.predict(normal_data))}")
        
    else:
        print("Missing required inputs")

if __name__ == '__main__':

    mdl, ct = __dependency_load("models/house_price_predictor/")
    
    prsr = argparse.ArgumentParser()
    prsr.add_argument("-s", help="size in feet.")
    prsr.add_argument("-r", help="no. of bedrooms.")
    prsr.add_argument("-b", help="no. of bathrooms.")
    prsr.add_argument("-a", help="age in years.")
    
    args = prsr.parse_args()
    
    # Convert namespace object to dictionary
    args_dict = vars(args)
    main(model=mdl, ct=ct, **args_dict)