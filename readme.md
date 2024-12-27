# Salvar o conteúdo do README.md gerado como arquivo para download
readme_content = """
# Análise de Métricas de Modelos de Machine Learning

Este projeto visa analisar as métricas de desempenho de um modelo de machine learning, fornecendo ferramentas para calcular e visualizar os principais indicadores de qualidade de um modelo preditivo, como matriz de confusão, acurácia, sensibilidade (recall), precisão, F1-score e a curva ROC.

## Contexto
O modelo utilizado neste projeto foi treinado ao longo de 5 épocas, com os seguintes resultados observados:

| Época | Acurácia (Treinamento) | Acurácia (Validação) | Loss (Treinamento) | Loss (Validação) |
|-------|-------------------------|----------------------|--------------------|------------------|
| 1     | 0.9253                 | 0.9859              | 0.2427            | 0.0431           |
| 2     | 0.9884                 | 0.9881              | 0.0384            | 0.0355           |
| 3     | 0.9925                 | 0.9866              | 0.0240            | 0.0380           |
| 4     | 0.9944                 | 0.9886              | 0.0172            | 0.0369           |
| 5     | 0.9964                 | 0.9890              | 0.0107            | 0.0375           |

## Funcionalidades
- **Cálculo de Métricas:**
  - Matriz de Confusão
  - Acurácia
  - Sensibilidade (Recall)
  - Precisão
  - F1-Score

- **Visualização Gráfica:**
  - Geração da Curva ROC com a área sob a curva (AUC).

## Ambiente de Execução
O projeto foi desenvolvido utilizando o ambiente Google Colab, que oferece uma plataforma prática para análise de dados e execução de scripts Python. A biblioteca `scikit-learn` foi utilizada para os cálculos das métricas e geração da curva ROC.

## Como Utilizar
1. Substitua os valores em `y_true` e `y_pred` pelos dados reais do seu modelo.
2. Execute o script fornecido para obter:
   - Métricas quantitativas de desempenho.
   - Gráfico da curva ROC.

## Resultados Esperados
- Com base nos dados de entrada, espera-se que o script exiba as métricas de avaliação do modelo e a matriz de confusão no console.
- Um gráfico da curva ROC será gerado para visualizar o desempenho geral do modelo em termos de sensibilidade e especificidade.

## Bibliotecas Utilizadas
- NumPy
- Matplotlib
- Scikit-learn

## Exemplo de Uso
A matriz de confusão calculada para os dados de exemplo foi: [[4 1] [1 4]]


As métricas calculadas foram:
- Acurácia: 0.80
- Sensibilidade (Recall): 0.80
- Precisão: 0.80
- F1-Score: 0.80

O gráfico da curva ROC apresentou uma área sob a curva (AUC) de 0.82.


