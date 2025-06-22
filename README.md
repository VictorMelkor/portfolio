# Portfólio Fullstack com Django

Projeto pessoal de portfólio desenvolvido com **Django (Python)** e frontend manual utilizando **HTML5, CSS3** e **JavaScript vanilla**.  
O objetivo é apresentar informações profissionais, projetos, habilidades e certificados, além de permitir contato direto por meio de um formulário funcional.

---

## 🚀 Tecnologias Utilizadas

- **Backend:** Django 4+, Python 3.12+
- **Frontend:** HTML, CSS modularizado, JavaScript puro
- **Banco de dados:** SQLite (desenvolvimento) e PostgreSQL (produção)
- **Template base:** iPortfolio (adaptado do BootstrapMade)
- **Deploy:** Plataforma gratuita [Render](https://render.com)
- **Gerenciamento de ambiente:** Variáveis sensíveis via `.env` com `python-dotenv`

---

## 🧱 Estrutura e Funcionalidades

- Organização modular com apps separados:
  - `core`, `contact`, `projects`, `resume`, `users`, `settings`, `portfolio`
- Painel administrativo via Django Admin, com modelo de usuário customizado
- Upload e exibição de mídias (imagens, PDFs)
- Formulário de contato funcional com persistência no banco e redirecionamento
- Página única (landing page) com seções: Sobre, Habilidades, Currículo, Portfólio, Serviços e Contato
- Suporte a responsividade e acessibilidade básica
- Design leve, baseado em tema escuro/claro (modo escuro planejado com persistência futura)

---

## 📌 Status do Projeto

- ✅ Estrutura base pronta e deploy funcional no Render
- ✅ Landing page finalizada com formulário dinâmico integrado
- ✅ Administração via Django Admin operante
- 🚧 Em desenvolvimento:
  - Forms e views para CRUD das demais entidades
  - Uploads e validações de arquivos
  - Páginas de erro personalizadas
  - SEO básico e acessibilidade
  - reCAPTCHA para formulário de contato
  - Testes automatizados (`pytest-django`)
  - Modo escuro com `localStorage`



---

## 🤝 Contato

Este projeto foi desenvolvido com fins pessoais e educacionais.  
Em caso de dúvidas, sugestões ou propostas, entre em contato por:

- Email: [victor.melkor@gmail.com](mailto:victor.melkor@gmail.com)


---

> **Nota:** Este repositório contém o backend completo do projeto. Para o deploy local, configure um ambiente virtual com as dependências listadas em `requirements.txt` e crie um arquivo `.env` conforme o exemplo.

