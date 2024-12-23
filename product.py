import streamlit as st

# Set the title of the webpage
st.set_page_config(page_title="Product Portfolio - Shreyas", page_icon="product-development.png")

# Create a header with image and personal details at the top
header_col1, header_col2 = st.columns([1, 4])  # Adjust column widths as needed

with header_col1:
    # Add an image at the top left corner (adjust size if needed)
    st.image("Shreyas.jpg", width=100)

with header_col2:
    # Add your name and details
    st.markdown("""
        # Shreyas Kosale
        ## Product Enthusiast & Data Analytics Expert

        Passionate about building innovative products that solve real-world problems. Leveraging data and analytics to make informed decisions and drive product strategies.

        **Email**: [shreyas.kosale@gmail.com](mailto:shreyas.kosale@gmail.com)  
        **LinkedIn**: [Shreyas Kosale](https://www.linkedin.com/in/shreyas-kosale)  
    """)

# Add an introduction section
st.write("""
    Hi there! I'm Shreyas Kosale. Welcome to my Product Portfolio.  
    I'm passionate about building amazing products and leveraging the power of data.
""")

# Create two columns for layout (About Me and Image)
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
    st.image("https://www.example.com/your-image.jpg", caption="A cool image", use_container_width=True)

# Create a radio button for navigating through projects
st.header("My Projects")
project_selection = st.radio(
    "Choose a project to explore:",
    ("Project 1", "Project 2", "Project 3")
)

if project_selection == "Project 1":
    st.subheader("Project 1: Task Management App")
    st.write("""
        **Description**: An innovative app that helps users manage tasks efficiently.  
        **Technologies Used**: Python, Streamlit, SQLite.
    """)
    st.image("https://www.example.com/project1-image.jpg", caption="Project 1 Screenshot", use_container_width=True)

elif project_selection == "Project 2":
    st.subheader("Project 2: Web Scraping Tool")
    st.write("""
        **Description**: A web scraping tool for collecting data from multiple websites.  
        **Technologies Used**: BeautifulSoup, Pandas, Python.
    """)
    st.image("https://www.example.com/project2-image.jpg", caption="Project 2 Screenshot", use_container_width=True)

elif project_selection == "Project 3":
    st.subheader("Project 3: Business Metrics Dashboard")
    st.write("""
        **Description**: A data visualization dashboard for tracking business metrics.  
        **Technologies Used**: Plotly, Dash, SQL.
    """)
    st.image("https://www.example.com/project3-image.jpg", caption="Project 3 Screenshot", use_container_width=True)

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
    © Shreyas Kosale 2024
""")
