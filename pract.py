import streamlit as st

def main():
    st.title("Streamlit Horizontal Navbar with Dropdown")

    menu_options = {
        "Home": [],
        "About": [],
        "Services": ["Service 1", "Service 2", "Service 3"],
        "Contact": []
    }

    selected_option = st.sidebar.radio("Select an option", list(menu_options.keys()))

    if selected_option == "Home":
        st.write("Welcome to the Home page!")
    elif selected_option == "About":
        st.write("This is the About page. Learn more about us here.")
    elif selected_option == "Services":
        st.write("Explore our services and what we offer.")
        selected_service = st.selectbox("Select a service", menu_options["Services"])
        st.write(f"You selected: {selected_service}")
    elif selected_option == "Contact":
        st.write("Contact us if you have any questions or inquiries.")

if __name__ == "__main__":
    main()
