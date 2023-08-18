import streamlit as st

def main():
    st.title("Streamlit Horizontal Tab Navigation")

    # Create a list of tab labels
    tabs = ["Home", "About", "Services", "Contact"]

    # Display the tabs horizontally
    selected_tab = st.radio("Select an option", tabs)

    # Display content based on the selected tab
    if selected_tab == "Home":
        st.write("Welcome to the Home page!")
    elif selected_tab == "About":
        st.write("This is the About page. Learn more about us here.")
    elif selected_tab == "Services":
        st.write("Explore our services and what we offer.")
    elif selected_tab == "Contact":
        st.write("Contact us if you have any questions or inquiries.")

if __name__ == "__main__":
    main()
