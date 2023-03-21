<h1>Bank Marketing Campaign - Decision Tree Classifier</h1>
<p>Neste código, utilizamos as bibliotecas Pandas e Scikit-learn para treinar um classificador de árvore de decisão que prevê se um cliente fará uma subscrição em um produto bancário. Utilizamos o conjunto de dados "bank.arff", que contém informações sobre clientes que foram ou não contatados em uma campanha de marketing anterior.</p>
<p>O código segue os seguintes passos:</p>
<ol>
    <li>Carregamos o arquivo "bank.arff" e criamos um dataframe com Pandas.</li>
    <li>Convertemos as variáveis binárias 'default', 'housing', 'loan' e 'subscribed' em 0 ou 1.</li>
    <li>Convertemos as variáveis categóricas restantes em variáveis numéricas utilizando a codificação one-hot encoding.</li>
    <li>Separamos o conjunto de dados em matriz de características (X) e vetor de destino (y).</li>
    <li>Treinamos um classificador de árvore de decisão com o critério de entropia e ajustamos a matriz de características e o vetor de destino.</li>
    <li>Plotamos a árvore de decisão treinada.</li>
    <li>Plotamos uma matriz de confusão para avaliar a precisão do modelo treinado.</li>
</ol>
<p>A árvore de decisão gerada e a matriz de confusão fornecem uma visualização do processo de tomada de decisão do modelo e avaliação da sua precisão.</p>