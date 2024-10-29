# TEXT BASED ML MODEL CLASSIFYING SENTIMENT BEHIND TWEETS  -
  * This model helps in identifying how a certain text is being perceived by people
  * the model has the capacity to analyse large number of tokens with good accuracy
## Table of Contents -
  * Installation
  * Data Definition
  * Data Preprocessing
  * Model Training and evaluation
  * Conclusion

*1.INSTALLATION AND SETUP* -
  * clone the repository <sentiment>
  * install python,nktk and pandas in the runnning system
  * install extra modules from reqirements.txt
  
*2.Data Definition* -
  * The dataset has 1.6 million data points and 7 columns
  * Target column 'labels' is balanced 
  * [Dataset link](https://www.kaggle.com/datasets/kazanova/sentiment140)

*3.Data Preprocessing -*
  * Dute to very large preprocessing time, the size of the chunk was reduced to 32k data points 
  * No Null values present in the data
  * The insignificant nummber of duplicate values were dropped because of the huge size of dataset
  * 2 columns : 'labels' and 'text_data' are important features
  * labels feature is our target column and is binary in nature
  * For understanding sentiment behind texts stemming is performed because it is fast and donot change the inherent meaning behind texts
  * TF-IDF vectorizer is used for feature extraction and encoding textual data
    
*4.Model Training -*
  * LOGISTIC REGRESSION model is used for this binary classification problem
  * performed GrdSearch Cross Validatio nto rule out any overfitting problem
    
*5.Model Evaluation -*
* Acheived an accuracy score of 78 percent
* Precision and Recall were very narrow reducing the chances of false classification

*6.Conclusionv -*
* Although Binary classification is applied,but with the presence of multiple classes complex algorithms like RandomForestClassifier or SVM can be used for better performance
