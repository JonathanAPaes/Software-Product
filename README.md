# PONTUAL

O Pontual é um aplicativo em Flask / Python & HTML5.

Criado para facilitar a obtenção e registro de horários de apontamento, Pontual é um aplicativo minimalista de registro de apontamento.

## Índice

- [Requisitos](#requisitos)
- [Composição](#composicao) 
- [Interface](#Interface)
- [Estrutura](#estrutura) 
- [Instalação](#instalacao)
- [Utilização](#utilizacao)
- [Licença](#licenca)

## Requisitos
- Docker
- Docker Compose

## Composição
**Pontual:1.0a**
- Python:3.8
- Flask:2.0.3
- MySQL:5.7
- HTML:5/CSS:3,JS/ES:2021)

Para mais informações, leia o arquivo requirements.txt ou [Componentes de Terceiros](THIRD-PARTY.md)

## Interface
![Interface desligada](views/screenshots/checkbox.off "Interface desligada")
![Interface ligada](views/screenshots/checkbox.on "Interface ligada")

## Estrutura
**Composição técnica:**

- Modelo MVC
- Sintaxe

| Tipos       | Notação                    | Exemplo            |
|-------------|----------------------------|--------------------|
| Constantes  | Snake case com caixa alta  | `NOME_FUNCIONARIO` |
| Variáveis   | Snake case caixa baixa     | `nome_funcionario` |
| Banco       | Snake case com caixa alta  | `NOME_FUNCIONARIO` |
| Classes     | Upper camel case           | `NomeFuncionario`  |
| Funções     | Camel case                 | `nomeFuncionario`  |

Para verificar as diretrizes de estilo de código Python (PEP8), acesse [PEP8](https://peps.python.org/pep-0008/).

## Instalação
- Extraia o conteúdo do zip em um diretório
- Navegue até o diretório com o terminal e escreva: 
- **`docker compose up`**

Em paralelo, pode ser iniciado pelo arquivo **`#docker.ps1`**, opção 1

## Utilização

O primeiro acesso possui modo debug ativado e fará gravações direto no banco.

URL de acesso: [localhost:5000](http://localhost:5000/)

Caso o banco não funcione, abra-o manualmente no arquivo **`#docker.ps1`**, opção 4 e cole o conteúdo do arquivo db.sql nele.

## Licença

O software é licenciado com licença MIT e permite o uso comercial e não comercial do software, alteração e distribuição livre. 

Para mais informações, leia o arquivo de [licença](LICENSE)
