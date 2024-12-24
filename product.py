import streamlit as st
from pathlib import Path

# Set the title of the webpage
st.set_page_config(page_title="Product Portfolio - Shreyas", page_icon="product-development.png")

DATA_FILENAME = Path(__file__).parent / 'data/base.csv'
df = pd.read_csv(DATA_FILENAME)
    
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
    st.sidebar.subheader("Select Date Range")
    start_date = st.sidebar.date_input("Start Date", df['order-date'].min())
    end_date = st.sidebar.date_input("End Date", df['order-date'].max())

    # Add filters for category, customer zone, and platform
    category_filter = st.sidebar.multiselect('Select Category', ['All'] + list(df['category'].unique()), default=['All'])
    zone_filter = st.sidebar.multiselect('Select Customer Zone', ['All'] + list(df['cust-zone'].unique()), default=['All'])
    platform_filter = st.sidebar.multiselect('Select Platform', ['All'] + list(df['platform'].unique()), default=['All'])

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
    st.write(f'Selected Data: Category - {category_filter}, Zone - {zone_filter}, Platform - {platform_filter}')

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

    if 'All' in category_filter:
        fdf = fdf
    else:
        fdf = fdf[fdf['category'].isin(category_filter)]

    # Filter by Customer Zone
    if 'All' in zone_filter:
        fdf = fdf
    else:
        fdf = fdf[fdf['cust-zone'].isin(zone_filter)]

    # Filter by Platform
    if 'All' in platform_filter:
        fdf = fdf
    else:
        fdf = fdf[fdf['platform'].isin(platform_filter)]

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
