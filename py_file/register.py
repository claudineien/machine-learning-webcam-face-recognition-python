import os
import subprocess
from cv2 import *
import cv2
from mtcnn.mtcnn import MTCNN

# Classe para registrar/gravar a imagem em seu computador
class RegisterImg:
    def __init__(self):
        # Local Gravar Imagem Do Participante
        self.grv_img = "C:\\zproject-course\\dataset\\"
        # Carregar Algoritmo Para Detectar Forma e Formato do rosto
        self.detector = MTCNN()
        print("= MACHINE LEARNING NO SISTEMA RECONHECIMENTO FACIAL ATRAVÉS DE CAMERA - OpenVC, MTCNN, LabelEncoder =")

    # Detectar Face Pela Webcam E Retornar Coordenadas Do Local Da Face
    def face_mtcnn_extractor(self, frame):
        result = self.detector.detect_faces(frame)
        return result
    
    # Pegar As Coordenadas Da Face E As Retornar Em Determinadas Variáveis
    def face_localizer(self, person):
        bounding_box = person['box']
        x1, y1 = abs(bounding_box[0]), abs(bounding_box[1])
        width, height = bounding_box[2], bounding_box[3]
        x2, y2 = x1 + width, y1 + height
        return x1, y1, x2, y2, width, height

    # Chamar Methodo para Gravar A Imagem Visualizada Atraves da Webcam
    def saveperson(self):
        os.system('cls')
        print("Gravando...")
        print("Digitar Dados Do Participante")
        matricula = 0
        try:
            matricula = int(input("Número Matrícula -> "))
        except ValueError:
            print("")
            print("== Atenção ==")
            print("Digite Valor Númerico")
            print("              =======")
        nome = input("Nome Completo -> ")
        
        # Inicializar Objeto Que Habilita Camera/WebCam Para Capturar Imagem. 0 = WebCam Notebook/PC
        cam = cv2.VideoCapture(0)

        # Enquanto A Webcam Estiver Ativa -Visualizando Imagem
        while True:
            # Detectar Face Em Cada Frame
            ret, frame = cam.read()
            if not ret:
                break
            # Detectar Face Pela Webcam E Retornar Coordenadas Do Local Da Face
            result = self.face_mtcnn_extractor(frame)
            # Exibir A Janela Ate Uma Tecla Ser Pressionada Para Uma Ação Qualquer
            k = cv2.waitKey(1)
            # Desenhar Retângulo Na Face Detectada Utilizando As Coordenadas
            for person in result:
                # Trazar As Coordenadas Da Face E As Colocar Em Determinadas Variáveis
                x1, y1, x2, y2, width, height = self.face_localizer(person)
                # Desenhar Linhas Do Retangulo Sobre A Imagem
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 155, 255), 2)
            # Mostrar Janela-Frame Com Descrição No Topo
            cv2.imshow("Coletar Imagens - ENTER = Gravar / ESC = Finalizar", frame)
            # Verificar Se Foi Pressionado A Tecla 27=ESC Para Fechar Webcam
            if k%256 == 27:
                k = cv2.waitKey(1)
                print("")
                print("ESC pressionado. Fechando Câmera")
                break
                # Verificar Se Foi Pressionado A Tecla 13=ENTER Para Gravar Imagem Através Da Webcam
            elif k%256 == 13: # Se pressionar o ENTER
                # Converter Imagem À Escala Cinza
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # Criar Diretótio Com Nome do Participante
                os.mkdir(self.grv_img+"train\\"+nome+"_"+str(matricula))
                os.mkdir(self.grv_img+"test\\"+nome+"_"+str(matricula))
                # Gravar Imagem Com Nome Filmado + Numero De Matrícula
                cv2.imwrite(self.grv_img+"train\\"+nome+"_"+str(matricula)+"\\part-"+str(matricula)+".jpg", gray[y1:y2,x1:x2])
                cv2.imwrite(self.grv_img+"test\\"+nome+"_"+str(matricula)+"\\part-"+str(matricula)+".jpg", gray[y1:y2,x1:x2])
                print("Imagem gravada!")
        # Ao Final Da Uso da Webcam Limpa As Variáveis Objeto Webcam E
        # Janelas Utilizadas Neste Processo, Respectivamente
        cam.release()
        cv2.destroyAllWindows()
        return

# Chamar Classe MainMenu Para Exibir Menu Que Será Manipulado
if __name__ == "__main__":
    os.system('cls')
    menu = RegisterImg()
    menu.saveperson()