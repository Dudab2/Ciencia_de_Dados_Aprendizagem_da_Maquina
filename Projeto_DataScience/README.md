# Adesão à medicação em idosos

Projeto da disciplina **Ciência de Dados e Aprendizagem de Máquina**, feito seguindo o modelo **CRISP-DM**.

**Dashboard:** [abrir o dashboard](https://dudab2.github.io/Ciencia_de_Dados_Aprendizagem_da_Maquina/Projeto_DataScience/docs/)
Os dados usados são **sintéticos** (não são de pessoas reais) e foram criados para fins didáticos.

## Perguntas do projeto

1. **Que porcentagem dos idosos esquece de tomar doses?**
2. **Quais características aumentam o risco de baixa adesão?**

Definição usada: *baixa adesão* = esquecer **20% ou mais** das doses prescritas na semana.

## Resultados

Base: 1.479 idosos após a limpeza.

**Pergunta 1**
- 73,2% esquecem pelo menos uma dose por semana.
- 7,5% têm baixa adesão.
- Em média, 7,7% das doses prescritas são esquecidas.
- A noite é o horário mais esquecido (43,8% dos que esquecem).

**Pergunta 2**
- Baixa adesão por número de fatores de risco (morar sozinho, não ter cuidador, ter comprometimento cognitivo): 0 fatores = 0,6%; 1 = 2,6%; 2 = 15,9%; 3 = 55,7%.
- Maiores taxas: comprometimento cognitivo moderado (30,6%), morar sozinho (20,1%), 80 anos ou mais (17,1%) e 7 ou mais medicamentos (20,3%).
- Cuidador (2,3% contra 12,3% sem) e alarme (2,2% contra 10,2% sem) aparecem como proteção.
- Escolaridade e sexo quase não mudam o resultado.

**Modelo (regressão logística, 70% treino / 30% teste)**
- AUC no teste: 0,92.
- Recall de baixa adesão: 0,79. Precisão: 0,28, ou seja, o modelo encontra a maioria dos casos de risco, mas gera muitos alarmes falsos.
- Fatores que mais aumentam o risco: comprometimento moderado, morar sozinho e idade. Alarme e cuidador reduzem.

## CRISP-DM

| Fase | O que foi feito |
|---|---|
| 1. Entendimento do negócio | Reduzir o esquecimento de doses; identificar quem tem baixa adesão e por quê |
| 2. Entendimento dos dados | 1.545 linhas e 14 colunas; 45 duplicatas, categorias inconsistentes, idades impossíveis, datas em dois formatos |
| 3. Preparação | `src/limpeza_dados.py`: padronização, idades por extenso convertidas, valores fora de faixa tratados como ausentes, 21 registros incoerentes removidos, criação da taxa de esquecimento |
| 4. Modelagem | `src/modelo.py`: regressão logística simples |
| 5. Avaliação | AUC, recall e precisão para a classe de baixa adesão |
| 6. Implantação | Dashboard em `docs/index.html` |

## Fonte dos dados

Base `idosos_medicacao.csv` (1.545 registros **sintéticos**, criados para fins didáticos), usada na disciplina Ciência de Dados e Aprendizagem de Máquina. Método: Guia Prático CRISP-DM da disciplina (Profa. Kadidja Valéria).

## Limitações

- Os dados são sintéticos, então os resultados valem só para este exercício e não são evidência clínica.
- Cognição, idade e número de medicamentos andam juntos, e as comparações simples não separam esses efeitos.
- O limite de 20% para baixa adesão é uma escolha do projeto.

## Como rodar

```bash
pip install -r requirements.txt
python src/limpeza_dados.py   # gera data/processed/idosos_medicacao_limpo.csv
python src/modelo.py          # treina e avalia o modelo
```

## Estrutura

```
data/raw/            base original
data/processed/      base limpa
src/                 limpeza e modelo
docs/index.html      dashboard
```
