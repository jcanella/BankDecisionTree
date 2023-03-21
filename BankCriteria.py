import pandas as pd
import numpy as np
from sklearn import tree, metrics
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from scipy.io import arff

def bank():
    data, meta = arff.loadarff('./bank.arff')

    df = pd.DataFrame(data)

    # Convert binary features to 0/1
    binary_features = ['default', 'housing', 'loan', 'subscribed']
    for feature in binary_features:
        df[feature] = df[feature].apply(lambda x: 1 if x == b'yes' else 0)

    # Convert categorical features to numerical using one-hot encoding
    categorical_features = ['job', 'marital', 'education', 'contact', 'month', 'poutcome']
    df = pd.get_dummies(df, columns=categorical_features)

    # Define feature matrix and target vector
    X = df.drop(['subscribed'], axis=1)
    y = df['subscribed']

    # Fit decision tree classifier and plot the tree
    dtc = DecisionTreeClassifier(criterion='entropy')
    dtc.fit(X, y)

    plt.figure(figsize=(30, 20))
    tree.plot_tree(dtc, feature_names=X.columns, class_names=['No', 'Yes'], filled=True, rounded=True)
    plt.show()

    # Plot confusion matrix
    fig, ax = plt.subplots(figsize=(10, 10))
    metrics.plot_confusion_matrix(dtc, X, y, display_labels=['No', 'Yes'], values_format='d', ax=ax)
    plt.show()

bank()
