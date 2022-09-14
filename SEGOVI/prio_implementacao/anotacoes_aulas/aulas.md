<h1> 👩‍💻 Formação em Infraestrutura de Dados - PCRJ 2022.2 </h1>

<h2>  Sumário </h2>

- [Meu Projeto](#projeto)
- [Exercicio de Aquecimento](#aquecimento)
- [Componentes da Infraestrura Introdução ao Github; ambiente de desenvolvimento](#aula_1)
- [Metadados, padronização e normalização](#aula_2)
- [Introdução a pipelines de dados e Prefect](#aula_3)
- [Deploy de pipelines na Infra do Escritório](#aula_4)
- [Publicando tabelas com DBT](#aula_5)
- [Construindo pipelines complexas com DBT e Prefect](#aula_6)
- [Encerramento com apresentação dos Projetos](#aula_7)
-----
<div id="projeto"/>
## Automação dos Indicadores de Implementação do [processo.rio](https://processo.rio/indicadores/) 

<h3> Overview </h3>

Este projeto visa gerar o relatório de indicadores de implementação do processo.rio, a partir de dados coletados no sistema de gestão da prefeitura da cidade do Rio de Janeiro.

<h3> Objetivos </h3>

Pretende-se automatizar a coleta de dados, para que o processo de atualização dos indicadores seja mais rápido e eficiente possibilitando o acompanhamento da meta do plano estratégico bem como identificar o andamento por órgão e foco nos esforços de implementação. 

<h3> Descrição da Solução </h3>

A solução proposta consiste em um script que coleta os dados do sistema de gestão da prefeitura faz a ingestão dos dados no BigQuery e permite a criação de um dashboard para acompanhamento dos indicadores.

----------------------------
<div id="aula_1"/>
<h2> Aula 1: Versionamento de Código  </h2>
<h3> 📌 Git essencial  </h3>

<h4> Configurações Básicas</h4>

~~~bash	
git config --global user.name "seu_nome" 
git config --global user.email "seu_email"
git config --list # lista as configurações
~~~

<h4> Comandos básicos </h4>

~~~bash	
git init # Inicializa o repositório
git add . # Adiciona todos os arquivos
git commit -m "first commit" # Cria o commit
git remote add origin # Adiciona o repositório remoto
git remote -v # Verifica o repositório remoto
git push -u origin main # Envia os arquivos para o repositório remoto
git pull # Atualiza o repositório local com o remoto
~~~

<h4> Listar arquivos modificados </h4>

~~~bash
git status
~~~

<h4> Desfazer alterações </h4>

~~~bash
git checkout -- <arquivo> # Desfaz as alterações do arquivo
git reset HEAD <arquivo> # Desfaz o git add
git reset --soft HEAD~1 # Desfaz o último commit
git reset --hard HEAD~1 # Desfaz o último commit e as alterações
~~~

<h4> Branches </h4>

~~~bash
git branch # Lista as branches
git  # exibir branch atual 
git branch <nome> # Cria uma nova branch
git checkout <nome> # Muda para a branch
git branch -m novo-nome-da-branc # Renomeia a branch atual
git branch -m nome-atual novo-nome # Renomeia a branch
git checkout -b <nome> # Cria e muda para a branch
git merge <nome> # Faz o merge da branch com a atual
git branch -d <nome> # Deleta a branch
git merge <nome> # Faz o merge da branch com a atual
~~~

**Merge Conflict:** pode ocorrer quando duas pessoas alteram o mesmo arquivo e tentam fazer o `merge`. O git não sabe qual das duas alterações deve ser mantida. Para resolver o conflito, basta abrir o arquivo e escolher qual das alterações deve ser mantida. 

<h4> Histórico de commits </h4>

~~~bash
git log # Lista os commits
git log --oneline # Lista os commits em uma linha
git log --oneline --graph # Lista os commits em uma linha com o gráfico
git log --oneline --graph --decorate # Lista os commits em uma linha com o gráfico e as branches
git log --oneline --graph --decorate --all # Lista os commits em uma linha com o gráfico e as branches
~~~

<h4> Histórico </h4>

~~~bash
git log # Lista os commits
git log --oneline # Lista os commits em uma linha
git log --oneline --graph # Lista os commits em uma linha com o gráfico
git log -p arquivo.txt # Mostra as alterações do arquivo
git log --autor=nome-autor # Mostra os commits do autor
git log --grep="palavra-chave" # Mostra os commits com a palavra-chave
~~~	

<div id="aula_2"/>
<h2> Aula 2:   </h2>
<h3>   </h3>




