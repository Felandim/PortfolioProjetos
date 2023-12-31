import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from matplotlib.colors import ListedColormap

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

def visualizar_clusters(
        dataframe,
        colunas,
        quantidade_de_cores,
        centroids,
        mostrar_centroides=True,
        mostrar_pontos=False,
        coluna_clusters=None):

    # pegar as 5 primeiras cores da palette tab10
    cores = plt.cm.tab10.colors[:quantidade_de_cores]
    cores = ListedColormap(cores)

    # declarar a figura
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')
    
    # declarar o que é cada valor de variável
    x = dataframe[colunas[0]]
    y = dataframe[colunas[1]]
    z = dataframe[colunas[2]]
    
    # criar uma função para mostrar os centroides
    ligar_centroides = mostrar_centroides
    ligar_pontos = mostrar_pontos


    for i, centroid in enumerate(centroids):
        if ligar_centroides:
            # fazer o unpacking do array
            # argumento s=500 indica o tamanho do marcador
            # argumento alpha indica a opacidade
            ax.scatter(*centroid, s=500, alpha = 0.5)

            # adicionar o número de cada cluster
            # adicionar argumentos para deixar o número dentro do marcador e centralizado
            ax.text(*centroid, f'{i}', fontsize=20, horizontalalignment='center', verticalalignment='center')

        if ligar_pontos:
            # colocar os pontos de dispersão
            # formatar para deixar as cores iguais ao centróide
            s = ax.scatter(x, y, z, c = coluna_clusters, cmap=cores)
            ax.legend(*s.legend_elements(), bbox_to_anchor=(1.1, 1), loc='upper left')

    ax.set_xlabel(colunas[0])
    ax.set_ylabel(colunas[1])
    ax.set_xlabel(colunas[2])
    
    # mostrar a figura
    plt.show()