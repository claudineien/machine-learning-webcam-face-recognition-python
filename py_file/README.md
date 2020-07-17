<h2 align="center"><strong><a id="lang-ptbr">Machine Learning no reconhecimento facial através da webcam</a></strong></h2>
<h5 align="left">Público alvo: Estudante de Machine Learning &#x1F393; - Objetivo: Demonstrar Machine Learning - Tempo leitura: 00:02:30 mins - Idioma : <a href="#lang-en">[EN]</a>󠁧󠁢󠁥󠁮󠁧󠁿</h5>
<details open class="sbdocs sbdocs-details">
  <summary class="sbdocs sbdocs-summary"><strong>1 SOBRE OS ARQUIVOS</strong></summary>
  <ol>
    <li><strong>menu.py</strong>
      <p>Este arquivo exibirá 4 opçoes que podem ser executadas pelo programa, sendo : </p>
      <p>1 Gravar Imagem : chamará a arquivo register.py</p>
      <p>2 Analisar Imagem : chamará o arquivo analyzer.py</p>
      <p>3 Identificar Imagem : chamará o arquivo identifier.py</p>
      <p>0 Sair Do Sistema : finalizará o programa</p>
    </li>
    <li><strong>register.py</strong>
      <p>Este arquivo ativará sua webcam e permitirá gravar sua imagem ao pressionar Enter ou fechar a janela ao pressionar Esc.</p>
      <p>Esta versão permite gravar apenas uma imagem a cada acesso. Para gravar outra imagem é necessário teclar Esc e digitar a opção 1 novamente.</p>
    </li>
    <li><strong>analyzer.py</strong>
      <p>Este arquivo contém os algorítimos para :</p>
      <p>1 calcular o standardization</p>
      <p>2 applicar o embedding na imagem</p>
      <p>3 executar o predict do conjunto de algoritmos treinado facenet_keras.h5 do keras</p>
      <p>4 aplicar Normalizer l2</p>
      <p>5 aplicar LabelEncoder</p>
      <p>6 treinar o modelo svm-SVC</p>
      <p>7 calcular e exibir a acurácia das imagens de treino e das imagens de teste</p>
    </li>
    <li><strong>identifier.py</strong>
      <p>É um algoritmo computacional que aprende com novos dados inseridos, simulando o cérebro humano.</p>
      <p>Exemplo: Programar um computador para aprender todos os detalhes de forma e formato de um determinado rosto, ao inserimos outros rostos ele automaticamente armazenara as suas formas e formatos e a partir dai conseguiremos extrair a quem pertence determinado rosto</p>
    </li>
  </ol>
</details><br>

<h2 align="center"><strong><a id="lang-en">Machine Learning on facial recognition by webcam</a></strong></h2>
<h5 align="left">Público alvo: Estudante de Machine Learning &#x1F393; - Objetivo: Demonstrar Machine Learning - Tempo leitura: 00:02:30 mins - Idioma : <a href="#lang-ptbr">[Pt-Br]</a>󠁧󠁢󠁥󠁮󠁧󠁿</h5>
<details open class="sbdocs sbdocs-details">
  <summary class="sbdocs sbdocs-summary"><strong>1 SOBRE OS ARQUIVOS</strong></summary>
  <ol>
    <li><strong>Reconhecimento Facial</strong>
      <p>É a técnica de capturar/pegar em uma imagem a parte frontal do rosto/face que envolve parte da cabeça, testa, olhos, nariz, maças do rosto, bochechas, boca, maxilar, queixo, analisar a distância entre cada uma destas partes, comparar com outras imagens, identificar diferenças, comparar similaridades e exibir o alvo desejado.</p>
      <p>A imagem considerada pode ser uma foto, vídeo ou câmera.</p>
      <p>O alvo desejado é o ser humano que será identificado.</p>
    </li>
    <li><strong>Machine Learning</strong>
      <p><b>Machine Learning é o objeto de estudo</b> neste projeto. É a técnica computacional de ensinar uma máquina com determinado poder computacional a analisar um conjunto de dados e predizer informações para auxiliar nas decisões.</p>
      <p>Esta técnica pode ser utilizada para tentar resolver qualquer tarefa -da mais simples a mais complexa.</p>
    </li>
    <li><strong>Deep Learning</strong>
      <p>É a técnica computacional que analisa muito detalhadamente determinadas características de imagem para auxiliar a identificar quem a imagem pertence.</p>
    </li>
    <li><strong>Neural Network</strong>
      <p>É um algoritmo computacional que aprende com novos dados inseridos, simulando o cérebro humano.</p>
      <p>Exemplo: Programar um computador para aprender todos os detalhes de forma e formato de um determinado rosto, ao inserimos outros rostos ele automaticamente armazenara as suas formas e formatos e a partir dai conseguiremos extrair a quem pertence determinado rosto</p>
    </li>
  </ol>
</details>
