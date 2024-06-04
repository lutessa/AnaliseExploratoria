import pandas as pd

file_path = 'AnaliseExploratoria\Delnorte.csv'  
df = pd.read_csv(file_path)

votes_by_candidate = df.groupby('candidate')['votes'].sum().reset_index()


print(votes_by_candidate)
 