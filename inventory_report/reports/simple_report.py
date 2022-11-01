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
