import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

os.makedirs("outputs", exist_ok=True)

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["species"] = iris.target

df["species"] = df["species"].replace({
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
})

print("=" * 60)
print("IRIS DATASET")
print("=" * 60)

print("\nFirst Five Records")
print(df.head())

print("\nLast Five Records")
print(df.tail())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDataset Information")
df.info()

print("\nStatistical Summary")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

duplicates = df.duplicated().sum()

print("\nDuplicate Records:", duplicates)

if duplicates > 0:
    df.drop_duplicates(inplace=True)
    print("Duplicate records removed.")
    print("New Shape:", df.shape)

print("\nSpecies Distribution")
print(df["species"].value_counts())

df.drop("species", axis=1).hist(
    figsize=(10, 8),
    bins=15,
    edgecolor="black"
)

plt.suptitle(
    "Distribution of Iris Flower Features",
    fontsize=16,
    fontweight="bold"
)

plt.savefig(
    "outputs/histogram.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nObservation (Histogram)")
print("- Features are well distributed.")
print("- Petal measurements show clear separation.")
print("- No abnormal distribution is observed.")

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df.drop("species", axis=1)
)

plt.title(
    "Box Plot of Iris Dataset Features",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Features", fontsize=12)
plt.ylabel("Measurement (cm)", fontsize=12)

plt.xticks(rotation=20)

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.savefig(
    "outputs/boxplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nObservation (Box Plot)")
print("- Sepal Width contains a few outliers.")
print("- Petal features have fewer outliers.")
print("- Overall data spread is consistent.")

plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x="sepal length (cm)",
    y="petal length (cm)",
    hue="species",
    s=90
)

plt.title(
    "Sepal Length vs Petal Length",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")

plt.grid(True, linestyle="--", alpha=0.4)

plt.legend(title="Species")

plt.savefig(
    "outputs/scatterplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nObservation (Scatter Plot)")
print("- Setosa is clearly separated.")
print("- Versicolor and Virginica overlap slightly.")
print("- Petal Length increases with Sepal Length.")

pair = sns.pairplot(
    df,
    hue="species",
    diag_kind="hist"
)

pair.fig.suptitle(
    "Pairwise Relationship of Iris Features",
    fontsize=16,
    fontweight="bold",
    y=1.02
)

pair.savefig(
    "outputs/pairplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nObservation (Pair Plot)")
print("- Setosa forms a distinct cluster.")
print("- Petal features separate species more clearly.")
print("- Versicolor and Virginica show slight overlap.")

plt.figure(figsize=(8, 6))

sns.heatmap(
    df.drop("species", axis=1).corr(),
    annot=True,
    cmap="coolwarm",
    linewidths=0.5,
    square=True
)

plt.title(
    "Correlation Heatmap of Iris Dataset",
    fontsize=16,
    fontweight="bold"
)

plt.savefig(
    "outputs/heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nObservation (Heatmap)")
print("- Petal Length and Petal Width have a strong positive correlation.")
print("- Sepal Width has a weak negative correlation with Petal Length.")
print("- Petal features are more useful for classification.")

print("\n" + "=" * 60)
print("FINAL CONCLUSION")
print("=" * 60)

print("""
1. The Iris dataset originally contained 150 records.
2. No missing values were found.
3. One duplicate record was detected and removed.
4. The dataset contains three Iris species:
   - Setosa
   - Versicolor
   - Virginica
5. Petal Length and Petal Width are highly correlated.
6. Setosa is clearly distinguishable from the other species.
7. Versicolor and Virginica overlap slightly.
8. The dataset is clean and suitable for machine learning classification tasks.
""")

print("=" * 60)
print("EDA Completed Successfully!")
print("Graphs have been saved in the 'outputs' folder.")
print("=" * 60)