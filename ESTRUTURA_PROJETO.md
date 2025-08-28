# 📁 Estrutura do Projeto Control Fintech

## 🏗️ Organização dos Diretórios

```
control-fintech/
│
├── 📄 readme.md                    # Documentação principal com resultados
├── 📄 requirements.txt             # Dependências Python
├── 📄 setup.py                     # Configuração de instalação
├── 📄 .gitignore                   # Arquivos ignorados pelo Git
├── 📄 LICENSE                      # Licença MIT
│
├── 📂 src/                         # Código fonte principal
│   ├── 📄 __init__.py             # Inicialização do pacote
│   ├── 📄 financial_impact_analyzer.py      # Análise de impacto financeiro
│   ├── 📄 opportunity_cost_calculator.py    # Calculadora de oportunidade
│   ├── 📄 lifestyle_comparison.py           # Comparação de estilos de vida
│   ├── 📄 behavioral_economics.py           # Análise comportamental
│   └── 📄 data_visualizer.py               # Gerador de visualizações
│
├── 📂 scripts/                     # Scripts executáveis
│   ├── 📄 gerar_resultados.py     # Geração completa de resultados
│   └── 📄 run_analysis.py         # Análise abrangente
│
├── 📂 examples/                    # Exemplos de uso
│   └── 📄 teste_simples.py        # Teste básico das funcionalidades
│
├── 📂 docs/                        # Documentação adicional
│   ├── 📄 COMO_USAR.md            # Guia de uso detalhado
│   ├── 📄 EXECUTAR.md             # Instruções de execução rápida
│   ├── 📄 CONTRIBUTING.md         # Guia para contribuições
│   ├── 📄 PROJETO_COMPLETO.md     # Visão geral do projeto
│   └── 📄 RESULTADOS_RESUMO.md    # Resumo dos resultados
│
└── 📂 resultados/                  # Resultados gerados
    ├── 📊 analise_cenarios.csv           # Dados dos cenários
    ├── 📊 analise_categorias.csv         # Dados das categorias
    ├── 📊 comparacao_estilos_vida.csv    # Dados dos estilos de vida
    ├── 📊 analise_comportamental.csv     # Dados comportamentais
    ├── 📈 opportunity_cost_comparison.png # Gráfico custo oportunidade
    ├── 📈 lifetime_impact_analysis.png   # Gráfico impacto na vida
    ├── 📈 category_spending_heatmap.png  # Mapa de calor categorias
    ├── 📈 compound_interest_power.png    # Gráfico juros compostos
    └── 📄 relatorio_final.md             # Relatório completo
```

## 📋 Descrição dos Componentes

### 🎯 Arquivos Raiz
- **readme.md**: Documentação principal com análises e interpretações
- **requirements.txt**: Lista de dependências Python necessárias
- **setup.py**: Configuração para instalação como pacote
- **.gitignore**: Arquivos e pastas ignorados pelo controle de versão
- **LICENSE**: Licença MIT do projeto

### 📦 src/ - Código Fonte
Contém os módulos principais do sistema:
- **financial_impact_analyzer.py**: Análise principal de impacto financeiro
- **opportunity_cost_calculator.py**: Calculadora de custo de oportunidade
- **lifestyle_comparison.py**: Comparação entre diferentes estilos de vida
- **behavioral_economics.py**: Modelagem de comportamentos financeiros
- **data_visualizer.py**: Geração de gráficos e visualizações

### 🔧 scripts/ - Scripts Executáveis
Scripts para execução das análises:
- **gerar_resultados.py**: Executa análise completa e gera todos os resultados
- **run_analysis.py**: Análise abrangente com relatórios detalhados

### 💡 examples/ - Exemplos
Exemplos práticos de uso:
- **teste_simples.py**: Demonstração básica das funcionalidades

### 📚 docs/ - Documentação
Documentação detalhada do projeto:
- **COMO_USAR.md**: Guia completo de utilização
- **EXECUTAR.md**: Instruções de execução rápida
- **CONTRIBUTING.md**: Guia para contribuidores
- **PROJETO_COMPLETO.md**: Visão geral completa do projeto
- **RESULTADOS_RESUMO.md**: Resumo dos principais resultados

### 📊 resultados/ - Resultados Gerados
Outputs do sistema:
- **CSV**: Dados estruturados das análises
- **PNG**: Visualizações gráficas
- **MD**: Relatórios em markdown

## 🚀 Como Navegar

### Para Usuários Iniciantes
1. Leia o **readme.md**
2. Execute **examples/teste_simples.py**
3. Consulte **docs/EXECUTAR.md** para uso básico

### Para Usuários Avançados
1. Explore **src/** para entender o código
2. Execute **scripts/gerar_resultados.py** para análise completa
3. Consulte **docs/COMO_USAR.md** para personalização

### Para Desenvolvedores
1. Leia **docs/CONTRIBUTING.md**
2. Analise **src/** e **setup.py**
3. Execute testes e contribua

## 🔧 Instalação e Uso

### Instalação Local
```bash
pip install -e .
```

### Execução Rápida
```bash
# Teste básico
python examples/teste_simples.py

# Análise completa
python scripts/gerar_resultados.py
```

### Importação como Pacote
```python
from src import FinancialImpactAnalyzer
analyzer = FinancialImpactAnalyzer()
```

---

Esta estrutura garante organização, escalabilidade e facilidade de manutenção do projeto Control Fintech.
