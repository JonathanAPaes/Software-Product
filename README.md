# PONTUAL

O Pontual é um aplicativo em Flask / Python & HTML5.

Criado para facilitar a obtenção e registro de horários de apontamento. 

Pontual é um aplicativo que visa minimalismo para o cliente final, e uma gama de dados de registro de apontamento para sua empresa!

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
<div style="display: flex; flex-wrap: wrap; justify-content: space-between;"> 
<figure> <img width="300" height="475" src="https://raw.githubusercontent.com/JonathanAPaes/Software-Product/main/views/screenshots/checkbox.on.png"> </figure>
<figure> <img width="300" height="475" src="https://raw.githubusercontent.com/JonathanAPaes/Software-Product/main/views/screenshots/checkbox.off.png"> </figure>
</div>

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

- [localhost:5000](http://localhost:5000/) - URL de acesso raiz
- [localhost:5000/funcionario](http://localhost:5000/funcionario) - URL de acesso funcionario
- [localhost:5000/administrador](http://localhost:5000/administrador)- URL de acesso administrador
 
Caso o banco não funcione, abra-o manualmente no arquivo **`#docker.ps1`**, opção 4, adicione a senha e cole o conteúdo do arquivo db.sql no console mysql.

## Licença

O software é licenciado com licença MIT e permite o uso comercial e não comercial do software, alteração e distribuição livre. 

Para mais informações, leia o arquivo de [licença](LICENSE)
