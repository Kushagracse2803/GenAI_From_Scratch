import streamlit as st
from secret_key_gem import gemini_key
from lang_chain_helper import generate_restaurant_name

# Streamlit UI setup
st.set_page_config(page_title="AI Restaurant Generator")
st.title("🍽️ AI Restaurant Name & Menu Generator")

# Sidebar input
cuisine = st.sidebar.selectbox(
    "Select a cuisine", 
    ["Italian", "Chinese", "Mexican", "Indian", "French"]
)

# On cuisine selection
if cuisine:
    with st.spinner("Generating..."):
        response = generate_restaurant_name(cuisine)

    st.header(f"✨ {response['restaurant_name'].strip()}")
    
    menu_items = response["menu_items"].strip().split(",")
    
    st.subheader("📋 Sample Menu Items:")
    for item in menu_items:
        st.write(f"• {item.strip()}")
