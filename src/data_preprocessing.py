import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataPreprocessor:
    def __init__(self):
        self.selected_features = None
        
    def load_data(self, train_path, validation_path, test_path):
        """
        Load datasets from CSV files
        """
        try:
            self.train_df = pd.read_csv(train_path)
            self.validation_df = pd.read_csv(validation_path)
            self.test_df = pd.read_csv(test_path)
            
            logger.info(f"Training set shape: {self.train_df.shape}")
            logger.info(f"Validation set shape: {self.validation_df.shape}")
            logger.info(f"Test set shape: {self.test_df.shape}")
            
            return True
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            return False
    
    def prepare_features(self, pfs_time_col='PFS_time', pfs_status_col='PFS_status'):
        """
        Prepare features and targets
        Note: PFS_time is mentioned as temporarily not used in your description
        """
        # Extract features (all columns except PFS time and status)
        feature_cols = [col for col in self.train_df.columns 
                       if col not in [pfs_time_col, pfs_status_col]]
        
        # Training set
        self.X_train = self.train_df[feature_cols]
        self.y_train = self.train_df[pfs_status_col]
        
        # Validation set  
        self.X_val = self.validation_df[feature_cols]
        self.y_val = self.validation_df[pfs_status_col]
        
        # Test set
        self.X_test = self.test_df[feature_cols]
        self.y_test = self.test_df[pfs_status_col]
        
        logger.info(f"Feature matrix shapes - Train: {self.X_train.shape}, "
                   f"Val: {self.X_val.shape}, Test: {self.X_test.shape}")
        
        return feature_cols
    
    def get_data(self):
        """
        Return processed data
        """
        return {
            'X_train': self.X_train, 'y_train': self.y_train,
            'X_val': self.X_val, 'y_val': self.y_val, 
            'X_test': self.X_test, 'y_test': self.y_test
        }
