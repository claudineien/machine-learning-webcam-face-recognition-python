<h2 align="center"><strong>Sistema Reconhecimento facial em tempo real através da webcam</strong></h2>
<details open>
  <summary><strong>1. CONCEITOS DE FORMA SIMPLES</strong></summary>
  <ol>
    <li><strong>Reconhecimento Facial</strong>
      <p>É a técnica de capturar/pegar em uma imagem toda a parte frontal do rosto/face que envolve parte da cabeça, testa, olhos, nariz, maças do rosto, bochechas, boca, maxilar, queixo, analisar a distância entre cada uma destas partes, comparar com outras imagens, identificar diferenças, comparar similaridades e exibir o alvo desejado</p>
      <p>A imagem considerada é obtida de uma foto, vídeo ou câmera</p>
      <p>O alvo desejado é o oser humano que esta sendo buscado</p>
      <p><b>Nota: </b>Esta técnica é normalmente utilizada em seres humanos</p>
    </li>
    <li><strong>Machine Learning</strong>
      <p>É a técnica computacional de ensinar uma máquina com determinado poder computacional a resolver tarefas complexas para predizer ações passadas ou futuras o mais automático possível</p>
      <p>Esta técnica pode ser utilizada para tentar resolver qualquer tarefa, por mais complexa que seja</p>
    </li>
    <li><strong>Deep Learning</strong>
      <p>É a técnica computacional que analisa muito detalhadamente determinadas características de imagem, aúdio ou voz para auxiliar a identificar o seu autor e/ou </p>
    </li>
  </ol>
</details>

<details open>
  <summary><strong>2. INFORMAÇÕES TÉCNICAS</strong></summary>
  <ol>
    <li><strong>Tecnologias utilizadas neste projeto</strong>
      <ol>
        <p>
        <li>- [x] Linguagem de programação : python 3.7.7</li>
        <li>- [x] Visual Studio Code : Version: 1.46.0 (user setup) Commit: a5d1cc28bb5da32ec67e86cc50f84c67cc690321 Date: 2020-06-10T09:03:20.462Z Electron: 7.3.1</li>
        <li>- [x] OS : Windows_NT Home x64 10.0.18363</li>
        <li>- [x] CPU : Intel(R) Corel(TM) i3-4005U CPU @ 1.70GHz 1.70 GHz</li>
        <li>- [x] RAM : 8GB</li>
        <li>- [x] SSD : 225GB</li>
        <li>- [x] Browser : Chrome: 78.0.3904.130</li>
        <li>- [x] Plataforma Front de Desenvolvimento : Jupyter notebook 4.6.3</li>
        <li>- [x] Plataforma Back de Desenvolvimento : miniconda-conda 4.8.3</li>
        </p>
      </ol>
    </li>
    <li><strong>Algoritmos de visão computacional <a href="https://opencv.org/" target="_blank"><img src="opencv-logo-white-mini.jpg" alt="OpenCV" width="28" height="28"></a> para</strong>
      <ol>
        <p>
        <li>- [x] Acessar a webcam local do computador, notebook </li>
        <li>- [x] Gravar a imagem capturada com outras imagens no computador local</li>
        </p>
      </ol>
    </li>
    <li><strong>Algoritmos deep learning e rede neural <a style="font-color:green"  href="https://pypi.org/project/mtcnn/" target="_blank">mtcnn 0.1.0</a> para</strong>
      <ol>
        <p>
        <li>- [x] Analisar imagem capturada</li>
        <li>- [x] Disponibilizar resultado da análise</li>
        </p>
      </ol>
    </li>    
    <li><strong>Utilizando as técnicas machine learning vamos</strong>
      <ol>
        <p>
          <li>- [x] Aplicar Standartization</li>
          <li>- [x] Aplicar Normatization</li>
          <li>- [x] Executar treinamento de reconhecimento facial do algorítimo MTCNN</li>
          <li>- [x] Utilizar técnica de Predição do algorítimo MTCNN</li>
          <li>- [x] Converter dados categóricos em numéricos com LabelEncoder</li>
          <li>- [x] Treinar o modelo Classificador SVC-SVM</li>
          <li>- [x] Exibir o resultado da identificação no algorítimo OpenCV pela webcam</li>
        </p>
      </ol>
    </li>    
  </ol>
</details>

<br>
<br>
<br>
<br>
<br>
<br>
<img src="opencv-logo-white-mini.jpg" alt="Workplace" usemap="#workmap" width="38" height="38">
<br>
<br>
<br>
<br>
<br>
<br>
<br>
## Sistema Reconhecimento facial em tempo real através da webcam

### 1. CONCEITOS DE FORMA SIMPLES
### Reconhecimento Facial
É a técnica de capturar/pegar toda a parte do rosto que envolve testa, olhos, nariz, bochechas, boca, maxilar, queixo, analisar a distância entre cada uma destas partes, comparar com outras imagens, identificar diferenças, apontar similaridades e exibir resultado mais próximo ao que desejamos

A imagem considerada é uma foto, vídeo ou câmera

### Machine Learning
É a técnica computacional de ensinar uma máquina com determinado poder computacional a resolver tarefas complexas para predizer ações passadas ou futuras o mais automático possível
Esta técnica pode ser utilizada para tentar resolver qualquer tarefa, por mais complexa que seja

### Deep Learning
É a técnica computacional que analisa muito detalhadamente determinadas características de imagem, aúdio ou voz para auxiliar a identificar o seu autor e/ou

### 2. INFORMAÇÕES TÉCNICAS
### Tecnologias utilizadas neste projeto
- [X] Linguagem de programação : python 3.7.7
- [X] Visual Studio Code : Version: 1.46.0 (user setup) Commit: a5d1cc28bb5da32ec67e86cc50f84c67cc690321 Date: 2020-06-10T09:03:20.462Z Electron: 7.3.1
- [X] OS : Windows_NT Home x64 10.0.18363
- [X] CPU : Intel(R) Corel(TM) i3-4005U CPU @ 1.70GHz 1.70 GHz
- [X] RAM : 8GB
- [X] SSD : 225GB
- [X] Browser : Chrome: 78.0.3904.130
- [X] Plataforma Front de Desenvolvimento : Jupyter notebook 4.6.3
- [X] Plataforma Back de Desenvolvimento : miniconda-conda 4.8.3

### Utilizando algoritmos deep learning para desenvolver um sistema que
- [X] Acessará a webcam local do computador, notebook com o algoritmo  [![OpenCV](opencv-logo-white-mini.jpg "OpenCV")](https://opencv.org/ "OpenCV")
- [X] Gravará a imagem com outras imagens no computador local

### Utilizando as técnicas machine learning vamos 
- [X] Aplicar Standartization
- [X] Aplicar Normatization
- [X] Executar treinamento de reconhecimento facial do algorítimo MTCNN
- [X] Utilizar técnica de Predição do algorítimo MTCNN
- [X] Converter dados categóricos em numéricos com LabelEncoder
- [X] Treinar o modelo Classificador SVC-SVM

### 3. PRE-REQUISITOS PARA FUNCIONAMENTO DO SISTEMA
### Plataformas para desenvolvimento
* Instalar miniconda3
* Instalar jupyter notebook
* Instalar Visual Studio Code

Observação: Analisar o item **Tecnologias utilizadas neste projeto**

### Bibliotecas python utilizadas
<ol>
  <li>opencv-custom</li>
  <li>pandas</li>
  <li>SVC</li>
  <li>MTCNN</li>
</ol>

### 4. FLUXO DO PROCESSO
Desenvolver com a linguagem python um algoritmo machine learning em modo supervisionado para utilizar a tecnologia deep learning no reconhecimento facial

### 5. INSTALAÇÃO DO SISTEMA RECONHECIMENTO FACIAL EM TEMPO REAL ATRAVÉS DA WEBCAM
- [X] Baixar o arquivo dszero-desafio-facenet-mtcnn-labelencoder.ipynb
- [X] 


#### Origem deste projeto
Este foi um desafio proposto no curso Data Science do Zero da equipe Minerando Dados


#### Fontes de estudo
* [Minerando Dados](https://minerandodados.com.br/ "Minerando Dados")
* [Site OpenCV](https://opencv.org/ "Site OpenCV")
* [OpenCV no github](https://github.com/opencv/opencv/ "OpenCV no github")
* [Partnershiponai.org](https://www.partnershiponai.org/wp-content/uploads/2020/02/Understanding-Facial-Recognition-Paper_final.pdf "Partnershiponai.org")



### *AGRADECIMENTOS*
*Ser agradecido para mim é a atitude que torna as pessoas seres melhores*

Agradeço a minha mãe sra Rosalita Borges Evangelista por ter me ensinado, através de suas ações, a ser um guerreiro que aprende com a perda das batalhas mas alcança a vitória da guerra, por me ensinar a ser um ser humano que tenta melhorar a vida das pessoas

Agradeço à minha esposa e às minhas filhas por serem minha inspiração e pelo apoio em minhas decisões

Agradeço aos criadores do computador, da internet, das linguagens para programação computacional, inteligência artificial e tecnologias em geral

Agradeço a equipe Mineirando Dados que criou o espaço Data Sciente do Zero, disponibilizando diversos ensinamentos em machine learning, estatísticas, deep learning e data science, parq encurtar meu aprendizado

Muito obrigado a todos :wink:
