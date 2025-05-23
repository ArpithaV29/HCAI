'''from django.http import HttpResponse
from django.shortcuts import render
from .forms import CSVUploadForm
import pandas as pd
import matplotlib.pyplot as plt
import os
from django.conf import settings

#def index(request):
    #return HttpResponse("Project 1 by Arpitha and Manvitha")


def upload_and_visualize(request):
    plot_url = None
    error = None

    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                csv_file = request.FILES['file']
                df = pd.read_csv(csv_file)

                # Plot: scatter plot of first 2 columns
                x_col, y_col = df.columns[:2]
                plt.figure()
                df.plot(kind='scatter', x=x_col, y=y_col)
                plt.title(f'{x_col} vs {y_col}')

                # Save plot
                plot_path = os.path.join(settings.MEDIA_ROOT, "plot.png")
                plt.savefig(plot_path)
                plt.close()

                plot_url = settings.MEDIA_URL + "plot.png"

            except Exception as e:
                error = str(e)
    else:
        form = CSVUploadForm()

    return render(request, 'project1/upload.html', {
        'form': form,
        'plot_url': plot_url,
        'error': error
    })'''

from django.shortcuts import render
from .forms import CSVUploadForm
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import os
from django.conf import settings

def upload_and_train(request):
    plot_url = None
    accuracy = None
    error = None

    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                csv_file = request.FILES['file']
                df = pd.read_csv(csv_file)

                # Assume the last column is the target
                X = df.iloc[:, :-1]
                y = df.iloc[:, -1]

                # Split the data
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

                # Train a Decision Tree
                model = DecisionTreeClassifier()
                model.fit(X_train, y_train)

                   # Predict and evaluate
                y_pred = model.predict(X_test)
                accuracy = accuracy_score(y_test, y_pred)

                # Plot the first two features
                x_col, y_col = X.columns[:2]
                plt.figure()
                df.plot(kind='scatter', x=x_col, y=y_col, c=y.map({'setosa': 0, 'versicolor': 1, 'virginica': 2}), cmap='viridis')
                plt.title(f'{x_col} vs {y_col}')

                plot_path = os.path.join(settings.MEDIA_ROOT, "train_plot.png")
                plt.savefig(plot_path)
                plt.close()

                plot_url = settings.MEDIA_URL + "train_plot.png"

            except Exception as e:
                error = str(e)
    else:
        form = CSVUploadForm()

    return render(request, 'project1/train.html', {
        'form': form,
        'plot_url': plot_url,
        'accuracy': round(accuracy * 100, 2) if accuracy else None,
        'error': error
    })


