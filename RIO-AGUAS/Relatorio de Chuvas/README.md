# **Relatório de Chuvas Intensas Automatizado**

## **Objetivos**

Este projeto tem como objetivo gerar um relatório de chuvas automatizado visando auxiliar, em tempo real, os tomadores de decisões e registrar o histórico de eventos hidrológicos extremos.  

## **Descrição da Solução**

A solução consiste em gerar um relatório automatizado com dados em tempo real em formato web com dashboards contendo análises estatísticas e comparativas de um evento chuvoso com a possibilidade de inserção de texto e exportação em formato PDF. Caso alguma estação pluviométrica registre precipitação que atingiu algum índice, conforme tabela abaixo, será disparado um email para os autores com instruções/link de acesso ao relatório.

|     Duração (min)    |     Precipitação (mm)    |
|----------------------|--------------------------|
|     15               |     15                   |
|     30               |     25                   |
|     45               |     35                   |
|     60               |     40                   |
|     90               |     46                   |
|     120              |     51                   |

## **Parâmetros**

### **Precipitação**
#### **Estações do Alerta Rio**
Uso de dados desde 1991 do sistema alerta-rio com os seguintes visualizações:  
- Mapa com estações indicando onde foi ou não atingido índice com a lista dos nomes dos postos que atigiram o indice.
- Tabelas contendo, para cada estação e duração, as precipitações acima do índice.
- Tabelas com precipitação máxima registrada para cada duração e estação agrupadas por sub-bacia que obtiveram chuvas acima do índice.
- Avaliação dos tempos de recorrência das precipitações.

#### **Estações do INEA**
>_A ser avaliado._

#### **Estações da Defesa Civil**
>_A ser disponibilizado no Datalake._

### **Maré**
Visualização dos dados de tábuas de maré disponibilizados pela Marinha do Brasil. [Link de acesso](https://www.marinha.mil.br/chm/sites/www.marinha.mil.br.chm/files/dados_de_mare/41-porto_do_rio_de_janeiro.pdf)

### Dados do Comando e do Waze
Mapa com pontos de eventos relacionados a alagamentos, bolsão d'água e inundação no dia do evento.

### **Nível de Reservatório de Detenção**
Dados com porcentagem de enchimento dos reservatórios da bacia do Canal do Mangue.  
>_Dados da Rua do Senado a ser avaliado._

### **Nível da Lagoa e Operação das Comportas**
Gráfico do nível da lagoa com indicação de estágios de normalidade, atenção e crítico.  
Gráfico com indicação da abertura e fechamento das comportas do canal da rua General Garzon, canal da Visconde de Albuquerque e do canal do Jardim de Alah.
>Avaliando login para acesso dos dados ou se há uma API.



