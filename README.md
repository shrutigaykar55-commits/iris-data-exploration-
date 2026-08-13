# Iris Data Exploration

## Data Science Internship Project

This project focuses on exploring and understanding the **Iris dataset** using Python. The main purpose of the project is to perform Exploratory Data Analysis (EDA), check the quality of the data, study the statistical properties of different features, and understand patterns through data visualization.

The project was completed as part of my **Data Science Internship** and helped me gain practical experience with the basic workflow of data exploration.

---

## Project Overview

The Iris dataset contains measurements of three different species of Iris flowers:

* Setosa
* Versicolor
* Virginica

The dataset includes four numerical features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

In this project, I explored the dataset using Python libraries and created different visualizations to understand the distribution and relationships between these features.

---

## Objectives

The main objectives of this project are:

* To understand the structure of the Iris dataset.
* To inspect the different features and data types.
* To check for missing values.
* To identify duplicate records.
* To perform basic statistical analysis.
* To understand feature distributions.
* To study relationships between different features.
* To create and interpret different visualizations.
* To summarize the important findings from the analysis.

---

## Dataset

The Iris dataset was loaded using **Scikit-learn**.

### Dataset Details

| Property                         | Details                       |
| -------------------------------- | ----------------------------- |
| Dataset                          | Iris Dataset                  |
| Original Records                 | 150                           |
| Features                         | 4                             |
| Target                           | Species                       |
| Species                          | Setosa, Versicolor, Virginica |
| Missing Values                   | 0                             |
| Duplicate Records Found          | 1                             |
| Records After Removing Duplicate | 149                           |

### Features

| Feature             | Description         |
| ------------------- | ------------------- |
| `sepal length (cm)` | Length of the sepal |
| `sepal width (cm)`  | Width of the sepal  |
| `petal length (cm)` | Length of the petal |
| `petal width (cm)`  | Width of the petal  |
| `species`           | Type of Iris flower |

---

## Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **Jupyter Notebook**
* **Visual Studio Code**

---

## Project Workflow

The project was completed through the following steps:

```text
Load Dataset
     ↓
Create DataFrame
     ↓
Explore Dataset
     ↓
Check Data Quality
     ↓
Statistical Analysis
     ↓
Data Visualization
     ↓
Identify Patterns
     ↓
Draw Conclusions
```

---

## Data Exploration

After loading the dataset, I performed an initial exploration to understand its structure.

The following operations were performed:

* Displayed the first five records.
* Displayed the last five records.
* Checked the shape of the dataset.
* Checked column names.
* Checked data types and non-null values.
* Generated a statistical summary.

The original dataset contained **150 rows and 5 columns**.

---

## Data Quality Check

### Missing Values

The dataset was checked for missing values.

**Result:** No missing values were found.

Therefore, no missing-value treatment was required.

### Duplicate Records

Duplicate records were also checked.

**Result:** One duplicate record was identified and removed before continuing with the analysis.

After removing the duplicate, the dataset contained **149 records**.

---

## Statistical Analysis

Descriptive statistics were used to understand the numerical features.

Some of the important values were:

| Feature      | Mean | Minimum | Maximum |
| ------------ | ---: | ------: | ------: |
| Sepal Length | 5.84 |     4.3 |     7.9 |
| Sepal Width  | 3.06 |     2.0 |     4.4 |
| Petal Length | 3.76 |     1.0 |     6.9 |
| Petal Width  | 1.20 |     0.1 |     2.5 |

This analysis helped in understanding the average values, range, and variation of the different flower measurements.

---

## Visualizations

Five visualizations were created as part of the project.

### 1. Histogram

The histogram was used to understand the distribution of the numerical features.

**Observation:**
The feature distributions are different, and the petal-related features show more noticeable separation between the flower groups.

### 2. Box Plot

The box plot was used to study the spread of the data and identify potential outliers.

**Observation:**
Some potential outlier values can be seen in Sepal Width, while the other features have relatively consistent distributions.

### 3. Scatter Plot

A scatter plot was created between **Sepal Length and Petal Length**.

**Observation:**
Setosa forms a clearly separated group, while Versicolor and Virginica have some overlapping values.

### 4. Pair Plot

The pair plot was used to compare relationships between all numerical features.

**Observation:**
Setosa is clearly separated from the other species across several feature combinations. Petal Length and Petal Width provide better separation between the species.

### 5. Correlation Heatmap

The correlation heatmap was used to understand relationships between numerical features.

**Observation:**
Petal Length and Petal Width show a strong positive correlation. Petal features also have a strong relationship with Sepal Length.

---

## Key Findings

The main findings from the analysis are:

* The Iris dataset originally contains 150 records.
* No missing values were found.
* One duplicate record was identified and removed.
* The three species are equally represented in the original dataset.
* Petal Length and Petal Width have a strong positive relationship.
* Setosa is clearly separated from the other two species in several visualizations.
* Versicolor and Virginica have some overlapping characteristics.
* Petal features appear to be more useful for distinguishing the species than the sepal features.

---

## Project Outputs

The visualizations generated during the analysis are stored in the `outputs` folder.

```text
outputs/
│
├── histogram.png
├── boxplot.png
├── scatterplot.png
├── pairplot.png
└── heatmap.png
```

The graphs were saved in high quality using **300 DPI**.

---

## Project Structure

```text
iris-data-exploration/
│
├── iris_exploration.py
├── iris_exploration.ipynb
├── README.md
├── requirements.txt
│
└── outputs/
    ├── histogram.png
    ├── boxplot.png
    ├── scatterplot.png
    ├── pairplot.png
    └── heatmap.png
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/iris-data-exploration.git
```

### 2. Open the Project Folder

```bash
cd iris-data-exploration
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Python File

```bash
python iris_exploration.py
```

### 5. Run the Jupyter Notebook

```bash
jupyter notebook
```

Then open:

```text
iris_exploration.ipynb
```

and run the cells.

---

## Learning Outcomes

Working on this project helped me improve my practical understanding of:

* Python for Data Science
* Pandas DataFrames
* Data inspection and cleaning
* Missing-value and duplicate checking
* Descriptive statistics
* Data visualization
* Correlation analysis
* Interpreting graphs
* Basic Exploratory Data Analysis

It also helped me understand why **EDA is an important step before moving toward further Data Science or Machine Learning tasks**.

---

## Future Scope

This project can be extended into a Machine Learning classification project.

Some possible next steps are:

* Splitting the dataset into training and testing data.
* Selecting useful features.
* Applying classification algorithms.
* Comparing different machine learning models.
* Evaluating model performance.
* Predicting the species of a new Iris flower.

These steps are not part of the current project, which is focused on **Data Exploration and EDA**.

---

## Conclusion

This project provided hands-on experience in exploring and understanding a real dataset using Python. I performed data inspection, checked the quality of the data, analyzed its statistical properties, and created different visualizations to identify patterns and relationships.

The analysis showed that the dataset had no missing values and that Petal Length and Petal Width have a strong relationship. The visualizations also showed a clear separation of Setosa from the other two species.

Overall, this project helped me build a stronger foundation in **Exploratory Data Analysis, data visualization, and Python-based data analysis** as part of my Data Science internship.

---

## Author

**Shruti Gaykar**

**Data Science Intern**

---

## Project Status

**Completed** ✅
