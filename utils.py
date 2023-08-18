import streamlit as st
import base64
from streamlit.components.v1 import html

from PATHS import NAVBAR_PATHS, SETTINGS

def inject_custom_css():
    with open('assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def get_current_route():
    try:
        return st.experimental_get_query_params()['nav'][0]
    except:
        return None

# Your model's title
model_title = "Your Model Title"

# Display the title for the dropdown
st.title(model_title)

# Display the custom navigation bar
with open("assets/images/settings.png", "rb") as image_file:
    image_as_base64 = base64.b64encode(image_file.read())

settings_items = ''
for key, value in SETTINGS.items():
    settings_items += (
        f'<a href="/?nav={value}" class="settingsNav">{key}</a>')

dropdown_component = rf'''
        <div class="dropdown" id="settingsDropDown">
            <img class="dropbtn" src="data:image/png;base64, {image_as_base64.decode("utf-8")}"/>
            <div id="myDropdown" class="dropdown-content">
                {settings_items}
            </div>
        </div>
        '''
st.markdown(dropdown_component, unsafe_allow_html=True)

js = '''
<script>
    // Dropdown hide / show
    var dropdown = window.parent.document.getElementById("settingsDropDown");
    dropdown.onclick = function() {
        var dropWindow = window.parent.document.getElementById("myDropdown");
        if (dropWindow.style.visibility == "hidden"){
            dropWindow.style.visibility = "visible";
        }else{
            dropWindow.style.visibility = "hidden";
        }
    };

    var settingsNavs = window.parent.document.getElementsByClassName("settingsNav");
    var cleanSettings = function(navigation_element) {
        navigation_element.removeAttribute('target')
    }

    for (var i = 0; i < settingsNavs.length; i++) {
        cleanSettings(settingsNavs[i]);
    }
</script>
'''
html(js)

# Your other Streamlit code here
