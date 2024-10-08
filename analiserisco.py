import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definindo as variáveis de entrada (inputs)
hist_credito = ctrl.Antecedent(np.arange(0, 11, 1), 'hist_credito')
renda_mensal = ctrl.Antecedent(np.arange(0, 11, 1), 'renda_mensal')
divida_atual = ctrl.Antecedent(np.arange(0, 11, 1), 'divida_atual')

# Definindo a variável de saída (output)
risco = ctrl.Consequent(np.arange(0, 11, 1), 'risco')

# Funções de pertinência para histórico de crédito (ajuste nas sobreposições)
hist_credito['ruim'] = fuzz.trimf(hist_credito.universe, [0, 0, 4])
hist_credito['regular'] = fuzz.trimf(hist_credito.universe, [2, 5, 8])
hist_credito['bom'] = fuzz.trimf(hist_credito.universe, [6, 8, 10])
hist_credito['excelente'] = fuzz.trimf(hist_credito.universe, [8, 10, 10])

# Funções de pertinência para renda mensal (ajuste nas sobreposições)
renda_mensal['baixa'] = fuzz.trimf(renda_mensal.universe, [0, 0, 4])
renda_mensal['media'] = fuzz.trimf(renda_mensal.universe, [2, 5, 8])
renda_mensal['alta'] = fuzz.trimf(renda_mensal.universe, [6, 10, 10])

# Funções de pertinência para dívida atual (ajuste nas sobreposições)
divida_atual['baixa'] = fuzz.trimf(divida_atual.universe, [0, 0, 4])
divida_atual['moderada'] = fuzz.trimf(divida_atual.universe, [2, 5, 8])
divida_atual['alta'] = fuzz.trimf(divida_atual.universe, [6, 10, 10])

# Funções de pertinência para risco
risco['baixo'] = fuzz.trimf(risco.universe, [0, 0, 4])
risco['medio'] = fuzz.trimf(risco.universe, [3, 5, 7])
risco['alto'] = fuzz.trimf(risco.universe, [6, 10, 10])

# Definindo as regras fuzzy
regra1 = ctrl.Rule(hist_credito['excelente'] & divida_atual['baixa'], risco['baixo'])
regra2 = ctrl.Rule(hist_credito['ruim'] & divida_atual['alta'], risco['alto'])
regra3 = ctrl.Rule(hist_credito['bom'] & renda_mensal['media'] & divida_atual['moderada'], risco['medio'])
regra4 = ctrl.Rule(hist_credito['regular'] & divida_atual['moderada'], risco['medio'])
regra5 = ctrl.Rule(hist_credito['regular'] & divida_atual['alta'], risco['alto'])

# Criando o sistema de controle
controle_risco = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5])
simulacao_risco = ctrl.ControlSystemSimulation(controle_risco)

# Teste do sistema com valores ajustados para ativar as regras
simulacao_risco.input['hist_credito'] = 7  # Bom
simulacao_risco.input['renda_mensal'] = 6  # Média-alta
simulacao_risco.input['divida_atual'] = 4  # Moderada

# Computando o resultado
simulacao_risco.compute()

# Verificando todas as variáveis de saída disponíveis
print(f"Variáveis de saída disponíveis: {simulacao_risco.output}")

# Exibindo o resultado, caso a variável 'risco' esteja presente
if 'risco' in simulacao_risco.output:
    print(f"Risco calculado: {simulacao_risco.output['risco']:.2f}")
else:
    print("Erro: A variável 'risco' não foi calculada corretamente.")
