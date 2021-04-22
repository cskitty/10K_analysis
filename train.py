from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

df = pd.read_csv('training.csv', sep = ',')

# Separating out the features
features = ['w{}'.format(i) for i in range(105)]
x = df.loc[:, features].values

# Standardizing the features
x = StandardScaler().fit_transform(x)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(x)

pca_df = pd.DataFrame(data = pca_result, columns = ['pc1', 'pc2', 'pc3'])
print(pca_df.head())
