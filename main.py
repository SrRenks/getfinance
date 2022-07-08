from src.getdata import get_stock
from src.to_csv import to_csv


def main(stock, range):
    data = get_stock(stock, range)
    to_csv(data)


# Por padrão, ações brasileiras devem ser escritas com o final ".SA", exemplos:
# "USIM5.SA", "PETR4.SA", "MGLU3.SA".
stock = "nome_da_ação"
# existem 6 ranges disponíveis: 1d, 5d, 1mo, 6mo, ytd e 1y.
range = "range"
main(stock, range)
