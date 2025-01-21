# MammographicMasses-KNN
# Mammographic Masses Classification using KNN

This project uses the **mammographic_masses** dataset to classify mammographic mass severity (benign or malignant) using the **K-Nearest Neighbors (KNN)** algorithm. The project demonstrates:
- Preprocessing data with missing values.
- Using KNN with different hyperparameters (`k`, `p`).
- Evaluating model accuracy and exploring different distance metrics (Euclidean and Manhattan).

## Dataset
The dataset, `mammographic_masses.data`, contains the following columns:
1. **BIRADS**: BI-RADS assessment (integer)
2. **Age**: Patient's age
3. **Shape**: Shape of the mass
4. **Margin**: Margin of the mass
5. **Density**: Mass density
6. **Severity**: Target label (0 = benign, 1 = malignant)

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/QueenAhllam/MammographicMasses-KNN.git
   cd MammographicMasses-KNN
