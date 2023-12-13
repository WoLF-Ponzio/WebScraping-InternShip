
<p style="text-align: center;">
    <a href="https://www.espm.br/cursos-de-graduacao/sistemas-de-informacao/"><img src="https://avatars.githubusercontent.com/u/49880458?s=200&v=4" alt="Sistemas de Informação ESPM" style="height: 200px; width: 200px;"/></a>
</p>

# WebScraping-InternShip
### Repositório dedicado ao projeto interdisciplinar do 4º semestre


### 2023-02

## Integrantes
- [Ana Laura Pereira](https://github.com/anacatarinop)
- [Artur Cozzi](https://github.com/ArturCozzi)
- [Gabriel Ponzio](https://github.com/WoLF-Ponzio)

## Descrição do Projeto

O projeto é uma iniciativa destinada a facilitar o acesso a oportunidades de emprego para profissionais em diversos estágios de suas carreiras. Ele se concentra em quatro categorias principais:

**Estágios**: Destinados a estudantes e recém-formados, oferecendo oportunidades de entrada no mercado de trabalho.

**Posições Júnior**: Para profissionais no início de suas carreiras, visando empregos que exijam alguma experiência prévia, mas ainda focados em desenvolvimento e aprendizado.

**Posições Sênior**: Para profissionais experientes, buscando oportunidades que exijam um alto nível de especialização e experiência.

**Cargos de Direção**: Focados em executivos e gestores, oferecendo oportunidades em níveis de alta gestão e liderança.

O projeto emprega uma plataforma online que permite aos usuários filtrar as vagas de acordo com seu nível de experiência, área de interesse e localização. 

# Detalhes de Configuração

```
Aqui deve ser colocado o conteúdo do arquivo .env e/ou de outros arquivos de configuração, ou detalhes de arquivos ou pastas que não estão no repositório do projeto, mas que devem existir para que o projeto possa ser executado com sucesso.

Por exemplo, a descrição do conteúdo do arquivo .env, ou nomes de pastas que precisam existir.

(Remover esse aviso na versão final)
```

Para funcionar corretamente, devem ser criados os seguintes arquivos/pastas nos caminhos especificados, com o conteúdo especificado:

- O arquivo `.env` deve ser criado em `/`, com o conteúdo abaixo:
```
app_localIp=0.0.0.0
app_port=3000
app_root=
# Não pode terminar com barra /
app_urlSite=http://localhost:3000
app_cookie=[NOME DO COOKIE]
app_cookieSecure=0
app_staticFilesDir=public
app_disableStaticFiles=0
app_sqlConfig_connectionLimit=30
app_sqlConfig_waitForConnections=1
app_sqlConfig_charset=utf8mb4
app_sqlConfig_host=localhost
app_sqlConfig_port=3306
app_sqlConfig_user=[USUÁRIO DO BANCO]
app_sqlConfig_password=[SENHA DO USUÁRIO DO BANCO]
app_sqlConfig_database=[NOME DO BANCO]
app_usuarioSenhaPadrao=[SENHA PADRÃO PARA NOVOS USUÁRIOS]
app_usuarioHashSenhaPadrao=[HASH DA SENHA PADRÃO PARA NOVOS USUÁRIOS]
# Não utilizar números > 0x7FFFFFFF pois os XOR resultarão em -1
app_usuarioHashId=[HASH DE 32 BITS PARA O ID EM HEXADECIMAL, COMO 0x1234ABCD]
```

- A pasta `dados` deve ser criada em `/`
- A pasta `imagens` dee ser criada em `/dados`

# Licença

Este projeto é licenciado sob a [MIT License](https://github.com/tech-espm/inter-1sem-2023-anonimos/blob/main/LICENSE).
