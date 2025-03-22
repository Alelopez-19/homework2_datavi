import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np


def plot_boxplot_students_by_country(df):
    return px.box(df, x="Country", y="Number of Students",
                  labels={"Number of Students": "Number of Students", "Country": "Country"},
                  title="Distribution of Number of Students by Country")


def plot_boxplot_students_by_rank_top15(df):

    df_top15 = df.sort_values(by='Rank').head(15)
    
    return px.box(df_top15, x="Rank", y="Number of Students",
                  labels={"Number of Students": "Number of Students", "Rank": "Rank"},
                  title="Distribution of Number of Students by Top 15 University Rank")


def page_1(df):
    df2 = df.sort_values(by='Established')
    gf = px.bar(df, x="Rank", y="Number of Students", 
                labels={"Rank": "Rank", "Number of Students": "Number of Students"},
                title="Number of students by top ranking Universities in North America", 
                range_x=[1, 25], color='Name', color_discrete_sequence=px.colors.qualitative.Set3)
    
    gf2 = px.scatter(df, x="Minimum Tuition cost", y="Number of Students", 
                     labels={"Minimum Tuition cost": "Minimum Tuition Cost", "Number of Students": "Number of Students"},
                     title="Number of Students VS Tuition fees", color='Rank', color_continuous_scale=px.colors.sequential.Inferno)
    
    gf3 = px.line(df2, x="Established", y="Name", 
                  labels={"Established": "Year of Establishment", "Name": "University Name"},
                  title="Timeline of the Establishment of the top Universities in North America")
    
    country_count = df['Country'].value_counts().reset_index()
    country_count.columns = ['Country', 'Count']
    gf4 = px.density_heatmap(country_count, x="Country", y="Count", 
                             labels={"Count": "Number of Universities", "Country": "Country"},
                             title="Number of Universities by Country")
    
    st.plotly_chart(gf, use_container_width=True)
    st.plotly_chart(gf2, use_container_width=True)
    st.plotly_chart(gf3, use_container_width=True)
    st.plotly_chart(gf4, use_container_width=True)


def page_2(df):
   
    boxplot_students = plot_boxplot_students_by_country(df)
    boxplot_students_by_rank_top15 = plot_boxplot_students_by_rank_top15(df)

  
    st.plotly_chart(boxplot_students, use_container_width=True)
    st.plotly_chart(boxplot_students_by_rank_top15, use_container_width=True)


def main():
    
    df = pd.read_csv("NorthAmericaUniversities.csv", encoding='windows-1252')
    
   
    page = st.sidebar.radio("Choose a page", ("Visualizations by Rank and Students", "Box Plots"))

    
    if page == "Visualizations by Rank and Students":
        page_1(df)
    elif page == "Box Plots":
        page_2(df)

if __name__ == "__main__":
    main()