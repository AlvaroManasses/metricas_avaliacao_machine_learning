import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc

# Dados de exemplo (substitua pelos dados reais)
y_true = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
y_pred = [0, 1, 0, 0, 1, 0, 1, 1, 1, 0]

# Informações adicionais das épocas (substituídas pelas métricas do modelo treinado)
epochs_info = [
    {"epoch": 1, "accuracy": 0.9253, "val_accuracy": 0.9859, "loss": 0.2427, "val_loss": 0.0431},
    {"epoch": 2, "accuracy": 0.9884, "val_accuracy": 0.9881, "loss": 0.0384, "val_loss": 0.0355},
    {"epoch": 3, "accuracy": 0.9925, "val_accuracy": 0.9866, "loss": 0.0240, "val_loss": 0.0380},
    {"epoch": 4, "accuracy": 0.9944, "val_accuracy": 0.9886, "loss": 0.0172, "val_loss": 0.0369},
    {"epoch": 5, "accuracy": 0.9964, "val_accuracy": 0.9890, "loss": 0.0107, "val_loss": 0.0375}
]

# Cálculo da matriz de confusão
con_mat = confusion_matrix(y_true, y_pred)
print("Matriz de Confusão:\n", con_mat)

# Cálculo das métricas
tn, fp, fn, tp = con_mat.ravel()
accuracy = accuracy_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

# Exibição das métricas
print(f"Acurácia: {accuracy:.2f}")
print(f"Sensibilidade (Recall): {recall:.2f}")
print(f"Precisão: {precision:.2f}")
print(f"F1-Score: {f1:.2f}")

# Exibir informações das épocas
for info in epochs_info:
    print(f"Época {info['epoch']}: Acurácia Treinamento = {info['accuracy']:.4f}, Validação = {info['val_accuracy']:.4f}, Loss Treinamento = {info['loss']:.4f}, Validação = {info['val_loss']:.4f}")

# Curva ROC
fpr, tpr, thresholds = roc_curve(y_true, y_pred)
roc_auc = auc(fpr, tpr)

# Plot da curva ROC
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Curva ROC (área = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('Taxa de Falsos Positivos')
plt.ylabel('Taxa de Verdadeiros Positivos')
plt.title('Curva ROC')
plt.legend(loc='lower right')
plt.show()
