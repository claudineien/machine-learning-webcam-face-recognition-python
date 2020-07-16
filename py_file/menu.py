import os
import subprocess
import cv2
from mtcnn.mtcnn import MTCNN

# Classe 
class MainMenu:
    def __init__(self):
        self.detector = MTCNN()
        self.file_path = "C:\\zproject-course\\"
        print("= MACHINE LEARNING NO SISTEMA RECONHECIMENTO FACIAL ATRAVÉS DE CAMERA - OpenVC, MTCNN, LabelEncoder =")

    def homemenu(self):
        print("")
        print("Digite O Número Relacionado a Opção Desejada")
        print("")
        print("1 Gravar Imagem")
        print("2 Analisar Imagem")
        print("3 Identificar Imagem")
        print("0 Sair Do Sistema")
        choice = 0
        try:
            choice = int(input(" >> "))
        except ValueError:
            print("")
            print("== Atenção ==")
            print("Digite Valor Númerico")
            print("             =======")
            self.homemenu()

        self.choice = choice
        self.callactions(str(self.choice))
   
    def saveperson(self):
        os.system('cls')
        print("Gravando...")
        print("Digitar Dados Do Participante")
        pathreg = self.file_path+"register.py"
        try:
            pathreg
            subprocess.call(["python",pathreg])
        except ValueError:
            print("Arquivo "+pathreg+" Nao Encontrado. Retornando ao menu principal")
        
        os.system('cls')
        self.homemenu()
        return

    def analyze(self):
        os.system('cls')
        print("Analisando Imagem ...")
        pathanlyz =  self.file_path+"analyzer.py"
        try:
            pathanlyz
            subprocess.call(["python",pathanlyz])
        except ValueError:
            print("Arquivo "+pathanlyz+" Nao Encontrado. Retornando ao menu principal")
        os.system('cls')
        self.homemenu()
        return

    def identifyimg(self):
        print("Identificando Imagem ...")
        pathident =  self.file_path+"identifier.py"
        try:
            pathident
            subprocess.call(["python",pathident])
        except ValueError:
            print("Arquivo "+pathident+" Nao Encontrado. Retornando ao menu principal")
        os.system('cls')
        self.homemenu()
        return

    def exitsystem(self):
        print("Sistema Encerrado !")
        os.system('cls')
        quit()
        return

    def callactions(self,ch):
        self.actionsmenu(ch)
        
        return

    def actionsmenu(self,opcao):
        menu_actions = {
                        'main_menu': self.homemenu,
                        '1': self.saveperson,
                        '2': self.analyze,
                        '3': self.identifyimg,
                        '0': self.exitsystem
                        }
        menu_actions[opcao]()
        return

# Chamar Classe MainMenu Para Exibir Menu Que Será Manipulado
if __name__ == "__main__":
    os.system('cls')
    menu = MainMenu()
    menu.homemenu()