# Calculadora de Custos e Precificação de Sacolas Personalizadas

print('=== CALCULADORA DE PREÇO DE SACOLAS PERSONALIZADAS ===\n')

# === Entradas ===
material = float(input('Custo total de MATERIAL por unidade (R$): '))
mao_obra = float(input('Custo de MÃO DE OBRA por unidade (R$): '))
fixos = float(input('Custo FIXO rateado por unidade (R$): '))

tipo = input('Tipo de sacola (papel / plastico / ecobag): ').strip().lower()

custo_total = material + mao_obra + fixos

print(f'\n✅ Custo Total por unidade: R$ {custo_total:.2f}')

# Markup
markup = float(input('\nQual markup desejado (%)? (ex: 80): ')) / 100
preco_venda = round(custo_total * (1 + markup), 2)

print(f'💰 Preço de Venda Sugerido: R$ {preco_venda}')
print(f'📈 Lucro bruto por unidade: R$ {round(preco_venda - custo_total, 2)} ({int(markup*100)}%)\n')

# Recomendações por tipo
recomendacoes = {
    'papel': 'Margem bruta recomendada: 50-75%. Bom para varejo e brindes.',
    'plastico': 'Margem bruta recomendada: 70-120%. Ideal para alto volume.',
    'ecobag': 'Margem bruta recomendada: 55-90%. Maior valor percebido (premium).'
}

print('💡 Recomendação:', recomendacoes.get(tipo, 'Ajuste conforme seu mercado e qualidade.'))