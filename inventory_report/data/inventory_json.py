# import json

# try:
#     with open('data/inventory.json', 'r') as file:
#         inventory = json.load(file)
# except FileNotFoundError as exc:
#     print("O arquivo não foi encontrado")
# except json.decoder.JSONDecodeError:
#     print("Tem alguma coisa errada com o arquivo")