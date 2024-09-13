import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definindo as variáveis de entrada (inputs)
hist_credito = ctrl.Antecedent(np.arange(0, 11, 1), 'hist_credito')
renda_mensal = ctrl.Antecedent(np.arange(0, 11, 1), 'renda_mensal')
divida_atual = ctrl.Antecedent(np.arange(0, 11, 1), 'divida_atual')

# Definindo a variável de saída (output)
risco = ctrl.Consequent(np.arange(0, 11, 1), 'risco')

# Funções de pertinência para histórico de crédito
hist_credito['ruim'] = fuzz.trimf(hist_credito.universe, [0, 0, 4])
hist_credito['regular'] = fuzz.trimf(hist_credito.universe, [3, 5, 7])
hist_credito['bom'] = fuzz.trimf(hist_credito.universe, [6, 8, 10])
hist_credito['excelente'] = fuzz.trimf(hist_credito.universe, [8, 10, 10])

# Funções de pertinência para renda mensal
renda_mensal['baixa'] = fuzz.trimf(renda_mensal.universe, [0, 0, 4])
renda_mensal['media'] = fuzz.trimf(renda_mensal.universe, [3, 5, 7])
renda_mensal['alta'] = fuzz.trimf(renda_mensal.universe, [6, 10, 10])

# Funções de pertinência para dívida atual
divida_atual['baixa'] = fuzz.trimf(divida_atual.universe, [0, 0, 4])
divida_atual['moderada'] = fuzz.trimf(divida_atual.universe, [3, 5, 7])
divida_atual['alta'] = fuzz.trimf(divida_atual.universe, [6, 10, 10])
