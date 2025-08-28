"""
Análise de Economia Comportamental
Modela padrões comportamentais de gastos e vieses cognitivos
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import random
from dataclasses import dataclass
from typing import List, Dict, Tuple
from datetime import datetime, timedelta

@dataclass
class SpendingTrigger:
    name: str
    probability: float
    impact_multiplier: float
    description: str

@dataclass
class CognitiveBias:
    name: str
    influence_strength: float
    affected_categories: List[str]
    description: str

class BehavioralEconomicsAnalyzer:
    def __init__(self):
        self.spending_triggers = self._create_spending_triggers()
        self.cognitive_biases = self._create_cognitive_biases()
        self.emotional_states = self._create_emotional_states()
        
    def _create_spending_triggers(self) -> List[SpendingTrigger]:
        """
        Define gatilhos de gastos baseados em pesquisas comportamentais
        """
        return [
            SpendingTrigger("Promoção/Desconto", 0.7, 1.8, "Sensação de economia leva ao gasto"),
            SpendingTrigger("Pressão Social", 0.4, 2.2, "Necessidade de pertencimento"),
            SpendingTrigger("Estado Emocional", 0.6, 1.9, "Compras por impulso emocional"),
            SpendingTrigger("Facilidade de Pagamento", 0.8, 1.5, "Cartão/PIX reduz percepção de gasto"),
            SpendingTrigger("Escassez Artificial", 0.3, 2.5, "Última peça/oferta limitada"),
            SpendingTrigger("Ancoragem de Preços", 0.5, 1.4, "Preço alto como referência"),
            SpendingTrigger("Reciprocidade", 0.3, 1.7, "Retribuir favores/cortesias"),
            SpendingTrigger("Autoridade/Influencer", 0.4, 1.6, "Recomendação de figura respeitada")
        ]
    
    def _create_cognitive_biases(self) -> List[CognitiveBias]:
        """
        Define vieses cognitivos que afetam decisões financeiras
        """
        return [
            CognitiveBias("Desconto Hiperbólico", 0.8, ["entretenimento", "comida"], 
                         "Preferência extrema pelo prazer imediato"),
            CognitiveBias("Aversão à Perda", 0.6, ["investimentos", "seguros"], 
                         "Medo de perder é maior que prazer de ganhar"),
            CognitiveBias("Contabilidade Mental", 0.7, ["todas"], 
                         "Separação artificial de categorias de dinheiro"),
            CognitiveBias("Ancoragem", 0.5, ["compras", "negociações"], 
                         "Fixação no primeiro preço apresentado"),
            CognitiveBias("Confirmação", 0.6, ["investimentos", "educação"], 
                         "Buscar informações que confirmem crenças"),
            CognitiveBias("Disponibilidade", 0.4, ["seguros", "emergências"], 
                         "Superestimar probabilidades de eventos recentes"),
            CognitiveBias("Otimismo", 0.5, ["planejamento", "aposentadoria"], 
                         "Subestimar riscos e superestimar capacidades")
        ]
    
    def _create_emotional_states(self) -> Dict[str, Dict]:
        """
        Define estados emocionais e seus impactos nos gastos
        """
        return {
            'Felicidade': {
                'spending_multiplier': 1.3,
                'categories_affected': ['entretenimento', 'presentes', 'viagens'],
                'probability': 0.25
            },
            'Tristeza': {
                'spending_multiplier': 1.6,
                'categories_affected': ['comida', 'compras_impulso', 'entretenimento'],
                'probability': 0.15
            },
            'Stress': {
                'spending_multiplier': 1.4,
                'categories_affected': ['comida', 'bebidas', 'relaxamento'],
                'probability': 0.30
            },
            'Ansiedade': {
                'spending_multiplier': 1.2,
                'categories_affected': ['compras_impulso', 'seguros', 'saude'],
                'probability': 0.20
            },
            'Neutro': {
                'spending_multiplier': 1.0,
                'categories_affected': [],
                'probability': 0.10
            }
        }
    
    def simulate_monthly_spending(self, base_budget: Dict[str, float], 
                                 personality_profile: str = 'medio') -> Dict:
        """
        Simula gastos mensais considerando fatores comportamentais
        """
        # Perfis de personalidade
        profiles = {
            'impulsivo': {'trigger_sensitivity': 1.5, 'bias_influence': 1.3},
            'medio': {'trigger_sensitivity': 1.0, 'bias_influence': 1.0},
            'controlado': {'trigger_sensitivity': 0.6, 'bias_influence': 0.7}
        }
        
        profile = profiles.get(personality_profile, profiles['medio'])
        
        # Simular 30 dias
        daily_spending = []
        triggered_events = []
        
        for day in range(30):
            day_spending = {}
            day_triggers = []
            
            # Verificar gatilhos do dia
            for trigger in self.spending_triggers:
                if random.random() < trigger.probability * profile['trigger_sensitivity']:
                    day_triggers.append(trigger)
            
            # Calcular gastos por categoria
            for category, base_amount in base_budget.items():
                daily_base = base_amount / 30
                
                # Aplicar gatilhos
                multiplier = 1.0
                for trigger in day_triggers:
                    multiplier *= trigger.impact_multiplier
                
                # Aplicar estado emocional
                emotional_state = np.random.choice(
                    list(self.emotional_states.keys()),
                    p=[state['probability'] for state in self.emotional_states.values()]
                )
                
                if category in self.emotional_states[emotional_state]['categories_affected']:
                    multiplier *= self.emotional_states[emotional_state]['spending_multiplier']
                
                # Aplicar vieses cognitivos
                for bias in self.cognitive_biases:
                    if category in bias.affected_categories or 'todas' in bias.affected_categories:
                        bias_effect = 1 + (bias.influence_strength - 1) * profile['bias_influence']
                        multiplier *= bias_effect
                
                # Adicionar variabilidade natural
                variability = np.random.normal(1.0, 0.2)
                final_amount = daily_base * multiplier * max(0.1, variability)
                
                day_spending[category] = final_amount
            
            daily_spending.append(day_spending)
            triggered_events.extend([(day, trigger.name) for trigger in day_triggers])
        
        # Consolidar resultados mensais
        monthly_totals = {}
        for category in base_budget.keys():
            monthly_totals[category] = sum(day[category] for day in daily_spending)
        
        return {
            'monthly_totals': monthly_totals,
            'daily_breakdown': daily_spending,
            'triggered_events': triggered_events,
            'budget_variance': {
                cat: (monthly_totals[cat] - base_budget[cat]) / base_budget[cat] * 100
                for cat in base_budget.keys()
            }
        }
    
    def analyze_spending_patterns(self, spending_history: List[Dict]) -> Dict:
        """
        Analisa padrões comportamentais em histórico de gastos
        """
        # Converter para DataFrame
        df = pd.DataFrame(spending_history)
        
        # Análise de variabilidade
        variability_analysis = {}
        for column in df.columns:
            if df[column].dtype in ['float64', 'int64']:
                variability_analysis[column] = {
                    'mean': df[column].mean(),
                    'std': df[column].std(),
                    'coefficient_variation': df[column].std() / df[column].mean(),
                    'volatility_score': min(df[column].std() / df[column].mean() * 10, 10)
                }
        
        # Detectar padrões temporais
        df['total_spending'] = df.sum(axis=1, numeric_only=True)
        
        # Análise de correlações
        correlation_matrix = df.corr(numeric_only=True)
        
        # Identificar categorias problemáticas
        problematic_categories = []
        for cat, analysis in variability_analysis.items():
            if analysis['volatility_score'] > 7:
                problematic_categories.append({
                    'category': cat,
                    'volatility': analysis['volatility_score'],
                    'reason': 'Alta variabilidade indica gastos impulsivos'
                })
        
        return {
            'variability_analysis': variability_analysis,
            'correlation_matrix': correlation_matrix.to_dict(),
            'problematic_categories': problematic_categories,
            'overall_spending_volatility': df['total_spending'].std() / df['total_spending'].mean()
        }
    
    def calculate_behavioral_cost(self, rational_budget: Dict[str, float], 
                                 actual_spending: Dict[str, float]) -> Dict:
        """
        Calcula o custo dos vieses comportamentais
        """
        behavioral_cost = {}
        total_rational = sum(rational_budget.values())
        total_actual = sum(actual_spending.values())
        
        for category in rational_budget.keys():
            rational = rational_budget[category]
            actual = actual_spending.get(category, 0)
            
            behavioral_cost[category] = {
                'excess_spending': max(0, actual - rational),
                'excess_percentage': ((actual - rational) / rational * 100) if rational > 0 else 0,
                'opportunity_cost_1_year': max(0, actual - rational) * 12 * 1.10,  # 10% retorno
                'opportunity_cost_10_years': max(0, actual - rational) * 12 * (1.10 ** 10)
            }
        
        return {
            'by_category': behavioral_cost,
            'total_excess': total_actual - total_rational,
            'total_excess_percentage': (total_actual - total_rational) / total_rational * 100,
            'annual_opportunity_cost': (total_actual - total_rational) * 12 * 1.10,
            'decade_opportunity_cost': (total_actual - total_rational) * 12 * (1.10 ** 10)
        }
    
    def create_intervention_strategies(self, behavioral_analysis: Dict) -> List[Dict]:
        """
        Cria estratégias de intervenção baseadas na análise comportamental
        """
        strategies = []
        
        # Estratégias baseadas em categorias problemáticas
        for cat_info in behavioral_analysis.get('problematic_categories', []):
            category = cat_info['category']
            
            if 'entretenimento' in category.lower():
                strategies.append({
                    'category': category,
                    'strategy': 'Orçamento Semanal Fixo',
                    'description': 'Definir valor fixo semanal para entretenimento em dinheiro',
                    'effectiveness': 8.5,
                    'difficulty': 'Média'
                })
            
            elif 'comida' in category.lower():
                strategies.append({
                    'category': category,
                    'strategy': 'Planejamento de Refeições',
                    'description': 'Planejar refeições semanalmente e fazer lista de compras',
                    'effectiveness': 9.0,
                    'difficulty': 'Alta'
                })
            
            elif 'compra' in category.lower():
                strategies.append({
                    'category': category,
                    'strategy': 'Regra das 24 Horas',
                    'description': 'Esperar 24h antes de qualquer compra não essencial',
                    'effectiveness': 7.5,
                    'difficulty': 'Baixa'
                })
        
        # Estratégias gerais baseadas na volatilidade geral
        overall_volatility = behavioral_analysis.get('overall_spending_volatility', 0)
        
        if overall_volatility > 0.3:  # Alta volatilidade
            strategies.extend([
                {
                    'category': 'Geral',
                    'strategy': 'Envelope Method Digital',
                    'description': 'Usar app para separar dinheiro por categoria mensalmente',
                    'effectiveness': 8.0,
                    'difficulty': 'Baixa'
                },
                {
                    'category': 'Geral',
                    'strategy': 'Automação de Poupança',
                    'description': 'Transferir automaticamente para poupança no dia do salário',
                    'effectiveness': 9.5,
                    'difficulty': 'Baixa'
                }
            ])
        
        # Ordenar por efetividade
        strategies.sort(key=lambda x: x['effectiveness'], reverse=True)
        
        return strategies
    
    def generate_behavioral_report(self, spending_data: Dict, 
                                  rational_budget: Dict) -> str:
        """
        Gera relatório comportamental completo
        """
        behavioral_cost = self.calculate_behavioral_cost(rational_budget, 
                                                        spending_data['monthly_totals'])
        
        report = f"""
=== RELATÓRIO DE ANÁLISE COMPORTAMENTAL ===

RESUMO EXECUTIVO:
- Excesso de gastos total: R$ {behavioral_cost['total_excess']:.2f} ({behavioral_cost['total_excess_percentage']:.1f}%)
- Custo de oportunidade anual: R$ {behavioral_cost['annual_opportunity_cost']:,.2f}
- Custo de oportunidade (10 anos): R$ {behavioral_cost['decade_opportunity_cost']:,.2f}

GATILHOS IDENTIFICADOS:
"""
        
        trigger_count = {}
        for day, trigger in spending_data['triggered_events']:
            trigger_count[trigger] = trigger_count.get(trigger, 0) + 1
        
        for trigger, count in sorted(trigger_count.items(), key=lambda x: x[1], reverse=True):
            report += f"- {trigger}: {count} ocorrências no mês\n"
        
        report += f"\nANÁLISE POR CATEGORIA:\n"
        
        for category, analysis in behavioral_cost['by_category'].items():
            if analysis['excess_spending'] > 0:
                report += f"\n{category.upper()}:\n"
                report += f"  Excesso: R$ {analysis['excess_spending']:.2f} ({analysis['excess_percentage']:.1f}%)\n"
                report += f"  Custo oportunidade (1 ano): R$ {analysis['opportunity_cost_1_year']:,.2f}\n"
                report += f"  Custo oportunidade (10 anos): R$ {analysis['opportunity_cost_10_years']:,.2f}\n"
        
        return report

def main():
    analyzer = BehavioralEconomicsAnalyzer()
    
    print("=== ANÁLISE DE ECONOMIA COMPORTAMENTAL ===\n")
    
    # Orçamento base racional
    rational_budget = {
        'alimentacao': 800,
        'transporte': 400,
        'entretenimento': 300,
        'compras_impulso': 100,
        'saude': 200,
        'educacao': 150
    }
    
    print("ORÇAMENTO RACIONAL MENSAL:")
    for category, amount in rational_budget.items():
        print(f"- {category.capitalize()}: R$ {amount:.2f}")
    print(f"Total: R$ {sum(rational_budget.values()):.2f}\n")
    
    # Simular gastos para diferentes perfis
    profiles = ['controlado', 'medio', 'impulsivo']
    
    for profile in profiles:
        print(f"=== PERFIL: {profile.upper()} ===")
        
        simulation = analyzer.simulate_monthly_spending(rational_budget, profile)
        
        print("GASTOS SIMULADOS:")
        total_simulated = 0
        for category, amount in simulation['monthly_totals'].items():
            variance = simulation['budget_variance'][category]
            print(f"- {category.capitalize()}: R$ {amount:.2f} ({variance:+.1f}%)")
            total_simulated += amount
        
        print(f"Total: R$ {total_simulated:.2f}")
        print(f"Diferença do orçamento: R$ {total_simulated - sum(rational_budget.values()):.2f}\n")
        
        # Análise comportamental
        behavioral_cost = analyzer.calculate_behavioral_cost(rational_budget, 
                                                           simulation['monthly_totals'])
        
        print(f"CUSTO COMPORTAMENTAL:")
        print(f"- Excesso mensal: R$ {behavioral_cost['total_excess']:.2f}")
        print(f"- Custo oportunidade (10 anos): R$ {behavioral_cost['decade_opportunity_cost']:,.2f}")
        
        # Principais gatilhos
        trigger_count = {}
        for day, trigger in simulation['triggered_events']:
            trigger_count[trigger] = trigger_count.get(trigger, 0) + 1
        
        print(f"- Principais gatilhos: {', '.join(sorted(trigger_count.keys(), key=lambda x: trigger_count[x], reverse=True)[:3])}")
        print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
