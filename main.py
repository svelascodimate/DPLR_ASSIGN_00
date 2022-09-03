import pandas as pd

if __name__ == '__main__':
    people_information = pd.read_csv('./data/data.csv')
    names_asc = people_information.sort_values(by=['Name'])['Name']
    print(names_asc)

