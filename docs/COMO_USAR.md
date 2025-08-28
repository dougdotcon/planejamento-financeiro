# 🚀 Como Usar o Control Fintech

## Instalação Rápida

1. **Clone ou baixe os arquivos**
2. **Instale as dependências**:
```bash
pip install pandas numpy matplotlib seaborn plotly scipy
```

## Execução Rápida

### 🧪 Teste Básico
```bash
python teste_simples.py
```
Este comando mostra um exemplo rápido das análises disponíveis.

### 📊 Análise Completa
```bash
python run_analysis.py
```
Gera relatório completo com todas as visualizações.

### 🔍 Análises Específicas

#### Calculadora de Custo de Oportunidade
```bash
# Analisar seus gastos pessoais
python opportunity_cost_calculator.py --renda 5000 --gastos 1200 --anos 10

# Analisar um valor específico
python opportunity_cost_calculator.py --valor 8000 --anos 5
```

#### Comparação de Estilos de Vida
```bash
python lifestyle_comparison.py
```

#### Análise Comportamental
```bash
python behavioral_economics.py
```

#### Gerador de Visualizações
```bash
python data_visualizer.py --all
```

## 📈 Exemplos Práticos

### Exemplo 1: Analisando seus gastos mensais
```python
from financial_impact_analyzer import FinancialImpactAnalyzer

analyzer = FinancialImpactAnalyzer()

# Seus dados
idade = 30
gastos_desnecessarios = 1000  # R$ por mês
renda_mensal = 6000

# Análise
resultado = analyzer.analyze_lifetime_impact(idade, gastos_desnecessarios, renda_mensal)

print(f"Você desperdiça R$ {resultado['total_waste']:,.2f} ao longo da vida")
print(f"Isso representa {resultado['total_years_life_wasted']:.1f} anos trabalhando")
```

### Exemplo 2: Comparando uma compra
```python
from opportunity_cost_calculator import OpportunityCostCalculator

calc = OpportunityCostCalculator()

# Comparar comprar vs investir
resultado = calc.compare_purchase_vs_investment(5000, 5, 'moderado')

for categoria, dados in resultado.items():
    print(f"{categoria}: Custo oportunidade R$ {dados['opportunity_cost']:,.2f}")
```

## 📊 Outputs Gerados

### Arquivos de Relatório
- `relatorio_financeiro_completo_YYYYMMDD_HHMMSS.md` - Relatório completo em markdown
- `financial_dashboard.html` - Dashboard interativo

### Gráficos Gerados
- `opportunity_cost_comparison.png` - Comparação de custos de oportunidade
- `lifetime_impact_analysis.png` - Análise de impacto ao longo da vida
- `category_spending_heatmap.png` - Mapa de calor de gastos por categoria
- `compound_interest_power.png` - Poder dos juros compostos

## 🎯 Casos de Uso

### Para Indivíduos
1. **Análise Pessoal**: Descubra quanto você perde com gastos desnecessários
2. **Planejamento**: Use os dados para definir metas financeiras
3. **Educação**: Entenda o impacto real de suas decisões

### Para Educadores Financeiros
1. **Material Didático**: Use os gráficos e relatórios em apresentações
2. **Exemplos Práticos**: Demonstre conceitos com dados reais
3. **Ferramentas**: Ofereça calculadoras para seus clientes

### Para Pesquisadores
1. **Base de Dados**: Use as estatísticas brasileiras compiladas
2. **Metodologia**: Adapte os cálculos para suas pesquisas
3. **Visualizações**: Gere gráficos para publicações

## 🔧 Personalização

### Modificar Parâmetros
Edite os arquivos para ajustar:
- Taxa de retorno de investimentos (padrão: 10%)
- Taxa de inflação (padrão: 4.5%)
- Idade de aposentadoria (padrão: 65 anos)

### Adicionar Categorias
No arquivo `financial_impact_analyzer.py`, seção `generate_spending_categories_analysis()`:
```python
'Nova Categoria': {'monthly': 200, 'necessity_score': 3}
```

### Criar Novos Perfis
No arquivo `lifestyle_comparison.py`, adicione novos perfis na função `_create_lifestyle_profiles()`.

## 🆘 Resolução de Problemas

### Erro de Importação
```bash
pip install --upgrade pandas numpy matplotlib seaborn
```

### Gráficos não aparecem
```bash
pip install plotly
```

### Erro de encoding
Certifique-se de que os arquivos estão salvos em UTF-8.

## 📚 Entendendo os Resultados

### Custo de Oportunidade
- **O que é**: Valor que você perdeu por não investir o dinheiro
- **Como ler**: Quanto maior, mais você "perdeu" ao gastar

### Anos de Vida Desperdiçados
- **O que é**: Tempo trabalhando para pagar gastos desnecessários
- **Como ler**: Cada ano representa 365 dias dedicados a pagar algo que não agregou valor

### Valor Futuro Perdido
- **O que é**: Quanto o dinheiro valeria se tivesse sido investido
- **Como ler**: A diferença entre o que você gastou e o que poderia ter

## 💡 Dicas de Uso

1. **Execute mensalmente** para acompanhar progresso
2. **Compare cenários** antes de grandes decisões
3. **Use os gráficos** para motivação visual
4. **Compartilhe** os resultados com família/amigos
5. **Adapte** os parâmetros à sua realidade

## 🎓 Próximos Passos

Depois de usar as ferramentas:
1. **Defina metas** baseadas nos resultados
2. **Implemente mudanças** gradualmente
3. **Monitore progresso** mensalmente
4. **Eduque-se** sobre investimentos
5. **Mantenha disciplina** financeira

---

**Lembre-se**: O objetivo não é eliminar todo prazer da vida, mas sim tomar decisões conscientes sobre onde vale a pena gastar seu dinheiro e tempo!

🚀 **Comece agora**: `python teste_simples.py`
