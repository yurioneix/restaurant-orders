# Restaurant Orders

<br>

## Premissa do projeto 
O Restaurante 🍝 🦐 Chapa Quente 🍛 🥘 precisa de você para finalizar sua ferramenta de construção de cardápios. O restaurante necessita desta ferramenta para que possa, de maneira simples, gerar seus cardápios considerando possíveis restrições alimentares e também a disponibilidade dos ingredientes em estoque. Hoje, a gestão das receitas e de estoque do restaurante acontece de forma muito ineficiente através de arquivos csv e, por essa razão, as pessoas fundadoras do estabelecimento desejam melhorar esta gestão.

Um primeiro time iniciou o desenvolvimento deste projeto e já preparou uma estrutura inicial para que você possa finalizar essa construção. Assim, ao longo deste projeto você será responsável por construir testes para classes já implementadas, implementará uma nova classe para mapear os pratos e suas respectivas receitas (ingredientes e quantidades), também implementará uma classe que gerará os cardápios que devem ser mostrados para as pessoas que frequentam o estabelecimento e outra que fará a gestão de estoque dos ingredientes.


🚵 Habilidades exercitadas:

- Praticar o conceito de Hashmaps através das estruturas de dados Dict e Set do Python;
- Praticar os conhecimentos de testes de software;
- Praticar os conhecimentos de orientação a objetos.

<br>

## Instalação 

1. Clone o repositório

  - Use o comando: `git clone git@github.com:yurioneix/restaurant-orders.git`.
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd restaurant-orders`

2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`

<br>

## Pastas/arquivos desenvolvidos por mim
```bash
    src/tests/ingredient/test_ingredient.py
    src/tests/dish/test_dish.py
    src/services/menu_data.py
    src/services/menu_builder.py
```
