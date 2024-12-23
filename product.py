import streamlit as st

# Set the title of the webpage
st.set_page_config(page_title="Product Portfolio - Shreyas", page_icon="🏠")

# Add a header and introduction
st.title("Welcome to My Portfolio !")
st.write("""
    Hi there! I'm Shreyas Kosale. Welcome to my Product Portfolio.  
    I'm passionate about building amazing products and leveraging the power of data. Explore below to know more about me and my work.
""")

# Create two columns for layout
col1, col2 = st.columns(2)

with col1:
    # Add an "About Me" section
    st.header("About Me")
    st.write("""
        I'm a product enthusiast with a strong background in data analytics.  
        I enjoy creating innovative solutions that solve real-world problems.  
        I’ve worked on several exciting projects, leveraging data-driven insights to shape product strategies.
    """)

with col2:
    # Add an image (replace with your own image URL or path)
    st.image("https://www.example.com/your-image.jpg", caption="A cool image", use_column_width=True)

# Add a Projects section with three columns
st.header("My Projects")

# Creating three columns for the projects section
project_col1, project_col2, project_col3 = st.columns(3)

with project_col1:
    st.subheader("Project 1")
    st.write("""
        **Description**: An innovative app that helps users manage tasks efficiently.  
        **Technologies Used**: Python, Streamlit, SQLite.
    """)

with project_col2:
    st.subheader("Project 2")
    st.write("""
        **Description**: A web scraping tool for collecting data from multiple websites.  
        **Technologies Used**: BeautifulSoup, Pandas, Python.
    """)

with project_col3:
    st.subheader("Project 3")
    st.write("""
        **Description**: A data visualization dashboard for tracking business metrics.  
        **Technologies Used**: Plotly, Dash, SQL.
    """)

# Add a Contact section in two columns
st.header("Contact Me")
contact_col1, contact_col2 = st.columns(2)

with contact_col1:
    st.write("""
        Feel free to reach out to me via email or social media:
    """)
    st.write("[Email me](mailto:your-email@example.com)")
    st.write("[LinkedIn](https://www.linkedin.com/in/your-profile)")

with contact_col2:
    st.write("""
        You can also check out my GitHub profile for some of my open-source projects:
    """)
    st.write("[GitHub](https://github.com/your-profile)")

# Footer section with custom styling
st.markdown("""
    ---
    Built with ❤️ using [Streamlit](https://streamlit.io)  
    © [Your Name] 2024
""")

