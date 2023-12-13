import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Função para plotar gráficos de cotovelo e silhueta
def elbow_silhouette_graphs(X, random_state=42, intervalo_k = (2, 11)):

    fig, axs = plt.subplots(nrows = 1, ncols = 2, figsize=(15, 5), tight_layout=True)

    elbow = {}
    silhouette = []
    
    k_range = range(*intervalo_k)
    
    for i in k_range:
        kmeans = KMeans(n_clusters=i, random_state=random_state, n_init=10)
        kmeans.fit(X)
        elbow[i] = kmeans.inertia_

        labels = kmeans.labels_
        silhouette.append(silhouette_score(X, labels))

    sns.lineplot(x=list(elbow.keys()), y=list(elbow.values()), ax=axs[0])
    axs[0].set_xlabel('k')
    axs[0].set_ylabel('Inertia')
    axs[0].set_title('Elbow Method')

    sns.lineplot(x=list(k_range), y=silhouette, ax=axs[1])
    axs[1].set_xlabel('k')
    axs[1].set_ylabel('Silhouette Score')
    axs[1].set_title('Silhouette Method')

    plt.show()
