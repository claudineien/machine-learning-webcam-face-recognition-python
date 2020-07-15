<h2 align="center"><strong>Machine Learning on facial recognition by webcam</strong></h2>
<h5 align="left">Target audience: Machine Learning Apprentice &#x1F393; - Objective: Demonstrate Machine Learning - Read Time: 00:09:30 mins - Language: 
<a href="https://github.com/claudineien/machine-learning-webcam-face-recognition-python">Portuguese</a>󠁧󠁢󠁥󠁮󠁧󠁿</h5>
<details class="sbdocs sbdocs-details">
  <summary class="sbdocs sbdocs-summary"><strong>1 CONCEPTS IN A SIMPLE WAY</strong></summary>
  <ol>
    <li><strong>Facial Recognition</strong>
      <p>It's the technique of capturing the front of the face in an image that involves part of the head, forhead, eyes, nose, cheek, mouth, jam, chin, analyzing the distance of between each of these parts, comparing them with other images, identifying differences, comparing similarities and displaying the desired target.</p>
      <p>The considered image can be in a picture, video or camera.</p>
      <p>The desired target is the human being that will be identified.</p>
    </li>
    <li><strong>Machine Learning</strong>
      <p><b>Machine Learning is the object of the study</b> in this project. It's the computational technique of teaching a machine whith a determined computing power to analyze a set of data and predict information to assist in decisions.</p>
      <p>This technique can be used to try to solve any task -from the simplest to the most complex.</p>
    </li>
    <li><strong>Deep Learning</strong>
      <p>It's the computational technique that analyzes  certain image characteristics in detail to help identify the owner of the image.</p>
    </li>
    <li><strong>Neural Network</strong>
      <p>It's the computational algorithm that learns from the new datas inserted, simulating the human brain.</p>
      <p>Example: We programmed a computer to learn all the details of the shapes and formats of a certain face, when inserting other faces it will automatically store its shapes and formats and from this datas the algorithm identifies who belongs to a a certain face</p>
    </li>
  </ol>
</details>

<details>
  <summary><strong>2 MACHINE LEARNING + WEBCAM - THE CHOICE </strong></summary><br>
  <p align="center" ><img title="Diagrama Machine Learning at Face Recognition" src="img/machlearnfacerecogn.png" alt="Machine Learning at Face Recognition" width="607" height="311"></p>
  <ol>
    <li><strong>Machine Learning as the back-end of the webcam</strong>
      <p>Demonstrating <b>machine learning</b> in facial recognition through a webcam, for me, is the easiest way to explain in pratice to anyone, that you can include intelligence in a machine with a certain amount of computing power. In this case I used the well-known Real-Time Facial Recognition.</p>
    </li>
    <li><strong>The following algorithm libraries were taugh in the Data Science do Zero training and produced an efficient result, even after these results I consulted various documentation, explanations and examples on data science sites to make this challenge. Core algotitms are :</strong>
      <p>
        <ul>
          <li>OpenCV</li>
          <li>MTCNN</li>
          <li>PIL</li>
          <li>numpy</li>
          <li>keras</li>
          <li>LabelEncoder</li>
          <li>svm-SVC</li>
          <li>Standardization</li>
          <li>Normalizer</li>
          <li>pickle</li>
        </ul>
      </p>
    </li>
    <p><b>Searched sources :</b> <a href="https://www.edureka.co/">edureka</a>, <a href="https://medium.com">medium</a>, <a href="https://stackoverflow.com/">stack overflow</a>, <a href="https://towardsdatascience.com/">towards data science</a></p>
  </ol>
</details>

<details>
  <summary><strong>3 TECHNICAL INFORMATION</strong></summary>
  <ol>
    <li><strong><a id="itemtec" >Technologies used in this project</a></strong>
      <ol>
        <p>
        <li>- [x] Programming language : python 3.7.7</li>
        <li>- [x] Python Package Index -pip : versão 20.1.1</li>
        <li>- [x] Visual Studio Code : Version: 1.46.0 (user setup) Electron: 7.3.1</li>
        <li>- [x] OS : Windows_NT x64 10.0.18363 (Windows 10 Home)</li>
        <li>- [x] CPU : Intel(R) Corel(TM) i3-4005U CPU @ 1.70GHz 1.70 GHz</li>
        <li>- [x] RAM : 8GB</li>
        <li>- [x] SSD : 225GB</li>
        <li>- [x] Browser : Chrome: 78.0.3904.130</li>
        <li>- [x] Development front plataform : Jupyter notebook 4.6.3</li>
        <li>- [x] Development back plataform : miniconda-conda 4.8.3</li>
        </p>
      </ol>
    </li>
    <li><strong>Computer vision algorithms <a href="https://opencv.org/" target="_blank"><img title="OpenCV" src="img/opencv-logo-white-mini.jpg" alt="OpenCV" width="28" height="28"></a> to </strong>
      <ol>
        <p>
        <li>- [x] Access the local computer/notebook webcam </li>
        <li>- [x] Display the real-time image through webcam</li>
        </p>
      </ol>
    </li>
    <li><strong>Deep learning and neural networks Algorithms <a style="font-color:green"  href="https://pypi.org/project/mtcnn/" target="_blank">mtcnn 0.1.0</a> to</strong>
      <ol>
        <p>
        <li>- [x] Apply multiple shape and format recognition calculations to the captured image</li>
        <li>- [x] Making calculations results available to machine learning algorithms</li>
        </p>
      </ol>
    </li>
    <li><strong>Using Machine Learning techniques we will learn how to :</strong>
      <ol>
        <p>
          <li>- [x] Calculet the Embedding of the image</li>
          <li>- [x] Apply Standardization</li>
          <li>- [x] Apply Normatization with sklearn Normalizer</li>
          <li>- [x] Convert categorical data to numerical data with LabelEncoder</li>
          <li>- [x] Perform facial recognition training with sklearn.svm's SVC algorithm
          </li>
          <li>- [x] Use sklearn.svm predict algorithm in the trainning and testing data</li>
          <li>- [x] Apply the accuracy/precision calculation of the sklearn.metrics accuracy_score algorithm  
        </li>
          <li>- [x] Calculate faces coordenates</li>
          <li>- [x] Use model predict method of the facenet_keras.h5's in the image viewed by webcam </li>
          <li>- [x] Apply the Normalizer l2 method</li>
          <li>- [x] Use LabelEncoder inverse transform</li>
          <li>- [x] Display the identification result on the webcam through the OpenCV algoritm</li>
        </p>
      </ol>
    </li>    
  </ol>
</details>

<details>
  <summary><strong><a id="prereq">4 PRE-REQUISITS FOR THE SYSTEM TO WORK</a></strong></summary>
  <ol>
    <li><strong>Install developement plataforms</strong>
      <ol>
        <p>
          <li>- [x] Install <a href="https://docs.conda.io/en/latest/miniconda.html" target="_blank">miniconda3</a></li>
          <li>- [x] Install <a href="https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html" target="_blank">jupyter notebook</a></li>
          <li>- [x] Install <a href="https://code.visualstudio.com/download" target="_blank">visual studio code</a></li>
        </p>
      </ol>
      <p><b>Note: </b><br>Analyze the item
       <em><a href="#itemtec">Technologies used in this project</a></em></p>
    </li>
    <li><strong>Install the algorithm libraries :</strong>
      <ol>
        <li>- [x] Update the pip python - python package index :computer: python3 -m pip install --upgrade pip</li>
        <li>- [x] I recommend using either anaconda prompt/terminal and/or miniconda to install the libraries for convenience and for having fewer inconsistences. </li>
        <li>- [x] Sintaxe for installing libraries : pip3 install [librarie_name] --user</li>
        <li>- [x] Unblock your webcam in your anti-virus and/or firewall
        </li>
      </ol>
    </li><br>
    <table>
      <thead>
        <tr>
          <th>Libraries</th>
          <th scope="col">Objective</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">pandas</th>
          <td>Easy-to-use data structures and data analisys tools</td>
        </tr>
        <tr>
          <th scope="row">numpy</th>
          <td>Algotithm for scientific and mathematical computing</td>
        </tr>
        <tr>
          <th>opencv-contrib-python</th>
          <td>Computer vision algorithm</td>
        </tr>
        <tr>
          <th>scikit-learn</th>
          <td>Algorithms for classification, regression, clustering, dimensionality, validations, prediction accuracy improvements, preprocessing, normalizations, etc</td>
        </tr>
        <tr>
          <th>scipy</th>
          <td>Scientific calculations with numpy</td>
        </tr>
        <tr>
          <th>keras</th>
          <td>Keras is an API designed for human beings, not machines.</td>
        </tr>
        <tr>
          <th>Pillow</th>
          <td>Libraries with algorithm to read, write, create, insert, convert, cut, resize images</td>
        </tr>
        <tr>
          <th>mtcnn</th>
          <td>Facial landmark localization algorithm</td>
        </tr>
        <tr>
          <th>tensorflow</th>
          <td>Intuitive higher-level APIs, and flexible model building on any platform </td>
        </tr>
      </tbody>
    </table>
  </ol>
</details>

<details>
  <summary><strong>5 SYSTEM INSTALLATION GUIDE</strong></summary>
  <ol>
    <li>First run <a href="#prereq">4 PRE-REQUISITS FOR THE SYSTEM TO WORK</a></li>
    <li>Download notebook <a href="files/facenet-keras-mtcnn-labelencoder.ipynb">facenet-keras-mtcnn-labelencoder.ipynb</a></li>
    <li>Download facenet_keras.part1, part2, part3 and part4.rar files. In these there is the facenet_keras.h5 trained model</li>
    <p><b>Note :</b> Check documentation <a href="files/readme.md">UNZIP THE CONTENT OF THE EXTENSION .rar - WINRAR</a>
    <li>Download dataset.rar file. There are several images to use for your training and tests</li>
  </ol>
  <p><b>Important :</b> I made the .py files available in case you want to tes with vscode, pycharm, spyder or others IDEs</p>
</details>

<details>
  <summary><strong>6 PROCEDURES FOR USING THE SYSTEM</strong></summary>
  <table>
    <thead>
      <tr>
        <ol>
          <li>Create a directory structure to store the files available in this repository. Following is a structure model as a guideline :
            <figure role="img" aria-labelledby="direc_struc">
              <pre>
              c:/temp/facenet/ : put here the content of the dataset.rar file. This file is in file folder
              c:/temp/facenet/ : put here the content of the facenet_keras.rar file. . This file is in file folder
              c:/temp/facenet/facerecognition : here the files will be creates in the model training routine
              </pre>
            </figure>
          </li>
          <li>Download facenet_keras.rar file and unzip it in the facenet directory</li>
          <li>Open the facenet-keras-mtcnn-labelencoder.ipynb notebook in the no jupyter and perform the following steps :
            <ol>
              <li>In the class RegisterImg : 
              replace variable content self.grv_img with the location where dataset.rar content were saved</li>
              <li>In the class FaceTrainer : replace content of the self.datasetpath variable with the location where dataset.rar content were saved</li>
              <li>In the class FaceTrainer : replace content of the self.faces_npz variable with the location where dataset.rar content were saved(*)</li>
              <li>In the class FaceTrainer : replace content of the self.keras_facenet variable with the location where .rar files were saved(**)</li>
              <li>In the class FaceTrainer : replace content of the self.faces_embeddings variable with the location where you have created facerecognition directory(*)
              </li>
              <li>In the class FaceTrainer : replace content of the self.svm_classifier variable with location where you have created facerecognition directory(*)</li>
              <li>In the class FaceDetector : replace content of the self.facenet_model variable with location where facenet_kerasX.rar were saved</li>
              <li>In the class FaceDetector : replace content of the self.svm_model variable with location where you have created facerecognition directory</li>
              <li>In the class FaceDetector : replace content of the self.data variable with location where you have created facerecognition directory</li>
            </ol><br>
            <p><b>Note : </b>(*) Keep the .npz extension;  (**) Keep the file name and extension; 
          </li>
          <li>Run the 5 lines of code</li>
          <li>The line whith the following codes will present a new line requesting some information
            <pre>
              if __name__ == "__main__":
                os.system('cls')
                menu = MainMenu()
                menu.menu_inicial()
            </pre>
          </li>
          <li>To save your image into data set, type 1 in the field followed by >> :<br>
            <img title="Options to system operate" src="img/06main_menu.png" alt="MainManu" width="521" height="206">
            <ol>
              <li>In the field 'Numero Matricula ->', enter the registration number<br>
                <img title="Register Number" src="img/07main_menu.png" alt="Register_Number" width="528" height="150">
              </li>
              <li>In the field 'Nome Completo -> ', enter the first cadidate name being filmed<br>
                <img title="Complete name" src="img/08main_menu.png" alt="Complete_Name" width="517" height="164">
              </li>
              <li>The system will connect to your webcam to film you. Your webcam light will turn on and one window with you image will be enable on your tasks bar<br>
                <img title="Webcam window" src="img/09webcamimg.png" alt="Image_Webcam" width="446" height="348">
              </li>
            </ol>
            <p><b>Note : </b> At the top of the webcam there is information to press Enter to record or press ESC to close/terminate</p>
            <p><b>Important : </b> Press Enter to exit, if you want to run on of the other tasks</p>
          </li>
          <li>To train the algorithm with a new image, type 2. The system will display an image similar to the following:<br>
            <img title="Train Algorithm" src="img/10trainalgor.png" alt="TrainAlgor" width="433" height="545">
            <p><b>Note : </b>The program<br>
              1. Will create faces_dataset_embeddings.npz and SVM_classifier.sav files into the facerecognition directory<br>
              2. Will create the faces_dataset.npz file into dataset directory<br>
              3. finalizara e retorna ao menu principal
            </p>
          </li>
          <li>To identify the person through the webcam type 3. The program will activate the webcam and will start the face recognition. It will display the follow similar window :<br>
            <img title="Webcam Window" src="img/11webcamimg.png" alt="Webcam_Window_Img" width="446" height="348">
          </li>
          <li>To finish the program, enter 0. A window similar to the following should appear:<br>
            <img title="Finish Program" src="img/15final.png" alt="FinishProgram" width="439" height="218">
          </li>
      </tr>
    </thead>
  </table>
</details>

<details>
  <summary><strong>7 SEARCHED SOURCES</strong></summary> 
  <ul>
    <li><a href="https://minerandodados.com.br/">Minerando Dados</a></li>
    <li><a href="https://opencv.org/">OpenCV Org</a></li>
    <li><a href="https://github.com/opencv/opencv/">OpenCV on github</a></li>
    <li><a href="https://www.partnershiponai.org/wp-content/uploads/2020/02/Understanding-Facial-Recognition-Paper_final.pdf">Partnershiponai.org</a></li>
    <li><a href="https://www.techradar.com/news/what-is-a-neural-network">Techradar</a></li>
    <li><a href="https://en.wikipedia.org/wiki/Artificial_neural_network">Wikpedia-Neural Network</a></li>
    <li><a href="https://scikit-learn.org/stable/">scikit-learn</a></li>
    <li><a href="https://scikit-learn.org/stable/_downloads/scikit-learn-docs.pdf">scikit-learn LabelEncoder</a></li>
    <li><a href="http://scipy.github.io/devdocs/hacking.html">scipy</a></li>
    <li><a href="https://keras.io/">keras</a></li>
    <li><a href="https://pillow.readthedocs.io/en/stable/">Pillow</a></li>
    <li><a href="https://pypi.org/project/mtcnn/">mtcnn</a></li>
    <li><a href="https://www.tensorflow.org/guide/tensor">tensorflow</a></li>
    <li><a href="https://pythonprogramming.net/linear-svc-example-scikit-learn-svm-python/r">SVC and svm</a></li>
    <li><a href="https://developers.google.com/machine-learning/crash-course/embeddings/video-lecture">Embedding</a></li>
  </ul>
</details>

<details>
  <summary><strong>8 GRATEFUL</strong></summary>
  <p>*To be gratful, to me, is the attitude that makes people better*</p>
  <p>I thank the most important woman in my life, my mother mrs Rosalita Borges Evangelista for having being a tireless fighter, fighting for me, for me, and with me and also with my brothers. My mother is the reason why I become an honorable human being.
  </p>
  <p>I thank to the my two brothers who helped me in the time I needed most.</p>
  <p>I thank to my wife and my two daughters for being my reason, emotion and inspiration and for supporting me at all moments.</p>
  <p>I thank to the creators of : computer, internet, computer programming languages, artificial intelligence and technologies in general</p>
  <p>I thank to Minerando Dados team for creating a Data Science do Zero space, providing several teachings in machine learning, statístics, deep learning and data science, to speed up my learning and for this propose challenge that I just concluded.</p><br><br>
  <p>Thank you all :wink:</p><br>
  <p>I wish you all great success !</p>
