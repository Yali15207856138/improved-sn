# improved-sn

# ctDNA-based Immunotherapy Response Prediction

This repository contains the code for reproducing the analysis from our study on predicting immunotherapy response using ctDNA data from NSCLC patients.

## Study Design
- **Training set**: OAK trial data (n=303)
- **Validation set**: POPLAR trial data (n=97) 
- **Test set**: Local hospital data (n=41)

## Methodology
1. **Data preprocessing**: Binary mutation features (1=mutated, 0=wild-type)
2. **Feature selection**: Univariate analysis (P < 0.2) followed by LASSO
3. **Model training**: XGBoost with 5-fold cross-validation and hyperparameter tuning
4. **Model evaluation**: AUC, accuracy, sensitivity, specificity, PPV, NPV
5. **Model interpretation**: SHAP analysis for feature importance

## Data Format
Expected CSV files should contain:
- First column: PFS_time (time-to-event)
- Second column: PFS_status (binary outcome: 0/1)
- Remaining columns: Gene mutation features (binary: 0/1)

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Place your data files in the `data/` directory
3. Run the analysis: `python examples/run_analysis.py`

## Results
The code reproduces all analyses from the manuscript including:
- Model performance metrics (AUC, accuracy, etc.)
- ROC curves
- SHAP analysis for model interpretation
- Kaplan-Meier survival curves (if PFS_time data available)

## Data Availability
Due to data use agreements, the original trial data must be requested from [www.clinicalstudydatarequest.com](http://www.clinicalstudydatarequest.com).
