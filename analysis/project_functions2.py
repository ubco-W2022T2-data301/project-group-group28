def load_and_process(path):
    import pandas as pd
    df = pd.read_csv(path).drop(["Forest area", "Individuals using the Internet", "People practicing open defecation", "Electric power consumption", "Year", "GDP per capita", "Military expenditure", "Beer consumption per capita"], axis = 1).rename(columns = {"CO2 emissions": "CO2"})
    return df