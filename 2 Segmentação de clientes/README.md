# Projeto de Segmentação de Clientes
Este projeto tem como objetivo segmentar clientes com base em seu comportamento de compra. O conjunto de dados utilizado neste projeto é o dataset Online Retail, que contém dados transacionais de uma varejista online do Reino Unido de 2009 a 2011.

link par ao original: https://www.kaggle.com/datasets/lakshmi25npathi/online-retail-dataset

Esse projeto é parte do curso Ciência de Dados Impressionador, da Hashtag Treinamentos.

# Métodos e análises utilizadas
- foi feita a comparação dos resultados com e sem pré processamento
- a clusterização foi feita através do elbow method e silhouette method.

## Estrutura do repositório

O repositório está estruturado da seguinte forma:

```
├── dados
├── imagens
├── modelos
├── notebooks
├── reports
```

- Na pasta `dados` estão os dados utilizados no projeto. O arquivo `Mall_Customers.csv` é o dataset utilizado originalmente. Os demais arquivos são os datasets gerados durante o projeto.
- Na pasta `modelos` estão os modelos gerados durante o projeto. 
- Na pasta `notebooks` estão os notebooks com o desenvolvimento do projeto.

# Instalação
Para executar este projeto, é necessário ter o Python 3 instalado na sua máquina. Você pode instalar os pacotes necessários executando o seguinte comando:

pip install -r requirements.txt

Certifique-se de criar um ambiente virtual para evitar conflitos entre pacotes.

# Uso
Após instalar os pacotes necessários, você pode rodar o caderno principal - projeto_supermercado_05_pipeline_pca.ipynb - para começar a análise de segmentação. O script usará técnicas de aprendizado de máquina para classificar os clientes.

# Contribuição
Contribuições para melhorar este projeto são bem-vindas. Para contribuir, por favor:

Faça um fork do repositório.
Crie uma branch para sua nova funcionalidade (git checkout -b feature/nova-funcionalidade).
Commit suas mudanças (git commit -am 'Adicionar nova funcionalidade').
Push para a branch (git push origin feature/nova-funcionalidade).
Crie um Pull Request.

# Versões das bibliotecas usadas nesse projeto
-------------------- | ----------
     Biblioteca      |   Versão  
-------------------- | ----------
Matplotlib           |      3.8.2
NumPy                |     1.26.2
Pandas               |      2.1.2
Scikit-Learn         |      1.3.2
Seaborn              |     0.13.0

Versão do Python: 3.12.0