# Contribuindo para o Control Fintech

Agradecemos seu interesse em contribuir para o projeto Control Fintech! Este documento fornece diretrizes para contribuições.

## Como Contribuir

### 1. Reportar Bugs
- Use o sistema de Issues do GitHub
- Descreva o problema detalhadamente
- Inclua passos para reproduzir
- Adicione prints se necessário

### 2. Sugerir Melhorias
- Abra uma Issue com tag "enhancement"
- Explique o benefício da melhoria
- Proponha uma implementação se possível

### 3. Contribuir com Código

#### Preparação do Ambiente
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/control-fintech.git
cd control-fintech

# Instale as dependências
pip install -r requirements.txt

# Execute os testes
python -m pytest tests/
```

#### Padrões de Código
- Use PEP 8 para formatação Python
- Adicione docstrings para funções públicas
- Mantenha funções com no máximo 50 linhas
- Use nomes descritivos para variáveis

#### Processo de Pull Request
1. Fork o repositório
2. Crie uma branch para sua feature: `git checkout -b feature/nova-funcionalidade`
3. Faça commits com mensagens claras
4. Adicione testes para novas funcionalidades
5. Execute todos os testes
6. Abra um Pull Request

### 4. Contribuir com Dados
- Dados devem ser de fontes confiáveis (IBGE, Banco Central, etc.)
- Inclua referências das fontes
- Mantenha dados atualizados

### 5. Documentação
- Mantenha README.md atualizado
- Documente novas funcionalidades
- Use português brasileiro
- Inclua exemplos práticos

## Estrutura do Projeto

```
control-fintech/
├── financial_impact_analyzer.py    # Análise principal
├── opportunity_cost_calculator.py  # Calculadora de custos
├── lifestyle_comparison.py         # Comparação de estilos
├── behavioral_economics.py         # Análise comportamental
├── data_visualizer.py              # Visualizações
├── run_analysis.py                 # Script principal
├── requirements.txt                # Dependências
├── tests/                          # Testes unitários
└── docs/                           # Documentação adicional
```

## Diretrizes de Commit

Use o formato Conventional Commits:

```
tipo(escopo): descrição

feat(analyzer): adiciona análise de inflação
fix(calculator): corrige cálculo de juros compostos
docs(readme): atualiza instruções de instalação
test(behavioral): adiciona testes para vieses cognitivos
```

## Tipos de Commit
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Manutenção

## Código de Conduta

### Nossos Compromissos
- Manter ambiente acolhedor e inclusivo
- Respeitar diferentes pontos de vista
- Focar no melhor para a comunidade
- Mostrar empatia com outros membros

### Comportamentos Esperados
- Usar linguagem acolhedora e inclusiva
- Respeitar diferentes opiniões
- Aceitar críticas construtivas
- Focar no melhor para a comunidade

### Comportamentos Inaceitáveis
- Linguagem ou imagens sexualizadas
- Comentários insultuosos ou depreciativos
- Assédio público ou privado
- Publicar informações privadas sem permissão

## Processo de Review

### Para Reviewers
1. Verifique se o código segue os padrões
2. Execute os testes localmente
3. Teste as funcionalidades manualmente
4. Verifique a documentação
5. Seja construtivo nos comentários

### Para Contribuidores
- Responda aos comentários rapidamente
- Faça as alterações solicitadas
- Mantenha o PR atualizado com a branch principal
- Seja paciente durante o processo

## Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a mesma licença do projeto (MIT).

## Dúvidas?

Se tiver dúvidas sobre como contribuir:
- Abra uma Issue com a tag "question"
- Entre em contato através do email do projeto
- Consulte a documentação existente

## Reconhecimento

Todos os contribuidores serão reconhecidos no arquivo CONTRIBUTORS.md e nos releases do projeto.

Obrigado por contribuir para tornar a educação financeira mais acessível! 🚀
