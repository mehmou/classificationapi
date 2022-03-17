from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
import json
import os
import numpy as np
import pickle

# Read in data
X_train = np.genfromtxt("data/train_features.csv")
y_train = np.genfromtxt("data/train_labels.csv")
X_test = np.genfromtxt("data/test_features.csv")
y_test = np.genfromtxt("data/test_labels.csv")

# Fit a model
depth = 5
clf = RandomForestClassifier(max_depth=depth)
clf.fit(X_train, y_train)

acc = clf.score(X_test, y_test) 
print(acc)
with open("metrics.txt", "w") as outfile:
    outfile.write("Accuracy: " + str(acc) + "\n")

model_dir = 'models'
model_name = 'model.pkl'

# Save it
if not os.path.isdir(model_dir):
    os.mkdir(model_dir)

pickle.dump(clf, open(os.path.join(model_dir, model_name), 'wb'))

# Plot it
disp = plot_confusion_matrix(clf, X_test, y_test, normalize="true", cmap=plt.cm.Blues)
plt.savefig("plot.png")