# House Price Prediction Tool

This tool allows you to predict house prices based on the size of the house, number of bedrooms, number of bathrooms, and the age of the house. It utilizes a machine learning model trained on historical house price data.

## Installation

You can install the required dependencies using pip with the following command:

```
pip install -r requirements.txt
```

This will install all the necessary Python packages specified in the `requirements.txt` file.

## Usage

To use the House Price Prediction Tool, follow these steps:

1. Ensure that you have installed all the dependencies by running the installation command mentioned above.

2. Run the `predict.py` script with the desired input parameters:

```
python predict.py -s <room_size> -r <no_of_bedrooms> -b <no_of_bathrooms> -a <age_in_years>
```

Replace `<room_size>`, `<no_of_bedrooms>`, `<no_of_bathrooms>`, and `<age_in_years>` with the respective values for the house you want to predict the price for.

3. The tool will output the predicted price of the house based on the provided input parameters.

## Example

Here's an example of how to use the tool:

```
python predict.py -s 2000 -r 3 -b 2 -a 10
```

This command will predict the price of a house with a size of 2000 square feet, 3 bedrooms, 2 bathrooms, and an age of 10 years.
