# Estrutura de Pastas do Projeto Django - Portfolio

```bash
contact/         # App responsável pelo formulário de contato e gerenciamento das mensagens enviadas pelos visitantes
└── migrations/  # Migrações do banco de dados para o app contact

core/            # App para funcionalidades centrais e compartilhadas do projeto (utils, context processors, etc)
└── migrations/  # Migrações do banco de dados para o app core

media/           # Pasta para armazenar arquivos enviados (imagens, PDFs, uploads do usuário)

portfolio/       # Projeto Django principal (configurações, urls principais, wsgi/asgi)
└── __pycache__/ # Cache compilado de arquivos Python do projeto portfolio

projects/        # App para gerenciar os projetos exibidos no portfólio (models, views, templates)
└── migrations/  # Migrações do banco de dados para o app projects

resume/          # App para gerenciar currículo, experiências, certificados e informações do usuário
└── migrations/  # Migrações do banco de dados para o app resume

settings/        # App para configurações específicas do projeto (ex: temas, SEO, configurações globais)
└── migrations/  # Migrações do banco de dados para o app settings

static/          # Arquivos estáticos (CSS, JS, imagens fixas) usados pelo frontend

templates/       # Templates HTML do Django para renderização das páginas
└── includes/    # Partials e componentes reutilizáveis de templates (ex: navbar, footer)

users/           # App para gerenciamento e autenticação de usuários/admin
└── migrations/  # Migrações do banco de dados para o app users
```

---

## Observações

- Cada app tem sua pasta e geralmente uma pasta `migrations` para as migrações do Django.
- As pastas `media`, `static` e `templates` ficam na raiz do projeto.
- A pasta `portfolio` é o projeto principal, contendo arquivos do Django.
- A pasta `venv` (não listada aqui) é o ambiente virtual e deve ser ignorada no controle de versão.