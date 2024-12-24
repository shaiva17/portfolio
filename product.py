import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from pathlib import Path
from datetime import datetime, timedelta
import geopandas as gpd

# Set the title of the webpage
st.set_page_config(page_title="Product Portfolio - Shreyas", page_icon="product-development.png")

DATA_FILENAME = Path(__file__).parent / 'data/base.csv'
df = pd.read_csv(DATA_FILENAME)
# Convert 'order-date' to datetime format (in case it's not already in datetime format
df['order-date'] = pd.to_datetime(df['order-date'], format='%Y-%m-%d', errors='coerce')
#df['order-date'] = df['order-date'].dt.date  # This will convert to just the date part

df['revenue'] = pd.to_numeric(df['revenue'],errors='coerce')
df['revenue'] = df['revenue'].round(0)
df = df.dropna(axis=1, how='all')

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
    st.image("manager.png", use_container_width=True)

# Create a radio button for navigating through projects
st.header("My Projects")
project_selection = st.radio(
    "Choose a project to explore:",
    ("Business Analysis", "Product Analysis 1", "Product Analysis 2"), horizontal = True)

if project_selection == "Business Analysis":
    st.subheader("Project 1: Business Dashboard")
    st.write("""
        **Description**: An interative dashboard built using streamlit.  
        **Technologies Used**: Python, Streamlit.
    """)

    # Sidebar filters
    st.subheader("Select Date Range")
    start_date = st.date_input("Start Date", df['order-date'].min())
    end_date = st.date_input("End Date", df['order-date'].max())

    # Add filters for category, customer zone, and platform
    category_filter = st.multiselect('Select Category', ['All'] + list(df['category'].unique()), default=['All'])
    zone_filter = st.multiselect('Select Customer Zone', ['All'] + list(df['cust-zone'].unique()), default=['All'])
    platform_filter = st.multiselect('Select Platform', ['All'] + list(df['platform'].unique()), default=['All'])

    # Apply filters to the DataFrame
    filtered_df = df.copy()

    # Filter by Category
    if 'All' in category_filter:
        filtered_df = filtered_df
    else:
        filtered_df = filtered_df[filtered_df['category'].isin(category_filter)]

    # Filter by Customer Zone
    if 'All' in zone_filter:
        filtered_df = filtered_df
    else:
        filtered_df = filtered_df[filtered_df['cust-zone'].isin(zone_filter)]

    # Filter by Platform
    if 'All' in platform_filter:
        filtered_df = filtered_df
    else:
        filtered_df = filtered_df[filtered_df['platform'].isin(platform_filter)]

    # Filter by Date Range
    filtered_df = filtered_df[(filtered_df['order-date'] >= pd.to_datetime(start_date)) &
                              (filtered_df['order-date'] <= pd.to_datetime(end_date))]

    st.subheader(f"KPI's")
    # st.write(f'Selected Data: Category - {category_filter}, Zone - {zone_filter}, Platform - {platform_filter}')

    # --- Display Total Revenue and Units (Card Style) ---
    total_revenue = filtered_df['revenue'].sum()
    tr = total_revenue / 100000
    total_units = filtered_df['qty'].sum()
    asp = round(total_revenue / total_units if total_units > 0 else 0)
    distinct_order_dates = filtered_df['order-date'].nunique()
    distinct_orders = filtered_df['order-no'].nunique()
    drr_gmv = tr / distinct_order_dates if distinct_order_dates > 0 else 0
    drr_units = total_units / distinct_order_dates if distinct_order_dates > 0 else 0
    aov = total_revenue / distinct_orders if distinct_orders > 0 else 0

    # Calculating data for trend
    min_order_date = filtered_df['order-date'].min()
    first_day_current_month = min_order_date.replace(day=1)
    last_day_last_month = first_day_current_month - timedelta(days=1)
    first_day_last_month = last_day_last_month.replace(day=1)

    fdf = df.copy()

    # if 'All' in category_filter:
    #     fdf = fdf
    # else:
    #     fdf = fdf[fdf['category'].isin(category_filter)]

    # # Filter by Customer Zone
    # if 'All' in zone_filter:
    #     fdf = fdf
    # else:
    #     fdf = fdf[fdf['cust-zone'].isin(zone_filter)]

    # # Filter by Platform
    # if 'All' in platform_filter:
    #     fdf = fdf
    # else:
    #     fdf = fdf[fdf['platform'].isin(platform_filter)]

    # Display cards with KPI values
    col1, col2, col3 = st.columns(3)

    # Card 1 (GMV)
    with col1:
        st.markdown(f"""
            <div style="padding: 15px; background-color: #f1f1f1; border-radius: 8px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
                <h3 style="text-align: center; font-size: 18px;"> Sales: ₹{tr:,.1f} Lakhs</h3>
            </div>
        """, unsafe_allow_html=True)

    # Card 2 (Units)
    with col2:
        st.markdown(f"""
            <div style="padding: 15px; background-color: #f1f1f1; border-radius: 8px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
                <h3 style="text-align: center; font-size: 18px;">Units: {total_units:,.0f}</h3>
            </div>
        """, unsafe_allow_html=True)

    # Card 3 (ASP)
    with col3:
        st.markdown(f"""
            <div style="padding: 15px; background-color: #f1f1f1; border-radius: 8px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
                <h3 style="text-align: center; font-size: 18px;">ASP: ₹{asp:,}</h3>
            </div>
        """, unsafe_allow_html=True)

    # Add space between rows
    st.write("")  # Line break

    # Create 3 more columns for the next row of cards
    col4, col5, col6 = st.columns(3)

    # Card 4 (DRR GMV)
    with col4:
        if rt >= 0:
            arrow = "&#x2191;"  # Up arrow (↑)
            arrow_color = "green"
        else:
            arrow = "&#x2193;"  # Down arrow (↓)
            arrow_color = "red"

        st.markdown(f"""
            <div style="padding: 15px; background-color: #f1f1f1; border-radius: 8px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
                <h3 style="text-align: center; font-size: 18px;">
                    DRR (Sales) : ₹{drr_gmv:,.1f} Lakhs<br>
                    <span style="font-size: 16px; color: {arrow_color};">
                        {arrow} {abs(rt):.2f}%
                    </span>
                </h3>  
            </div>
        """, unsafe_allow_html=True)

    # Card 5 (DRR Units)
    with col5:
        if ut >= 0:
            arrow = "&#x2191;"  # Up arrow (↑)
            arrow_color = "green"
        else:
            arrow = "&#x2193;"  # Down arrow (↓)
            arrow_color = "red"

        st.markdown(f"""
            <div style="padding: 15px; background-color: #f1f1f1; border-radius: 8px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
                <h3 style="text-align: center; font-size: 18px;">
                    DRR (Units) : {drr_units:,.0f}<br>
                    <span style="font-size: 16px; color: {arrow_color};">
                        {arrow} {abs(ut):.2f}%
                    </span>
                </h3>  
            </div>
        """, unsafe_allow_html=True)

    # Card 6 (AOV)
    with col6:
        if aovt >= 0:
            arrow = "&#x2191;"  # Up arrow (↑)
            arrow_color = "green"
        else:
            arrow = "&#x2193;"  # Down arrow (↓)
            arrow_color = "red"

        st.markdown(f"""
            <div style="padding: 15px; background-color: #f1f1f1; border-radius: 8px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
                <h3 style="text-align: center; font-size: 18px;">
                    AOV : ₹{aov:,.0f}<br>
                    <span style="font-size: 16px; color: {arrow_color};">
                        {arrow} {abs(aovt):.2f}%
                    </span>
                </h3>  
            </div>
        """, unsafe_allow_html=True)

    # Display Revenue Over Time chart
    st.subheader('Revenue Over Time')
    time_revenue = filtered_df.groupby('order-date')['revenue'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(time_revenue['order-date'], time_revenue['revenue'], marker='o', color='green')
    ax.set_title('Revenue Over Time')
    ax.set_xlabel('Order Date')
    ax.set_ylabel('Revenue')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # --- Revenue Split by Category (Pie Chart) ---
    category_revenue_pie = filtered_df.groupby('category')['revenue'].sum().reset_index()
    fig = px.pie(category_revenue_pie, names='category', values='revenue', title='Revenue Split by Category')
    st.plotly_chart(fig)

    # --- India Map ---
    shapefile_path = Path(__file__).parent / 'shapefile/india-states.shp'
    gdf = gpd.read_file(shapefile_path)
    gdf["STATE_NAME"] = gdf["ST_NM"].str.lower()
    filtered_df["state"] = filtered_df["state"].str.lower()
    test = filtered_df.groupby('state')['revenue'].sum().reset_index()
    test['revenue'] = test['revenue'] / 100000
    gdf = gdf.merge(test, left_on="STATE_NAME", right_on="state", how="left")
    gdf['revenue'] = gdf['revenue'].fillna(0)
    gdf.loc[gdf['STATE_NAME'] == 'dadra and nagar haveli and daman and diu', 'STATE_NAME'] = 'daman'

    # Plot map
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    gdf.plot(column='revenue', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

    for idx, row in gdf.iterrows():
        centroid = row['geometry'].centroid
        ax.annotate(text=row['STATE_NAME'], xy=(centroid.x, centroid.y), color='black', fontsize=6, ha='center')

    ax.set_title("Revenue by State", fontsize=15)
    ax.axis('off')
    st.pyplot(fig)







    
elif project_selection == "Product Analysis 1":
    import streamlit as st

    # Set the title and page config
    st.set_page_config(page_title="Inshorts - Product Design", page_icon="📱")

    # Add a header and introduction
    st.title("Inshorts App - Product Design")
    st.write("""
        Welcome to the product design for the Inshorts app with new features:
        - **Offline Mode**
        - **Community Engagement**
        - **Improved Search**
    """)

    # Create navigation sidebar
    sidebar = st.sidebar.radio("Navigate", ("Home", "Offline Mode", "Community", "Search"))

    if sidebar == "Home":
        # Home screen with categories, news feed, and options for the new features
        st.header("Personalized News Feed")
        st.write("Here’s a quick look at the latest stories!")
        
        # Categories to simulate personalized content
        categories = ["Top Stories", "Technology", "Business", "Sports", "Entertainment"]
        
        for category in categories:
            st.subheader(f"Category: {category}")
            st.write(f"Latest news about {category}...")
            st.write("-" * 40)

    elif sidebar == "Offline Mode":
        # Offline Mode simulation - Download articles
        st.header("Offline Mode: Download News for Later")
        
        # List of available articles to "download"
        articles = [
            {"title": "Tech Breakthrough: AI Advancements", "category": "Technology", "downloaded": False},
            {"title": "Breaking: Stock Market Hits Record High", "category": "Business", "downloaded": False},
            {"title": "World Cup: Latest Updates", "category": "Sports", "downloaded": False},
            {"title": "Entertainment News: Top Movies of the Year", "category": "Entertainment", "downloaded": False}
        ]
        
        # Simulate downloading articles
        for i, article in enumerate(articles):
            download_button = st.button(f"Download {article['title']}")
            if download_button:
                st.write(f"Downloaded: {article['title']} for offline reading.")
                articles[i]["downloaded"] = True
                
        # Show currently downloaded articles
        st.subheader("Downloaded Articles")
        for article in articles:
            if article["downloaded"]:
                st.write(f"- {article['title']} ({article['category']})")
    
    elif sidebar == "Community":
        # Community Engagement: User comments, ratings, and news submission
        st.header("Community Engagement: Share Your Thoughts")
        
        # Comment Section for a news article
        article_title = st.selectbox("Choose an article to comment on:", ["Tech Breakthrough: AI Advancements", "Stock Market Record", "World Cup Updates", "Top Movies of the Year"])
        
        comment = st.text_area(f"Comment on {article_title}:")
        if comment:
            st.write(f"Thank you for your comment: {comment}")
        
        # Simulate liking the article
        like_button = st.button("Like This Article")
        if like_button:
            st.write(f"You liked the article: {article_title}")
        
        # Submit news (user-generated content)
        submitted_news = st.text_area("Submit Your News Snippet")
        if submitted_news:
            st.write(f"Your news has been submitted: {submitted_news}")
    
    elif sidebar == "Search":
        # Search Functionality: Search and filter news
        st.header("Search News Articles")
        
        # Search bar with filters
        query = st.text_input("Enter a keyword or topic to search:")
        if query:
            st.write(f"Searching for: {query}")
        
        # Filter options
        filter_category = st.selectbox("Filter by category", ["All", "Technology", "Business", "Sports", "Entertainment"])
        if filter_category != "All":
            st.write(f"Filtering by: {filter_category}")
        
        # Display search results (simulated)
        st.write(f"Results for '{query}' in {filter_category}:")
        st.write("-" * 40)
        st.write(f"1. {query} article 1 (from {filter_category})")
        st.write(f"2. {query} article 2 (from {filter_category})")
        st.write(f"3. {query} article 3 (from {filter_category})")



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

