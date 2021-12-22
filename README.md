# ProjectNLP

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/RobbyAkbar/JobFlex">
    <img src="movie_search.png" alt="Logo" height="80">
  </a>

  <h2 align="center">Movie Searching Platform</h2>

  <p align="center">
    Project UAS NLP - PSTI - 2018
    <br />
    <a href="https://colab.research.google.com/drive/1p1Zpx1bHn_iB5ai0uxlq5R7mcq4a0xNI"><strong>Explore the Notebook »</strong></a>
    <br />
    <br />
  </p>
</p>

<h4>Team Members</h4>
<ul>
  <li>Asry Yuniarti - 1804975</li>
  <li>Robby Akbar - 1805386</li>
</ul>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#background">Background</a></li>
    <li><a href="#objective">Objective</a></li>
    <li><a href="#projectstructure">Project Structure</a></li>
    <li><a href="#metrics">Metrics</a></li>
    <li><a href="#evaluation">Evaluation</a></li>
    <li><a href="#howtorunmovierecommend">How to Run Movie Recommendation</a></li>
  </ol>
</details>

## Background
Berbagai macam teknologi saat ini telah dimanfaatkan oleh manusia dalam kehidupan sehari-hari. Film adalah salah satu media hiburan maupun sarana dalam menyampaikan informasi yang merupakan gabungan antara perkembangan teknologi audio dan visual. Setiap tahun jumlah yang tersebar semakin banyak dan terus meningkat. Pada halaman web The Movie
Database (TMDb) terdapat 14.971 judul film yang telah diproduksi oleh industri perfilman dari tahun 1900 hingga tahun 2019. Dalam menonton sebuah film setiap orang memiliki ketertarikan atau kecenderungan terhadap film yang berbeda-beda. Sinopsis merupakan salah satu cara yang membantu kita dalam memahami alur cerita dari sebuah film, sedangkan genre membantu kita dalam mengetahui apakah film itu sesuai dengan genre yang kita sukai atau tidak.
Banyaknya data film yang tersedia pada sosial media, akan membutuhkan waktu yang lama untuk mencari film yang memiliki sinopsis dan genre yang serupa atau sama secara manual. Rekomendasi merupakan alat penyaringan informasi dari jejaring sosial yang dapat digunakan untuk mengatasi data yang berlebih (Roy dan Kundu, 2013). 

## Objective
1. Sistem dapat merekomendasikan film yang serupa berdasarkan judul film yang diberikan.

## Project Structure
1. Colab
Dalam folder ini berisi data preparation dalam format ipynb yang telah diolah sesuai dengan kebutuhan (cleaning data, cleaning fitur, filter data)
2. Data
Foldr data berisi link dataset yang digunakan dalam project ini
3. Model berisi data yang telah diolah dan siap untuk digunakan 
4. Output terdiri dari dua folder yaitu :
a. Folder data berisi dataset, data training, data test, val data dalam format csv yang akan digunakan dalam proses ...
b. img yang berisi gambar dari hasil visualisasi data
4. Params
5. Src yang berisi file main.py untuk menjalankan sistem rekomendasi film


## Metrics
1. TF-IDF
2. F1-score
3. 

## How to Run Movie Recommendation
Buka folder src > file main.py > run
