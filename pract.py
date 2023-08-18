import streamlit as st

def main():
    st.title("Custom Horizontal Navbar")

    menu = ["Home", "About", "Services", "Contact"]
    selected_page = st.radio("", menu)

    # Create a custom horizontal navbar
    st.markdown(
        """
        <style>
            .navbar {
                display: flex;
                justify-content: center;
                background-color: #f1f1f1;
                padding: 1rem;
                margin-bottom: 1rem;
            }
            .navbar a {
                padding: 0.5rem 1rem;
                text-decoration: none;
                color: #333;
                font-weight: bold;
                border: 1px solid transparent;
            }
            .navbar a:hover {
                background-color: #ddd;
                border: 1px solid #333;
            }
        </style>
        <div class="navbar">
            <a href="#" class="active">Home</a>

