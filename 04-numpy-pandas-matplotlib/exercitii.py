import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Afisare totala (ex 1)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv('data.csv')
# --- CURĂȚARE DATE (Adaugă asta sus, după citirea CSV-ului) ---
def clean_currency(value):
    if isinstance(value, str):
        value = value.replace('€', '')
        if 'M' in value:
            return float(value.replace('M', '')) * 1000000
        elif 'K' in value:
            return float(value.replace('K', '')) * 1000
        return float(value)
    return value
df['Value'] = df['Value'].apply(clean_currency)
df['Wage'] = df['Wage'].apply(clean_currency)
#print(df)

# Ex 2
jucatori_peste_40 = df[df['Age'] > 40]
#print(jucatori_peste_40.head(10))

# Ex 3
tineri_talentati = df[(df['Overall'] >= 85) & (df['Age'] < 25)]
#print(tineri_talentati[['Name', 'Age', 'Overall']])

# Ex 4
jucatori_skill_moves = df.sort_values(by='Skill Moves', ascending=False)
#print(jucatori_skill_moves[['Name', 'Skill Moves']].head(15))

# Ex 5
jucatori_2021 = df[df['Contract Valid Until'].str.contains('2021', na=False)]
#print(jucatori_2021[['Name', 'Contract Valid Until']].head())

# Ex 6
#print("Dimensiuni dataset (randuri, coloane):", df.shape)
numar_jucatori_unici = df['ID'].nunique()
#print("Numar jucatori unici:", numar_jucatori_unici)

# Ex 7
top_nationalitati = df['Nationality'].value_counts().head(5)
#print("\nTop 5 naționalități:")
#print(top_nationalitati)

# Ex 8
top_nationalitati.plot(kind='pie', autopct='%1.1f%%', title='Top 5 Naționalități')
plt.ylabel('')
#plt.show()

# Ex 9
medii_viteza = df.groupby('Nationality')[['SprintSpeed', 'Acceleration']].mean()
#print("\nMedia de viteză și accelerație pe naționalități:")
#print(medii_viteza.head(10))

# Ex 10
df['Position'] = df['Position'].fillna('Unknown')
valori_lipsa = df['Position'].isna().sum() #cate valori NaN au mai ramas
#print(f"\nValori lipsă în coloana Position după curățare: {valori_lipsa}")

# Ex 11
cluburi_top = df.groupby('Club')['Overall'].mean().sort_values(ascending=False)
#print("\nClubul cu cea mai mare medie de Overall:")
#print(cluburi_top.head(1))

# Ex 12
numar_jucatori = (df['Value'] > df['Wage']).sum()
#print(f"\nNumăr jucători cu Value > Wage: {numar_jucatori}")

# Ex 13
df['is_underpaid'] = df['Wage'] < (df['Value'] / 100)
#print("\nVerificare jucători subplătiți:")
#print(df[['Name', 'Wage', 'Value', 'is_underpaid']].head(10))
total_subplatiti = df['is_underpaid'].sum()
#print(f"Total jucători subplătiți: {total_subplatiti}")

# Ex 14
df['Scor_Personalizat'] = (
    df['Overall'] * 0.3 +
    df['Potential'] * 0.3 +
    df['SprintSpeed'] * 0.2 +
    df['LongPassing'].fillna(0) * 0.2
)
#print("\nTop 5 jucători conform scorului personalizat:")
#print(df[['Name', 'Scor_Personalizat']].sort_values(by='Scor_Personalizat', ascending=False).head(5))

# Ex 15
df_afacere = df[['Name', 'Wage', 'Value']].copy()
df_afacere['difference'] = df_afacere['Value'] - df_afacere['Wage']
df_afacere_sortat = df_afacere.sort_values(by='difference', ascending=False)
print("\nTop 10 jucători care reprezintă o 'afacere bună':")
print(df_afacere_sortat.head(10))

# Ex 16
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Value', y='Wage')
plt.title('Relația dintre Valoarea de Piață și Salariu')
plt.xlabel('Valoare (Euro)')
plt.ylabel('Salariu (Euro)')
plt.show()