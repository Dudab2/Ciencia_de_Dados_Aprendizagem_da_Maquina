<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Aula 1 — Conceitos e classificação de problemas

## Identificação

- Estudante ou equipe: **Maria Eduarda Gonaçalves Rodrigues**
- Turma: **Ciência de Dados e Aprendizagem de Máquina**
- Data de realização: **28/10/2026**
- Integrantes e contribuições (se em equipe): **PREENCHER**

## Objetivos

Distinguir programação tradicional e Machine Learning, identificar atributos e alvo e diferenciar classificação, regressão e agrupamento.

## 1. Explicação com suas palavras

1. **Como um modelo aprende com dados?**  
   Um modelo aprende analisando dados e identificando padrões e relações entre as informações. Durante o treinamento, ele ajusta seus parâmetros para melhorar os resultados e, depois, pode utilizar o que aprendeu para fazer previsões sobre novos dados.

2. **Qual diferença entre algoritmo e modelo?**  
   O algoritmo é o método utilizado para aprender com os dados. O modelo é o resultado desse aprendizado, que pode ser utilizado para fazer previsões ou identificar padrões.

3. **Compare uma regra de bloqueio de palavra com um modelo de spam.**  
   Uma regra de bloqueio identifica mensagens por uma condição definida manualmente, como a presença de determinada palavra. Já um modelo de spam aprende com exemplos de mensagens classificadas como spam ou legítimas e utiliza os padrões encontrados para analisar novas mensagens.

4. **Dê um exemplo de atributo e alvo e defina o momento da previsão.**  
   Em um sistema que prevê a evasão escolar, os atributos podem ser frequência, notas e quantidade de atividades entregues. O alvo é a situação do estudante, como evadiu ou permaneceu. A previsão acontece quando o modelo recebe os dados de um estudante e estima sua situação, antes de o resultado real ser conhecido.

## 2. Quadro comparativo

| Critério | Supervisionado | Não supervisionado |
| --- | --- | --- |
| Presença de alvo no treino | Possui um alvo conhecido nos dados de treinamento. | Não possui um alvo previamente definido. |
| Pergunta que pode responder | Qual será a categoria ou o valor previsto? | Quais padrões ou grupos existem nos dados? |
| Tipo de saída | Categorias ou valores numéricos. | Grupos, padrões ou estruturas encontradas. |
| Tarefas e exemplo | Classificação de spam e previsão de vendas. | Agrupamento de clientes por comportamento de compra. |
| Dados necessários | Dados com exemplos e resultados conhecidos. | Dados sem rótulos previamente definidos. |
| Forma de avaliação | Comparação das previsões com os resultados reais. | Análise da qualidade dos grupos e da utilidade dos padrões encontrados. |
| Limitação | Depende da qualidade dos rótulos e pode reproduzir vieses dos dados. | Os grupos encontrados podem ser difíceis de interpretar e não representar categorias úteis. |

## 3. Situações-problema

Os casos escolhidos são 1, 2, 3, 4 e 5, contemplando classificação, regressão e agrupamento.

| Caso escolhido | Alvo ou ausência de alvo | Categoria, quantidade ou grupos? | Abordagem e justificativa | Dados necessários e limitação |
| --- | --- | --- | --- | --- |
| 1 — Educação | Alvo: evadiu ou permaneceu. | Categoria. | Aprendizado supervisionado, pois existem resultados conhecidos de turmas anteriores. É um problema de classificação. | Histórico de notas, frequência e situação final dos estudantes. Pode haver dados incompletos e fatores externos que influenciam a evasão. |
| 2 — Saúde | Alvo: tempo de espera em minutos. | Quantidade numérica. | Aprendizado supervisionado, pois o modelo utiliza tempos de espera registrados para estimar novos valores. É um problema de regressão. | Horários de chegada, início do atendimento, prioridade e quantidade de pacientes. A demanda pode variar inesperadamente. |
| 3 — Comércio | Não existe alvo previamente definido. | Grupos de clientes. | Aprendizado não supervisionado, pois busca identificar perfis semelhantes de compra sem categorias predefinidas. É um problema de agrupamento. | Histórico de compras, frequência, valores gastos e produtos adquiridos. Os grupos dependem dos dados e dos critérios utilizados. |
| 4 — Finanças | Alvo: inadimplente ou adimplente. | Categoria. | Aprendizado supervisionado, pois utiliza contratos com desfechos conhecidos para classificar novos casos. | Histórico de pagamentos, valores contratados e prazos. Os dados podem conter vieses e não garantem o comportamento futuro. |
| 5 — Segurança digital | Alvo: spam ou legítima. | Categoria. | Aprendizado supervisionado, pois aprende com mensagens previamente revisadas e classificadas. É um problema de classificação. | Texto das mensagens e rótulos corretos. Novas técnicas de spam podem reduzir a precisão do modelo. |

## 4. Raciocínio crítico

Detectar fraude não define sozinho o tipo de aprendizado utilizado. Quando existem exemplos anteriores identificados como fraudulentos ou legítimos, pode-se utilizar o aprendizado supervisionado para aprender os padrões dessas operações e classificar novas transações.

Por outro lado, quando não existem rótulos, pode-se utilizar o aprendizado não supervisionado para identificar operações que apresentam comportamentos diferentes do padrão habitual. Essas operações podem ser consideradas suspeitas, mas nem todas são necessariamente fraudes.

Portanto, a escolha da abordagem depende dos dados disponíveis e do objetivo do sistema. O aprendizado supervisionado utiliza resultados conhecidos, enquanto o não supervisionado busca padrões sem depender de categorias previamente definidas.

## Entrega

Antes de entregar, preencha os campos de identificação que faltam e confira se a professora solicitou algum formato específico de arquivo.

[Voltar ao início](README.md)
