import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster._bicluster import SpectralCoclustering

whiskies_file_name = "C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Whiskey Classification/whiskies.txt"
whiskies = pd.read_csv(whiskies_file_name)

regions_file_name = "C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Whiskey Classification/regions.txt"
whiskies["Region"] = pd.read_csv(regions_file_name)

flavors = whiskies.iloc[:, 2:14]
flavors_correlation = flavors.corr()

plt.figure(figsize = (10, 10))
plt.pcolor(flavors_correlation)
plt.colorbar()
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Whiskey Classification/flavors_correlation.pdf")
plt.show()

transposed_flavors_correlation = flavors.transpose().corr()

plt.figure(figsize = (10, 10))
plt.pcolor(transposed_flavors_correlation)
plt.colorbar()
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Whiskey Classification/transposed_flavors_correlation.pdf")
plt.show()

model = SpectralCoclustering(n_clusters = 6, random_state = 0)
model.fit(transposed_flavors_correlation)

whiskies["Group"] = pd.Series(model.row_labels_, index = whiskies.index)
whiskies = whiskies.loc[np.argsort(model.row_labels_)]
whiskies = whiskies.reset_index(drop = True)

correlations = whiskies.iloc[:, 2:14].transpose().corr()
correlations = np.array(correlations)

plt.figure(figsize = (14, 7))
plt.subplot(121)
plt.pcolor(transposed_flavors_correlation)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")
plt.savefig("C:/Users/DS/Desktop/Python/Harvard Using Python for Research Course/Week 4/Whiskey Classification/correlations.pdf")
plt.show()