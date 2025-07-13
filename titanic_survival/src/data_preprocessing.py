import pandas as pd
import os

# Load data
train_df = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\parth\Machine learning and deep learning project\\titanic_surival\\DATA\\train.csv')
test_df = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\parth\\Machine learning and deep learning project\\titanic_surival\\DATA\\test.csv')

def preprocess(df):
    df = df.copy()
    
    # Drop columns that are not useful.these are identifiers are not useful for prediction
    df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True, errors='ignore')
    
    # Fill missing Age with median
    df['Age'].fillna(df['Age'].median(), inplace=True)
    
    # Fill missing Fare with median (only needed for test.csv)
    if 'Fare' in df.columns:
        df['Fare'].fillna(df['Fare'].median(), inplace=True)
    
    # Fill missing Embarked with mode
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    
    # Encode 'Sex': male = 1, female = 0
    df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})
    
    # Encode 'Embarked': C = 0, Q = 1, S = 2
    embarked_map = {'C': 0, 'Q': 1, 'S': 2}
    df['Embarked'] = df['Embarked'].map(embarked_map)
    
    return df

# Separate features and target


y = train_df['Survived']
X = preprocess(train_df.drop('Survived', axis=1))
print(f" Number of X Missing Value\n{X.isnull().sum()}\n")
print(f" Number of y Missing Value\n{y.isnull().sum()}")
os.makedirs('../data', exist_ok=True)

# Now save

print(f"Clean X Data {X.to_csv('C:\\Users\\parth\\OneDrive\\Desktop\\parth\\Machine learning and deep learning project\\titanic_surival\\data\\X_data.csv', index=False)}")
print(f"Clean y Data {y.to_csv('C:\\Users\\parth\\OneDrive\\Desktop\\parth\\Machine learning and deep learning project\\titanic_surival\\data\\y_data.csv', index=False)}")

