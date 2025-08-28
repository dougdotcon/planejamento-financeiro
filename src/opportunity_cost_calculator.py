"""
Calculadora de Custo de Oportunidade
Ferramenta interativa para calcular o impacto de decisões financeiras
"""

import argparse
import pandas as pd
import numpy as np
from datetime import datetime
import json
from dados_oficiais import dados_brasil

class OpportunityCostCalculator:
    def __init__(self):
        # TAXAS DE INVESTIMENTO REAIS (2025)
        self.investment_rates = {
            'conservador': dados_brasil.get_taxa_investimento_conservador() / 100,  # Tesouro IPCA+ real
            'moderado': dados_brasil.get_taxa_investimento_moderado() / 100,       # CDB 99% CDI
            'agressivo': dados_brasil.get_taxa_investimento_agressivo() / 100,     # Ações + dividendos
            'poupanca': dados_brasil.investimentos['poupanca'] / 100,              # Poupança atual
            'tesouro_selic': dados_brasil.investimentos['tesouro_selic'] / 100     # Tesouro Selic
        }
        
        # DADOS BRASILEIROS OFICIAIS (2025)
        self.brazilian_data = {
            'salario_minimo': dados_brasil.salario_minimo['valor'],                    # R$ 1.518 (2025)
            'renda_media': dados_brasil.renda_trabalho['renda_media_nacional'],       # R$ 3.200
            'renda_formal': dados_brasil.renda_trabalho['renda_media_formal'],        # R$ 4.500
            'inflacao_atual': dados_brasil.indicadores_bc['inflacao_atual'],         # 4,86%
            'selic_atual': dados_brasil.indicadores_bc['selic'],                     # 14,25%
            'horas_trabalho_mes': dados_brasil.renda_trabalho['horas_trabalho_mes'], # 192h
            'expectativa_vida': dados_brasil.demografia['expectativa_vida'],         # 76,4 anos
            'fonte': 'IBGE, Banco Central, Gov. Federal (2025)'
        }
    
    def calculate_time_cost(self, amount, hourly_wage):
        """
        Calcula quantas horas de trabalho custam um determinado valor
        """
        hours = amount / hourly_wage
        days = hours / 8  # 8 horas por dia
        weeks = days / 5  # 5 dias úteis por semana
        months = days / 22  # 22 dias úteis por mês
        
        return {
            'hours': hours,
            'days': days,
            'weeks': weeks,
            'months': months
        }
    
    def compare_purchase_vs_investment(self, purchase_amount, investment_period_years, 
                                     investment_type='moderado'):
        """
        Compara comprar algo vs investir o dinheiro
        """
        rate = self.investment_rates[investment_type]
        future_value = purchase_amount * (1 + rate) ** investment_period_years
        
        # Depreciação típica de produtos
        depreciation_rates = {
            'eletronicos': 0.3,  # 30% ao ano
            'veiculos': 0.15,    # 15% ao ano
            'roupas': 0.8,       # 80% no primeiro ano
            'moveis': 0.1        # 10% ao ano
        }
        
        results = {}
        for category, dep_rate in depreciation_rates.items():
            item_value = purchase_amount * (1 - dep_rate) ** investment_period_years
            opportunity_cost = future_value - item_value
            
            results[category] = {
                'item_future_value': item_value,
                'investment_future_value': future_value,
                'opportunity_cost': opportunity_cost,
                'cost_percentage': (opportunity_cost / purchase_amount) * 100
            }
        
        return results
    
    def analyze_subscription_services(self, monthly_cost, years=10):
        """
        Analisa o custo real de serviços de assinatura
        """
        total_paid = monthly_cost * 12 * years
        
        results = {}
        for investment_type, rate in self.investment_rates.items():
            # Valor futuro se investisse mensalmente
            future_value = monthly_cost * (((1 + rate/12) ** (12 * years) - 1) / (rate/12))
            opportunity_cost = future_value - total_paid
            
            results[investment_type] = {
                'total_paid': total_paid,
                'future_value_if_invested': future_value,
                'opportunity_cost': opportunity_cost,
                'multiplier': future_value / total_paid
            }
        
        return results
    
    def calculate_lifestyle_inflation_impact(self, base_salary, lifestyle_increase_rate, 
                                           years=20):
        """
        Calcula o impacto da inflação do estilo de vida
        """
        scenarios = {}
        
        # Cenário 1: Mantém padrão de vida
        maintained_lifestyle = {
            'annual_expenses': base_salary * 0.7,  # 70% da renda em gastos
            'annual_savings': base_salary * 0.3    # 30% em poupança
        }
        
        # Cenário 2: Inflação do estilo de vida
        inflated_lifestyle = {
            'annual_expenses': base_salary * 0.7 * (1 + lifestyle_increase_rate) ** years,
            'annual_savings': base_salary * 0.3 * (1 - lifestyle_increase_rate/2) ** years
        }
        
        for scenario_name, scenario in [('Controlado', maintained_lifestyle), 
                                       ('Inflacionado', inflated_lifestyle)]:
            
            # Cálculo de patrimônio acumulado
            total_savings = 0
            for year in range(years):
                if scenario_name == 'Controlado':
                    annual_saving = scenario['annual_savings']
                else:
                    annual_saving = base_salary * 0.3 * (1 - lifestyle_increase_rate/2) ** year
                
                total_savings += annual_saving * (1 + self.investment_rates['moderado']) ** (years - year)
            
            scenarios[scenario_name] = {
                'final_annual_expenses': scenario['annual_expenses'],
                'total_accumulated': total_savings,
                'years_of_expenses_covered': total_savings / scenario['annual_expenses']
            }
        
        return scenarios
    
    def generate_real_world_comparisons(self, amount):
        """
        Gera comparações com itens do mundo real
        """
        comparisons = {
            'Alimentação': {
                'refeicoes_restaurante': amount / 25,  # R$ 25 por refeição
                'meses_supermercado': amount / 600,     # R$ 600/mês supermercado
                'cafes_padaria': amount / 8             # R$ 8 café + pão
            },
            'Transporte': {
                'corridas_uber': amount / 15,           # R$ 15 por corrida
                'tanques_combustivel': amount / 300,    # R$ 300 tanque cheio
                'passagens_aereas_nacionais': amount / 400  # R$ 400 passagem média
            },
            'Educação': {
                'cursos_online': amount / 150,          # R$ 150 curso médio
                'livros': amount / 40,                  # R$ 40 por livro
                'mensalidades_faculdade': amount / 800   # R$ 800 mensalidade EAD
            },
            'Experiências': {
                'ingressos_cinema': amount / 30,        # R$ 30 ingresso
                'jantares_casal': amount / 120,         # R$ 120 jantar para dois
                'viagens_fim_semana': amount / 800      # R$ 800 viagem curta
            }
        }
        
        return comparisons
    
    def create_decision_matrix(self, options):
        """
        Cria matriz de decisão para múltiplas opções
        """
        results = []
        
        for option in options:
            name = option['name']
            cost = option['cost']
            utility_score = option.get('utility_score', 5)  # 1-10
            duration_years = option.get('duration_years', 1)
            
            # Custo de oportunidade
            opp_cost = self.calculate_opportunity_cost(cost, duration_years)
            
            # Score custo-benefício
            cost_benefit_score = utility_score / (cost / 1000)  # Normalizado
            
            results.append({
                'name': name,
                'cost': cost,
                'utility_score': utility_score,
                'opportunity_cost': opp_cost,
                'cost_benefit_score': cost_benefit_score,
                'recommendation': 'COMPRAR' if cost_benefit_score > 0.5 else 'NÃO COMPRAR'
            })
        
        # Ordenar por custo-benefício
        results.sort(key=lambda x: x['cost_benefit_score'], reverse=True)
        return results
    
    def calculate_opportunity_cost(self, amount, years, rate=0.10):
        """
        Cálculo básico de custo de oportunidade
        """
        future_value = amount * (1 + rate) ** years
        return future_value - amount

def main():
    parser = argparse.ArgumentParser(description='Calculadora de Custo de Oportunidade')
    parser.add_argument('--renda', type=float, help='Renda mensal em reais')
    parser.add_argument('--gastos', type=float, help='Gastos mensais desnecessários')
    parser.add_argument('--valor', type=float, help='Valor específico para análise')
    parser.add_argument('--anos', type=int, default=10, help='Período de análise em anos')
    
    args = parser.parse_args()
    
    calculator = OpportunityCostCalculator()
    
    print("=== CALCULADORA DE CUSTO DE OPORTUNIDADE ===\n")
    
    if args.renda and args.gastos:
        # Análise de gastos mensais
        hourly_wage = (args.renda * 12) / (calculator.brazilian_data['horas_trabalho_mes'] * 12)
        time_cost = calculator.calculate_time_cost(args.gastos, hourly_wage)
        
        print(f"--- ANÁLISE DE GASTOS MENSAIS ---")
        print(f"Renda mensal: R$ {args.renda:,.2f}")
        print(f"Gastos desnecessários: R$ {args.gastos:,.2f}")
        print(f"Salário por hora: R$ {hourly_wage:.2f}")
        print(f"\nTempo trabalhado para estes gastos:")
        print(f"  {time_cost['hours']:.1f} horas")
        print(f"  {time_cost['days']:.1f} dias")
        print(f"  {time_cost['weeks']:.1f} semanas")
        print(f"  {time_cost['months']:.2f} meses\n")
        
        # Análise de assinatura
        subscription_analysis = calculator.analyze_subscription_services(args.gastos, args.anos)
        print(f"--- SE INVESTISSE AO INVÉS DE GASTAR ({args.anos} anos) ---")
        for investment_type, result in subscription_analysis.items():
            print(f"{investment_type.capitalize()}:")
            print(f"  Total pago: R$ {result['total_paid']:,.2f}")
            print(f"  Valor se investido: R$ {result['future_value_if_invested']:,.2f}")
            print(f"  Custo oportunidade: R$ {result['opportunity_cost']:,.2f}")
            print(f"  Multiplicador: {result['multiplier']:.1f}x\n")
    
    if args.valor:
        # Análise de compra específica
        print(f"--- ANÁLISE DE COMPRA: R$ {args.valor:,.2f} ---")
        
        comparison = calculator.compare_purchase_vs_investment(args.valor, args.anos)
        for category, result in comparison.items():
            print(f"{category.capitalize()}:")
            print(f"  Valor do item após {args.anos} anos: R$ {result['item_future_value']:,.2f}")
            print(f"  Valor se investido: R$ {result['investment_future_value']:,.2f}")
            print(f"  Custo oportunidade: R$ {result['opportunity_cost']:,.2f}")
            print(f"  Custo percentual: {result['cost_percentage']:.1f}%\n")
        
        # Comparações do mundo real
        print("--- COMPARAÇÕES DO MUNDO REAL ---")
        comparisons = calculator.generate_real_world_comparisons(args.valor)
        for category, items in comparisons.items():
            print(f"{category}:")
            for item, quantity in items.items():
                if quantity >= 1:
                    print(f"  {quantity:.0f} {item.replace('_', ' ')}")
            print()
    
    # Exemplo de matriz de decisão
    print("--- EXEMPLO: MATRIZ DE DECISÃO ---")
    options = [
        {'name': 'iPhone Novo', 'cost': 8000, 'utility_score': 6, 'duration_years': 3},
        {'name': 'Curso de Python', 'cost': 500, 'utility_score': 9, 'duration_years': 1},
        {'name': 'Viagem Europa', 'cost': 12000, 'utility_score': 8, 'duration_years': 1},
        {'name': 'Academia (1 ano)', 'cost': 1200, 'utility_score': 7, 'duration_years': 1}
    ]
    
    decision_matrix = calculator.create_decision_matrix(options)
    for i, option in enumerate(decision_matrix, 1):
        print(f"{i}. {option['name']}")
        print(f"   Custo: R$ {option['cost']:,.2f}")
        print(f"   Utilidade: {option['utility_score']}/10")
        print(f"   Custo oportunidade: R$ {option['opportunity_cost']:,.2f}")
        print(f"   Score custo-benefício: {option['cost_benefit_score']:.2f}")
        print(f"   Recomendação: {option['recommendation']}\n")

if __name__ == "__main__":
    main()
