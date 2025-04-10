#Task1

import pandas as pd
import numpy as np

df = pd.read_csv("production_data.csv")


missing_vals = ['-', 'missing', 'null', 'none', 'n/a', '', 'NaN', 'NA', 'nan', ' ', np.nan]

# -------------------- batch_id --------------------

df = df[~df['batch_id'].isin(missing_vals)]
df = df[df['batch_id'].notna()]

# -------------------- production_date --------------------

df['production_date'] = pd.to_datetime(df['production_date'], errors='coerce')
df = df[df['production_date'].notna()]

# -------------------- raw_material_supplier --------------------

df['raw_material_supplier'] = df['raw_material_supplier'].astype(str).str.strip().str.lower()
df['raw_material_supplier'] = df['raw_material_supplier'].replace({
    '1': 'national_supplier',
    '2': 'international_supplier',
    **{val: np.nan for val in missing_vals}  # Mark all missing values as NaN
})
df['raw_material_supplier'].fillna('national_supplier', inplace=True)

# -------------------- pigment_type --------------------

df['pigment_type'] = df['pigment_type'].astype(str).str.strip().str.lower()
df['pigment_type'] = df['pigment_type'].replace({
    **{val: 'other' for val in missing_vals}  # Handle missing values
})

valid_types = ['type_a', 'type_b', 'type_c']
df['pigment_type'] = df['pigment_type'].apply(
    lambda x: x if x in valid_types else 'other'
)

# -------------------- pigment_quantity --------------------

df['pigment_quantity'] = pd.to_numeric(df['pigment_quantity'], errors='coerce')
df['pigment_quantity'] = df['pigment_quantity'].replace({val: np.nan for val in missing_vals})
median_pigment = df['pigment_quantity'].median()
df['pigment_quantity'].fillna(median_pigment, inplace=True)
df['pigment_quantity'] = df['pigment_quantity'].clip(1, 100)

# -------------------- mixing_time --------------------

df['mixing_time'] = pd.to_numeric(df['mixing_time'], errors='coerce')
df['mixing_time'] = df['mixing_time'].replace({val: np.nan for val in missing_vals})
mean_mixing_time = round(df['mixing_time'].mean(), 2)
df['mixing_time'].fillna(mean_mixing_time, inplace=True)

# -------------------- mixing_speed --------------------

df['mixing_speed'] = df['mixing_speed'].astype(str).str.strip().str.title()
df['mixing_speed'] = df['mixing_speed'].replace({
    **{val: 'Not Specified' for val in missing_vals}  # Handle missing values
})
valid_speeds = ['Low', 'Medium', 'High']
df['mixing_speed'] = df['mixing_speed'].apply(
    lambda x: x if x in valid_speeds else 'Not Specified'
)

# -------------------- product_quality_score --------------------

df['product_quality_score'] = pd.to_numeric(df['product_quality_score'], errors='coerce')
df['product_quality_score'] = df['product_quality_score'].replace({val: np.nan for val in missing_vals})
mean_quality = round(df['product_quality_score'].mean(), 2)
df['product_quality_score'].fillna(mean_quality, inplace=True)

clean_data = df.copy()
