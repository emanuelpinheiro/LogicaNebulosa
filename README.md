# LogicaNebulosa - Emanuel Pinheiro
 
# Sistema de Análise de Risco do Banco

Este projeto implementa um sistema de análise de risco para clientes de um banco utilizando Lógica Fuzzy com a biblioteca `scikit-fuzzy`. O sistema avalia três variáveis de entrada: **Histórico de Crédito**, **Renda Mensal** e **Dívida Atual**, e determina o nível de risco de crédito (Baixo, Médio, Alto).

## Instalação

Certifique-se de ter o Python e o VSCode instalado e abra o projeto no VSCode. Execute o seguinte comando para iniciar o VSCode em um ambiente virtual:

venv\Scripts\Activate

Caso apareça que não existe algum ambiente virtual, execute esse código e tente novamente:

python -m venv venv

Depois instale as dependências (um comando de cada vez): 
pip install numpy

pip install scikit-fuzzy

E finalmente execute a aplicação:
python analiserisco.py
