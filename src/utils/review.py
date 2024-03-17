import pandas as pd


def generate_review(data):
    df = pd.read_csv(f"src/data/{data}")
    vocabulary = df.iloc[:, 0:3].values
    mean_list = df.iloc[:, 2].values.tolist()
    vocabulary_list = []
    for i in range(len(df)):
        vocabulary_list.append(' '.join(str(i)
                                        for i in vocabulary[i][0:3]))

    return vocabulary_list, mean_list
