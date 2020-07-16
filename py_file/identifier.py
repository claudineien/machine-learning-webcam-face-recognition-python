import cv2
import os
from PIL import Image
import numpy as np
from mtcnn.mtcnn import MTCNN
from keras.models import load_model
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import LabelEncoder
import pickle

# Identificar A Quem Pertence A Face Da Pessoa Através Da Webcam
class FaceDetector:
    def __init__(self):
        self.facenet_model = load_model("C:\\zproject-course\\facenet\\facenet_keras.h5")
        self.svm_model = pickle.load(open("C:\\zproject-course\\facerecognition\\SVM_classifier.sav", 'rb'))
        self.data = np.load('C:\\zproject-course\\facerecognition\\faces_dataset_embeddings.npz')
        # Instanciar Objeto MTCNN Para Detectar Face
        self.detector = MTCNN()

    # Detectar Face Pela Webcam E Retornar Coordenadas Do Local Da Face
    def face_mtcnn_extractor(self, frame):
        result = self.detector.detect_faces(frame)
        return result

    # Trazer As Coordenadas Da Face Para Ser Identificada Pelo Classificador
    def face_localizer(self, person):
        bounding_box = person['box']
        x1, y1 = abs(bounding_box[0]), abs(bounding_box[1])
        width, height = bounding_box[2], bounding_box[3]
        x2, y2 = x1 + width, y1 + height
        return x1, y1, x2, y2, width, height

    # Reprocessar As Imagens Aplicando Standardization, Normalization, Embedding
    # Retornar A Coordenada Predita da Imagem Sob O modelo facenet_keras.h5
    def face_preprocessor(self, frame, x1, y1, x2, y2, required_size=(160, 160)):
        # Redimensiona A Imagem
        face = frame[y1:y2, x1:x2]
        image = Image.fromarray(face)
        image = image.resize(required_size)
        face_array = np.asarray(image)
        # Converte A Imagem Para Tipo Float32 Da numpy
        face_pixels = face_array.astype('float32')
        # Aplica O Standardization
        mean, std = face_pixels.mean(), face_pixels.std()
        face_pixels = (face_pixels - mean) / std
        # Expande A Imagem Array
        samples = np.expand_dims(face_pixels, axis=0)
        # Retorna A Coordenada Predita Da Imagem
        yhat = self.facenet_model.predict(samples)
        face_embedded = yhat[0]
        # Normalizar A Imagem-Vetores
        in_encoder = Normalizer(norm='l2')
        X = in_encoder.transform(face_embedded.reshape(1, -1))
        return X

    # Faz A Predição Sobre A Imagen Filmada Pela Webcam, Sob a Modelo Treinado pelo svm-SVC
    # Aplica O LabelEncoder e Retorna A Informação Predita E A Probabilidade Da Identificação
    def face_svm_classifier(self, X):
        # Predição Sob a Modelo Treinado pelo svm-SVC
        yhat = self.svm_model.predict(X)
        label = yhat[0]
        yhat_prob = self.svm_model.predict_proba(X)
        probability = round(yhat_prob[0][label], 2)
        trainy = self.data['arr_1']
        # Predição Sob Labelencoder
        out_encoder = LabelEncoder()
        out_encoder.fit(trainy)
        predicted_class_label = out_encoder.inverse_transform(yhat)
        label = predicted_class_label[0]
        return label, str(probability)

    # Retornar O Resultado Da Predição Em Tempo Real Na Webcam : Nome e Probabilidade
    def face_detector(self):
        # Inicializar Objeto Que Habilita Camera/WebCam Para Capturar Imagem. 0 = WebCam Notebook/PC
        cap = cv2.VideoCapture(0)
        # Enquanto A Webcam Estiver Ativa -Visualizando Imagem
        while True:
            # Detectar Face Em Cada Frame
            __, frame = cap.read()
            # Detectar Face Pela Webcam E Retornar Coordenadas Do Local Da Face
            result = self.face_mtcnn_extractor(frame)
            if result:
                # Desenhar Retângulo Na Face Detectada Utilizando As Coordenadas
                for person in result:
                    # Trazer As Coordenadas Da Face Para Ser Identificada Pelo Classificador
                    x1, y1, x2, y2, width, height = self.face_localizer(person)
                    # Reprocessar As Imagens Aplicando Standardization, Normalization, Embedding
                    # Retornar A Coordenada Predita da Imagem Sob O modelo facenet_keras.h5
                    X = self.face_preprocessor(frame, x1, y1, x2, y2, required_size=(160, 160))
                    # Predizer A Etiqueta Com Nome E Probabilidade
                    label, probability = self.face_svm_classifier(X)
                    print(" Person : {} , Probability : {}".format(label, probability))
                    # Desenhar Linhas Do Retangulo Sobre A Imagem
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 155, 255), 2)
                    # Exibir Na Janela WebCam O Nome Localizado E A Probabilidade
                    cv2.putText(frame, label+probability, (x1, height),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255),
                                lineType=cv2.LINE_AA)
            # Exibir A Janela Infinitamente Ate Uma Tecla Ser Pressionada Para Uma Ação Qualquer
            k = cv2.waitKey(1)
            # Mostrar Janela-Frame Com Descrição No Topo
            cv2.imshow("Identificando Imagem - ESC = Finalizar", frame)
            # Verificar Se Foi Pressionado A Tecla 27=ESC Para Fechar Webcam
            if k%256 == 27:
                k = cv2.waitKey(1)
                print("")
                print("ESC pressionado. Fechando Câmera")
                break

        # Ao Final Da Uso da Webcam Limpa As Variáveis Objeto Webcam E
        # Janelas Utilizadas Neste Processo, Respectivamente
        cap.release()
        cv2.destroyAllWindows()

# Chamar Classe MainMenu Para Exibir Menu Que Será Manipulado
if __name__ == "__main__":
    os.system('cls')
    menu = FaceDetector()
    menu.face_detector()