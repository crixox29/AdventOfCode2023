import pandas as pd
import re

# Input Data
file_path="input.txt"
#Split Data in Lines and Procces each line:
data = []
with open(file_path,'r') as file:
    for line in file:
        game_id = int(re.search(r'Game (\d+):', line).group(1))
        parts = line.split(":")[1].split(";")
        print(parts)
        for part in parts:
            cubes = map(str.strip, re.findall(r'(\d+ \w+)', part))
            for cube in cubes:
                number, color = cube.split()
                data.append({'Game ID': game_id, 'Color': color, 'Number': int(number)})

# Crear DataFrame
df = pd.DataFrame(data)
print(df)
# Establecer límites para cada color
limits = {'red': 12, 'green': 13, 'blue': 14}

# Verificar cada juego
possible_games = []
for game_id in df['Game ID'].unique():
    game_df = df[df['Game ID'] == game_id]
    if all(game_df[game_df['Color'] == color]['Number'].max() <= limit for color, limit in limits.items()):
        possible_games.append(game_id)

# Sumar los ID de juegos posibles
total_sum = sum(possible_games)

print("Suma de los ID de juegos posibles:", total_sum)
