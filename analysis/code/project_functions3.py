def load_and_process(file_path):

    # Method Chain 1 (Load data and remove unused columns)

    df1 = (
          pd.read_csv(file_path, sep=';')
          .drop(['Continent', 'Least Developed', 'Population', 'People practicing open defecation', 
                 'People using at least basic drinking water services', 'Obesity among adults', 
                 'Beer consumption per capita'], axis=1)
          .dropna()
      )

    # Method Chain 2 (Create new column expenditure_type)

    df2 = (
          df1
          .assign(expenditure_type=lambda x: np.where(x['Health expenditure'] > x['Military expenditure'], 'H', 'M'))
      )

    return df2
