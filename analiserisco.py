import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definindo as variáveis de entrada (inputs)
hist_credito = ctrl.Antecedent(np.arange(0, 11, 1), 'hist_credito')
renda_mensal = ctrl.Antecedent(np.arange(0, 11, 1), 'renda_mensal')
divida_atual = ctrl.Antecedent(np.arange(0, 11, 1), 'divida_atual')

# Definindo a variável de saída (output)
risco = ctrl.Consequent(np.arange(0, 11, 1), 'risco')

