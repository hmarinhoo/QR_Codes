# 📌 Gerador de QR Codes para Repositórios do GitHub

Projeto em **Python** que gera automaticamente **QR Codes personalizados** para repositórios do GitHub.  
Cada QR Code contém a URL do repositório e exibe o nome do projeto logo abaixo da imagem.

O foco deste projeto é demonstrar **organização de código**, **automação**, **uso de bibliotecas externas** e **manipulação de imagens**, sendo ideal para portfólio.

---

## 📷 Exemplo de QR Code gerado

A imagem abaixo é um exemplo de QR Code criado pelo script após a execução:

<div align="center">
  <img src="assets/exemplo_qrcode.png" alt="Exemplo de QR Code" width="300">
</div>

---

## 🚀 Funcionalidades

- Geração automática de QR Codes
- Personalização de cores
- Inclusão do nome do repositório abaixo do QR Code
- Criação automática da pasta de saída
- Código modular e reutilizável

---

## 🛠️ Tecnologias utilizadas

- Python 3
- qrcode
- Pillow (PIL)

---

## 📂 Estrutura do projeto
```text
QR_Codes/
├── gerando_qrcode.py
├── teste_api.py
├── README.md
├── assets/
│   └── exemplo_qrcode.png
└── qrcodes/
    └── (QR codes gerados)
```

---

## ⚙️ Pré-requisitos

- Python 3.10 ou superior  
- Pip configurado no sistema  

---

## 📦 Instalação das dependências

No terminal, dentro da pasta do projeto, execute:
```bash
pip install qrcode Pillow
```

---

## 🧾 Configuração dos dados

No arquivo `teste_api.py`, defina os repositórios que terão QR Codes gerados:
```python
repositorios = [
    {"nome": "nome-do-repositorio"},
    {"nome": "outro-repositorio"}
]
```

---

## ▶️ Como executar o projeto

No terminal, na raiz do projeto:
```bash
python gerando_qrcode.py
```

Após a execução:

- A pasta `qrcodes/` será criada automaticamente  
- Os QR Codes gerados serão salvos dentro dessa pasta

---

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.

---

## 👤 Autor

Desenvolvido por [Hellen Marinho](https://github.com/hmarinhoo)

