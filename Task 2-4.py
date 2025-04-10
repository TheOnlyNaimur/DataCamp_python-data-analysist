#Task2

aggregated_data = (
    df.groupby("raw_material_supplier")
    .agg(
        avg_product_quality_score=("product_quality_score", lambda x: round(x.mean(), 2)),
        avg_pigment_quantity=("pigment_quantity", lambda x: round(x.mean(), 2))
    )
    .reset_index()
)


#Task-3
import pandas as pd

df = pd.read_csv("production_data.csv")

df["raw_material_supplier"] = pd.to_numeric(df["raw_material_supplier"], errors="coerce")
df["pigment_quantity"] = pd.to_numeric(df["pigment_quantity"], errors="coerce")
df["product_quality_score"] = pd.to_numeric(df["product_quality_score"], errors="coerce")

filtered = df[(df["raw_material_supplier"] == 2) & (df["pigment_quantity"] > 35)]


avg_quantity = round(filtered["pigment_quantity"].mean(), 2)
avg_quality = round(filtered["product_quality_score"].mean(), 2)

pigment_data = pd.DataFrame([{
    "raw_material_supplier": 2,
    "pigment_quantity": avg_quantity,
    "avg_product_quality_score": avg_quality
}])


#Task-4


product_quality_score_mean = round(df["product_quality_score"].mean(), 2)
product_quality_score_sd = round(df["product_quality_score"].std(), 2)
pigment_quantity_mean = round(df["pigment_quantity"].mean(), 2)
pigment_quantity_sd = round(df["pigment_quantity"].std(), 2)

corr_coef = round(df["pigment_quantity"].corr(df["product_quality_score"]), 2)

product_quality = pd.DataFrame([{
    "product_quality_score_mean": product_quality_score_mean,
    "product_quality_score_sd": product_quality_score_sd,
    "pigment_quantity_mean": pigment_quantity_mean,
    "pigment_quantity_sd": pigment_quantity_sd,
    "corr_coef": corr_coef
}])
