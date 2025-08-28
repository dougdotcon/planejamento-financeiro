"""
Análise Comparativa de Estilos de Vida
Compara diferentes padrões de vida e seus impactos financeiros a longo prazo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from dataclasses import dataclass
from typing import Dict, List
import json

@dataclass
class LifestyleProfile:
    name: str
    monthly_income: float
    housing_cost: float
    food_cost: float
    transportation_cost: float
    entertainment_cost: float
    shopping_cost: float
    education_cost: float
    healthcare_cost: float
    savings_rate: float
    age: int

class LifestyleComparator:
    def __init__(self):
        self.investment_return = 0.10
        self.inflation_rate = 0.045
        self.retirement_age = 65
        
        # Definir perfis de estilo de vida
        self.lifestyle_profiles = self._create_lifestyle_profiles()
    
    def _create_lifestyle_profiles(self) -> Dict[str, LifestyleProfile]:
        """
        Cria perfis de estilo de vida baseados em dados reais brasileiros
        """
        profiles = {
            'Minimalista': LifestyleProfile(
                name='Minimalista',
                monthly_income=5000,
                housing_cost=1200,  # 24%
                food_cost=600,      # 12%
                transportation_cost=300,  # 6%
                entertainment_cost=200,   # 4%
                shopping_cost=100,        # 2%
                education_cost=300,       # 6%
                healthcare_cost=200,      # 4%
                savings_rate=0.40,        # 40%
                age=28
            ),
            
            'Classe Média Tradicional': LifestyleProfile(
                name='Classe Média Tradicional',
                monthly_income=5000,
                housing_cost=1800,  # 36%
                food_cost=800,      # 16%
                transportation_cost=600,  # 12%
                entertainment_cost=400,   # 8%
                shopping_cost=300,        # 6%
                education_cost=200,       # 4%
                healthcare_cost=300,      # 6%
                savings_rate=0.12,        # 12%
                age=28
            ),
            
            'Consumista': LifestyleProfile(
                name='Consumista',
                monthly_income=5000,
                housing_cost=2000,  # 40%
                food_cost=1000,     # 20%
                transportation_cost=800,  # 16%
                entertainment_cost=600,   # 12%
                shopping_cost=500,        # 10%
                education_cost=50,        # 1%
                healthcare_cost=250,      # 5%
                savings_rate=-0.04,       # -4% (endividamento)
                age=28
            ),
            
            'Investidor Jovem': LifestyleProfile(
                name='Investidor Jovem',
                monthly_income=6000,
                housing_cost=1400,  # 23%
                food_cost=700,      # 12%
                transportation_cost=400,  # 7%
                entertainment_cost=300,   # 5%
                shopping_cost=150,        # 3%
                education_cost=500,       # 8%
                healthcare_cost=300,      # 5%
                savings_rate=0.37,        # 37%
                age=25
            ),
            
            'Família Equilibrada': LifestyleProfile(
                name='Família Equilibrada',
                monthly_income=10000,
                housing_cost=3000,  # 30%
                food_cost=1500,     # 15%
                transportation_cost=1000, # 10%
                entertainment_cost=800,   # 8%
                shopping_cost=600,        # 6%
                education_cost=800,       # 8%
                healthcare_cost=500,      # 5%
                savings_rate=0.18,        # 18%
                age=35
            )
        }
        
        return profiles
    
    def calculate_lifetime_wealth(self, profile: LifestyleProfile) -> Dict:
        """
        Calcula o patrimônio acumulado ao longo da vida
        """
        working_years = self.retirement_age - profile.age
        monthly_savings = profile.monthly_income * profile.savings_rate
        
        # Cálculo com aportes mensais e juros compostos
        if monthly_savings > 0:
            total_months = working_years * 12
            monthly_rate = self.investment_return / 12
            
            # Fórmula para valor futuro de anuidade
            if monthly_rate > 0:
                future_value = monthly_savings * (((1 + monthly_rate) ** total_months - 1) / monthly_rate)
            else:
                future_value = monthly_savings * total_months
        else:
            # Se savings_rate é negativo, calcula endividamento
            future_value = monthly_savings * working_years * 12
        
        # Valor necessário para aposentadoria (regra 4%)
        annual_expenses = (profile.monthly_income - monthly_savings) * 12
        retirement_needed = annual_expenses / 0.04
        
        # Anos de aposentadoria cobertos
        if future_value > 0:
            retirement_years_covered = future_value / annual_expenses
        else:
            retirement_years_covered = 0
        
        return {
            'working_years': working_years,
            'monthly_savings': monthly_savings,
            'total_saved': monthly_savings * working_years * 12,
            'future_value': future_value,
            'retirement_needed': retirement_needed,
            'retirement_years_covered': retirement_years_covered,
            'financial_independence': future_value >= retirement_needed
        }
    
    def analyze_spending_efficiency(self, profile: LifestyleProfile) -> Dict:
        """
        Analisa a eficiência dos gastos de um perfil
        """
        total_expenses = (profile.housing_cost + profile.food_cost + 
                         profile.transportation_cost + profile.entertainment_cost +
                         profile.shopping_cost + profile.education_cost + 
                         profile.healthcare_cost)
        
        # Categorizar gastos por necessidade
        essential_expenses = profile.housing_cost + profile.food_cost + profile.healthcare_cost
        productive_expenses = profile.education_cost + profile.transportation_cost
        lifestyle_expenses = profile.entertainment_cost + profile.shopping_cost
        
        # Scores de eficiência (0-10)
        efficiency_scores = {
            'essential_ratio': (essential_expenses / total_expenses) * 10,
            'productive_ratio': (productive_expenses / total_expenses) * 10,
            'lifestyle_ratio': 10 - ((lifestyle_expenses / total_expenses) * 10),
            'savings_score': min(profile.savings_rate * 25, 10)  # 40% = score 10
        }
        
        overall_efficiency = np.mean(list(efficiency_scores.values()))
        
        return {
            'total_expenses': total_expenses,
            'essential_expenses': essential_expenses,
            'productive_expenses': productive_expenses,
            'lifestyle_expenses': lifestyle_expenses,
            'efficiency_scores': efficiency_scores,
            'overall_efficiency': overall_efficiency
        }
    
    def compare_all_profiles(self) -> pd.DataFrame:
        """
        Compara todos os perfis de estilo de vida
        """
        comparison_data = []
        
        for name, profile in self.lifestyle_profiles.items():
            wealth_analysis = self.calculate_lifetime_wealth(profile)
            efficiency_analysis = self.analyze_spending_efficiency(profile)
            
            comparison_data.append({
                'Perfil': name,
                'Renda Mensal': profile.monthly_income,
                'Taxa Poupança': f"{profile.savings_rate*100:.1f}%",
                'Poupança Mensal': wealth_analysis['monthly_savings'],
                'Patrimônio Futuro': wealth_analysis['future_value'],
                'Anos Aposentadoria': wealth_analysis['retirement_years_covered'],
                'Independência Financeira': 'Sim' if wealth_analysis['financial_independence'] else 'Não',
                'Eficiência Geral': efficiency_analysis['overall_efficiency'],
                'Gastos Essenciais': efficiency_analysis['essential_expenses'],
                'Gastos Produtivos': efficiency_analysis['productive_expenses'],
                'Gastos Lifestyle': efficiency_analysis['lifestyle_expenses']
            })
        
        return pd.DataFrame(comparison_data)
    
    def simulate_lifestyle_changes(self, base_profile: str, modifications: Dict) -> Dict:
        """
        Simula mudanças no estilo de vida
        """
        if base_profile not in self.lifestyle_profiles:
            raise ValueError(f"Perfil {base_profile} não encontrado")
        
        original = self.lifestyle_profiles[base_profile]
        
        # Criar perfil modificado
        modified_profile = LifestyleProfile(
            name=f"{original.name} (Modificado)",
            monthly_income=modifications.get('income', original.monthly_income),
            housing_cost=modifications.get('housing', original.housing_cost),
            food_cost=modifications.get('food', original.food_cost),
            transportation_cost=modifications.get('transport', original.transportation_cost),
            entertainment_cost=modifications.get('entertainment', original.entertainment_cost),
            shopping_cost=modifications.get('shopping', original.shopping_cost),
            education_cost=modifications.get('education', original.education_cost),
            healthcare_cost=modifications.get('healthcare', original.healthcare_cost),
            savings_rate=modifications.get('savings_rate', original.savings_rate),
            age=modifications.get('age', original.age)
        )
        
        # Analisar ambos os perfis
        original_analysis = self.calculate_lifetime_wealth(original)
        modified_analysis = self.calculate_lifetime_wealth(modified_profile)
        
        # Calcular diferenças
        wealth_difference = modified_analysis['future_value'] - original_analysis['future_value']
        retirement_difference = (modified_analysis['retirement_years_covered'] - 
                               original_analysis['retirement_years_covered'])
        
        return {
            'original': original_analysis,
            'modified': modified_analysis,
            'wealth_difference': wealth_difference,
            'retirement_difference': retirement_difference,
            'improvement_percentage': (wealth_difference / original_analysis['future_value']) * 100
        }
    
    def create_lifestyle_optimization_suggestions(self, profile_name: str) -> List[Dict]:
        """
        Cria sugestões de otimização para um perfil específico
        """
        if profile_name not in self.lifestyle_profiles:
            return []
        
        profile = self.lifestyle_profiles[profile_name]
        suggestions = []
        
        # Sugestão 1: Reduzir gastos com entretenimento
        if profile.entertainment_cost > profile.monthly_income * 0.05:  # Mais que 5%
            reduction = profile.entertainment_cost * 0.3  # Reduzir 30%
            modified = self.simulate_lifestyle_changes(profile_name, {
                'entertainment': profile.entertainment_cost - reduction,
                'savings_rate': profile.savings_rate + (reduction / profile.monthly_income)
            })
            
            suggestions.append({
                'type': 'Reduzir Entretenimento',
                'description': f'Reduzir gastos com entretenimento em R$ {reduction:.0f}',
                'impact': f'Ganho de R$ {modified["wealth_difference"]:,.0f} no patrimônio futuro',
                'feasibility': 'Alta'
            })
        
        # Sugestão 2: Otimizar moradia
        if profile.housing_cost > profile.monthly_income * 0.30:  # Mais que 30%
            reduction = profile.housing_cost * 0.15  # Reduzir 15%
            modified = self.simulate_lifestyle_changes(profile_name, {
                'housing': profile.housing_cost - reduction,
                'savings_rate': profile.savings_rate + (reduction / profile.monthly_income)
            })
            
            suggestions.append({
                'type': 'Otimizar Moradia',
                'description': f'Reduzir custos de moradia em R$ {reduction:.0f}',
                'impact': f'Ganho de R$ {modified["wealth_difference"]:,.0f} no patrimônio futuro',
                'feasibility': 'Média'
            })
        
        # Sugestão 3: Aumentar investimento em educação
        if profile.education_cost < profile.monthly_income * 0.05:  # Menos que 5%
            increase = profile.monthly_income * 0.03  # Aumentar para 3%
            modified = self.simulate_lifestyle_changes(profile_name, {
                'education': profile.education_cost + increase,
                'shopping': max(0, profile.shopping_cost - increase)
            })
            
            suggestions.append({
                'type': 'Investir em Educação',
                'description': f'Aumentar investimento em educação em R$ {increase:.0f}',
                'impact': 'Potencial aumento de renda de 20-50% em 2-3 anos',
                'feasibility': 'Alta'
            })
        
        return suggestions
    
    def generate_lifestyle_report(self, profile_name: str) -> str:
        """
        Gera relatório completo de um estilo de vida
        """
        if profile_name not in self.lifestyle_profiles:
            return f"Perfil {profile_name} não encontrado"
        
        profile = self.lifestyle_profiles[profile_name]
        wealth_analysis = self.calculate_lifetime_wealth(profile)
        efficiency_analysis = self.analyze_spending_efficiency(profile)
        suggestions = self.create_lifestyle_optimization_suggestions(profile_name)
        
        report = f"""
=== RELATÓRIO DE ESTILO DE VIDA: {profile_name.upper()} ===

PERFIL FINANCEIRO:
- Renda Mensal: R$ {profile.monthly_income:,.2f}
- Taxa de Poupança: {profile.savings_rate*100:.1f}%
- Poupança Mensal: R$ {wealth_analysis['monthly_savings']:,.2f}

DISTRIBUIÇÃO DE GASTOS:
- Moradia: R$ {profile.housing_cost:,.2f} ({profile.housing_cost/profile.monthly_income*100:.1f}%)
- Alimentação: R$ {profile.food_cost:,.2f} ({profile.food_cost/profile.monthly_income*100:.1f}%)
- Transporte: R$ {profile.transportation_cost:,.2f} ({profile.transportation_cost/profile.monthly_income*100:.1f}%)
- Entretenimento: R$ {profile.entertainment_cost:,.2f} ({profile.entertainment_cost/profile.monthly_income*100:.1f}%)
- Compras: R$ {profile.shopping_cost:,.2f} ({profile.shopping_cost/profile.monthly_income*100:.1f}%)
- Educação: R$ {profile.education_cost:,.2f} ({profile.education_cost/profile.monthly_income*100:.1f}%)
- Saúde: R$ {profile.healthcare_cost:,.2f} ({profile.healthcare_cost/profile.monthly_income*100:.1f}%)

PROJEÇÃO PATRIMONIAL:
- Anos de trabalho restantes: {wealth_analysis['working_years']}
- Patrimônio futuro estimado: R$ {wealth_analysis['future_value']:,.2f}
- Anos de aposentadoria cobertos: {wealth_analysis['retirement_years_covered']:.1f}
- Independência financeira: {'SIM' if wealth_analysis['financial_independence'] else 'NÃO'}

ANÁLISE DE EFICIÊNCIA:
- Score geral: {efficiency_analysis['overall_efficiency']:.1f}/10
- Gastos essenciais: R$ {efficiency_analysis['essential_expenses']:,.2f}
- Gastos produtivos: R$ {efficiency_analysis['productive_expenses']:,.2f}
- Gastos de lifestyle: R$ {efficiency_analysis['lifestyle_expenses']:,.2f}

SUGESTÕES DE OTIMIZAÇÃO:
"""
        
        for i, suggestion in enumerate(suggestions, 1):
            report += f"{i}. {suggestion['type']}: {suggestion['description']}\n"
            report += f"   Impacto: {suggestion['impact']}\n"
            report += f"   Viabilidade: {suggestion['feasibility']}\n\n"
        
        return report

def main():
    comparator = LifestyleComparator()
    
    print("=== ANÁLISE COMPARATIVA DE ESTILOS DE VIDA ===\n")
    
    # Comparação geral
    comparison_df = comparator.compare_all_profiles()
    print("COMPARAÇÃO GERAL:")
    print(comparison_df.to_string(index=False))
    print("\n" + "="*80 + "\n")
    
    # Relatórios individuais
    for profile_name in comparator.lifestyle_profiles.keys():
        report = comparator.generate_lifestyle_report(profile_name)
        print(report)
        print("="*80 + "\n")
    
    # Simulação de mudança
    print("=== SIMULAÇÃO: CONSUMISTA → MINIMALISTA ===")
    
    modifications = {
        'housing': 1200,      # Reduzir moradia
        'food': 600,          # Reduzir alimentação
        'entertainment': 200, # Reduzir entretenimento
        'shopping': 100,      # Reduzir compras
        'education': 300,     # Aumentar educação
        'savings_rate': 0.40  # Aumentar poupança para 40%
    }
    
    simulation = comparator.simulate_lifestyle_changes('Consumista', modifications)
    
    print(f"Patrimônio original: R$ {simulation['original']['future_value']:,.2f}")
    print(f"Patrimônio modificado: R$ {simulation['modified']['future_value']:,.2f}")
    print(f"Diferença: R$ {simulation['wealth_difference']:,.2f}")
    print(f"Melhoria: {simulation['improvement_percentage']:.1f}%")
    print(f"Anos extras de aposentadoria: {simulation['retirement_difference']:.1f}")

if __name__ == "__main__":
    main()
