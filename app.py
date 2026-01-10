import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Veggie Nutrition Analyzer", layout="wide")

st.title("🥦 Vegetarian Food Nutrition Analysis")
st.markdown("Developed by: **Antra & Anusha**")

# Load cleaned data
df = pd.read_csv('cleaned_vegetable_nutrition.csv')

# Sidebar selection
veg_list = sorted(df['Vegetable'].unique())
selected_veg = st.sidebar.multiselect("Select Vegetables to Compare", veg_list, default=veg_list[:3])

if selected_veg:
    filtered_df = df[df['Vegetable'].isin(selected_veg)]
    
    # Show Data
    st.subheader("Nutritional Data Comparison")
    st.dataframe(filtered_df)

    # Visualization
    st.subheader("Visual Analysis")
    fig = px.bar(filtered_df, x='Vegetable', y=['Protein (g)', 'Carbs (g)', 'Fiber (g)'], 
                 barmode='group', title="Macro-nutrient Comparison")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write("Please select at least one vegetable from the sidebar.")