def analisa_faturamento(faturamento_diario):
  """Analisa o faturamento diário de uma distribuidora.

  Args:
    faturamento_diario: Uma lista com os valores de faturamento de cada dia.

  Returns:
    Uma tupla com o menor valor, o maior valor e a quantidade de dias com faturamento acima da média.
  """

  # Verifica se a lista está vazia
  if not faturamento_diario:
    return None, None, 0

  # Calcula a média mensal
  media_mensal = sum(faturamento_diario) / len(faturamento_diario)

  # Encontra o menor e o maior valor
  menor_valor = min(faturamento_diario)
  maior_valor = max(faturamento_diario)

  # Conta os dias com faturamento acima da média
  dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

  return menor_valor, maior_valor, dias_acima_media

# Exemplo de uso:
faturamento_diario = [1000, 1500, 2000, 500, 1200]
menor, maior, dias_acima = analisa_faturamento(faturamento_diario)

print("Menor valor:", menor)
print("Maior valor:", maior)
print("Dias acima da média:", dias_acima)