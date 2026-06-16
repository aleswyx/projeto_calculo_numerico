# Projeto de Cálculo Numérico - Unidade 2

Este repositório contém o desenvolvimento de um pacote computacional de métodos numéricos construído do zero, utilizando apenas estruturas de dados e lógicas nativas da linguagem Python (sem o uso de bibliotecas externas como `numpy` ou `scipy`).

## 👥 Integrantes
* Alessandro Franca Ramos
* Eduardo Di Minda Pereira Machado Chagas Oliveira

---

## 📁 Estrutura do Repositório

O projeto está organizado em módulos específicos para cada categoria de problema analítico estudado em aula:

```text
projeto_calculo_numerico/
│
├── ajuste_de_curva/
│   └── ajuste_de_curva_mmq.py              # Previsão de tráfego do DEINF/UFMA (Slide 9)
│
├── integracao/
│   ├── integracao_numerica_formula_de...   # Trabalho total via Quadratura de Gauss (Slide 12)
│   ├── integracao_numerica_newton_cot...   # Taxa de transferência via Regra 3/8 de Simpson (Slide 10)
│   └── integracao_numerica_trapezios_...   # Distância do Carro Elétrico (Trapézios e 1/3) (Slide 11)
│
├── interpolacao/
│   ├── interpolacao_gregory_newton.py      # Resfriamento do Data Center (Slide 7)
│   ├── interpolacao_lagrange.py            # Telemetria do Drone (Slide 6)
│   ├── interpolacao_newton.py              # Telemetria do Drone via Diferenças Divididas (Slide 6)
│   └── interpolacao_splines_linear_cubica.py # Trajetória do Braço Robótico (Slide 8)
│
└── metodos_diretos.py                      # Abordagem de Interpolação via Matriz de Vandermonde

---

## 🚀 Como Executar os Módulos

Cada algoritmo possui um bloco de execução isolado (`if __name__ == "__main__":`) ao final do arquivo, configurado com os respectivos conjuntos de dados práticos fornecidos no PDF da avaliação.

Para testar qualquer método, abra o terminal na pasta raiz do projeto e execute o comando correspondente utilizando o interpretador padrão do Python:

### Módulo de Interpolação
```bash
python interpolacao/interpolacao_lagrange.py
python interpolacao/interpolacao_newton.py
python interpolacao/interpolacao_gregory_newton.py
python interpolacao/interpolacao_splines_linear_cubica.py

python integracao/integracao_numerica_newton_cotes_FQNC.py
python integracao/integracao_numerica_trapezios_e_simpson.py
python integracao/integracao_numerica_formula_de_quadratura_gauss.py

python ajuste_de_curva/ajuste_de_curva_mmq.py

python metodos_diretos.py

