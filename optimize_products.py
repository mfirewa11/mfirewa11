import pandas as pd
from bs4 import BeautifulSoup

# Load the CSV file
file_path = r'C:\Users\11mfi\Desktop\Product VS\product sheet for gpt.csv'
product_data = pd.read_csv(file_path)

# Define a function to generate the SEO content with cleaned key features
def generate_seo_content_cleaned(row):
    # Extract product details
    product_name = row['Product Name']
    brand_name = row['Brand Name']
    key_features = row['Key Features/Benefits']
    target_keywords = row['Target Keywords']
    
    # Clean the key features to remove HTML tags
    clean_features = BeautifulSoup(key_features, "html.parser").get_text()
    
    # Generate Page Title
    if pd.notnull(brand_name):
        page_title = f"{product_name} | {brand_name} | Key Features & Benefits"
    else:
        page_title = f"{product_name} | Key Features & Benefits"
    
    # Generate Meta Description
    meta_description = f"Discover the {product_name}. {clean_features[:120]}... Shop now!"
    
    # Generate H1 Tag
    h1_tag = product_name
    
    return page_title, meta_description, h1_tag

# Apply the function to each row in the DataFrame
seo_content_cleaned = product_data.apply(generate_seo_content_cleaned, axis=1)

# Create a new DataFrame with the SEO content
seo_df_cleaned = pd.DataFrame(seo_content_cleaned.tolist(), columns=['Page Title', 'Meta Description', 'H1 Tag'])

# Combine the original data with the SEO content
result_df_cleaned = pd.concat([product_data, seo_df_cleaned], axis=1)

# Save the cleaned and optimized DataFrame to a new CSV file
output_file_path = r'C:\Users\11mfi\Desktop\Product VS\optimized_product_data.csv'
result_df_cleaned.to_csv(output_file_path, index=False)

print(f"Optimized data saved to {output_file_path}")