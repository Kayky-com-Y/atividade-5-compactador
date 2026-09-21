class Compactador:
    def __init__(self, data: str = ""):
        self.data = data

    def compactar(self):
        with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
            texto = arquivo.read()

        quantidade = len(texto)

        for caractere in texto:
            if caractere == "A":
                self.data += "00"
            elif caractere == "T":
                self.data += "01"
            elif caractere == "G":
                self.data += "10"
            elif caractere == "C":
                self.data += "11"

        dados = bytearray()

        dados.extend(quantidade.to_bytes(4, "big"))

        for i in range(0, len(self.data), 8):
            bloco = self.data[i:i + 8]

            if len(bloco) < 8:
                bloco = bloco.ljust(8, "0")

            dados.append(int(bloco, 2))

        with open("arquivoCompactado.txt", "wb") as arquivo:
            arquivo.write(dados)

    def descompactar(self):
        with open("arquivoCompactado.txt", "rb") as arquivo:
            dados = arquivo.read()

        quantidade = int.from_bytes(dados[:4], "big")

        dados = dados[4:]

        bits = ''.join(format(byte, '08b') for byte in dados)

        bits = bits[:quantidade * 2]

        texto = ""

        for i in range(0, len(bits), 2):
            bloco = bits[i:i + 2]

            if bloco == "00":
                texto += "A"
            elif bloco == "01":
                texto += "T"
            elif bloco == "10":
                texto += "G"
            elif bloco == "11":
                texto += "C"

        with open("arquivoDescompactado.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)


arquivo = Compactador()

arquivo.compactar()
arquivo.descompactar()