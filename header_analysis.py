import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

dataset_path = 'C:/Users/juika/OneDrive/Desktop/cyberdosti/spam_ham_dataset.csv'
df = pd.read_csv(dataset_path)

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_vectorized, y_train)

y_pred = model.predict(X_test_vectorized)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

for i in range(len(X_test)):
    print("Email:", X_test.iloc[i])
    print("given Label:", y_test.iloc[i])
    print("label after prediction:", y_pred[i])
    if y_test.iloc[i] == y_pred[i]:
        print("This is spam email")
    else:
        print("This is not a spam email")
    print("\n")

