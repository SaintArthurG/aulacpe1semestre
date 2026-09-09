import random
aleatorio = int(random.random() * 11)
print(aleatorio)


crc = 0
for i in range 


function calcularCRC(dados) :
    let crc = 0
    for (let i = 0; i < dados.length; i++) {
      crc = (crc * 3 + dados[i]) % 97
    
    return crc;
  