from django.shortcuts import render
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.ensemble import BaggingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import os

# Create your views here.
def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    if request.method == 'POST':
        # Use relative path to access the dataset
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, 'data', 'diabetes.csv')

        # Load the dataset
        df = pd.read_csv(file_path)
        X = df.drop('Outcome', axis=1)
        y = df['Outcome']

        # Standardize the data
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Initialize the base estimator
        dt = DecisionTreeClassifier(min_samples_split=2, min_samples_leaf=10, max_depth=50, criterion='entropy')

        # Initialize the BaggingClassifier
        bc = BaggingClassifier(estimator=dt, n_estimators=300, random_state=42)

        # Fit the model
        bc.fit(X_scaled, y)

        # Get values from the request
        val1 = float(request.POST.get('n1', 0))
        val2 = float(request.POST.get('n2', 0))
        val3 = float(request.POST.get('n3', 0))
        val4 = float(request.POST.get('n4', 0))
        val5 = float(request.POST.get('n5', 0))
        val6 = float(request.POST.get('n6', 0))
        val7 = float(request.POST.get('n7', 0))
        val8 = float(request.POST.get('n8', 0))

        # Scale the input values
        input_data = scaler.transform([[val1, val2, val3, val4, val5, val6, val7, val8]])

        # Predict using the trained model
        prediction = bc.predict(input_data)

        # Determine the result
        result1 = "Positive" if prediction == 1 else "Negative"

        # Render the result
        return render(request, 'predict.html', {"result2": result1})
    else:
        # Handle GET request or other cases
        return render(request, 'predict.html')
