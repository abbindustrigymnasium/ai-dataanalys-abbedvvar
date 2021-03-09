import numpy as np
from sklearn import preprocessing, neighbors, model_selection
import pandas as pd

df = pd.read_csv('votering.csv')
print(list(df))

df.drop(['punkt'], 1, inplace=True)

df = df[['rost', 'parti', 'fodd', 'kon', 'intressent_id']]


input_labels = ['kvinna', 'man']  # kvinna ----> 0; man ----> 1
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)
df['kon'] = encoder.transform(df['kon'])


input_labels = ['C', 'KD', 'SD', 'V', 'M', 'MP',
                'L', 'S', '-']  # - => 0 C => 1 KD => 2 L => 3 M => 4 MP => 5 S => 6 SD => 7 V => 8
encoder.fit(input_labels)
df['parti'] = encoder.transform(df['parti'])

input_labels = ['Nej', 'Ja', 'Frånvarande',
                'Avstår']  # Avstår ----> 0 Frånvarande => 1 Ja => 2 Nej => 3
encoder.fit(input_labels)
df['rost'] = encoder.transform(df['rost'])

for i, item in enumerate(encoder.classes_):
    print(item, '---->', i)

df.replace('?', '-9999', inplace=True)
print(df.head(3))


X = np.array(df.drop(['rost'], 1))
Y = np.array(df['rost'])

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(
    X, Y, test_size=0.2)
X_train = X_train.reshape(len(X_train), -1)
Y_train = Y_train.reshape(len(Y_train), -1)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, Y_train)
accuracy = clf.score(X_test, Y_test)
print('accuracy',  accuracy)

# ""Matheus Enholm","202577142527","SD","Västra Götalands läns norra","Ja","sakfrågan","230","man","1979","2019-11-28""
# Daniel Bäckström","665485817222","C","Värmlands län","Ja","sakfrågan","46","man","1975","2019-11-28

example_measure = np.array(
    [[7, 1979, 1, 202577142527], [1, 1975, 1, 665485817222]])
example_measure = example_measure.reshape(len(example_measure), -1)
prediction = clf.predict(example_measure)
print(prediction)
decoded_list = encoder.inverse_transform(prediction)
print('Decoded', list(decoded_list))
