# News Category Classification 

This project focuses on classifying news articles into various predefined categories using Natural Language Processing (NLP) and Machine Learning (ML) techniques. The main objective is to create a model that accurately categorizes articles into topics like **Politics**, **Economics**, **Sports**, **Technology**, **Social**, **Cultural**, and **Miscellaneous**.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Training Process](#training-process)
- [Evaluation](#evaluation)
- [Results](#results)
- [Future Improvements](#future-improvements)
- [User Interface](#user-interface)

## Overview
This project leverages NLP techniques to preprocess and classify news articles. The model is designed to efficiently handle large volumes of textual data, performing one category per article. The key steps involve text preprocessing, feature extraction, and model training using various ML algorithms:

<p align="center">
  <img alt="Road Map" src="https://github.com/user-attachments/assets/ce6fce27-3a0d-4b30-8707-1fa81fd1cd18" width="600">
</p>

## Dataset
The dataset includes thousands of news articles labeled under seven different categories:
```
Politics, Economics, Sports, Technology, Social, Cultural, and Miscellaneous.
```
 These categories were selected to cover a wide range of topics of general interest. 

### Preprocessing
- **Text Preprocessing**: Tokenization, stopword removal, and punctuation cleaning were performed using Python's NLP libraries.
- **Feature Extraction**: The **TF-IDF** method was used to convert text into numerical features. We considered different n-gram ranges for feature extraction and experimented with the number of features to optimize model performance.

## Model Architecture
The classification model is built using a neural network with the following architecture:
1. **Input Layer**: Accepts the TF-IDF feature vectors.
2. **Dense Layer 1**: Contains 32 units with ReLU activation.
3. **Dense Layer 2**: Contains 32 units with ReLU activation.
4. **Output Layer**: For mono-label classification, the output layer has 9 units (one for each category) with a softmax activation function.

<p align="center">
  <img alt="Model" src="https://github.com/user-attachments/assets/0a43cf8c-a1f7-44b7-8d59-e59e890c1454" width="600">
</p>

### Loss and Optimizer
- **Loss Function**: Categorical Crossentropy.
- **Optimizer**: Adam optimizer was used to minimize the loss function.

## Training Process
The model was trained on a split dataset:
- **Training Data**: 80% of the dataset.
- **Validation Data**: 20% of the dataset.
- **Batch Size**: 32
- **Epochs**: 10

The training process involved backpropagation to minimize loss and improve accuracy.


<p align="center">
  <img alt="Accuracy" src="https://github.com/user-attachments/assets/f5fbc24c-4fd4-4acf-a502-374ed1bfd901" width="407">
  <img alt="Loss" src="https://github.com/user-attachments/assets/df584bbf-82f8-4c3e-9cb7-762a27eac6f0" width="400">
</p>

## Evaluation
Evaluation metrics such as **accuracy**, **precision**, **recall**, and **F1-score** were used to assess the performance of the model. In addition, **Confusion Matrix** was used to analyze misclassification.

<p align="center">
  <img alt="Confusion" src="https://github.com/user-attachments/assets/39abcc81-bf86-4246-83f8-145ee930aa55" width="600">
</p>

## Results
- **Training Accuracy**: 98%
- **Test Accuracy**: 83%
- **Training Loss**: 0.1
- **Test Loss**: 0.8

## Future Improvements

1. **Hyperparameter Tuning**: Experiment with different learning rates, batch sizes, and optimizer algorithms.
2. **Data Augmentation**: Increase dataset size by scraping more news articles to improve generalization.
3. **Advanced NLP Techniques**: Implement models like BERT or GPT for improved classification accuracy.

## User Interface

A web-based user interface was created using **React** on the front end and **Django (FastAPI)** on the back end. This interface allows users to:
- Upload new articles for classification.
- View classification results instantly on the dashboard.
- Analyze model performance through real-time visualizations and feedback.

<p align="center">
  <img alt="Confusion" src="https://github.com/user-attachments/assets/ae2828d6-2f87-4139-919a-011041982050" width="400">
  <img alt="Confusion" src="https://github.com/user-attachments/assets/d555509c-e750-46f9-8198-aa132e0f7e01" width="410">
</p>

## License 
This project is under the MIT License, and I’d be thrilled if you use and improve my work!


