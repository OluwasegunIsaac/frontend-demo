import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def main():
    # Set the page layout to wide
    st.set_page_config(layout="wide")
    
    
    # Sidebar configuration
    with st.sidebar:
        st.markdown("<h2 style='text-align: center;'>User Inputs</h2>", unsafe_allow_html=True)

        st.multiselect(
            "Portfolio size:",
            options=[10, 15, 20, 25, 30, 40, 50],
            default=[10, 20]
        )

        # Time period inputs
        st.date_input("In-sample time period:", value=[pd.to_datetime("2019-01-01"), pd.to_datetime("2023-12-31")])
        st.date_input("Out-of-sample period:", value=[pd.to_datetime("2024-01-01"), pd.to_datetime("2024-07-31")])

        # Model selection
        st.selectbox(
            "Estimation model:",
            ["Historical timeseries", "Fama-French 3-factor", "Fama-French 5-factor", "APCA"]
        )

        # Bounds on weights
        st.slider("minWeight:", 0, 20, 3)
        st.slider("maxWeight:", 10, 50, 13)

        # Comparison benchmarks
        st.multiselect(
            "Comparison benchmarks:",
            options=["S&P500 index", "Russell 3000 index", "Dow Jones index", "NASDAQ Composite", "Popular invest funds"],
            default=["S&P500 index"]
        )

        st.button("Run", type="primary", use_container_width=True)

    # Main content
    _, col1, _ = st.columns(3)
    with col1:
        st.markdown("""
            <style>
            .app-spacing {
                margin-top: 0px;
                margin-bottom: -40px;
            }
            </style>
            """, unsafe_allow_html=True)

        app_name = """
            <div class='app-spacing' style="padding:4px">
            <h1 style='text-align: center; font-size: 40px;'>Outputs</h1>
            </div>
        """
        st.markdown(app_name, unsafe_allow_html=True)

    _, col1, _ = st.columns([1,3,1])
    with col1:
        st.markdown("<h1 style='text-align: center; font-size: 24px;'>ChatGPT Asset Selection</h1>",unsafe_allow_html=True)
    asset_selection_image = Image.open("placeholder_images/fig1.png")
    st.image(asset_selection_image, use_column_width=True)
    _, col1, _ = st.columns([1,3,1])
    with col1:
        st.markdown("<h1 style='text-align: center; font-size: 24px;'>In-sample Efficient Frontiers</h1>",unsafe_allow_html=True)
    efficient_frontier_image = Image.open("placeholder_images/fig2.png")
    st.image(efficient_frontier_image, use_column_width=True)
    _, col1, _ = st.columns([1,3,1])
    with col1:
        st.markdown("<h1 style='text-align: center; font-size: 24px;'>Out-of-Sample Cumulative Returns</h1>",unsafe_allow_html=True)
    cum_image = Image.open("placeholder_images/fig3.png")
    st.image(cum_image, use_column_width=True)
    _, col1, _ = st.columns([1,3,1])
    with col1:
        st.markdown("<h1 style='text-align: center; font-size: 24px;'>Out-of-Sample Risk and Reward Measures</h1>",unsafe_allow_html=True)
    reward_image = Image.open("placeholder_images/fig4.png")
    st.image(reward_image, use_column_width=True)


if __name__ == "__main__":
    main()
