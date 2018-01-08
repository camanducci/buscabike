# Busca Bike

Sistema voltado para agregação de anúncios de bicicletas vendidas em serviços como:

 - OLX

Em breve para os seguintes serviços:

 - Mercado Livre

Todos os anúncios são coletados via crawling usando o [Busca Bike Scraper](https://github.com/rochacbruno/buscabike-scraper).


## Instalação

Faça o checkout do projeto:

```shell
$ git clone https://github.com/rochacbruno/buscabike
```

Prepare o ambiente com virtualenv e instale as dependências:

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
$ make install
```

Então inicie o servidor local:

```shell
$ bike runserver
```

## Testes

O projeto usa Selenium para testes de aceitação. Com isso é recomendável ter o PhantomJS instalado. Com tudo pronto digite o comando:

```shell
$ make test
```

## Outros comandos

Mais dúvidas sobre os comandos disponíveis, digite os comandos abaixo:


```shell
$ make help

Usage:
  make <target>

Targets:
  help        Display this help
  clean       remove Python file artifacts
  test        run tests quickly with the default Python
  install     install the package to the active Python's site-packages
```

```shell
$ bike

Usage: bike [OPTIONS] COMMAND [ARGS]...

  Busca Bike APP

Options:
  --help  Show this message and exit.

Commands:
  runserver  Run the server with dev/debug mode
  shell      Open a shell with app in the context
```

## Como Contribuir
Veja mais no arquivo `CONTRIBUTING.md`, as formas de ajudar com o projeto, e o `AUTHORS.md` para saber quem estão a frente e que pode te auxiliar.

## Sobre a logo

A logo usada foi encontrado no serviço [Icon Finder](https://www.iconfinder.com/) e está sob a licença GPL. Mais detalhes sobre as licenças dos ícones, veja no [site do serviço](https://docs.google.com/spreadsheets/u/1/d/1E8X2_xmJkkoeZwa1HPNG6jT3ytAZlcAgzTDRX0jDF-Q/pubhtml?gid=0&single=true).
