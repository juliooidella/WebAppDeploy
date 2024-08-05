# WebAppDeploy
- Paradigmas de Programação
    
    Paradigmas de programação são abordagens ou estilos de programação que fornecem uma forma de estruturar e organizar o código em um programa de computador. Eles representam diferentes formas de pensar sobre como resolver problemas usando um computador e influenciam a maneira como o código é escrito e estruturado. Alguns dos principais paradigmas de programação incluem:
    
    1. **Paradigma Procedural:** Baseia-se na execução sequencial de instruções. Os programas são divididos em procedimentos ou funções que realizam tarefas específicas. Exemplos de linguagens: C, Pascal.
    2. **Paradigma Orientado a Objetos:** Enfatiza a organização do software em objetos, que encapsulam dados e comportamentos. Objetos são instâncias de classes e interagem entre si através de métodos. Exemplos de linguagens: Java, C++, Python.
    3. **Paradigma Funcional:** Foca em funções matemáticas, evitando estados mutáveis e efeitos colaterais. As funções são tratadas como cidadãos de primeira classe, podendo ser passadas como argumentos e retornadas de outras funções. Exemplos de linguagens: Haskell, Lisp, Elixir.
    4. **Paradigma Lógico:** Baseia-se na lógica formal e em regras para descrever relações entre fatos. Programas são formados por uma base de fatos e regras, e a execução é feita através de consultas. Exemplos de linguagens: Prolog.
    5. **Paradigma de Programação Declarativa:** Especifica o que deve ser feito sem descrever como fazer. Inclui paradigmas como programação lógica e funcional. Exemplos de linguagens: SQL (para consulta de dados).
    6. **Paradigma de Programação Imperativa:** Descreve a computação em termos de declarações que alteram o estado do programa. É o oposto da programação declarativa. Exemplos de linguagens: Python, JavaScript.
    
    Cada paradigma oferece uma maneira diferente de pensar sobre a construção de software e pode ser mais adequado para certos tipos de problemas ou contextos de desenvolvimento.
    
- O que vamos usar: **Paradigma Orientado a Objetos**
    
    O **paradigma orientado a objetos** em Python é um estilo de programação que utiliza objetos e classes para organizar e estruturar o código. Esse paradigma se baseia em quatro princípios fundamentais: encapsulamento, abstração, herança e polimorfismo.
    
    ### Princípios da Orientação a Objetos
    
    1. **Encapsulamento:**
        - Refere-se ao agrupamento de dados (atributos) e métodos (funções) que operam sobre esses dados em uma única unidade chamada classe. O encapsulamento também controla o acesso aos dados, permitindo ocultar detalhes internos de implementação e proteger o estado de um objeto.
    2. **Abstração:**
        - Consiste em expor apenas os aspectos relevantes de um objeto, escondendo os detalhes complexos de sua implementação. A abstração permite que os desenvolvedores se concentrem em interações de alto nível sem se preocupar com detalhes de baixo nível.
    3. **Herança:**
        - Permite criar novas classes a partir de classes existentes, herdando seus atributos e métodos. A herança facilita o reuso de código e a criação de hierarquias de classes, onde classes derivadas podem adicionar ou modificar funcionalidades.
    4. **Polimorfismo:**
        - Refere-se à capacidade de diferentes objetos responderem a uma mesma mensagem (ou método) de maneiras diferentes. Em Python, isso é frequentemente implementado através de métodos que podem ser sobrecarregados (override) ou através de interfaces comuns que diferentes classes implementam.
    
    ### Implementação em Python
    
    Em Python, a orientação a objetos é implementada usando **classes** e **objetos**:
    
    - **Classe:** É uma definição de um tipo de objeto. Define um conjunto de atributos e métodos que os objetos dessa classe terão. Por exemplo:
        
        ```python
        class Animal:
            def __init__(self, nome):
                self.nome = nome
        
            def emitir_som(self):
                pass
        
        ```
        
    - **Objeto:** É uma instância de uma classe. Quando você cria um objeto de uma classe, você está criando uma instância dessa classe com atributos específicos.
        
        ```python
        cachorro = Animal("Rex")
        ```
        
    
    ### Exemplo de Implementação
    
    Aqui está um exemplo simples de como criar e usar classes em Python:
    
    ```python
    class Animal:
        def __init__(self, nome):
            self.nome = nome
    
        def emitir_som(self):
            print("Som genérico de animal")
    
    class Cachorro(Animal):
        def emitir_som(self):
            print("Au Au")
    
    class Gato(Animal):
        def emitir_som(self):
            print("Miau")
    
    # Criando objetos das classes
    cachorro = Cachorro("Rex")
    gato = Gato("Mia")
    
    # Chamando métodos
    cachorro.emitir_som()  # Saída: Au Au
    gato.emitir_som()      # Saída: Miau
    ```
    
    Neste exemplo:
    
    - **Animal** é uma classe base que define o método `emitir_som`.
    - **Cachorro** e **Gato** são classes derivadas que herdam de `Animal` e sobrescrevem o método `emitir_som` para fornecer sons específicos para cada tipo de animal.
    
    A orientação a objetos em Python é poderosa e flexível, permitindo a criação de software modular, reutilizável e fácil de manter.
    
    ### Outro exemplo de abstração de objeto do Mundo Real para classes:
    
    ### Programação Orientada a Objetos
    
    **Vamos imaginar que estamos falando sobre um ar condicionado. Um ar condicionado tem várias partes e funções, mas podemos entendê-lo melhor se pensarmos em como ele funciona no dia a dia.**
    
    ### Princípios da Orientação a Objetos
    
    1. **Encapsulamento:**
        
        **Pense no controle remoto do ar condicionado. O controle remoto permite que você ajuste a temperatura, ligue e desligue o ar condicionado, e mude o modo de funcionamento. Você não precisa abrir o ar condicionado e mexer nas partes internas para fazer isso.**
        
        - **Encapsulamento** é como usar o controle remoto para ajustar o ar condicionado sem precisar mexer nas partes internas.
        - Em programação, isso significa que uma classe guarda seus dados e funções dentro dela e só mostra o que é necessário, protegendo as partes internas.
    2. **Abstração:**
        
        **Imagine que você quer resfriar um quarto. Você só precisa ajustar a temperatura no controle remoto. Você não precisa entender como o compressor, o refrigerante e as outras partes do ar condicionado funcionam para fazer o quarto ficar mais frio.**
        
        - **Abstração** é como ajustar a temperatura no controle remoto sem se preocupar com os detalhes internos do ar condicionado.
        - Em programação, isso significa que mostramos apenas as partes importantes de um objeto e escondemos os detalhes complexos.
    3. **Herança:**
        
        **Vamos imaginar que existem diferentes modelos de ar condicionado. Todos eles podem resfriar o quarto, mas alguns modelos mais novos também podem aquecer e desumidificar. Esses modelos mais novos ainda têm todas as funções básicas dos modelos antigos, mas com funções extras.**
        
        - **Herança** é como ter um modelo básico de ar condicionado e adicionar novas funções aos modelos mais novos.
        - Em programação, isso significa que podemos criar novas classes baseadas em classes existentes, reutilizando e ampliando o que já temos.
    4. **Polimorfismo:**
        
        **Imagine que você tem diferentes aparelhos de ar condicionado, cada um com um controle remoto. Embora todos os controles remotos tenham um botão de ligar/desligar, o que acontece quando você pressiona o botão pode ser diferente. Um ar condicionado pode começar a resfriar, enquanto outro pode começar a aquecer.**
        
        - **Polimorfismo** é como ter um botão de ligar/desligar que faz diferentes coisas em diferentes aparelhos de ar condicionado.
        - Em programação, isso significa que diferentes objetos podem usar a mesma ação (ou método) de maneiras diferentes, dependendo de qual objeto você está usando.
    
    ---
    
    **Então, a programação orientada a objetos é como usar e entender um ar condicionado. Você segue algumas regras básicas (encapsulamento, abstração, herança e polimorfismo) para garantir que tudo funcione bem e de forma eficiente, sem precisar saber todos os detalhes internos.**
    
    Imagine novamente um controle de Ar Condicionado, ele possui uma forma, uma cor, marca, modelo, tipo de pilhas e etc… Além das características do controle ele possui funções, como por exemplo: Liga/Desliga, Aumentar/Diminuir temperatura, Oscilar, Desligar Display e etc…
    
    Em linguagem natural temos a seguinte representação dele: 
    
    Objeto: Controle de Ar Condicionado
    
    Características: 
    
    - Cor: Branco
    - Largura: 3 centímetros
    - Altura: 5 centímetros
    - Peso: 200 gramas
    - Marca: Elgin
    - Modelo: Sem Modelo
    - Tipo de Pilhas: AAA
    
    Funções:
    
    - Liga/Desliga
    - Aumentar Temperatura
    - Diminuir Temperatura
    - Velocidade do Vento
    - Tempo
    - Ligar/Desligar o Visor (Display)
    
    Agora em Python como ele é representado:
    
    Crie um novo arquivo chamado ar_condicionado.py, copie o código a seguir e cole.
    
    ```python
    class ControleArCondicionado:
        def __init__(self, cor, largura, altura, peso, marca, modelo, tipo_de_pilha):
            self.cor = cor
            self.largura = largura
            self.altura = altura
            self.peso = peso
            self.marca = marca
            self.modelo = modelo
            self.tipo_de_pilha = tipo_de_pilha
            self.ligado = False
            self.temperatura = 20
    
        def liga_desliga(self):
            self.ligado = not self.ligado
    
            if self.ligado:
                return "Ar condicionado ligado"
            else:
                return "Ar condicionado desligado"
    
        def aumenta_temperatura(self):
            if self.ligado:
                self.temperatura += 1
                print(f"Temperatura aumentada para {self.temperatura}")
            else:
                print("Ar condicionado desligado")
    
        def diminui_temperatura(self):
            if self.ligado:
                self.temperatura -= 1
                print(f"Temperatura diminuida para {self.temperatura}")
            else:
                print("Ar condicionado desligado")
    
    # Estanciando a classe do Objeto
    controle = ControleArCondicionado("branco", 20, 20, 10, "LG", "ABC", "AAA")
    
    # Executando uma das funções dele
    print(controle.liga_desliga())
    
    # Criando uma rotina de repetição com entrada do usuário
    print("Digite 1 para Ligar ou Desligar o Ar Condicionado")
    print("Digite 2 para aumentar a temperatura")
    print("Digite 3 para diminuir a temperatura")
    
    while True:
        comando = input()
    
        if comando == "sair":
            break
        if comando == "1":
            print(controle.liga_desliga())
        elif comando == "2":
            controle.aumenta_temperatura()
        elif comando == "3":
            controle.diminui_temperatura()
        else:
            print("Comando inválido")
    
    ```
    
- Tornando o nosso projeto Orientado a Objetos
    
    Vamos agora implementar a **estrutura de classe** e adotar o paradigma da orientação a objetos em nosso projeto. Mas por que estamos optando por isso? Por que não continuar usando simplesmente uma lista com os títulos dos livros? Por que complicar adicionando orientação a objetos? A razão é que queremos associar outras **características específicas** a cada livro que iremos criar.
    
    Queremos, por exemplo, poder identificar o autor, a **categoria, o ano que o livro foi publicado, a editora e se o livro está disponível para ser reservado na biblioteca.** E para alcançar esse objetivo, não há estrutura mais adequada do que uma **classe**.
    
    ### **Usando a classe em nosso Projeto:**
    
    Vamos criar uma classe no topo do arquivo `app.py` com `class`  chamada `Livro`. Na sequência, usamos `def __init__(self)`. Como parâmetro, colocamos `titulo`, `autor`, `categoria` , `ano`, `editora`, `ativo`.
    
    - **app.py**
        
        ```
        from flask import Flask, render_template
        
        app = Flask(__name__)
        
        class Livro:
            def __init__(self, titulo, autor, categoria, ano, editora):
                
        // Resto do código omitido
        ```
        
    
    Logo após, terminamos de associar as variáveis. Então, `self.titulo = titulo`, fazemos o mesmo para `autor` , `categoria`, `ano` e `editora` .
    
    - **app.py**
        
        ```
        from flask import Flask, render_template
        
        app = Flask(__name__)
        
        class Livro:
            def __init__(self, titulo, autor, categoria, ano, editora):
                self.titulo = titulo
                self.autor = autor
                self.categoria = categoria
                self.ano = ano
                self.editora = editora
        // Resto do código omitido
        ```
        
    
    Temos a seguinte regra de negócio em nossa biblioteca, quando um novo livro é cadastrado, ele automaticamente fica como indisponível, e só mudará para ativo quando houver uma compra dele, futuramente implementaremos essa lógica. Para que o livro seja inicializado como indisponível devemos definir o atributo `ativo` como `False`, para isso, após a `editora`  informe `self.ativo = False`
    
    - **app.py**
        
        ```
        from flask import Flask, render_template
        
        app = Flask(__name__)
        
        class Livro:
            def __init__(self, titulo, autor, categoria, ano, editora):
                self.titulo = titulo
                self.autor = autor
                self.categoria = categoria
                self.ano = ano
                self.editora = editora
                self.ativo = False
        // Resto do código omitido
        ```
        
    
    A classe `Livro` está criada e agora precisamos **instanciar os objetos**. ou seja, precisamos declaras as variáveis dos livros.
    
    Dentro do `ola()`, começamos com o `livro1`. Primeiro, vamos apagar essa lista `(**"O Senhor dos Anéis", "Dom Casmurro", "O Alquimista"**)` que podemos reutilizar posteriormente. Então, vamos deixá-la separada. 
    
    Criamos um objeto `livro1` e vamos colocar os atributos dele, que são: 
    
    **Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 1954, "HarperCollins")**
    
    Por enquanto, temos:
    
    ```python
    // Resto do código omitido
    
    class Livro:
        def __init__(self, titulo, autor, categoria, ano, editora):
            self.titulo = titulo
            self.autor = autor
            self.categoria = categoria
            self.ano = ano
            self.editora = editora
            self.ativo = False
    
    @app.route("/inicio")
    def ola():
        livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 1954, "HarperCollins")
        lista = ["O Senhor dos Anéis", "Dom Casmurro", "O Alquimista"]
    
        return render_template(
            "lista.html", titulo="Listagem de Livros - SENAI", lista_de_livros=lista
        )
    
    // Resto do código omitido
    
    ```
    
    Agora defina 2 novos livros
    
    ```python
        livro2 = Livro("Dom Casmurro", "Machado de Assis", "Romance", 1899, "Martin Claret")
        livro3 = Livro("O Alquimista", "Paulo Coelho", "Autoajuda", 1988, "Rocco")
    ```
    
    Comente a lista atual e implemente uma nova com o mesmo nome da seguinte forma:
    
    ```python
        # lista = ["O Senhor dos Anéis", "Dom Casmurro", "O Alquimista"]
        lista = [livro1, livro2, livro3]
    ```
    
    - app.py
        
        A esse ponto deverá ter a seguinte implementação:
        
        ```python
        // Resto do código omitido
        
        class Livro:
            def __init__(self, titulo, autor, categoria, ano, editora):
                self.titulo = titulo
                self.autor = autor
                self.categoria = categoria
                self.ano = ano
                self.editora = editora
                self.ativo = False
        
        @app.route("/inicio")
        def ola():
            livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 1954, "HarperCollins")
            livro2 = Livro("Dom Casmurro", "Machado de Assis", "Romance", 1899, "Martin Claret")
            livro3 = Livro("O Alquimista", "Paulo Coelho", "Autoajuda", 1988, "Rocco")
        
            # lista = ["O Senhor dos Anéis", "Dom Casmurro", "O Alquimista"]
            lista = [livro1, livro2, livro3]
        
            return render_template(
                "lista.html", titulo="Listagem de Livros - SENAI", lista_de_livros=lista
            )
        
        // Resto do código omitido
        ```
        
    
    Com isso, temos a nossa lista.
    
    E agora vamos iniciar a execução. Vamos pressionar "Ctrl + S" para salvar e depois executar a nossa . Agora, vamos acessar nosso *site* e atualizar também. Surgiu um problema aqui, não é mesmo? Está exibindo muito código.
    
    > <__main__.Livro object at 0x7f469f463d60>
    > 
    > 
    > <__main__.Livro object at 0x7f469f463d90>
    > 
    
    O que é isso? Isso é a **referência do nosso objeto na memória do computador**. Mas por que está mostrando isso em vez das informações do Livro? Porque há algo faltando aqui, não é? Nós fizemos alterações no nosso arquivo `app.py`, mas não mexemos no `lista.html`.
    
    Para resolver isso, precisamos alterar algo no código do `lista.html`, uma vez que já fizemos todas as alterações possíveis no `app.py`. Então, dentro da nossa estrutura de repetição, na nossa variável livro, colocamos `.titulo`.
    
    > lista.html
    > 
    
    ```html
    <!-- código omitido -->
    
    <tbody>
        {% for livro in lista_de_livros %}
        <tr>
            <td>{{ livro.titulo }}</td>
        </tr>
        {% endfor %}
    </tbody>
    
    <!-- código omitido -->
    ```
    
    Esse `.titulo` é o que **acessará a informação do título dentro do nosso objeto**. Salvamos as alterações com "Ctrl + S", reiniciamos o servidor e atualizamos a nossa página. E pronto! Resolvemos o problema do nosso título.
    
    Porém, há uma questão: **por que usamos a estrutura de classe, em vez de uma lista simples?** Porque queríamos **adicionar mais informações para cada Livro**, para cada objeto que criamos. No entanto, só temos o titulo.
    
    Desejamos que apareçam os demais atributos do livro.
    
    # Exercícios
    
    1. Inclua as demais colunas da classe livro ao HTML:
        1. Autor
        2. Categoria
        3. Ano
        4. Editora
        5. Ativo
    2. Nesse desafio, você deve adicionar uma função na classe `Livro` para atualizar o atributo `ativo` para `True`. Isso permitirá que a gente "ative" um livro quando necessário.
        1. Dica: Crie uma função dentro da classe `Livro` chamada `ativar` que atualiza o atributo `ativo` para `True`.
    3. Vamos melhorar a classe `Livro` para que, quando um livro não tiver uma editora especificada, ele mostre automaticamente o texto "Sem Editora". Isso significa que se você não fornecer o nome da editora ao criar um livro, o programa deve preencher essa informação com "Sem Editora".
        1. Dica: Atualize o método construtor (`__init__`) da classe `Livro` para que, se a editora não for fornecida, ele atribua o valor "Sem Editora" ao atributo correspondente.
    4.  Adicionar uma função na classe `Livro` para atualizar a`editora` do livro, ou seja, imagem que no momento que os livros foram cadastrados não tínhamos a informação sobre a editora do livro, porém após uma verificação foi encontrada a editora, e para isso precisamos alterar a editora do livro existente sem alterar os demais dados dele. 
    5. Leia novamente o csv da tabela de livro https://docs.google.com/spreadsheets/d/17qfn_9NfDtZUteh5GjDCw951poi4kNY4rndevxINnfE/edit?gid=1984618649#gid=1984618649 usando o pandas, porém agora ao invés de uma simples lista de títulos, passe para a classe livro os demais atributos do livro.
        1. Dica: Algumas formas para percorrer as linhas da tabela com pandas são:
            
            Obs: Use um dos exemplos para alimentar a classe com os valores referente aos Livros. Ou Seja, substitua o print de algum exemplo pela classe Livro.
            
            ### Usando `iterrows`
            
            O método `iterrows` permite percorrer o DataFrame linha por linha:
            
            ```python
            for index, row in df.iterrows():
                print(f"Nome: {row['Nome']}, Idade: {row['Idade']}")
            ```
            
            ### Usando `iloc` para índices
            
            Outra abordagem é usar `iloc` para acessar linhas específicas pelo índice:
            
            ```python
            for i in range(len(df)):
                print(f"Nome: {df.iloc[i]['Nome']}, Idade: {df.iloc[i]['Idade']}")
            ```
            
            ### Usando uma seleção de colunas
            
            Se você quiser percorrer apenas algumas colunas, pode selecionar essas colunas primeiro:
            
            ```python
            selected_columns = df[['Nome', 'Idade']]
            
            for index, row in selected_columns.iterrows():
                print(f"Nome: {row['Nome']}, Idade: {row['Idade']}")
            ```
            
            ### Usando `apply`
            
            O método `apply` pode ser usado para aplicar uma função a cada linha ou coluna:
            
            ```python
            def print_info(row):
                print(f"Nome: {row['Nome']}, Idade: {row['Idade']}")
            
            df.apply(print_info, axis=1)
            ```
            
    

- **Melhorando a visualização de tabelas**
    
    **Vanilla DataTable** é uma biblioteca JavaScript leve e sem dependências que melhora a visualização de tabelas HTML, adicionando funcionalidades como paginação, ordenação e pesquisa. Abaixo, segue um guia simples para integrá-la em seus projetos.
    
    ### 1. **Instalação**
    
    Para começar, você precisa incluir o CSS e o JavaScript da biblioteca Vanilla DataTable em sua página HTML. Você pode fazer isso diretamente através do CDN.
    
    ```html
    <!DOCTYPE html>
    <html>
      <head>
        <!-- Charset utf-8 para corrigir problemas de caracter especiais -->
        <meta charset="utf-8" />
        <title>Biblioteca</title>
        <!-- Importação da Biblioteca CSS do Vanilla -->
        <link
          rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/vanilla-datatables@latest/dist/vanilla-dataTables.min.css"
        />
        <script src="https://cdn.jsdelivr.net/npm/vanilla-datatables@latest/dist/vanilla-dataTables.min.js"></script>
        <!-- Importação da Biblioteca CSS do Vanilla -->
        
        // Resto do código omitido
    
    ```
    
    ### 2. **Estrutura Básica da Tabela HTML**
    
    A estrutura de tabelas permanece a mesma, não há necessidade de alterar, pois a biblioteca fará o trabalho de alteração.
    
    ```html
    <div class="container">
          <div class="page-header">
            <h1>Listagem de Livros - SENAI</h1>
          </div>
          <a class="url" href="/curriculo">Currículo</a><br />
          <table class="table table-striped table-hover">
            <thead class="thead-default">
              <tr>
                <th>Livro</th>
              </tr>
            </thead>
            <tbody>
              {% for livro in lista_de_livros %}
              <tr>
                <td>{{ livro.titulo }}</td>
              </tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
    
    ```
    
    ### 3. **Inicialização do DataTable**
    
    Depois de definir sua tabela HTML, inicialize o DataTable no arquivo JavaScript. Isso pode ser feito logo após a definição da tabela ou ao final do corpo do documento.
    
    ```html
    <script>
      document.addEventListener('DOMContentLoaded', function() {
        var tabela = document.querySelector('.table');
        var dataTable = new DataTable(tabela);
      });
    </script>
    
    ```
    
    4. **Personalizações Opcionais**
    
    A biblioteca Vanilla DataTable permite algumas personalizações, como desativar a pesquisa ou a paginação. Para configurar essas opções, você pode passar um objeto de configuração ao inicializar o DataTable:
    
    ```html
    
    <script>
      document.addEventListener('DOMContentLoaded', function() {
        var tabela = document.querySelector('.table');
        var dataTable = new DataTable(tabela, {
          searchable: true,  // Habilita a pesquisa
          sortable: true,    // Habilita a ordenação
          perPage: 5,         // Define 5 linhas por página
           columns: [
                { select: 0, sort: "desc" }, // Ordena a primeira coluna em ordem ascendente
              ],
              labels: {
                placeholder: "Pesquisar...", // Texto do placeholder da barra de pesquisa
                perPage: "{select} resultados por página", // Texto da seleção de itens por página
                noRows: "Nenhum resultado encontrado", // Texto quando não há resultados
                info: "Mostrando {start} a {end} de {rows} resultados", // Texto de informações
              },
        });
      });
    </script>
    
    ```
    
    ### 5. **Exemplo Completo**
    
    ```html
    <!DOCTYPE html>
    <html>
      <head>
        <!-- Charset utf-8 para corrigir problemas de caracter especiais -->
        <meta charset="utf-8" />
        <title>Biblioteca</title>
        <link
          rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/vanilla-datatables@latest/dist/vanilla-dataTables.min.css"
        />
        <script src="https://cdn.jsdelivr.net/npm/vanilla-datatables@latest/dist/vanilla-dataTables.min.js"></script>
    
        <!-- Estilo usando CDN para o bootstrap-->
        <link
          rel="stylesheet"
          href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        />
    
        <!-- Estilo usando CSS interno -->
        <style>
          footer {
            text-align: center;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="page-header">
            <h1>Listagem de Livros - SENAI</h1>
          </div>
          <a class="url" href="/curriculo">Currículo</a><br />
          <table class="table table-striped table-hover">
            <thead class="thead-default">
              <tr>
                <th>Livro</th>
              </tr>
            </thead>
            <tbody>
              {% for livro in lista_de_livros %}
              <tr>
                <td>{{ livro.titulo }}</td>
              </tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
        <footer>
          <p>&copy; 2024 SENAI. Todos os direitos reservados.</p>
        </footer>
        <script>
          document.addEventListener("DOMContentLoaded", function () {
            var table = document.querySelector(".table");
            var dataTable = new DataTable(table, {
              // Opções de configuração
              sortable: true,
              searchable: true,
              paging: true,
              perPage: 20,
              columns: [
                { select: 0, sort: "desc" }, // Ordena a primeira coluna em ordem ascendente
              ],
              labels: {
                placeholder: "Pesquisar...", // Texto do placeholder da barra de pesquisa
                perPage: "{select} resultados por página", // Texto da seleção de itens por página
                noRows: "Nenhum resultado encontrado", // Texto quando não há resultados
                info: "Mostrando {start} a {end} de {rows} resultados", // Texto de informações
              },
            });
          });
        </script>
      </body>
    </html>
    
    ```
    
    ### Considerações Finais
    
    A biblioteca Vanilla DataTable é uma solução simples e eficaz para melhorar a usabilidade de tabelas HTML em seus projetos. Com funcionalidades básicas e fácil implementação, é ideal para quem busca uma ferramenta leve e sem dependências externas.
