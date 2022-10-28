from inventory_report.inventory.product import Product


def test_cria_produto():
    dataModel = Product(
        1,
        "Borracha",
        "Papelaria Solar",
        "2021-07-04",
        "2029-02-09",
        "FR48",
        "Ao abrigo de luz solar"
    ) 
    
    assert dataModel.id == 1
    assert dataModel.nome_do_produto == "Borracha"
    assert dataModel.nome_da_empresa == "Papelaria Solar"
    assert dataModel.data_de_fabricacao == "2021-07-04"
    assert dataModel.data_de_validade == "2029-02-09"
    assert dataModel.numero_de_serie == "FR48"
    assert dataModel.instrucoes_de_armazenamento == "Ao abrigo de luz solar"