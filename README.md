# XJCO2121-Data-Mining

## Analysing Consumer Sentiment Across Smartphone Brands Using Data Mining and Text Analytics 

### Project Overview
This project applies data mining and text analytics techniques to analyse customer sentiment across different smartphone brands using Amazon product reviews. The work follows the CRISP-DM methodology and compares several classification models to explore how consumer emotions differ between brands.

> This repository supports the pilot study and proposal submission for the XJCO2121 Data Mining module (2024-2025).

### Objectives

- Automatically classify Amazon product reviews as positive or negative based on text and star ratings  
- Preprocess and vectorise user reviews using TF-IDF  
- Evaluate classification performance using Naive Bayes, SMO, and Random Forest in Weka  
- Provide visual insights such as word clouds and sentiment distributions  

### Repository Structure

```
XJCO2121-Data-Mining/
├── classidier output/
├── code/
│   ├── draw.py
│   ├── pre-proceed.py
│   ├── samples.py
│   ├── TF-DIF.py
│   └── transform,py
├── dataset/                     
│   ├── Amazon_10k_Sample.csv
│   └── full_10000_cleaned.csv
├── dataset_weka/
│   ├── full_10000_vectorized.arff          
│   └── full_10000_cleaned.arff
├── pictures/               
│   ├── full_10000_vectorized.arff          
│   └── full_10000_cleaned.arff
├── scripts/                 
│   ├── floechart.png
│   └── gannt.png
├── LICENSE
├── README.md
└── .git/
```

### Dataset
The raw dataset can be downloaded from [https://www.kaggle.com/datasets/PromptCloudHQ/amazon-reviews-unlocked-mobile-phones](https://www.kaggle.com/datasets/PromptCloudHQ/amazon-reviews-unlocked-mobile-phones)

### Tools Used
- **Python 3.9.19** (Pandas, NLTK, Scikit-learn)  
- **Weka 3.8.6** (Machine learning interface and evaluation)  
- **ChatGPT** (Drafting, linguistic summarisation)  
- **SketchEngine** (Corpus exploration)  
- **matplotlib/seaborn** (Visualisation)  
- **GitHub** (Version control and documentation)

### Workflow (CRISP-DM)

1. **Business Understanding**: Compare sentiment across smartphone brands
2. **Data Understanding**: Explore Amazon reviews 
3. **Data Preparation**: Clean, label, and convert text into TF-IDF vectors  
4. **Modelling**: Classify with Naive Bayes, SMO, RandomForest in Weka  
5. **Evaluation**: Analyse F1-score, interpret misclassifications, visualise sentiment  
6. **Deployment**: Archive final report, reproducible scripts, and model files

### Pilot Study Summary

- Dataset: 10,000 Amazon reviews randomly selected from a corpus of ~400,000  
- Labels: Based on star rating (4–5 = positive, 1–2 = negative, 3 = excluded)  
- Best model: Random Forest (F1-score ~0.89)  
- Outputs: Confusion matrices, word clouds, error analysis

### How to Reproduce

1. Clone this repo  
   ```bash
   git clone https://github.com/arsenal5239812/XJCO2121-Data-Mining.git
   cd XJCO2121-Data-Mining
2. Set up your Python environment
   ```bash
   pip install -r requirements.txt
3. Run preprocessing pipeline
   ```bash
   python samples.py
   python pre-proceed.py
   python TF-DIF.py
   python transform,py
4. Open ```.arff``` file in Weka for training and evaluation
5. Draw workflow chart
   ```bash
   python draw.py

### License
This repository is for academic purposes only under the XJCO2121 Data Mining module at the University of Leeds. The project is licensed under the [MIT License](./LICENSE). All dataset use complies with Kaggle’s open license.
