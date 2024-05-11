
import pandas as pd

def impute_min_vaccinations(data):
    # Calculate the minimum daily vaccinations per country
    min_vaccinations = data.groupby('country')['daily_vaccinations'].min()
    
    # Create a copy of the data to avoid modifying the original dataframe
    imputed_data = data.copy()
    
    # Fill missing values in daily_vaccinations with the minimum for each country
    for country in min_vaccinations.index:
        if pd.isna(min_vaccinations[country]):
            # If minimum is NaN, replace missing values with 0 for this country
            imputed_data.loc[imputed_data['country'] == country, 'daily_vaccinations'] = imputed_data.loc[
                imputed_data['country'] == country, 'daily_vaccinations'].fillna(0)
        else:
            # Otherwise, use the minimum non-null value
            imputed_data.loc[imputed_data['country'] == country, 'daily_vaccinations'] = imputed_data.loc[
                imputed_data['country'] == country, 'daily_vaccinations'].fillna(min_vaccinations[country])

    return imputed_data

# Load the data
data = pd.read_csv('country_vaccination_stats.csv')

# Impute missing data
imputed_data = impute_min_vaccinations(data)

# Optionally save the imputed data to a new CSV
imputed_data.to_csv('imputed_vaccination_data.csv', index=False)
