import pandas as pd

if __name__ == '__main__':
    people_information = pd.read_csv('./data/data.csv')
    people_information['Rank'] = people_information['Name'].rank(ascending=True)
    print(people_information)

