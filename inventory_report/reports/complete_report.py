from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def productsInStock(produtosParamslist):
        resultCompanyComplete = list(
            each_line["nome_da_empresa"]
            for each_line in produtosParamslist
            if each_line["nome_da_empresa"]
        )
        resultCompanyFilter = Counter(resultCompanyComplete).most_common()

        resultToformat = ""
        for company in resultCompanyFilter:
            resultToformat += f"- {company[0]}: {company[1]}\n"
        return resultToformat

    @classmethod
    def generate(cls, produtosParamslist):
        productsInStock = CompleteReport.productsInStock(produtosParamslist)

        return (
            super().generate(produtosParamslist)
            + "\nProdutos estocados por empresa:\n"
            + productsInStock
        )
