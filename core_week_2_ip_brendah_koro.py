# -*- coding: utf-8 -*-
"""Core_Week 2 IP_Brendah Koro

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AYuMvy0Nl1ssaMvsDj0lSTkFGmsMUqHP

# **Problem Statement**

Financial Inclusion remains one of the main obstacles to economic and human development in Africa. For example, across Kenya, Rwanda, Tanzania, and Uganda only 9.1 million adults (or 13.9% of the adult population) have access to or use a commercial bank account.

# **Analytic Question**

Which individuals are most likely to have or use a bank account

# **Metric for Success**

Household size with Bank accounts

##  Reading the Data
"""

# Commented out IPython magic to ensure Python compatibility.
#imprting libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# Loading the Data from the source 
# ---
# Dataset url = http://bit.ly/VariableDefinitions
#Dataset url= http://bit.ly/FinancialDataset
# ---
#
df= pd.read_csv("http://bit.ly/VariableDefinitions")
dg=pd.read_csv("http://bit.ly/FinancialDataset")

#preview columns
print(df)
print(dg)

#join datasets
core_df= pd.concat([df, dg], axis=1)
core_df.head()

"""##  Checking the Data"""

# Determining the no. of records in our dataset
#
core_df.shape

# Previewing the top of our dataset
#
core_df.head()

# Previewing the bottom of our dataset
# 
core_df.tail()

# Checking whether each column has an appropriate datatype
#
core_df.info()

"""## External Data Source Validation

# Data is valid. It matches https://zindi.africa/competitions/financial-inclusion-in-africa/data from Zindi Africa

**# DATA CLEANING**
"""

#drop unnecessary columns
core_df.drop(['uniqueid'],axis=1, inplace=True)

core_df.drop(['The relathip with head'],axis=1, inplace=True)

core_df.drop(['Variable Definitions'],axis=1, inplace=True)

core_df.drop(['Unnamed: 1'],axis=1, inplace=True)

core_df.head(2)

#rename columns
core_df.columns =['country',	'year',	'has_bank_account',	'location_type',	'cell_phone_access',	'household_size',	'respondent_age',	'gender_of_respondent',	'marital_status', 'education_level', 'job_type']

#check if columns were correctly renamed
core_df.head(2)

# Checking for Outliers
#household size
sns.boxplot(core_df['household_size'])

"""The dots represents outliers. Household_size contains outliers

"""

#checking for age outliers 
sns.boxplot(core_df['respondent_age'])

"""ages of respondents also have outliers"""

#checking for anomalies
#most columns contain 'nan' as anomalies which will be dropped

core_df.country.unique()

core_df.has_bank_account.unique()

core_df.location_type.unique()

core_df.gender_of_respondent.unique()

core_df.respondent_age.unique()

core_df.year.unique()

#dealing with year anomalies
#drop 2029,2056,2039

anomaly = core_df[core_df['year'] > 2018].index
core_df = core_df.drop(anomaly)
core_df['year'].unique()

# Identifying the Missing Data
#
core_df.isnull().sum()

"""The data contains missing values which will be dropped"""

# Dealing with the Missing Data
#drop missing values
core_df.dropna(inplace=True)

#check if missing values were dropped
core_df.isnull().sum()

"""zeros shows that missing values were actuually dropped"""

# check duplicates
#
core_df.duplicated().sum()

"""I chose to retain duplicates because they are significant in our study

# **`EXPLORATORY ANALYSIS`**

# `**(i) UNIVARIATE ANALYSIS**`

***Measures of central tendency***
"""

#household_size mean
core_df['household_size'].mean()

#respondent_age mean
core_df['respondent_age'].mean()

#county mode
core_df['country'].mode()

#year mode
core_df['year'].mode()

#has bank account mode
core_df['has_bank_account'].mode()

#location type mode
core_df['location_type'].mode()

#respondent age mode
core_df['respondent_age'].mode()

#gender of respondent mode
core_df['gender_of_respondent'].mode()

#marital status mode
core_df['marital_status'].mode()

#education level mode
core_df['education_level'].mode()

#job type mode
core_df.job_type.mode()

#median()
core_df.median()

"""***Measures of Dispesion***"""

#range of household size column
maxhousehold = core_df.household_size.max()
minhousehold = core_df.household_size.min()
range = maxhousehold - minhousehold
range

#range of Age column
maxage = core_df.respondent_age.max()
minage = core_df.respondent_age.min()
range = maxage - minage
range

#variance
core_df.var()

#standard deviation
core_df.std()

#sskewness
core_df.skew()

"""The data is slighly skewed positively which also portrays normal distribution"""

#kurtosis
core_df.kurt()

#histogram displaying the column Age

sns.distplot(core_df['respondent_age'], kde=True)
plt.title('Respondent_age Histogram',weight='bold',fontsize=14)
sns.set_context('talk')
sns.set_theme(palette='flag_r')

"""The distribution is right skewed but still portray normal distribution"""

#bar chart displaying the column household size
plt.bar(core_df['country'],core_df['household_size'])
plt.title('Household Size',fontsize=14, weight='bold')
plt.xlabel('Country')
plt.ylabel('Size')
sns.set_theme(context='paper', palette='flag_r')

#Boxplot displaying the column age
#The data is tightly grouped
#There are presence of outliers in the column that were retained since they proved useful

sns.boxplot(core_df['respondent_age'])
plt.title("Age BoxPlot", weight='bold', fontsize=14)
plt.show()

#Boxplot showing relationship between year and household sizes

sns.boxplot(core_df['year'],core_df['household_size'])
plt.title('Household size boxplot',weight='bold',fontsize=14)
#plt.xticks(rotation=45)
#plt.xticks(np.arange(min(year), max(year)+1, 1.0))
#plt.show()

#frequency table of the respondent age
core_df.respondent_age.value_counts()

#frequency table of  household size column
core_df.household_size.value_counts()

#frequency table of the year 
core_df.year.value_counts()

"""# **`(ii) BIVARIATE ANALYSIS`**

> Indented block


"""

#scatter plot 
#Age vs household size
plt.scatter(core_df['respondent_age'],core_df['household_size'],color='b')
plt.title('Age vs Households',weight='bold',fontsize=14)
plt.xlabel("Age")
plt.ylabel("Household size")

plt.show()

"""The distribution is inclined more to the young people as compared to the old people"""

#scatter plot showing relatinship between
#cell phone access and household size
plt.scatter(core_df['cell_phone_access'],core_df['household_size'],label='size',color='b')
plt.title('cell phones vs households')

"""a greater number of people living in households have no cell_phone access"""

#scatter
#bank account vs households
plt.scatter(core_df['has_bank_account'],core_df['household_size'], color='green')
plt.title('Households vs Bank accounts')

plt.show()

"""Fewer number of households have bank accounts compared to those who don't"""

#scatter
#job type vs households
plt.scatter(core_df['job_type'],core_df['household_size'], color='green')
plt.title('Job type vs household_size')
plt.xticks(rotation=90)

"""There are relatively fewer government dependent and those formally employed by the goverment compared to other job types in the households"""

#scatter
#education level vs households
plt.scatter(core_df['education_level'],core_df['household_size'], color='green')
plt.title('Education level vs household_size')
plt.xticks(rotation=90)

core_df['education_level'].unique()

#year vs household size
plt.scatter(core_df["year"],core_df["household_size"])
plt.title("Year vs household size")
plt.xlabel('year')
plt.ylabel("household_size")
#plt.xticks(np.arange(min(year), max(year)+1, 1.0))
plt.show()

"""There exists a decrease in household size from 2016 to 2017 , but the number showed a steady increase going on to 2018."""

#line chart showing relationship between
#cellphone acess & respondent age
#bank account & respondent age
plt.plot(core_df['cell_phone_access'],core_df['respondent_age'], color='r')
plt.plot(core_df['has_bank_account'],core_df['respondent_age'],color='black')

#correlation between age and household size variables
corr = core_df["respondent_age"].corr(core_df["household_size"],method = "pearson")
corr

"""low degree of corelation"""

#correlation between year and household size variables
corr = core_df["year"].corr(core_df["household_size"],method = "pearson")
corr

"""weak correlation"""

#line chart
#year vs respondent age
var = core_df.groupby('year').respondent_age.sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('Year')
ax1.set_ylabel('respondent_age')
ax1.set_title("Year vs respondent_age")
var.plot(kind='line')
#plt.xticks(np.arange(min(year), max(year)+1, 1.0))

"""# **`(iii) MULTIVARIATE ANALYSIS`**

# ***`(a) PRINCIPAL COMPONENT ANALYSIS (PCA)`***
"""

#Creating Dummy Variables-numerical variable for pca analysis
dummy = pd.get_dummies(core_df)
dummy.head()

pd.get_dummies(core_df)

dummy.shape

#Preprocessing
#Dividing my features into the feature set and corresponding labels: X and Y respectively.
x = core_df.drop("has_bank_account",1)
y = core_df["has_bank_account"]
x.head()

x.shape

y.shape

#creating dummy for the categorical data
x = pd.get_dummies(x)
x.head(2)

#splitting the data into training and test sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y)
x_train, x_test, y_train, y_test

#Perform Feature Scaling#standardisation
#As you can see in the dataset, all values are not in the same range. And that requires a lot of time for calculation. So to overcome this problem, we perform feature scaling.

#Feature scaling help us to normalize the data within a particular range.
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
x_test
x_train

#Principal Component Analysis
from sklearn.decomposition import PCA
pca = PCA()
x_train = pca.fit_transform(x_train)
x_test = pca.transform(x_test)
x_train
x_test

#Explained Variance Ratio
#returns the variance caused by each of the principal components.
explained_variance = pca.explained_variance_ratio_
explained_variance

#Apply PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
x_train = pca.fit_transform(x_train)
x_test = pca.transform(x_test)

#training and making prediction
#we use random forest
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(x_train,y_train)

#Predict the Test Set Results
y_pred = rfc.predict(x_test)
y_pred

#Make the Confusion Matrix
#to explain predicted values
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test,y_pred)*100

"""It has an accuracy of 84.63%

# ***`(b) FACTOR ANALYSIS`***
"""

core_df.head()

#get dummy data
dummy = pd.get_dummies(core_df)

dummy.info()

#perform adequacy test
#Use Bartlett’s test
# Bartlett’s test of sphericity checks whether or not the observed variables intercorrelate at all 
# Installing factor analyzer 
!pip install factor_analyzer==0.2.3

from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity

chi_square_value,p_value=calculate_bartlett_sphericity(dummy)
chi_square_value, p_value

# 
from factor_analyzer.factor_analyzer import calculate_kmo

kmo_all,kmo_model=calculate_kmo(dummy)

#choose numbe of factors
from factor_analyzer.factor_analyzer import FactorAnalyzer

# Creating factor analysis object and perform factor analysis
fa = FactorAnalyzer()
fa.analyze(dummy, 36, rotation=None)

# Checking the Eigenvalues
ev, v = fa.get_eigenvalues()
ev

"""#  31-factors eigenvalues are greater than one. 
# so we are choosing 31 factors (or unobserved variables).
"""

#Performing Factor Analysis
# Creating factor analysis object and perform factor analysis
#
fa = FactorAnalyzer()
fa.analyze(dummy, 31, rotation="varimax")
fa.loadings

#Performing factor analysis for 31 factors
# 
# Create factor analysis object and perform factor analysis using 5 factors
fa = FactorAnalyzer()
fa.analyze(dummy, 31, rotation="varimax")
fa.loadings

#  Getting variance of each factors
# 
fa.get_factor_variance()

# 96% cumulative Variance explained by the 31factors.

"""# ***(c) DISCRIMINANT ANALYSIS***"""

core_df.head()

#divide dataset
X = core_df.iloc[:, 0:6].values
y = core_df.iloc[:, 7:10].values

#divide dataset into labels and features
X = core_df.iloc[:, 0:7].values
from sklearn.preprocessing import normalize
X = core_df.iloc[:, 0:6].values
y = core_df.iloc[:, 7:10].values
X

# divides data into training and test sets
#
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Step 5: Feature scaling
# We now need to perform feature scaling. We execute the following code to do so:
# 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#performing LDA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda = LDA(n_components=1)
X_train = lda.fit_transform(X_train, y_train)
X_test = lda.transform(X_test)

#training and making predictions
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(max_depth=2, random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

#evaluating performance

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

cm = confusion_matrix(y_test, y_pred)
print(cm)
#print('Accuracy' + str(accuracy_score(y_test, y_pred)))

"""## Implementing the Solution

1. A big percentage of households had different job occupations other than government dependent and government formal employments

2. A big percentage of the surveyed households have acquired education less than tertiary education level

 These accounts for high number of households without bank accounts.
 Maybe big percentage of the informally employed households have not opened bank accoun

##  Challenging the solution

Knowing exactly occupation and education level of housseholds with bank accounts will be more insightful.

Other factors such as households' income are important

## Follow up questions

The research question was right. The data for this research had insufficient information. More information is required to trickle down the research question
"""



"""# **`LDA-MOST USED WITH SUPERVISED DATA`**

---


"""

# Separating our target label (has bank account) from the other features
feat= core_df.drop(['Has a Bank account','country','year', 'uniqueid'])
bank_label = core_df['Has a Bank account']

# Subject our features to LDA model

# Import Linear Discriminant Analysis method from sklearn library
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# Create an instance of LDA
lda = LDA()

lda_= lda.fit(feat, bank_label)
lda_feat = lda_.transform(feat)

# Display the coeficients of the reducted columns
lda_.coef_

# Since the coefficients are in an array, we needto create a dataframe so that we can extract the name of the columns
f_imp = pd.DataFrame(index=feat.columns.values, data=lda_.coef_[0].T)
f_imp.sort_values(0, ascending=False)





from sklearn.preprocessing import LabelEncoder
en = LabelEncoder()

core_df['Level of Education'] = en.fit_transform(core_df['Level of Education'])
core_df['Type of Job'] = en.fit_transform(core_df['Type of Job'])
core_df['The relationship with head'] = en.fit_transform(core_df['The relationship with head'])
core_df['Cell Phone Access'] = en.fit_transform(core_df['Cell Phone Access'])
etc
11:21
:computer: Correlation Matrix:
# Create a correlation matrix
corrMatrix = data.corr()
corrMatrix

# Vizualise the correlation matrix using a heat map

fig, ax = plt.subplots(figsize=(10,10)) 
sns.heatmap(corrMatrix, annot=True,  linewidths=.5, ax=ax)