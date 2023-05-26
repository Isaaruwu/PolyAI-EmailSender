from data_utils import transform_data

if __name__ == "__main__":
    df = transform_data('./data/list_sponsorship.csv', [1, 2, 3, 4, 7, 8, 9, 10])
    print(df)
