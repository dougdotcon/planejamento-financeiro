"""
Analisador de Impacto Financeiro
Calcula o verdadeiro custo das decisões financeiras ao longo do tempo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import json
from dados_oficiais import dados_brasil

class FinancialImpactAnalyzer:
    def __init__(self):
        # DADOS REAIS ATUALIZADOS (2025)
        self.inflation_rate = dados_brasil.indicadores_bc['inflacao_atual'] / 100  # 4.86% (projeção 2025)
        self.investment_return = dados_brasil.get_taxa_investimento_moderado() / 100  # 14% (CDB digitais)
        self.life_expectancy = dados_brasil.demografia['expectativa_vida']  # 76.4 anos
        self.retirement_age = dados_brasil.demografia['idade_aposentadoria_media']  # 65 anos
        
        # Taxas de investimento por perfil (dados reais 2025)
        self.investment_rates = {
            'conservador': dados_brasil.get_taxa_investimento_conservador() / 100,  # Tesouro IPCA+
            'moderado': dados_brasil.get_taxa_investimento_moderado() / 100,       # CDB 99% CDI
            'agressivo': dados_brasil.get_taxa_investimento_agressivo() / 100      # Ações + dividendos
        }
        
    def calculate_opportunity_cost(self, amount, years, investment_rate=None):
        """
        Calcula o custo de oportunidade de um gasto
        """
        if investment_rate is None:
            investment_rate = self.investment_return
            
        future_value_invested = amount * (1 + investment_rate) ** years
        return {
            'amount_spent': amount,
            'years': years,
            'opportunity_cost': future_value_invested - amount,
            'future_value_if_invested': future_value_invested,
            'total_loss': future_value_invested
        }
    
    def analyze_lifetime_impact(self, current_age, monthly_waste, monthly_income):
        """
        Analisa o impacto ao longo da vida
        """
        working_years = self.retirement_age - current_age
        annual_waste = monthly_waste * 12
        annual_income = monthly_income * 12
        
        # Cálculo do impacto cumulativo
        total_waste = annual_waste * working_years
        opportunity_cost = self.calculate_opportunity_cost(
            annual_waste, working_years
        )
        
        # Tempo de vida "perdido" trabalhando para gastos desnecessários
        percentage_wasted = (monthly_waste / monthly_income) * 100
        days_per_year_wasted = (percentage_wasted / 100) * 365
        total_days_wasted = days_per_year_wasted * working_years
        years_wasted = total_days_wasted / 365
        
        return {
            'working_years_remaining': working_years,
            'total_waste': total_waste,
            'opportunity_cost': opportunity_cost['opportunity_cost'],
            'future_value_lost': opportunity_cost['future_value_if_invested'],
            'percentage_income_wasted': percentage_wasted,
            'days_per_year_wasted': days_per_year_wasted,
            'total_years_life_wasted': years_wasted,
            'potential_early_retirement_years': years_wasted / 5  # Estimativa conservadora
        }
    
    def compare_scenarios(self, scenarios):
        """
        Compara diferentes cenários de gastos
        """
        results = {}
        
        for name, scenario in scenarios.items():
            impact = self.analyze_lifetime_impact(
                scenario['age'],
                scenario['monthly_waste'],
                scenario['monthly_income']
            )
            results[name] = impact
            
        return results
    
    def generate_spending_categories_analysis(self):
        """
        Análise de categorias de gastos brasileiros baseada em dados reais (2024-2025)
        Fontes: IBGE POF, Associações Setoriais, Pesquisas de Mercado
        """
        # Usando dados reais do módulo dados_oficiais
        gastos_reais = dados_brasil.gastos_desnecessarios
        
        categories = {
            'Alimentação Fora': {
                'monthly': gastos_reais['alimentacao_fora']['valor_medio_mensal'],
                'necessity_score': gastos_reais['alimentacao_fora']['necessidade']
            },
            'Streaming/Assinaturas': {
                'monthly': gastos_reais['streaming_assinaturas']['valor_medio_mensal'],
                'necessity_score': gastos_reais['streaming_assinaturas']['necessidade']
            },
            'Delivery Apps': {
                'monthly': gastos_reais['delivery_apps']['valor_medio_mensal'],
                'necessity_score': gastos_reais['delivery_apps']['necessidade']
            },
            'Roupas/Acessórios': {
                'monthly': gastos_reais['roupas_acessorios']['valor_medio_mensal'],
                'necessity_score': gastos_reais['roupas_acessorios']['necessidade']
            },
            'Bebidas Alcoólicas': {
                'monthly': gastos_reais['bebidas_alcoolicas']['valor_medio_mensal'],
                'necessity_score': gastos_reais['bebidas_alcoolicas']['necessidade']
            },
            'Cigarro/Tabaco': {
                'monthly': gastos_reais['cigarro_tabaco']['valor_medio_mensal'],
                'necessity_score': gastos_reais['cigarro_tabaco']['necessidade']
            },
            'Transporte Desnecessário': {
                'monthly': gastos_reais['transporte_desnecessario']['valor_medio_mensal'],
                'necessity_score': gastos_reais['transporte_desnecessario']['necessidade']
            },
            'Compras Impulsivas': {
                'monthly': gastos_reais['compras_impulso']['valor_medio_mensal'],
                'necessity_score': gastos_reais['compras_impulso']['necessidade']
            },
            'Jogos/Apostas Online': {
                'monthly': gastos_reais['jogos_apostas']['valor_medio_mensal'],
                'necessity_score': gastos_reais['jogos_apostas']['necessidade']
            }
        }
        
        analysis = {}
        for category, data in categories.items():
            cost_10_years = self.calculate_opportunity_cost(
                data['monthly'] * 12, 10
            )
            
            analysis[category] = {
                'monthly_cost': data['monthly'],
                'annual_cost': data['monthly'] * 12,
                'necessity_score': data['necessity_score'],
                '10_year_opportunity_cost': cost_10_years['opportunity_cost'],
                'future_value_if_invested': cost_10_years['future_value_if_invested']
            }
            
        return analysis
    
    def calculate_financial_freedom_timeline(self, current_savings, monthly_savings, 
                                          target_multiplier=25):
        """
        Calcula tempo para independência financeira (regra 4%)
        """
        monthly_expenses = monthly_savings / 0.2  # Assumindo 20% de taxa de poupança
        target_amount = monthly_expenses * 12 * target_multiplier
        
        # Cálculo com juros compostos
        months = np.log(1 + (target_amount * self.investment_return/12) / 
                       (monthly_savings + current_savings * self.investment_return/12)) / np.log(1 + self.investment_return/12)
        
        years = months / 12
        
        return {
            'target_amount': target_amount,
            'monthly_expenses': monthly_expenses,
            'years_to_freedom': years,
            'current_savings': current_savings,
            'monthly_savings': monthly_savings
        }

def main():
    analyzer = FinancialImpactAnalyzer()
    
    # Exemplo de análise
    print("=== ANÁLISE DE IMPACTO FINANCEIRO ===\n")
    
    # Cenários de exemplo
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
    
    results = analyzer.compare_scenarios(scenarios)
    
    for scenario_name, result in results.items():
        print(f"--- {scenario_name} ---")
        print(f"Desperdício total na vida: R$ {result['total_waste']:,.2f}")
        print(f"Custo de oportunidade: R$ {result['opportunity_cost']:,.2f}")
        print(f"Valor futuro perdido: R$ {result['future_value_lost']:,.2f}")
        print(f"Anos de vida 'desperdiçados': {result['total_years_life_wasted']:.1f}")
        print(f"Potencial aposentadoria antecipada: {result['potential_early_retirement_years']:.1f} anos")
        print(f"% da renda desperdiçada: {result['percentage_income_wasted']:.1f}%\n")
    
    # Análise por categorias
    print("=== ANÁLISE POR CATEGORIAS DE GASTOS ===\n")
    categories = analyzer.generate_spending_categories_analysis()
    
    for category, data in sorted(categories.items(), 
                                key=lambda x: x[1]['10_year_opportunity_cost'], 
                                reverse=True):
        print(f"{category}:")
        print(f"  Mensal: R$ {data['monthly_cost']}")
        print(f"  Custo oportunidade (10 anos): R$ {data['10_year_opportunity_cost']:,.2f}")
        print(f"  Valor futuro perdido: R$ {data['future_value_if_invested']:,.2f}")
        print(f"  Necessidade (0-5): {data['necessity_score']}\n")
    
    # Análise de liberdade financeira
    print("=== CENÁRIO DE LIBERDADE FINANCEIRA ===\n")
    freedom = analyzer.calculate_financial_freedom_timeline(
        current_savings=50000,
        monthly_savings=2000
    )
    
    print(f"Valor necessário para independência: R$ {freedom['target_amount']:,.2f}")
    print(f"Anos para liberdade financeira: {freedom['years_to_freedom']:.1f}")
    print(f"Gastos mensais estimados: R$ {freedom['monthly_expenses']:,.2f}")

if __name__ == "__main__":
    main()
