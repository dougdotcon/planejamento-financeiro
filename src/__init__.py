"""
Control Fintech - Sistema de Análise Financeira
===============================================

Este pacote contém ferramentas para análise do impacto financeiro de decisões cotidianas.

Módulos disponíveis:
- financial_impact_analyzer: Análise principal de impacto financeiro
- opportunity_cost_calculator: Calculadora de custo de oportunidade
- lifestyle_comparison: Comparação de estilos de vida
- behavioral_economics: Análise de economia comportamental
- data_visualizer: Gerador de visualizações
"""

__version__ = "1.0.0"
__author__ = "Control Fintech Team"
__email__ = "contato@controlfintech.com"

# Importações principais para facilitar uso
from .financial_impact_analyzer import FinancialImpactAnalyzer
from .opportunity_cost_calculator import OpportunityCostCalculator
from .lifestyle_comparison import LifestyleComparator
from .behavioral_economics import BehavioralEconomicsAnalyzer
from .data_visualizer import FinancialDataVisualizer

__all__ = [
    'FinancialImpactAnalyzer',
    'OpportunityCostCalculator', 
    'LifestyleComparator',
    'BehavioralEconomicsAnalyzer',
    'FinancialDataVisualizer'
]
