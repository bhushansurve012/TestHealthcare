import streamlit as st

def main():
    st.title("Simple Streamlit Navbar")

    menu = ["Home", "About", "Services", "Contact"]
    selected_page = st.radio("Navigate", menu)

    if selected_page == "Home":
        st.write("Welcome to the Home page!")
    elif selected_page == "About":
        st.write("This is the About page. Learn more about us here.")
    elif selected_page == "Services":
        st.write("Explore our services and what we offer.")
    elif selected_page == "Contact":
        st.write("Contact us if you have any questions or inquiries.")

if __name__ == "__main__":
    main()

