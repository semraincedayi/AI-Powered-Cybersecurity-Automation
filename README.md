# 🤖 Yapay Zeka Tabanlı Siber Güvenlik Analizi

# 🤖 AI-Powered Cybersecurity Analysis

## 📘 Proje Hakkında / Project Overview

Bu tez projesi, ağa izinsiz giriş tespit sistemleri için kapsamlı bir veri seti kullanarak yapay zekâ tabanlı bir saldırı tespit analizi gerçekleştirmeyi amaçlamaktadır. UNSW-NB15 ve KDD veri setleri kullanılarak ağda kaydedilmiş trafikler analiz edilmiş ve saldırı ile normal trafik ayrıştırılmıştır. Yapay zekâ algoritmaları sayesinde, model sadece imza tabanlı veya anomali tabanlı sistemlerden daha üstün şekilde, eğitildiği veriler üzerinden saldırıları tanıyabilmiş ve doğruluk oranı değerlendirilmiştir.

Bu çalışma ileride otomasyon haline getirilebilir; kullanıcı CSV yükleyip modelin tahmin yapmasını sağlayacak bir pipeline tasarlanabilir.

This thesis project aims to perform an AI-powered attack detection analysis using comprehensive datasets for intrusion detection systems. UNSW-NB15 and KDD datasets were used to analyze network traffic and distinguish between attack and normal traffic. The AI algorithms allowed the model to detect attacks beyond the capability of signature-based or anomaly-based systems, and its accuracy was evaluated.

This work can be extended into an automation system in the future, where a user could upload a CSV file and the model would provide predictions through a processing pipeline.

## 🔍 Amaç / Objective

* Ağ trafiğinde anormal ve zararlı durumları tespit etmek

* Yapay zekâ algoritmaları ile saldırı ve normal trafik ayrımı yapmak

* Büyük veri setleri üzerinden eğitim yaparak modelin doğruluğunu değerlendirmek

* Detect abnormal and malicious activities in network traffic

* Classify attack and normal traffic using AI algorithms

* Train on large datasets and evaluate model accuracy

## 📊 Veri Seti / Dataset

Projede kullanılan veri setleri:

* **UNSW-NB15**: Ağ trafiği ve saldırıları içeren kapsamlı bir veri seti
* **KDD**: DARPA tarafından sağlanan saldırı verilerini içeren klasik veri seti

Veri dosyaları repoda şu şekilde yer almaktadır:

* `sayisallasan.csv` → Ham veri / Raw data
* `veriler_filtre.csv` → Ön işlenmiş ve filtrelenmiş veri / Preprocessed and filtered data

## 🧪 Yöntem / Methodology

* Yapay Sinir Ağları (YSA) ve diğer makine öğrenimi algoritmaları kullanılmıştır

* Veri ön işleme ve normalizasyon yapılmıştır

* Eğitim ve test veri setleri oluşturulmuş, model eğitilmiştir

* Modelin doğruluğu ve saldırı tespit başarısı değerlendirilmiştir

* Artificial Neural Networks (ANN) and other machine learning algorithms are employed

* Data preprocessing and normalization are applied

* Training and testing datasets are created and the model is trained

* Model accuracy and attack detection performance are evaluated

## 📈 Sonuçlar / Results

Geliştirilen yapay zekâ modeli, farklı saldırı türlerini başarılı şekilde tespit etmiş ve doğruluk oranı değerlendirilmiştir.

The developed AI model successfully detected different attack types and its accuracy was evaluated.

## 📂 Dosya Yapısı / File Structure

```
AI-Powered-Cybersecurity-Analysis/
│
├── sayisallasan.csv     # Ham veri / Raw dataset
├── veriler_filtre.csv    # Ön işlenmiş/filtrelenmiş veri / Preprocessed dataset
├── untitled0.py          # Modelleme ve analiz kodları / Modeling and analysis scripts
└── README.md             # Proje hakkında bilgi / Project information
```

## 🛠️ Kurulum / Installation

Projeyi çalıştırmak için gerekli Python kütüphanelerini manuel olarak yükleyebilirsiniz:

To run the project, manually install the required Python libraries:

```bash
pip install pandas numpy tensorflow scikit-learn matplotlib seaborn
```
