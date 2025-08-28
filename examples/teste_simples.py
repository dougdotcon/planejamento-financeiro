"""
Teste simples das funcionalidades do Control Fintech
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from financial_impact_analyzer import FinancialImpactAnalyzer

def main():
    print("=== TESTE RÁPIDO DE ANÁLISE FINANCEIRA ===\n")
    
    analyzer = FinancialImpactAnalyzer()
    
    # Teste 1: Custo de oportunidade
    print("1. CUSTO DE OPORTUNIDADE")
    result = analyzer.calculate_opportunity_cost(1000, 10)
    print(f"Investindo R$ 1.000 por 10 anos:")
    print(f"Valor futuro: R$ {result['future_value_if_invested']:,.2f}")
    print(f"Custo de oportunidade: R$ {result['opportunity_cost']:,.2f}\n")
    
    # Teste 2: Análise de impacto na vida
    print("2. IMPACTO NA VIDA - JOVEM PROFISSIONAL")
    impact = analyzer.analyze_lifetime_impact(25, 800, 4000)
    print(f"Idade: 25 anos")
    print(f"Desperdício mensal: R$ 800")
    print(f"Renda mensal: R$ 4.000")
    print(f"Desperdício total na vida: R$ {impact['total_waste']:,.2f}")
    print(f"Custo de oportunidade: R$ {impact['opportunity_cost']:,.2f}")
    print(f"Anos de vida desperdiçados: {impact['total_years_life_wasted']:.1f}")
    print(f"Potencial aposentadoria antecipada: {impact['potential_early_retirement_years']:.1f} anos\n")
    
    # Teste 3: Análise por categorias
    print("3. ANÁLISE POR CATEGORIAS (TOP 3 MAIS CARAS)")
    categories = analyzer.generate_spending_categories_analysis()
    
    top_categories = sorted(categories.items(), 
                           key=lambda x: x[1]['10_year_opportunity_cost'], 
                           reverse=True)[:3]
    
    for category, data in top_categories:
        print(f"{category}:")
        print(f"  Custo mensal: R$ {data['monthly_cost']}")
        print(f"  Custo oportunidade (10 anos): R$ {data['10_year_opportunity_cost']:,.2f}")
    
    print(f"\n=== CONCLUSÃO ===")
    print("Pequenos gastos aparentemente insignificantes podem representar")
    print("enormes custos de oportunidade ao longo da vida!")
    print("\nPara análise completa, execute: python run_analysis.py")

if __name__ == "__main__":
    main()
