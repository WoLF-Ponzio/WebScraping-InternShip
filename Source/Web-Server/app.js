const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const path = require('path');

const app = express();
const port = 3000;

// Configuração do banco de dados (substitua as credenciais conforme necessário)
const db = mysql.createConnection({
  host: 'localhost',
  port: 3306,
  user: 'root',
  password: 'root',
  database: 'Raspagem', //Trocar nome do schema
});

// Conecta ao banco de dados
db.connect((err) => {
  if (err) {
    console.error('Erro na conexão com o banco de dados:', err);
    return;
  }
  console.log('Conexão ao banco de dados estabelecida.');
});

// Configura o middleware para análise do corpo da solicitação (body-parser)
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Rota index que renderiza "Hello World"
app.get('/', (req, res) => {
  res.send('Hello World');
});

// Rota para obter a vaga e o tipo da vaga do banco de dados
app.get('/vagas', (req, res) => {
  const query = 'select v.vaga, v.Empresa, v.Local, v.Data, v.Descricao, tv.descricao from vagas v inner join tipo_vaga tv on tv.id = v.TipoVaga;'
  db.query(query, (err, result) => {
    if (err) {
      console.error('Erro ao executar a consulta:', err);
      res.status(500).send('Erro ao obter as vagas do banco de dados');
      return;
    }
    res.json(result);
  });
});

// Inicia o servidor
app.listen(port, () => {
  console.log(`Servidor iniciado na porta ${port}`);
});
