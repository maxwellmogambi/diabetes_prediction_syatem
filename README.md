# Diabetes Prediction Hub

This repository contains the code for a Diabetes Prediction model hosted on a Django application. 

## Project Overview

The Diabetes Prediction Hub leverages machine learning models to predict the likelihood of a patient having diabetes based on various medical attributes. The Django application provides an interface for users to input their data and get predictions.

## Models Used
- Decision Trees
- Random Forests
- K-Nearest Neighbors (KNN)
- Voting Classifier
- Gradient Boosting
- Bagging Classifier

The Bagging Classifier achieved the highest accuracy in our tests.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/maxwellmogambi/diabetes-prediction-hub.git
   cd diabetes-prediction-hub
   ```

2. Create and activate a virtual environment:   
   ```bash
   python -m venv env
   source env/bin/activate # On Windows use `env\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

## Usage

Open your browser and navigate to http://127.0.0.1:8000/ to access the application. Enter the required medical attributes to get a diabetes prediction.

## Future Work

Further improvements can be made by:

* Exploring more advanced feature engineering techniques.
* Trying out other ensemble methods like Stacking.
* Incorporating deep learning models for better accuracy.

## Author

Maxwell Mogambi [linkendIn](https://www.linkedin.com/in/maxwell-mogambi/) <br>
Norman Munguti  [email](normanmunguti@gmail.com)

## Licence

This project is licensed under the MIT License - see the LICENSE file for details.


