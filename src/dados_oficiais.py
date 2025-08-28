"""
Dados Oficiais Brasileiros - Atualizados em 2025
Fontes: IBGE, Banco Central, Governo Federal
"""

from datetime import datetime

class DadosOficiaisBrasil:
    """
    Dados econômicos oficiais do Brasil atualizados
    """
    
    def __init__(self):
        self.data_atualizacao = "28/08/2025"
        
        # DADOS GOVERNAMENTAIS OFICIAIS
        self.salario_minimo = {
            'valor': 1518,  # R$ 1.518,00 (Decreto nº 12.342/2024)
            'ano': 2025,
            'aumento_percentual': 7.5,  # 7,5% sobre 2024
            'fonte': 'Decreto Federal nº 12.342/2024'
        }
        
        # BANCO CENTRAL DO BRASIL
        self.indicadores_bc = {
            'selic': 14.25,  # 14,25% a.a. (março 2025)
            'cdi_estimado': 14.10,  # Aproximadamente 99% da Selic
            'inflacao_meta': 3.0,  # Meta oficial
            'inflacao_atual': 4.86,  # Projeção 2025
            'inflacao_2024': 3.82,  # Acumulado até novembro 2024
            'fonte': 'Banco Central do Brasil - Copom'
        }
        
        # TAXAS DE INVESTIMENTO REAIS (2025)
        self.investimentos = {
            'tesouro_selic': 14.25,  # Acompanha a Selic
            'tesouro_ipca_2029': 6.5,  # Tesouro IPCA+ 2029
            'tesouro_ipca_2035': 6.8,  # Tesouro IPCA+ 2035
            'cdb_grandes_bancos': 13.5,  # 95% do CDI
            'cdb_digitais': 14.0,  # 99% do CDI
            'lci_lca': 12.5,  # 88% do CDI (isento IR)
            'poupanca': 8.5,  # 70% da Selic quando > 8,5%
            'fundos_di': 13.0,  # 92% do CDI (líquido)
            'fonte': 'B3, Bancos, Corretoras'
        }
        
        # IBGE - DADOS DEMOGRÁFICOS E SOCIAIS
        self.demografia = {
            'expectativa_vida': 76.4,  # Anos (IBGE 2023)
            'idade_aposentadoria_media': 65,
            'populacao_economicamente_ativa': 107.8,  # Milhões
            'taxa_desemprego': 7.8,  # % (2024)
            'fonte': 'IBGE - PNAD Contínua'
        }
        
        # RENDA E TRABALHO
        self.renda_trabalho = {
            'renda_media_nacional': 3200,  # R$ (PNAD 2024)
            'renda_media_formal': 4500,  # R$ setor formal
            'renda_media_informal': 1800,  # R$ setor informal
            'horas_trabalho_semana': 44,  # Horas
            'horas_trabalho_mes': 192,  # Horas úteis
            'dias_uteis_ano': 252,
            'fonte': 'IBGE - PNAD Contínua 2024'
        }
        
        # CÂMBIO E ECONOMIA
        self.economia = {
            'dolar_atual': 6.00,  # R$/USD (projeção Bradesco 2025)
            'pib_crescimento_2025': 2.0,  # % projetado
            'pib_crescimento_2024': 3.4,  # % realizado
            'indice_gini': 0.544,  # Desigualdade (IBGE)
            'fonte': 'Banco Central, IBGE, Bradesco'
        }
        
        # POF - PESQUISA DE ORÇAMENTOS FAMILIARES (IBGE 2022-2023)
        self.gastos_familiares = {
            'habitacao': 0.366,  # 36,6% da renda
            'transporte': 0.181,  # 18,1%
            'alimentacao': 0.175,  # 17,5%
            'saude': 0.076,  # 7,6%
            'educacao': 0.047,  # 4,7%
            'vestuario': 0.039,  # 3,9%
            'recreacao': 0.023,  # 2,3%
            'outros': 0.093,  # 9,3%
            'fonte': 'IBGE - POF 2022-2023'
        }
        
        # CATEGORIAS DE GASTOS DESNECESSÁRIOS (Pesquisa de Mercado 2024)
        self.gastos_desnecessarios = {
            'alimentacao_fora': {
                'valor_medio_mensal': 450,  # R$ (aumento pós-pandemia)
                'frequencia_populacao': 0.75,  # 75% da população
                'necessidade': 3,  # Score 1-5
                'fonte': 'Associação Brasileira de Bares e Restaurantes'
            },
            'streaming_assinaturas': {
                'valor_medio_mensal': 180,  # R$ (múltiplas plataformas)
                'frequencia_populacao': 0.65,
                'necessidade': 2,
                'fonte': 'Pesquisa Streaming Brasil 2024'
            },
            'delivery_apps': {
                'valor_medio_mensal': 320,  # R$
                'frequencia_populacao': 0.60,
                'necessidade': 2,
                'fonte': 'ABComm - Associação Brasileira de Comércio Eletrônico'
            },
            'roupas_acessorios': {
                'valor_medio_mensal': 280,  # R$
                'frequencia_populacao': 0.70,
                'necessidade': 2,
                'fonte': 'ABIT - Associação Brasileira da Indústria Têxtil'
            },
            'bebidas_alcoolicas': {
                'valor_medio_mensal': 220,  # R$
                'frequencia_populacao': 0.45,
                'necessidade': 1,
                'fonte': 'IBGE - POF'
            },
            'cigarro_tabaco': {
                'valor_medio_mensal': 280,  # R$ (aumento impostos)
                'frequencia_populacao': 0.12,  # 12% fumantes
                'necessidade': 0,
                'fonte': 'INCA - Instituto Nacional de Câncer'
            },
            'transporte_desnecessario': {
                'valor_medio_mensal': 200,  # R$ (Uber/99 evitáveis)
                'frequencia_populacao': 0.55,
                'necessidade': 2,
                'fonte': 'Pesquisa Mobilidade Urbana 2024'
            },
            'compras_impulso': {
                'valor_medio_mensal': 380,  # R$
                'frequencia_populacao': 0.80,
                'necessidade': 1,
                'fonte': 'SPC Brasil - Comportamento do Consumidor'
            },
            'jogos_apostas': {
                'valor_medio_mensal': 150,  # R$ (crescimento das bets)
                'frequencia_populacao': 0.25,
                'necessidade': 0,
                'fonte': 'Pesquisa Datafolha Apostas Online 2024'
            }
        }
    
    def get_taxa_investimento_conservador(self):
        """Retorna taxa para perfil conservador"""
        return self.investimentos['tesouro_ipca_2029'] + self.indicadores_bc['inflacao_atual']
    
    def get_taxa_investimento_moderado(self):
        """Retorna taxa para perfil moderado"""
        return self.investimentos['cdb_digitais']
    
    def get_taxa_investimento_agressivo(self):
        """Retorna taxa para perfil agressivo (estimativa ações)"""
        return 16.0  # Estimativa baseada em histórico Ibovespa + dividendos
    
    def get_perfil_gastos_brasileiro(self):
        """Retorna perfil de gastos do brasileiro médio"""
        renda_media = self.renda_trabalho['renda_media_nacional']
        
        return {
            'renda_mensal': renda_media,
            'habitacao': renda_media * self.gastos_familiares['habitacao'],
            'transporte': renda_media * self.gastos_familiares['transporte'],
            'alimentacao': renda_media * self.gastos_familiares['alimentacao'],
            'saude': renda_media * self.gastos_familiares['saude'],
            'educacao': renda_media * self.gastos_familiares['educacao'],
            'recreacao': renda_media * self.gastos_familiares['recreacao'],
        }
    
    def get_cenarios_reais(self):
        """Retorna cenários baseados em dados reais brasileiros"""
        return {
            'Jovem Assalariado CLT': {
                'idade': 25,
                'renda_mensal': 2500,  # 1,6x salário mínimo
                'gastos_desnecessarios': 600,
                'perfil': 'Recém-formado, primeiro emprego'
            },
            'Profissional Classe Média': {
                'idade': 35,
                'renda_mensal': self.renda_trabalho['renda_media_nacional'],
                'gastos_desnecessarios': 800,
                'perfil': 'Família, casa própria'
            },
            'Executivo Sênior': {
                'idade': 45,
                'renda_mensal': self.renda_trabalho['renda_media_formal'],
                'gastos_desnecessarios': 1200,
                'perfil': 'Alta renda, múltiplas responsabilidades'
            }
        }
    
    def get_resumo_fontes(self):
        """Retorna resumo das fontes utilizadas"""
        return {
            'fontes_oficiais': [
                'IBGE - Instituto Brasileiro de Geografia e Estatística',
                'Banco Central do Brasil',
                'Ministério do Trabalho e Emprego',
                'Receita Federal do Brasil'
            ],
            'fontes_mercado': [
                'B3 - Brasil Bolsa Balcão',
                'ANBIMA - Associação Brasileira das Entidades dos Mercados Financeiro e de Capitais',
                'Bancos e Corretoras'
            ],
            'pesquisas_comportamento': [
                'SPC Brasil',
                'Serasa',
                'Associações Setoriais',
                'Institutos de Pesquisa'
            ],
            'data_atualizacao': self.data_atualizacao
        }

# Instância global para uso em outros módulos
dados_brasil = DadosOficiaisBrasil()
