import streamlit as st

def main():
    st.title("Horizontal Navbar Example")

    # Create a list of menu items
    menu_items = ["Home", "About", "Services", "Contact"]

    # Display the navbar
    with st.beta_container():  # You can use 'st.container' for Streamlit 0.89+
        nav_item = st.radio("Navigation", menu_items)
        
        if nav_item == "Home":
            st.write("Welcome to the Home page!")
        elif nav_item == "About":
            st.write("This is the About page.")
        elif nav_item == "Services":
            st.write("Explore our Services.")
        elif nav_item == "Contact":
            st.write("Contact us for more information.")

if __name__ == "__main__":
    main()
