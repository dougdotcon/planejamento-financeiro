"""
Script para gerar todos os resultados e salvar na pasta 'resultados'
"""

import os
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from financial_impact_analyzer import FinancialImpactAnalyzer
from opportunity_cost_calculator import OpportunityCostCalculator
from lifestyle_comparison import LifestyleComparator
from behavioral_economics import BehavioralEconomicsAnalyzer
from data_visualizer import FinancialDataVisualizer

# Criar pasta de resultados se não existir
if not os.path.exists('resultados'):
    os.makedirs('resultados')

def main():
    print("=== GERANDO RESULTADOS COMPLETOS ===\n")
    
    # Inicializar analisadores
    impact_analyzer = FinancialImpactAnalyzer()
    cost_calculator = OpportunityCostCalculator()
    lifestyle_comparator = LifestyleComparator()
    behavioral_analyzer = BehavioralEconomicsAnalyzer()
    
    # 1. Análise de Cenários de Vida
    print("1. Analisando cenários de vida...")
    scenarios = {
        'Jovem Profissional (25 anos)': {
            'age': 25,
            'monthly_waste': 800,
            'monthly_income': 4000
        },
        'Família Classe Média (35 anos)': {
            'age': 35,
            'monthly_waste': 1200,
            'monthly_income': 8000
        },
        'Profissional Sênior (45 anos)': {
            'age': 45,
            'monthly_waste': 1500,
            'monthly_income': 12000
        }
    }
    
    results = impact_analyzer.compare_scenarios(scenarios)
    
    # Salvar dados dos cenários
    scenario_data = []
    for name, result in results.items():
        scenario_data.append({
            'Cenário': name,
            'Desperdício Total': result['total_waste'],
            'Custo Oportunidade': result['opportunity_cost'],
            'Anos Desperdiçados': result['total_years_life_wasted'],
            'Aposentadoria Antecipada': result['potential_early_retirement_years'],
            '% Renda Desperdiçada': result['percentage_income_wasted']
        })
    
    df_scenarios = pd.DataFrame(scenario_data)
    df_scenarios.to_csv('resultados/analise_cenarios.csv', index=False)
    
    # 2. Análise por Categorias
    print("2. Analisando categorias de gastos...")
    categories = impact_analyzer.generate_spending_categories_analysis()
    
    category_data = []
    for category, data in categories.items():
        category_data.append({
            'Categoria': category,
            'Custo Mensal': data['monthly_cost'],
            'Custo Anual': data['annual_cost'],
            'Score Necessidade': data['necessity_score'],
            'Custo Oportunidade 10 anos': data['10_year_opportunity_cost'],
            'Valor Futuro Perdido': data['future_value_if_invested']
        })
    
    df_categories = pd.DataFrame(category_data)
    df_categories = df_categories.sort_values('Custo Oportunidade 10 anos', ascending=False)
    df_categories.to_csv('resultados/analise_categorias.csv', index=False)
    
    # 3. Comparação de Estilos de Vida
    print("3. Comparando estilos de vida...")
    lifestyle_comparison = lifestyle_comparator.compare_all_profiles()
    lifestyle_comparison.to_csv('resultados/comparacao_estilos_vida.csv', index=False)
    
    # 4. Análise Comportamental
    print("4. Executando análise comportamental...")
    rational_budget = {
        'alimentacao': 800,
        'transporte': 400,
        'entretenimento': 300,
        'compras_impulso': 100,
        'saude': 200,
        'educacao': 150
    }
    
    behavioral_results = {}
    for profile in ['controlado', 'medio', 'impulsivo']:
        simulation = behavioral_analyzer.simulate_monthly_spending(rational_budget, profile)
        behavioral_cost = behavioral_analyzer.calculate_behavioral_cost(
            rational_budget, simulation['monthly_totals']
        )
        behavioral_results[profile] = behavioral_cost
    
    # Salvar análise comportamental
    behavioral_data = []
    for profile, data in behavioral_results.items():
        behavioral_data.append({
            'Perfil': profile.capitalize(),
            'Excesso Mensal': data['total_excess'],
            'Excesso %': data['total_excess_percentage'],
            'Custo Oportunidade Anual': data['annual_opportunity_cost'],
            'Custo Oportunidade 10 anos': data['decade_opportunity_cost']
        })
    
    df_behavioral = pd.DataFrame(behavioral_data)
    df_behavioral.to_csv('resultados/analise_comportamental.csv', index=False)
    
    # 5. Gerar Visualizações
    print("5. Gerando visualizações...")
    
    # Gráfico 1: Custo de Oportunidade por Valores
    plt.figure(figsize=(12, 8))
    amounts = [1000, 5000, 10000, 20000, 50000]
    years = 10
    
    investment_types = ['conservador', 'moderado', 'agressivo']
    colors = ['#2E86AB', '#A23B72', '#F18F01']
    rates = [0.08, 0.10, 0.12]
    
    x = range(len(amounts))
    width = 0.25
    
    for i, (inv_type, rate, color) in enumerate(zip(investment_types, rates, colors)):
        opportunity_costs = [amount * (1 + rate) ** years - amount for amount in amounts]
        plt.bar([pos + i * width for pos in x], opportunity_costs, width, 
               label=f'{inv_type.capitalize()} ({rate*100:.0f}%)', 
               color=color, alpha=0.8)
    
    plt.xlabel('Valores Gastos (R$)', fontsize=12)
    plt.ylabel('Custo de Oportunidade (R$)', fontsize=12)
    plt.title(f'Custo de Oportunidade por Tipo de Investimento ({years} anos)', 
             fontsize=14, fontweight='bold')
    plt.xticks([pos + width for pos in x], [f'R$ {amount:,.0f}' for amount in amounts])
    plt.legend()
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x:,.0f}'))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('resultados/opportunity_cost_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Gráfico 2: Impacto por Cenário
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    profile_names = list(results.keys())
    
    # Desperdício total
    total_wastes = [results[name]['total_waste'] for name in profile_names]
    ax1.bar(range(len(profile_names)), total_wastes, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    ax1.set_title('Desperdício Total na Vida', fontweight='bold')
    ax1.set_ylabel('Valor (R$)')
    ax1.set_xticks(range(len(profile_names)))
    ax1.set_xticklabels([name.split('(')[0].strip() for name in profile_names], rotation=45)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x/1000:.0f}k'))
    
    # Anos desperdiçados
    years_wasted = [results[name]['total_years_life_wasted'] for name in profile_names]
    ax2.bar(range(len(profile_names)), years_wasted, color=['#96CEB4', '#FFEAA7', '#DDA0DD'])
    ax2.set_title('Anos de Vida "Desperdiçados"', fontweight='bold')
    ax2.set_ylabel('Anos')
    ax2.set_xticks(range(len(profile_names)))
    ax2.set_xticklabels([name.split('(')[0].strip() for name in profile_names], rotation=45)
    
    # Percentual desperdiçado
    percentages = [results[name]['percentage_income_wasted'] for name in profile_names]
    ax3.pie(percentages, labels=[name.split('(')[0].strip() for name in profile_names], 
            autopct='%1.1f%%', colors=['#FF7675', '#74B9FF', '#00B894'])
    ax3.set_title('% da Renda Desperdiçada', fontweight='bold')
    
    # Custo de oportunidade
    opportunity_costs = [results[name]['opportunity_cost'] for name in profile_names]
    ax4.bar(range(len(profile_names)), opportunity_costs, color=['#E17055', '#00CEC9', '#6C5CE7'])
    ax4.set_title('Custo de Oportunidade', fontweight='bold')
    ax4.set_ylabel('Valor (R$)')
    ax4.set_xticks(range(len(profile_names)))
    ax4.set_xticklabels([name.split('(')[0].strip() for name in profile_names], rotation=45)
    ax4.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x/1000:.0f}k'))
    
    plt.tight_layout()
    plt.savefig('resultados/lifetime_impact_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Gráfico 3: Mapa de Calor Categorias
    import seaborn as sns
    
    plt.figure(figsize=(12, 8))
    
    # Preparar dados para heatmap
    heatmap_data = []
    categories_list = list(categories.keys())
    
    for category in categories_list:
        data = categories[category]
        heatmap_data.append([
            data['monthly_cost'] / max([categories[c]['monthly_cost'] for c in categories_list]),
            data['necessity_score'] / 5,
            data['10_year_opportunity_cost'] / max([categories[c]['10_year_opportunity_cost'] for c in categories_list])
        ])
    
    df_heatmap = pd.DataFrame(heatmap_data, 
                             index=categories_list,
                             columns=['Custo Mensal', 'Necessidade', 'Custo Oportunidade'])
    
    sns.heatmap(df_heatmap, annot=True, fmt='.2f', cmap='RdYlBu_r')
    plt.title('Análise de Categorias de Gastos\n(Valores Normalizados)', 
             fontsize=14, fontweight='bold')
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig('resultados/category_spending_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Gráfico 4: Poder dos Juros Compostos
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    principal = 1000
    years_range = range(1, 31)
    
    # Crescimento por tipo de investimento
    for inv_type, rate, color in zip(investment_types, rates, colors):
        values = [principal * (1 + rate) ** year for year in years_range]
        ax1.plot(years_range, values, marker='o', label=f'{inv_type.capitalize()} ({rate*100:.0f}%)', 
                color=color, linewidth=2)
    
    ax1.set_xlabel('Anos')
    ax1.set_ylabel('Valor (R$)')
    ax1.set_title('Crescimento de R$ 1.000 ao Longo do Tempo')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x:,.0f}'))
    
    # Linear vs Exponencial
    linear_growth = [principal + (principal * 0.10 * year) for year in years_range]
    compound_growth = [principal * (1.10) ** year for year in years_range]
    
    ax2.plot(years_range, linear_growth, label='Crescimento Linear (10%)', 
             linestyle='--', linewidth=3, color='#FF6B6B')
    ax2.plot(years_range, compound_growth, label='Juros Compostos (10%)', 
             linewidth=3, color='#4ECDC4')
    ax2.fill_between(years_range, linear_growth, compound_growth, 
                    alpha=0.3, color='#45B7D1', label='Diferença')
    
    ax2.set_xlabel('Anos')
    ax2.set_ylabel('Valor (R$)')
    ax2.set_title('Linear vs Juros Compostos')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x:,.0f}'))
    
    plt.tight_layout()
    plt.savefig('resultados/compound_interest_power.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 6. Gerar Relatório Final
    print("6. Gerando relatório final...")
    
    report = f"""# RELATÓRIO DE RESULTADOS - CONTROL FINTECH
Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

## RESUMO EXECUTIVO

Esta análise demonstra o impacto real das decisões financeiras cotidianas na vida de brasileiros de diferentes perfis.

## PRINCIPAIS DESCOBERTAS

### 1. Cenários de Vida Analisados
"""
    
    for name, result in results.items():
        report += f"""
**{name}**
- Desperdício total na vida: R$ {result['total_waste']:,.2f}
- Custo de oportunidade: R$ {result['opportunity_cost']:,.2f}
- Anos de vida desperdiçados: {result['total_years_life_wasted']:.1f}
- Potencial aposentadoria antecipada: {result['potential_early_retirement_years']:.1f} anos
"""
    
    report += f"""
### 2. Categorias Mais Impactantes (Top 5)
"""
    
    top_5_categories = df_categories.head(5)
    for _, row in top_5_categories.iterrows():
        report += f"""
**{row['Categoria']}**
- Custo mensal: R$ {row['Custo Mensal']:.2f}
- Custo oportunidade (10 anos): R$ {row['Custo Oportunidade 10 anos']:,.2f}
- Score necessidade: {row['Score Necessidade']}/5
"""
    
    report += f"""
### 3. Análise Comportamental

Os diferentes perfis comportamentais mostram variações significativas no desperdício:
"""
    
    for _, row in df_behavioral.iterrows():
        report += f"""
**Perfil {row['Perfil']}**
- Excesso mensal: R$ {row['Excesso Mensal']:.2f} ({row['Excesso %']:.1f}%)
- Custo oportunidade (10 anos): R$ {row['Custo Oportunidade 10 anos']:,.2f}
"""
    
    report += f"""
## CONCLUSÕES

1. **Impacto Significativo**: Pequenos gastos desnecessários podem custar centenas de milhares de reais ao longo da vida.

2. **Diferença de Perfis**: O perfil comportamental pode triplicar o custo de oportunidade.

3. **Categorias Críticas**: Alimentação fora, compras impulsivas e roupas são as categorias com maior impacto.

4. **Poder dos Juros Compostos**: A diferença entre crescimento linear e exponencial é dramática ao longo do tempo.

## RECOMENDAÇÕES

1. Foque nas categorias com maior custo de oportunidade
2. Desenvolva disciplina comportamental
3. Invista o dinheiro poupado consistentemente
4. Revise gastos mensalmente

---
*Relatório gerado automaticamente pelo sistema Control Fintech*
"""
    
    with open('resultados/relatorio_final.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print("\n✅ RESULTADOS GERADOS COM SUCESSO!")
    print("\nArquivos criados na pasta 'resultados':")
    print("📊 analise_cenarios.csv")
    print("📊 analise_categorias.csv") 
    print("📊 comparacao_estilos_vida.csv")
    print("📊 analise_comportamental.csv")
    print("📈 opportunity_cost_comparison.png")
    print("📈 lifetime_impact_analysis.png")
    print("📈 category_spending_heatmap.png")
    print("📈 compound_interest_power.png")
    print("📄 relatorio_final.md")

if __name__ == "__main__":
    main()
