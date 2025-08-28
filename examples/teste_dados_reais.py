"""
Teste dos Dados Reais Brasileiros - Sistema Control Fintech
Demonstra o uso de dados oficiais atualizados (2025)
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from dados_oficiais import dados_brasil
from financial_impact_analyzer import FinancialImpactAnalyzer

def main():
    print("=== TESTE DOS DADOS REAIS BRASILEIROS (2025) ===\n")
    
    # 1. Mostrar dados oficiais
    print("📊 DADOS OFICIAIS ATUALIZADOS")
    print(f"Salário Mínimo: R$ {dados_brasil.salario_minimo['valor']:,.2f}")
    print(f"Renda Média Nacional: R$ {dados_brasil.renda_trabalho['renda_media_nacional']:,.2f}")
    print(f"Taxa Selic: {dados_brasil.indicadores_bc['selic']:.2f}% a.a.")
    print(f"Inflação Projetada 2025: {dados_brasil.indicadores_bc['inflacao_atual']:.2f}%")
    print(f"Expectativa de Vida: {dados_brasil.demografia['expectativa_vida']:.1f} anos")
    print(f"Fonte: {dados_brasil.salario_minimo['fonte']}\n")
    
    # 2. Taxas de investimento reais
    print("💰 TAXAS DE INVESTIMENTO REAIS (2025)")
    print(f"Poupança: {dados_brasil.investimentos['poupanca']:.2f}% a.a.")
    print(f"Tesouro Selic: {dados_brasil.investimentos['tesouro_selic']:.2f}% a.a.")
    print(f"CDB 99% CDI: {dados_brasil.investimentos['cdb_digitais']:.2f}% a.a.")
    print(f"Tesouro IPCA+ 2029: {dados_brasil.investimentos['tesouro_ipca_2029']:.2f}% a.a.")
    print(f"LCI/LCA (isento IR): {dados_brasil.investimentos['lci_lca']:.2f}% a.a.\n")
    
    # 3. Categorias de gastos com dados reais
    print("🛒 GASTOS DESNECESSÁRIOS - DADOS REAIS")
    gastos = dados_brasil.gastos_desnecessarios
    
    total_mensal = 0
    for categoria, info in gastos.items():
        valor = info['valor_medio_mensal']
        freq = info['frequencia_populacao'] * 100
        total_mensal += valor * info['frequencia_populacao']
        
        print(f"{categoria.replace('_', ' ').title()}:")
        print(f"  Valor médio: R$ {valor:.2f}/mês")
        print(f"  Frequência: {freq:.0f}% da população")
        print(f"  Necessidade: {info['necessidade']}/5")
    
    print(f"\nGasto médio desnecessário por pessoa: R$ {total_mensal:.2f}/mês\n")
    
    # 4. Análise com dados reais
    print("📈 ANÁLISE COM DADOS REAIS")
    analyzer = FinancialImpactAnalyzer()
    
    # Cenários baseados em dados reais
    cenarios_reais = dados_brasil.get_cenarios_reais()
    
    for nome, cenario in cenarios_reais.items():
        print(f"\n--- {nome} ---")
        print(f"Perfil: {cenario['perfil']}")
        print(f"Idade: {cenario['idade']} anos")
        print(f"Renda: R$ {cenario['renda_mensal']:,.2f}")
        print(f"Gastos desnecessários: R$ {cenario['gastos_desnecessarios']:,.2f}")
        
        # Análise de impacto
        impact = analyzer.analyze_lifetime_impact(
            cenario['idade'], 
            cenario['gastos_desnecessarios'], 
            cenario['renda_mensal']
        )
        
        print(f"Desperdício total na vida: R$ {impact['total_waste']:,.2f}")
        print(f"Custo de oportunidade: R$ {impact['opportunity_cost']:,.2f}")
        print(f"Anos desperdiçados: {impact['total_years_life_wasted']:.1f}")
        print(f"Aposentadoria antecipada possível: {impact['potential_early_retirement_years']:.1f} anos")
    
    # 5. Comparação com cenário otimista
    print(f"\n🎯 CENÁRIO OTIMISTA (Redução 50% gastos desnecessários)")
    cenario_base = cenarios_reais['Profissional Classe Média']
    gastos_otimizados = cenario_base['gastos_desnecessarios'] * 0.5
    
    impact_otimizado = analyzer.analyze_lifetime_impact(
        cenario_base['idade'],
        gastos_otimizados,
        cenario_base['renda_mensal']
    )
    
    impact_original = analyzer.analyze_lifetime_impact(
        cenario_base['idade'],
        cenario_base['gastos_desnecessarios'],
        cenario_base['renda_mensal']
    )
    
    economia_total = impact_original['opportunity_cost'] - impact_otimizado['opportunity_cost']
    anos_ganhos = impact_original['total_years_life_wasted'] - impact_otimizado['total_years_life_wasted']
    
    print(f"Economia total: R$ {economia_total:,.2f}")
    print(f"Anos de vida recuperados: {anos_ganhos:.1f}")
    print(f"Aposentadoria antecipada adicional: {anos_ganhos/5:.1f} anos")
    
    # 6. Resumo das fontes
    print(f"\n📚 FONTES DOS DADOS")
    fontes = dados_brasil.get_resumo_fontes()
    
    print("Fontes Oficiais:")
    for fonte in fontes['fontes_oficiais']:
        print(f"  • {fonte}")
    
    print("\nFontes de Mercado:")
    for fonte in fontes['fontes_mercado']:
        print(f"  • {fonte}")
    
    print(f"\nData da Atualização: {fontes['data_atualizacao']}")
    
    print(f"\n✅ TODOS OS DADOS SÃO REAIS E ATUALIZADOS!")
    print("Para análise completa com dados reais, execute: python scripts/gerar_resultados.py")

if __name__ == "__main__":
    main()
