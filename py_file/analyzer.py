import datetime
import time
import os
from os import listdir
from os.path import isdir
from PIL import Image
from numpy import savez_compressed, asarray, load, expand_dims
from mtcnn.mtcnn import MTCNN
from keras.models import load_model
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
import pickle

# Classe Que Treina O Modelo svm-SVC Para Reconhecer A Imagem 
class FaceTrainer:
    def __init__(self):
        # Local Armazenar Imagens De Treino E Teste
        self.datasetpath = "C:\\zproject-course\\dataset\\" #"C:\\zproject-course\\deeplearn\\dataset\\"
        # Local Armazenar Imagens De Treino E Teste Compactadas
        self.faces_npz = "C:\\zproject-course\\dataset\\faces_dataset.npz" #"C:\\zproject-course\\deeplearn\\dataset\\faces_dataset.npz"
        # Local Armazenar Algoritimo De Reconhecimento Facial Treinado Com Centenas de Milhares de Imagens
        self.keras_facenet = "C:\\zproject-course\\facenet\\facenet_keras.h5" #"C:\\zproject-course\\deeplearn\\facenet\\facenet_keras.h5"
        # Local Armazenar 
        self.faces_embeddings = "C:\\zproject-course\\facerecognition\\faces_dataset_embeddings.npz" #"C:\\zproject-course\\deeplearn\\facerecognition\\faces_dataset_embeddings.npz"
        self.svm_classifier = "C:\\zproject-course\\facerecognition\\SVM_classifier.sav" #"C:\\zproject-course\\deeplearn\\facerecognition\\SVM_classifier.sav"
        return

    # Retornar Somente Face Das Imagens De Treino e Teste Convertidas Em Array
    def load_dataset(self, directory):
        X = []
        y = []
        # Trazer Somente A Face De Cada Imagem Nos Diretórios Informados
        for subdir in listdir(directory):
            path = directory + subdir + '\\'
            # Desconsiderar Qualquer Arquivo Que Pode Estar No Diretorio
            if not isdir(path):
                continue
            # Carregar Todas As Faces No Subdiretório
            faces = self.load_faces(path)
            # Criar Legenda/Etiqueta
            labels = [subdir for _ in range(len(faces))]
            print("carregado {} exemplos para classificar: {}".format(len(faces), subdir))
            X.extend(faces)
            y.extend(labels)
        return asarray(X), asarray(y)

    # Retornar Apenas A Face De Cada Imagem Gravada Em Determinado Dataset, Com Dimensão 160x160
    def load_faces(self, directory):
        faces = []
        # Percorrer Por Todos Os Diretórios
        for filename in listdir(directory):
            path = directory + filename
            # Retorna A Face De Cada Imagem Gravada Em Determinado Dataset Com Dimensão 160x160
            face = self.extract_face(path)
            faces.append(face)
        return faces

    # Extrair A Face De Cada Imagem Gravada Em Determinado Dataset
    def extract_face(self, filename, required_size=(160, 160)):
        image = Image.open(filename)
        image = image.convert('RGB')
        pixels = asarray(image)
        # Instanciar Objeto Para Detectar Face Da Imagem Convertida Em Array
        detector = MTCNN()
        results = detector.detect_faces(pixels)
        # Extrair Os Limites Da Caixa Da Primeira Face
        x1, y1, width, height = results[0]['box']
        # Convertendo Coordenadas x, y Em Valores Absolutos (Corrigir Inconsistencia)
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + width, y1 + height
        # Extrair Apenas A Face
        face = pixels[y1:y2, x1:x2]
        # Redimensionar Pixels Ao Tamanho Do Modelo
        image = Image.fromarray(face)
        image = image.resize(required_size)
        face_array = asarray(image)
        return face_array

    # Criar Arquivo Comprimido De Todas As Faces Convertidas Em Array, Que Serão Treinadas E Validadas
    def create_faces_npz(self):
        trainX, trainy = self.load_dataset(self.datasetpath+"train\\")
        print("Treinando conjunto de dados . . .")
        testX, testy = self.load_dataset(self.datasetpath+"test\\")
        print("Testando conjunto de dados . . .")
        # Comprimir As Imagens Convertidas em Array E Gravar Em Determinado Local
        savez_compressed(self.faces_npz, trainX, trainy, testX, testy)
        return

    # Retornar O Arquivo Criado Com A Predição Das Imagens De Treino E Teste Embedded
    def create_faces_embedding_npz(self):
        # Traz O Dataset Com As Faces Em Array E Exibe Informação Em Tela
        data = load(self.faces_npz)
        trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
        print('Carregado: ', trainX.shape, trainy.shape, testX.shape, testy.shape)
        # Carrega O Modelo Facenet facenet_keras.h5 E Exibe Informação em Tela
        model = load_model(self.keras_facenet)
        print('Keras Facenet Model Carregado')
        # Fazer Embedding De Cada Imagens De Treino Que Esta Convertida em Array numpy
        newTrainX = list()
        for face_pixels in trainX:
            embedding = self.get_embedding(model, face_pixels)
            newTrainX.append(embedding)
        newTrainX = asarray(newTrainX)
        # Fazer Embedding De Cada Imagens De Teste Que Esta Convertida em Array numpy
        newTestX = list()
        for face_pixels in testX:
            embedding = self.get_embedding(model, face_pixels)
            newTestX.append(embedding)
        newTestX = asarray(newTestX)
        # Comprimir As Imagens Embedded E Salvar Em Um Arquivo
        savez_compressed(self.faces_embeddings, newTrainX, trainy, newTestX, testy)
        return

    # Retornar A Predição De Cada Imagem Sob Face Embedding
    def get_embedding(self, model, face_pixels):
        # Escalar Valores De Pixel
        face_pixels = face_pixels.astype('float32')
        # Aplicar Standardization : Calculo de Média Aritmética / Desvio Padrão Nas Imagems Numéricas
        mean, std = face_pixels.mean(), face_pixels.std()
        face_pixels = (face_pixels - mean) / std
        # Expandir A Forma Da Imagem Que Esta Convertido Em Array
        samples = expand_dims(face_pixels, axis=0)
        # Fazer A Predição Sobre As Imagems Em Embedding
        yhat = model.predict(samples)
        return yhat[0]

    # Retornar A Predição Das Imagens De Treino e Teste Sob a Classificador svm-SVC
    def classifier(self):
        data = load(self.faces_embeddings)
        trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
        print('Dataset: treino=%d, teste=%d' % (trainX.shape[0], testX.shape[0]))
        # Normalizar Com l2 As Imagens Embedded
        in_encoder = Normalizer(norm='l2')
        trainX = in_encoder.transform(trainX)
        testX = in_encoder.transform(testX)
        # Aplicar o labelEncoder Noas Imagens De Treino E Teste
        out_encoder = LabelEncoder()
        out_encoder.fit(trainy)
        trainy = out_encoder.transform(trainy)
        testy = out_encoder.transform(testy)
        # Treinar Modelo svm-SVC Com As Imagens de Treino
        model = SVC(kernel='linear', probability=True)
        model.fit(trainX, trainy)
        # Salvar O Modelo Treinado Em Um Local No Computador
        filename = self.svm_classifier
        pickle.dump(model, open(filename, 'wb'))
        # Predizer As Imagens De Treino e Teste
        yhat_train = model.predict(trainX)
        yhat_test = model.predict(testX)
        # Regornar A Pontuação Da Precisão Da Predição Sobre As Imagens De Treino e Teste
        score_train = accuracy_score(trainy, yhat_train)
        score_test = accuracy_score(testy, yhat_test)
        print('Acurácia: treino=%.3f, teste=%.3f' % (score_train * 100, score_test * 100))
        return

    # Iniciar Processo Treinamento Do Algoritmo
    def start(self):
        start_time = time.time()
        st = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
        print("----------------------------------------------------------------------------------------")
        print("Analise Reconhecimento Facial Iniciado em {}".format(st))
        print("----------------------------------------------------------------------------------------")
        # Criar Arquivo Comprimido De Todas As Faces Convertidas Em Array, Que Serão Treinadas E Validadas
        self.create_faces_npz()
        # Retornar O Arquivo Criado Com A Predição Das Imagens De Treino E Teste Embedded
        self.create_faces_embedding_npz()
        # Retornar A Predição Das Imagens De Treino e Teste Sob a Classificador svm-SVC
        self.classifier()
        end_time = time.time()
        et = datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
        print("----------------------------------------------------------------------------------------")
        print("Analise Reconhecimento Facial Finalizado em {}".format(et))
        print("Total Tempo Decorrido {} segs".format(round(end_time - start_time), 0))
        print("----------------------------------------------------------------------------------------")
        return

# Chamar Classe MainMenu Para Exibir Menu Que Será Manipulado
if __name__ == "__main__":
    os.system('cls')
    menu = FaceTrainer()
    menu.start()