import streamlit as st

def main():
    st.title("Models")
    
    # Create a navigation menu with options
    menu_options = ["Home", "About", "Services", "Contact"]
    selected_option = st.sidebar.selectbox("Select an option", menu_options)
    
    # Display content based on the selected option
    if selected_option == "Home":
        st.write("Welcome to the Home page!")
    elif selected_option == "About":
        st.write("This is the About page. Learn more about us here.")
    elif selected_option == "Services":
        st.write("Explore our services and what we offer.")
    elif selected_option == "Contact":
        st.write("Contact us if you have any questions or inquiries.")

if __name__ == "__main__":
    main()
