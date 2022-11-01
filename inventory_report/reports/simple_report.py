from collections import Counter
from datetime import date


class SimpleReport:
    @staticmethod
    def companyName(paramsData):
        resultNEmpresa = list()
        for each_line in paramsData:
            resultNEmpresa.append(each_line["nome_da_empresa"])
            biggestCompany = Counter(resultNEmpresa)
        return biggestCompany.most_common()[0][0]

    @staticmethod
    def expirationDate(paramsData):
        DATENOW = date.today()
        lisValidate = list()

        for each_line in paramsData:
            if each_line["data_de_validade"] >= str(DATENOW):
                lisValidate.append(each_line["data_de_validade"])
        return min(lisValidate)

    @staticmethod
    def manufacturingDate(paramsData):
        lisFabricacao = list()

        for each_line in paramsData:
            lisFabricacao.append(each_line["data_de_fabricacao"])
        return min(lisFabricacao)

    @staticmethod
    def generate(data):
        resultData = list()
        for each_line in data:
            if not (
                each_line["nome_do_produto"]
                or each_line["data_de_fabricacao"]
                or each_line["data_de_validade"]
            ):
                ValueError('Not Found.')
            resultData.append(each_line)
            resultNome = SimpleReport.companyName(resultData)
            resultFabricacao = SimpleReport.manufacturingDate(resultData)
            resultValidade = SimpleReport.expirationDate(resultData)
        return (
            f"Data de fabricação mais antiga: {resultFabricacao}\n"
            f"Data de validade mais próxima: {resultValidade}\n"
            f"Empresa com mais produtos: {resultNome}"
        )


# if __name__ == "__main__":
# web_server = SimpleReport(1, "CADEIRA", "Forces of Nature", "2022-04-04", "2023-02-09", "FR48", "Conservar em local fresco")
# web_server = SimpleReport()
# web_server.test()
#   data = [
# {
#   "id": 0,
#   "nome_do_produto": "laborum",
#   "nome_da_empresa": "da Luz - ME",
#   "data_de_fabricacao": "2022-10-06",
#   "data_de_validade": "2022-12-10",
#   "numero_de_serie": 0,
#   "instrucoes_de_armazenamento": "Nobis deleniti nulla consequatur sunt aperiam iure. Blanditiis vero molestias itaque itaque rem ipsam. Suscipit temporibus ex commodi eaque illo praesentium."
# },
# {
#   "id": 1,
#   "nome_do_produto": "eius",
#   "nome_da_empresa": "Barros",
#   "data_de_fabricacao": "2022-10-06",
#   "data_de_validade": "2022-12-10",
#   "numero_de_serie": 1,
#   "instrucoes_de_armazenamento": "Voluptatem fuga optio iste mollitia iusto. Incidunt autem veritatis animi. Beatae sapiente beatae qui in."
# },
# {
#   "id": 2,
#   "nome_do_produto": "dolor",
#   "nome_da_empresa": "Barros",
#   "data_de_fabricacao": "2022-10-06",
#   "data_de_validade": "2022-12-10",
#   "numero_de_serie": 2,
#   "instrucoes_de_armazenamento": "Consequatur sunt soluta harum at laudantium suscipit. Similique fuga ex maiores delectus dignissimos. Ex voluptate excepturi illum."
# },
# {
#   "id": 3,
#   "nome_do_produto": "ipsum",
#   "nome_da_empresa": "Rocha",
#   "data_de_fabricacao": "2022-09-06",
#   "data_de_validade": "2022-11-07",
#   "numero_de_serie": 3,
#   "instrucoes_de_armazenamento": "Libero ab quaerat. Numquam corporis voluptates aut laudantium libero culpa. Rem eaque quasi et. Aperiam dignissimos sed."
# }
# ]
#   SimpleReport.generate(data)

# console = SimpleReport.__init__(1, "CADEIRA", "Forces of Nature", "2022-04-04", "2023-02-09", "2023-02-09", "FR48", "Conservar em local fresco")
# print("entrei aqui", SimpleReport.__init__(1, "CADEIRA", "Forces of Nature", "2022-04-04", "2023-02-09", "FR48", "Conservar em local fresco").__nomeDoProduto, SimpleReport.nomeDaEmpresa,)
