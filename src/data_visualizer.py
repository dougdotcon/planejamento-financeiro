"""
Visualizador de Dados Financeiros
Gera gráficos e relatórios visuais sobre impacto financeiro
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import argparse
from financial_impact_analyzer import FinancialImpactAnalyzer
from opportunity_cost_calculator import OpportunityCostCalculator

# Configuração para português
plt.rcParams['font.family'] = 'DejaVu Sans'
sns.set_style("whitegrid")
sns.set_palette("husl")

class FinancialDataVisualizer:
    def __init__(self):
        self.analyzer = FinancialImpactAnalyzer()
        self.calculator = OpportunityCostCalculator()
        
    def create_opportunity_cost_chart(self, amounts, years=10):
        """
        Cria gráfico de custo de oportunidade para diferentes valores
        """
        fig, ax = plt.subplots(figsize=(12, 8))
        
        investment_types = ['conservador', 'moderado', 'agressivo']
        colors = ['#2E86AB', '#A23B72', '#F18F01']
        
        x = np.arange(len(amounts))
        width = 0.25
        
        for i, inv_type in enumerate(investment_types):
            rate = self.calculator.investment_rates[inv_type]
            opportunity_costs = [amount * (1 + rate) ** years - amount for amount in amounts]
            
            ax.bar(x + i * width, opportunity_costs, width, 
                   label=f'{inv_type.capitalize()} ({rate*100:.0f}%)', 
                   color=colors[i], alpha=0.8)
        
        ax.set_xlabel('Valores Gastos (R$)', fontsize=12)
        ax.set_ylabel('Custo de Oportunidade (R$)', fontsize=12)
        ax.set_title(f'Custo de Oportunidade por Tipo de Investimento ({years} anos)', 
                     fontsize=14, fontweight='bold')
        ax.set_xticks(x + width)
        ax.set_xticklabels([f'R$ {amount:,.0f}' for amount in amounts])
        ax.legend()
        
        # Formato dos valores no eixo Y
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x:,.0f}'))
        
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('opportunity_cost_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_lifetime_impact_visualization(self, profiles):
        """
        Visualiza o impacto ao longo da vida para diferentes perfis
        """
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        
        profile_names = list(profiles.keys())
        
        # 1. Desperdício total
        total_wastes = [profiles[name]['total_waste'] for name in profile_names]
        ax1.bar(profile_names, total_wastes, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        ax1.set_title('Desperdício Total na Vida', fontweight='bold')
        ax1.set_ylabel('Valor (R$)')
        ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x/1000:.0f}k'))
        
        # 2. Anos de vida desperdiçados
        years_wasted = [profiles[name]['total_years_life_wasted'] for name in profile_names]
        ax2.bar(profile_names, years_wasted, color=['#96CEB4', '#FFEAA7', '#DDA0DD'])
        ax2.set_title('Anos de Vida "Desperdiçados"', fontweight='bold')
        ax2.set_ylabel('Anos')
        
        # 3. Percentual da renda desperdiçada
        percentages = [profiles[name]['percentage_income_wasted'] for name in profile_names]
        ax3.pie(percentages, labels=profile_names, autopct='%1.1f%%', 
                colors=['#FF7675', '#74B9FF', '#00B894'])
        ax3.set_title('% da Renda Desperdiçada', fontweight='bold')
        
        # 4. Custo de oportunidade
        opportunity_costs = [profiles[name]['opportunity_cost'] for name in profile_names]
        ax4.bar(profile_names, opportunity_costs, color=['#E17055', '#00CEC9', '#6C5CE7'])
        ax4.set_title('Custo de Oportunidade', fontweight='bold')
        ax4.set_ylabel('Valor (R$)')
        ax4.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x/1000:.0f}k'))
        
        plt.tight_layout()
        plt.savefig('lifetime_impact_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_category_spending_heatmap(self):
        """
        Cria mapa de calor dos gastos por categoria
        """
        categories = self.analyzer.generate_spending_categories_analysis()
        
        # Preparar dados
        data = []
        for category, info in categories.items():
            data.append({
                'Categoria': category,
                'Custo Mensal': info['monthly_cost'],
                'Necessidade': info['necessity_score'],
                'Custo Oportunidade 10 anos': info['10_year_opportunity_cost'],
                'Valor Futuro Perdido': info['future_value_if_invested']
            })
        
        df = pd.DataFrame(data)
        
        # Normalizar valores para o heatmap
        df_norm = df.copy()
        for col in ['Custo Mensal', 'Custo Oportunidade 10 anos', 'Valor Futuro Perdido']:
            df_norm[col] = (df_norm[col] - df_norm[col].min()) / (df_norm[col].max() - df_norm[col].min())
        
        # Criar heatmap
        fig, ax = plt.subplots(figsize=(12, 8))
        
        heatmap_data = df_norm[['Custo Mensal', 'Necessidade', 'Custo Oportunidade 10 anos']].T
        
        sns.heatmap(heatmap_data, 
                    xticklabels=df['Categoria'],
                    yticklabels=['Custo Mensal', 'Necessidade', 'Custo Oportunidade'],
                    annot=True, 
                    fmt='.2f', 
                    cmap='RdYlBu_r',
                    ax=ax)
        
        ax.set_title('Análise de Categorias de Gastos\n(Valores Normalizados)', 
                     fontsize=14, fontweight='bold')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('category_spending_heatmap.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_compound_interest_visualization(self, principal=1000, years=30):
        """
        Visualiza o poder dos juros compostos
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        years_range = range(1, years + 1)
        
        # Gráfico 1: Crescimento do investimento
        for inv_type, rate in self.calculator.investment_rates.items():
            values = [principal * (1 + rate) ** year for year in years_range]
            ax1.plot(years_range, values, marker='o', label=f'{inv_type.capitalize()} ({rate*100:.0f}%)')
        
        ax1.set_xlabel('Anos')
        ax1.set_ylabel('Valor (R$)')
        ax1.set_title('Crescimento de R$ 1.000 ao Longo do Tempo')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x:,.0f}'))
        
        # Gráfico 2: Comparação linear vs exponencial
        linear_growth = [principal + (principal * 0.10 * year) for year in years_range]
        compound_growth = [principal * (1.10) ** year for year in years_range]
        
        ax2.plot(years_range, linear_growth, label='Crescimento Linear (10%)', 
                 linestyle='--', linewidth=2)
        ax2.plot(years_range, compound_growth, label='Juros Compostos (10%)', 
                 linewidth=2)
        ax2.fill_between(years_range, linear_growth, compound_growth, 
                        alpha=0.3, label='Diferença')
        
        ax2.set_xlabel('Anos')
        ax2.set_ylabel('Valor (R$)')
        ax2.set_title('Linear vs Juros Compostos')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'R$ {x:,.0f}'))
        
        plt.tight_layout()
        plt.savefig('compound_interest_power.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_interactive_dashboard(self, profile_data):
        """
        Cria dashboard interativo com Plotly
        """
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Custo de Oportunidade por Idade', 
                           'Distribuição de Gastos por Categoria',
                           'Evolução Patrimonial', 
                           'Tempo vs Dinheiro'),
            specs=[[{"secondary_y": True}, {"type": "pie"}],
                   [{"secondary_y": True}, {"type": "bar"}]]
        )
        
        # Gráfico 1: Custo de oportunidade por idade
        ages = list(range(25, 66))
        opportunity_costs = []
        for age in ages:
            impact = self.analyzer.analyze_lifetime_impact(age, 1000, 5000)
            opportunity_costs.append(impact['opportunity_cost'])
        
        fig.add_trace(
            go.Scatter(x=ages, y=opportunity_costs, name="Custo de Oportunidade",
                      line=dict(color='#FF6B6B', width=3)),
            row=1, col=1
        )
        
        # Gráfico 2: Pizza de categorias
        categories = self.analyzer.generate_spending_categories_analysis()
        cat_names = list(categories.keys())
        cat_values = [categories[cat]['monthly_cost'] for cat in cat_names]
        
        fig.add_trace(
            go.Pie(labels=cat_names, values=cat_values, name="Gastos por Categoria"),
            row=1, col=2
        )
        
        # Gráfico 3: Evolução patrimonial
        years = list(range(1, 31))
        patrimonio_controlado = []
        patrimonio_descontrolado = []
        
        for year in years:
            # Cenário controlado (poupança 20%)
            patrimonio_controlado.append(1000 * year * (1.10 ** year))
            # Cenário descontrolado (poupança 5%)
            patrimonio_descontrolado.append(250 * year * (1.10 ** year))
        
        fig.add_trace(
            go.Scatter(x=years, y=patrimonio_controlado, name="Controlado (20% poupança)",
                      line=dict(color='#4ECDC4', width=3)),
            row=2, col=1
        )
        fig.add_trace(
            go.Scatter(x=years, y=patrimonio_descontrolado, name="Descontrolado (5% poupança)",
                      line=dict(color='#FF6B6B', width=3)),
            row=2, col=1
        )
        
        # Gráfico 4: Tempo vs Dinheiro
        gastos = [500, 1000, 1500, 2000, 2500]
        horas_trabalho = [gasto / 25 for gasto in gastos]  # R$ 25/hora
        
        fig.add_trace(
            go.Bar(x=[f'R$ {gasto}' for gasto in gastos], y=horas_trabalho,
                  name="Horas de Trabalho", marker_color='#45B7D1'),
            row=2, col=2
        )
        
        fig.update_layout(height=800, showlegend=True, 
                         title_text="Dashboard Financeiro Interativo")
        
        fig.write_html("financial_dashboard.html")
        fig.show()
        
    def generate_all_visualizations(self, profile='default'):
        """
        Gera todas as visualizações
        """
        print("Gerando visualizações...")
        
        # Dados de exemplo
        scenarios = {
            'Jovem Profissional': {
                'age': 25,
                'monthly_waste': 800,
                'monthly_income': 4000
            },
            'Família Classe Média': {
                'age': 35,
                'monthly_waste': 1200,
                'monthly_income': 8000
            },
            'Profissional Sênior': {
                'age': 45,
                'monthly_waste': 1500,
                'monthly_income': 12000
            }
        }
        
        # Analisar cenários
        results = self.analyzer.compare_scenarios(scenarios)
        
        # Gerar gráficos
        print("1. Criando gráfico de custo de oportunidade...")
        self.create_opportunity_cost_chart([1000, 5000, 10000, 20000, 50000])
        
        print("2. Criando análise de impacto ao longo da vida...")
        self.create_lifetime_impact_visualization(results)
        
        print("3. Criando mapa de calor de categorias...")
        self.create_category_spending_heatmap()
        
        print("4. Criando visualização de juros compostos...")
        self.create_compound_interest_visualization()
        
        print("5. Criando dashboard interativo...")
        self.create_interactive_dashboard(results)
        
        print("Todas as visualizações foram geradas!")
        print("Arquivos criados:")
        print("- opportunity_cost_comparison.png")
        print("- lifetime_impact_analysis.png")
        print("- category_spending_heatmap.png")
        print("- compound_interest_power.png")
        print("- financial_dashboard.html")

def main():
    parser = argparse.ArgumentParser(description='Gerador de Visualizações Financeiras')
    parser.add_argument('--profile', default='default', help='Perfil de análise')
    parser.add_argument('--all', action='store_true', help='Gerar todas as visualizações')
    
    args = parser.parse_args()
    
    visualizer = FinancialDataVisualizer()
    
    if args.all:
        visualizer.generate_all_visualizations(args.profile)
    else:
        print("Use --all para gerar todas as visualizações")
        print("Exemplo: python data_visualizer.py --all")

if __name__ == "__main__":
    main()
