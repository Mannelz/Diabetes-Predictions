import pandas as pd
import numpy as np

data = pd.read_csv('diabetes.csv')

# GENERO
genders = np.random.randint(0, 2, 1000)

# HIPERTENSAO
hypertensions = np.random.randint(0, 2, 1000)

# DOENÇA CARDIACA
heartDiseases = np.random.randint(0, 2, 1000)

# HISTORICO DE FUMAR
smokingHistories = np.random.randint(0, 6, 1000)

# IDADE
meanAge = np.mean(data["age"])
stdAge = np.std(data["age"], ddof=2)

topAge = meanAge + stdAge 
bottomAge = meanAge - stdAge

ages = np.random.randint(bottomAge, topAge, 1000)

# IMC - INDICE DE MASSA CORPORAL
meanBMI = np.mean(data["bmi"])
stdBMI = np.std(data["bmi"], ddof=2)

topBMI = meanBMI + stdBMI 
bottomBMI = meanBMI - stdBMI

bmis = np.random.uniform(bottomBMI, topBMI, 1000).round(2)

# NIVEL DE HEMOGLOBINA A1C
meanHemoLevel = np.mean(data["HbA1c_level"])
stdHemoLevel = np.std(data["HbA1c_level"], ddof=2)

topHemoLevel = meanHemoLevel + stdHemoLevel 
bottomHemoLevel = meanHemoLevel - stdHemoLevel

hemoLevels = np.random.uniform(bottomHemoLevel, topHemoLevel, 1000).round(1)

# NIVEL DE GLICOSE
meanGlucoseLevel = np.mean(data["blood_glucose_level"])
stdGlucoseLevel = np.std(data["blood_glucose_level"], ddof=2)

topGlucoseLevel = meanGlucoseLevel + stdGlucoseLevel 
bottomGlucoseLevel = meanGlucoseLevel - stdGlucoseLevel

glucoseLevels = np.random.randint(bottomGlucoseLevel, topGlucoseLevel, 1000)

newData = pd.DataFrame({
    'gender': genders,
    'age': ages,
    'hypertension': hypertensions,
    'heart_disease': heartDiseases,
    'smoking_history': smokingHistories,
    'bmi': bmis,
    'HbA1c_level': hemoLevels,
    'blood_glucose_level': glucoseLevels
})

newData.to_csv('new_diabetes.csv', index=False)