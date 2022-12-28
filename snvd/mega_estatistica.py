import pandas as pd


arquivo = (r".\\snvd\\mega_sena_resultados.xlsx")

dataframe = pd.read_excel(arquivo)
ranqueamento = dataframe.rank()
ranqueamento.to_excel("ranqueamento.xlsx")
print(dataframe.rank())
