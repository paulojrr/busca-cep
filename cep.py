import requests
import json

print("**************** Consulta cep ********************")
print("**************************************************\n")

continua = True

while(continua):
    cep = input('Digite o cep que deseja buscar!\n')

    req_url = "http://viacep.com.br/ws/{}/json".format(cep)

    req = requests.get(req_url)
    if(req.status_code == 200):
        json_data = json.loads(req.text)
        for key, value in json_data.items():
            if(value == ""):
                continue
            print(key + " : " + value)
    else:
        print("Cep não encontrado")

    loop = input("Deseja buscar outro cep ? 1 = sim, 2 = não\n")
    if(loop == "1"):
        continua = True
    elif(loop == "2"):
        print("Programa encerrado!")
        continua = False
    else:
        print("Digito incorreto, programa encerrado!")
        continua = False
    
