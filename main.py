# library 
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
from st_on_hover_tabs import on_hover_tabs
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
import pycountry
import plotly.graph_objects as go
import plotly.express as px
import us
import re
from streamlit_lottie import st_lottie
import circlify
import time
from wordcloud import WordCloud
import os
print(os.getcwd())

# set halaman dan css
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# load data
dfCp = pd.read_csv(os.path.join('dataset', 'merged_company.csv'))
dfJob= pd.read_csv(os.path.join('dataset', 'merged_job.csv'))

# mengganti nama negara
def get_country_name(country_code):
    try:
        return pycountry.countries.get(alpha_2=country_code).name
    except AttributeError:
        return country_code
    
dfCp['country'] = dfCp['country'].apply(get_country_name)

# mengganti nama negara bagian
def get_state_name(state_code):
    try:
        # Pastikan state_code adalah string
        if isinstance(state_code, str):
            state_obj = us.states.lookup(state_code)
            # Pastikan state_obj tidak None
            if state_obj is not None:
                return state_obj.name
            else:
                return state_code
        else:
            return state_code
    except (AttributeError, re.error):
        return state_code

dfCp['state'] = dfCp['state'].apply(get_state_name)

# pengaturan sidebar
with st.sidebar:
    tabs = on_hover_tabs(tabName=['Dashboard', 'Company', 'Job', 'About'], 
                         iconName=['home', 'account_balance', 'work', 'space_dashboard'], default_choice=0)

# sidebar 1 : dashboard
if tabs =='Dashboard':
    
    #section 1
    col1, col2 = st.columns([5,4])
    with col1:
        title = '''<br>
        <span style='color: black; font-weight: 700'>A </span><span style='color: #00c9a4; font-weight: 700'>faster way</span><span style='color: black; font-weight: 700'> to know everything about </span><span style='color: #00c9a4; font-weight: 900'>LinkedIn</span>'''
        st.markdown(f"<h1 style='text-align: left; font-size: 60px; font-weight: 900;'>{title}</h1>", unsafe_allow_html=True)
        sub_title = '''Unleash the potential of seamless data exploration with Streamlit.
        Your ultimate tool for translating LinkedIn data into dynamic visualizations, all readily accessible.'''
        st.markdown(f"<p style='text-align: justify; font-size: 18px; color: #555555;'>{sub_title}</p>", unsafe_allow_html=True)

        # Tombol untuk memunculkan balon-balon
        m = st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #00c9a4;
            color: white;
            height: 3em;
            width: 12em;
            border-radius:20px;
            font-size:20px;
            font-weight: 500;
            display: block;
        }   

        div.stButton > button:hover {
            background-color:#2fe3c1;
            color: white;
            border: none;
        }

        div.stButton > button:active {
            position:relative;
            top:3px;
            border: none;
            color: black;
        }

        </style>""", unsafe_allow_html=True)

        if st.button("Get ready with us"):
            st.balloons()

    with col2:
        st_lottie("https://lottie.host/51b8afd7-a453-4a19-add8-f01284591879/jzdPPfCPOU.json")

    # section 2 
    favorite_job = '''Discover big companies. Chase your dreams with them.'''
    st.markdown(f"<p style='text-align: center; font-size: 18px; color: #555555; margin-top: 100px'>{favorite_job}</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,3,1])
    with col1:
        st.write(' ')
    with col2:
        st.image(r'img/logo.png', use_column_width=True)
    with col3:
        st.write(' ')

    # section 3
    st.markdown("<hr style='border: 1px solid #cccccc; margin-top: 100px'>", unsafe_allow_html=True)
    sub_title = '''The Cutting-Edge Standard in LinkedIn Insights'''
    st.markdown(f"<p style='text-align: center; font-size: 34px; color: #00c9a4; font-weight: 700;'>{sub_title}</p>", unsafe_allow_html=True)
    desc = '''Elevate your LinkedIn analytics with Lottie, the compact, scriptable animation format. Embraced by top platforms, it transforms data into interactive visualizations for an unparalleled user experience.'''
    st.markdown(f"<p style='text-align: center; font-size: 18px; color: #555555; width: 700px; align-item: center; margin: auto'>{desc}</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid #cccccc; margin-top: 50px; margin-bottom: 100px;'>", unsafe_allow_html=True)

    # section 4
    # Calculate metrics
    sub_title = '''Explore insights seamlessly on this site. How was it?'''
    st.markdown(f"<p style='text-align: center; font-size: 34px; color: #00c9a4; font-weight: 700'>{sub_title}</p>", unsafe_allow_html=True)
    desc = '''Gain insights effortlessly! Check out key metrics for companies, industries, jobs, skills, and countries. Explore the data with ease.'''
    st.markdown(f"<p style='text-align: center; font-size: 18px; color: #555555; width: 700px; align-item: center; margin: auto'>{desc}</p>", unsafe_allow_html=True)
    st.title('')

    total_companies = dfCp['name'].nunique()
    total_industries = dfCp['industry'].nunique()
    total_job = dfJob['title'].nunique()
    total_skill = dfJob['skill'].nunique()
    total_countries = dfCp['country'].nunique()

    # Display metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total Companies", total_companies)
    col2.metric("Total Industries", total_industries)
    col3.metric("Total Job", total_job)
    col4.metric("Total Skill", total_skill)
    col5.metric("Total Countries", total_countries)
    style_metric_cards()

    # section 4
    st.title('')
    col1, col2 = st.columns([5,4])
    with col1:
        st.markdown("<h2 style='color: black; font-weight: 500; font-size: 34px; margin-top: 50px'>Analyze. Visualize. Elevate.</h2></div", unsafe_allow_html=True)
        st.markdown("<p style='color: #555555; font-size: 18px; margin-bottom: 50px'>Effortlessly infuse dynamics into your LinkedIn insights.</p></div", unsafe_allow_html=True)
        def redirect_button(url: str, text: str = None, color="#00c9a4"):
            m = st.markdown(
                f"""
                <style>
                div.stButton > button:first-child {{
                    background-color: {color};
                    color: white;
                    height: 3em;
                    width: 12em;
                    border-radius: 20px;
                    font-size: 20px;
                    font-weight: 500;
                    display: inline-block;
                    text-decoration: none;
                    border-style: none;
                }}   
                div.stButton > button:hover {{
                    background-color: #2fe3c1;
                    color: white;
                    border: none;
                }}
                div.stButton > button:active {{
                    position: relative;
                    top: 3px;
                    border: none;
                    color: black;
                }}
                </style>
                """
                , unsafe_allow_html=True
            )
            st.markdown(
                f"""
                <a href="{url}" target="_self">
                    <div class="stButton">
                        <button>{text}</button>
                    </div>
                </a>
                """
                , unsafe_allow_html=True
            )
        redirect_button("http://www.linkedin.com/", "Go to LinkedIn")

    with col2:
        st_lottie("https://lottie.host/f10df395-fcfa-45d5-a917-85ccf6be3c0e/iBSlzFGPKP.json")

# sidebar 2 : search
elif tabs == 'Company':
    tab_c1, tab_c2, tab_c3 = st.tabs(['Dataset', 'Company Insight', 'wordcloud'])
    with tab_c1:

        # form filtering
        with st.form(key='my_form'):
            col_country, col_industry, col_size = st.columns(3)
            with col_country:
                selected_country = st.selectbox('Country', dfCp['country'].unique())
            with col_industry:
                selected_industry = st.selectbox('Industry', dfCp['industry'].unique())
            with col_size:
                selected_size = st.selectbox('Size Company', dfCp['company_size'].unique())
            submitted = st.form_submit_button(label="Search")

        if submitted:
            # Pilih kolom-kolom tertentu yang ingin ditampilkan
            selected_columns = ['name', 'industry', 'speciality', 'company_size', 'state', 'country']

            filtered_df = dfCp[dfCp['country'] == selected_country]
            selected_industry = [] if selected_industry is None else selected_industry
            if isinstance(selected_industry, str):
                selected_industry = [selected_industry]
            if selected_industry:
                filtered_df = filtered_df[filtered_df['industry'].isin(selected_industry)]

            filtered_df = filtered_df[filtered_df['company_size'] == selected_size]
            filtered_df.reset_index(drop=True, inplace=True)
            filtered_df.index += 1

            # Clear previous table
            table_placeholder = st.empty()
            # Display the DataFrame using st.table
            table_placeholder.table(filtered_df[selected_columns])


    with tab_c2:
        st.header('Company Insight ')
        info_company_insight = '''Explore the dynamics of various industries, company sizes, and geographical locations in our Company 
        Insights section. Gain valuable insights into the distribution of companies, their sizes, and follower counts. Uncover trends 
        in the corporate landscape to make informed decisions.'''
        st.markdown(f'<p style="text-align: justify; margin-bottom: 30px;">{info_company_insight}</p>', unsafe_allow_html=True)

        # ------------------- METRIC -------------------------
        # Calculate metrics
        total_industries = dfCp['industry'].nunique()
        total_companies = dfCp['name'].nunique()
        total_specialities = dfCp['speciality'].nunique()
        total_countries = dfCp['country'].nunique()

        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Companies", total_companies)
        col2.metric("Total Industries", total_industries)
        col3.metric("Total Specialities", total_specialities)
        col4.metric("Total Countries", total_countries)
        style_metric_cards()
        st.markdown("***")

        # ------------------- INDUSTRY DISTRIBUTION -------------------------
        with st.expander("Top 10 Industry Distribution with the Number of Companies"):
            col_industry, col_industry_info = st.columns([3,2])
            with col_industry:
                industry_counts = dfCp['industry'].value_counts().head(10)
                plt.rc('xtick', labelsize=8)
                plt.rc('ytick', labelsize=8)
                plt.figure(figsize=(8, 4))
                sns.barplot(x=industry_counts.index, y=industry_counts.values, palette='viridis')
                plt.xlabel('Industry')
                plt.ylabel('Number of Companies')
                plt.xticks(rotation=45, ha='right')
                sns.despine()
                st.pyplot()
            with col_industry_info:
                st.info('Information')
                st.markdown("- 'Staffing & Recruiting' industry ranks highest in the number of company, followed by 'Information Technology & Services', and 'Hospital & Health Case' indicating high demand in the field of health.")
                st.markdown("- This trend underscores the robust opportunities available in the Staffing & Recruiting industry in 2023, catering to those looking to kickstart their careers in Staffing & Recruiting industry.")
                st.markdown('''
                <style>
                [data-testid="stMarkdownContainer"] ul{
                    padding-left: 20px;
                    text-align: justify;
                    font-size: 12px;
                }
                </style>
                ''', unsafe_allow_html=True)

        # ------------------- SIZE DISTRIBUTION -------------------------
        with st.expander("Company Size Distribution"):
            col_size, col_size_info = st.columns([3,2])
            with col_size:
                plt.rc('xtick', labelsize=8)
                plt.rc('ytick', labelsize=8)
                plt.figure(figsize=(8, 4))
                sns.countplot(x='company_size', data=dfCp, order=dfCp['company_size'].value_counts().index, palette='viridis')
                plt.xlabel('Company Size')
                plt.ylabel('Number of Companies')
                plt.xticks(rotation=0)
                sns.despine()
                st.pyplot()
            with col_size_info:
                st.info('Information')
                st.markdown("- Companies with a size classification of '2' have the highest number of companies, followed by those with a size classification of '5' and '1.' This reveals that companies as represented by the '2' classification, are the primary contributors to the company distribution in 2023, with '5' and '1' classified companies also playing substantial roles in companies distribution.")
                st.markdown("- This trend signifies that companies (size '2') dominate the companies landscape in 2023, likely offering diverse career prospects. However, companies categorized as '5' and '1' also maintain a significant presence, showcasing a variety of employment options across different company sizes to cater to the preferences and career goals of job seekers.")
                st.markdown('''
                <style>
                [data-testid="stMarkdownContainer"] ul{
                    padding-left: 20px;
                    text-align: justify;
                    font-size: 12px;
                }
                </style>
                ''', unsafe_allow_html=True)

        # ------------------- POPULAR COMPANY DISTRIBUTION -------------------------
        with st.expander("Top 10 Popular Company Distribution"):
            col_comp, col_info = st.columns([3,2])
            with col_comp:
                dfCp['follower_count'] = pd.to_numeric(dfCp['follower_count'], errors='coerce')
                print(dfCp['follower_count'].dtype)
                plt.figure(figsize=(12, 6))
                top_10_followers = dfCp.nlargest(10, 'follower_count')
                sns.barplot(x='follower_count', y='name', data=top_10_followers, palette='viridis')
                plt.xlabel('Follower Count')
                plt.ylabel('Company Name')
                st.pyplot()
            with col_info:
                st.info('Information')
                st.markdown("- Amazon is the highest ranks in the popularitation, followed by Google and Unilever")
                st.markdown("- This trend indicates that companies in the field of Information Technology & Services are in great demand by many people in 2023.")
                st.markdown('''
                <style>
                [data-testid="stMarkdownContainer"] ul{
                    padding-left: 20px;
                    text-align: justify;
                    font-size: 12px;
                }
                </style>
                ''', unsafe_allow_html=True)

        # ------------------- INDUSTRY DISTRIBUTION WITH COMPANY SIZE -------------------------
        with st.expander("Top 10 Industry Distribution with Company Size"):
            col_comp, col_info = st.columns([3,2])
            with col_comp:
                top_10_industries = dfCp['industry'].value_counts().head(10).index
                dfTopIndustries = dfCp[dfCp['industry'].isin(top_10_industries)]
                plt.figure(figsize=(12, 6))
                sns.countplot(x='industry', hue='company_size', data=dfTopIndustries)
                plt.xticks(rotation=45)
                plt.xlabel('Industry')
                plt.ylabel('Count')
                st.pyplot()
            with col_info:
                st.info('Information')
                st.markdown("- Companies with size 3 from the Information Technology &; Service industry, have the largest number of companies, followed by company size 2 and size 3 from the field of staffing & recruiting. ")
                st.markdown("- This trend indicates that most companies from the information technology &; services industry and staffing & recruiting industry are included in medium-sized companies with a company size range of 2-4.")
                st.markdown('''
                <style>
                [data-testid="stMarkdownContainer"] ul{
                    padding-left: 20px;
                    text-align: justify;
                    font-size: 12px;
                }
                </style>
                ''', unsafe_allow_html=True)

        # ------------------- TOP 10 SPECIALITY -------------------------
        with st.expander("Top 10 Speciality"):
            col_comp, col_info = st.columns([3,2])
            with col_comp:
                top_10_specialties = dfCp['speciality'].value_counts().head(10)
                top_10_specialties = top_10_specialties[top_10_specialties.index != "-"]
                plt.figure(figsize=(10, 5))
                sns.barplot(x=top_10_specialties.values, y=top_10_specialties.index, palette='viridis')
                plt.xlabel('Count')
                plt.ylabel('Specialty')
                st.pyplot()
            with col_info:
                st.info('Information')
                st.markdown("- Recruiting ranks as the most of the specialties needed in companies in 2023. This was followed by staffing and technology.")
                st.markdown("- This trend indicates that recruiting is the primary specialty in a company. In addition, staffing and technology also play an active role in the company")
                st.markdown('''
                <style>
                [data-testid="stMarkdownContainer"] ul{
                    padding-left: 20px;
                    text-align: justify;
                    font-size: 12px;
                }
                </style>
                ''', unsafe_allow_html=True)

    with tab_c3:
        # Function to generate Word Cloud
        def generate_wordcloud(text):
            print("Generating Word Cloud for text:", text)
            wordcloud = WordCloud(width=1200, height=300, background_color='white').generate(text)
            plt.figure(figsize=(12, 6))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            st.image(wordcloud.to_image())

        # Streamlit app
        st.header("Word Clouds for Company Descriptions")

        # Choose a company for analysis
        col1, col2 = st.columns([1, 2])
        with col1:
            selected_company = st.selectbox("Select a Company", dfCp['name'].unique())
        with col2:
            st.write('')

        # Filter the dataset for the selected company
        selected_company_data = dfCp[dfCp['name'] == selected_company]
        st.write('')

        # Generate Word Cloud for the description of the selected company
        generate_wordcloud(selected_company_data['description'].iloc[0])

        # Display company details
        st.title('')
        st.subheader(f"Details for {selected_company}")
        st.write(selected_company_data[['name', 'description']])


elif tabs == 'Job':
    tab_j1, tab_j2, tab_j3 = st.tabs(['Dataset', 'Job Insight', 'wordcloud'])
    with tab_j1:

        # form filtering
        with st.form(key='my_form'):
            col_skill, col_pay, col_work = st.columns(3)
            with col_skill:
                selected_skill = st.selectbox('Skill', dfJob['skill'].unique())
            with col_pay:
                selected_pay = st.selectbox('Pay Period', dfJob['pay_period'].unique())
            with col_work:
                selected_work = st.selectbox('Work Type', dfJob['work_type'].unique())
            submitted = st.form_submit_button(label="Search")

        if submitted:
            # Pilih kolom-kolom tertentu yang ingin ditampilkan
            selected_columns = ['company', 'title', 'location', 'skill', 'max_salary', 'min_salary', 'pay_period', 'work_type', 'benefit']

            filtered_df = dfJob[(dfJob['skill'] == selected_skill) & (dfJob['pay_period'] == selected_pay) & (dfJob['work_type'] == selected_work)]
            filtered_df.reset_index(drop=True, inplace=True)
            filtered_df.index += 1

            # Clear previous table
            table_placeholder = st.empty()
            # Display the DataFrame using st.table
            table_placeholder.table(filtered_df[selected_columns])


    with tab_j2:
        st.header('Job Insight ')
        info_job_insight = '''Explore the dynamics of various job, required skill, work type, company sizes, and geographical locations in our Job  
        Insights section. Gain valuable insights into the total of job, their required skill, and salary. Uncover trends 
        in the corporate landscape to make informed decisions.'''
        st.markdown(f'<p style="text-align: justify;">{info_job_insight}</p>', unsafe_allow_html=True)
        st.write()

        # ------------------- METRIC -------------------------
        # Calculate metrics
        total_job = dfJob['title'].nunique()
        total_skill = dfJob['skill'].nunique()
        average_min_salary = dfJob['min_salary'].mean()
        average_max_salary = dfJob['max_salary'].mean()

        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Job", total_job)
        col2.metric("Total Skill", total_skill)
        col3.metric("Average Minimal Salary", f"${average_min_salary:,.2f}")
        col4.metric("Average Maximal Salary", f"${average_max_salary:,.2f}")
        style_metric_cards()
        st.markdown("***")

        # ------------------- TOP 10 JOB TITLE WITH THE NUMBER OF JOB POSTINGS -------------------------
        with st.expander("Top 10 Job Title with the Number of Job Postings"):
            col_job, col_info = st.columns([3,2])
            with col_job:
                job_counts = dfJob['title'].value_counts().head(10)
                plt.rc('xtick', labelsize=8)
                plt.rc('ytick', labelsize=8)
                plt.figure(figsize=(8, 4))
                sns.barplot(x=job_counts.index, y=job_counts.values, palette='viridis')
                plt.xlabel('Job Title')
                plt.ylabel('Number of Job')
                plt.xticks(rotation=45, ha='right')
                sns.despine()
                st.pyplot()
            with col_info:
                st.info('Information')
                st.markdown("- 'Sales Director' dominates the number of job openings, followed by 'Sales Associate' and 'Retail Sales Associate.' This indicates that 'City Lifestyle' is a major player in the job market for 2023.")
                st.markdown("- This trend underscores the significance of 'Sales' as a required job in 2023, likely offering a range of job opportunities across various sectors. 'Accountant' and 'Project Manager' also maintain a strong presence in the job market, reflecting their continued importance in the professional landscape during the same period")
                st.markdown('''
                <style>
                [data-testid="stMarkdownContainer"] ul{
                    padding-left: 20px;
                    text-align: justify;
                    font-size: 12px;
                }
                </style>
                ''', unsafe_allow_html=True)

        # ------------------- TOP 10 SKILLS WITH THE NUMBER OF JOB POSTINGS -------------------------
        with st.expander("Top 10 Skills with the Number of Job Postings"):
            col_job, col_info = st.columns([3,2])
            with col_job:
                job_counts = dfJob['skill'].value_counts().head(10)
                plt.rc('xtick', labelsize=8)
                plt.rc('ytick', labelsize=8)
                fig, ax = plt.subplots(figsize=(8, 4))
                sns.barplot(x=job_counts.index, y=job_counts.values, palette='viridis')
                plt.xlabel('Skills')
                plt.ylabel('Number of Job Posting')
                plt.xticks(rotation=45,ha='right')
                sns.despine()
                st.pyplot(fig)
            with col_info:
                st.info('Information')
                st.markdown("- Information Technology dominates as the most frequently appearing skill, followed by Management and Sales. ")
                st.markdown("- This indicates that Information Technology skills are in the highest demand, followed by skills in the fields of Management and Sales. Job seekers with in these areas may find suitable opportunities in the job market.")
                st.markdown('''
                <style>
                [data-testid="stMarkdownContainer"] ul{
                    padding-left: 20px;
                    text-align: justify;
                    font-size: 12px;
                }
                </style>
                ''', unsafe_allow_html=True)

        # ------------------- WORK TYPE DISTRIBUTION -------------------------
        with st.expander("Work Type Distribution"):
            col_job, col_info = st.columns([3,2])
            with col_job:
                work_type_data = dfJob['work_type']
                colours = ['#492c68', '#46507f', '#35947d', '#60b671', '#88c35b', '#b2c83c', '#367282']
                # Calculate percentages
                total = len(work_type_data)
                work_type_counts = work_type_data.value_counts(normalize=True) * 100
                
                # Create labels with both Work Type and Percentage
                plot_labels = [f'{work_type} ({percentage:.2f}%)' for work_type, percentage in work_type_counts.items()]
                circle_plot = circlify.circlify(work_type_counts.tolist(), target_enclosure=circlify.Circle(x=0, y=0))
                circle_plot.reverse()

                # Create a Matplotlib figure with the title
                fig, axs = plt.subplots(figsize=(8, 8))
                lim = max(max(abs(circle.x) + circle.r, abs(circle.y) + circle.r) for circle in circle_plot)
                plt.xlim(-lim, lim)
                plt.ylim(-lim, lim)

                # Display circles and labels
                for circle, colour, label in zip(circle_plot, colours, plot_labels):
                    x, y, r = circle
                    axs.add_patch(plt.Circle((x, y), r, linewidth=1, facecolor=colour, edgecolor='grey'))
                    plt.annotate(label, (x, y), va='center', ha='center', fontweight='bold')

                plt.axis('off')
                st.pyplot()
            with col_info:
                st.info('Information')
                st.markdown("- Full-Time' work type leads in the number of job postings, followed by 'contract' and 'part-time' positions. This suggests a prevailing preference for full-time employment opportunities, with contract and part-time roles also being significant options in the job market for 2023.")
                st.markdown("- This trend highlights the prevalence of 'full-time' positions as the primary choice for job seekers in 2023, likely reflecting a strong demand for stable, full-time employment. Additionally, the availability of 'contract' and 'part-time' roles demonstrates the diversity of work arrangements in the job market, catering to individuals seeking various employment options to fit their lifestyles and career goals.")
                st.markdown('''
                <style>
                [data-testid="stMarkdownContainer"] ul{
                    padding-left: 20px;
                    text-align: justify;
                    font-size: 12px;
                }
                </style>
                ''', unsafe_allow_html=True)

        # ------------------- COMPANY SIZE DISTRIBUTION WITH THE NUMBER OF JOB POSTINGS -------------------------
        with st.expander("Company Size Distribution with the Number of Job Postings"):
            col_job_skill, col_job_info = st.columns([3,2])
            with col_job_skill:
                filtered_df = dfJob[dfJob['company_size'].isin(['-', '0.0']) == False]
                job_counts = filtered_df['company_size'].value_counts()
                labels = job_counts.index
                values = job_counts.values
                plt.figure(figsize=(7,4))
                plt.pie(job_counts, labels=job_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('viridis'), textprops={'fontsize': 10})
                st.pyplot()
            with col_job_info:
                st.info('Information')
                st.markdown("- Companies with a size classification of '7' have the highest number of job postings, followed by those with a size classification of '5' and '2.' This reveals that medium-sized companies, as represented by the '7' classification, are the primary contributors to the job market in 2023, with '5' and '2' classified companies also playing substantial roles in offering employment opportunities")
                st.markdown("- This trend signifies that medium-sized companies (size '7') dominate the job market landscape in 2023, likely offering diverse career prospects. However, companies categorized as '5' and '2' also maintain a significant presence, showcasing a variety of employment options across different company sizes to cater to the preferences and career goals of job seekers.")
                st.markdown('''
                <style>
                [data-testid="stMarkdownContainer"] ul{
                    padding-left: 20px;
                    text-align: justify;
                    font-size: 12px;
                }
                </style>
                ''', unsafe_allow_html=True)

        # ------------------- COUNTRY WITH THE MOST JOB POSTINGS -------------------------
        with st.expander("Country with the Most Job Postings"):
            col_job_skill, col_job_info = st.columns([3,2])
            with col_job_skill:
                filtered_df = dfJob[dfJob['country'].isin(['-', 'OO']) == False]
                job_counts = dfJob['country'].value_counts().head(10)
                plt.figure(figsize=(7,5))
                sns.barplot(x=job_counts.values, y=job_counts.index, palette='viridis', edgecolor=None)
                plt.xlabel('Number of Job Postings')
                plt.ylabel('Country')
                st.pyplot()
            with col_job_info:
                st.info('Information')
                st.markdown("- United States (US) has the largest number of job postings, followed by the United Kingdom (GB). This indicates that the United States and the United Kingdom are the two prominent job markets within this dataset in the year 2023.")
                st.markdown("- United States (US) boasts the largest number of job postings, followed by the United Kingdom (GB). It signifies that the job market in the United States is the most prominent , with the United Kingdom also playing a significant role in terms of job opportunities available in 2023.")
                st.markdown('''
                <style>
                [data-testid="stMarkdownContainer"] ul{
                    padding-left: 20px;
                    text-align: justify;
                    font-size: 12px;
                }
                </style>
                ''', unsafe_allow_html=True)

    with tab_j3:
        # Function to generate Word Cloud
        def generate_wordcloud(text):
            print("Generating Word Cloud for text:", text)
            wordcloud = WordCloud(width=1200, height=300, background_color='white').generate(text)
            plt.figure(figsize=(12, 6))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            st.image(wordcloud.to_image())

        # Streamlit app
        st.header("Word Clouds for Job Descriptions")

        # Choose a company for analysis
        col1, col2 = st.columns([1, 2])
        with col1:
            selected_company = st.selectbox("Select a Company", dfJob['title'].unique())
        with col2:
            st.write('')

        # Filter the dataset for the selected company
        selected_company_data = dfJob[dfJob['title'] == selected_company]
        st.write('')

        # Generate Word Cloud for the description of the selected company
        generate_wordcloud(selected_company_data['description'].iloc[0])

        # Display company details
        st.title('')
        st.subheader(f"Details for {selected_company}")
        st.write(selected_company_data[['title', 'description']])

elif tabs == 'About':
    # section 1
    st.image(r'img/banner1.jpg', use_column_width=True)
    sub_title = '''Project Overview'''
    st.markdown(f"<p style='text-align: center; font-size: 34px; color: #00c9a4; font-weight: 700; margin-top:100px'>{sub_title}</p>", unsafe_allow_html=True)
    desc = '''Our website specializes in comprehensive LinkedIn data analysis and visualization, offering a powerful platform for unlocking valuable insights. With dynamic visualizations, users gain enhanced understanding of professional networks, industry trends, and skill landscapes. The project aims to streamline data exploration, serving as an invaluable tool for harnessing the full potential of LinkedIn data through intuitive and interactive representations.'''
    st.markdown(f"<p style='text-align: center; font-size: 16px; color: #555555; align-item: center; margin-bottom: 150px'>{desc}</p>", unsafe_allow_html=True)

    # section 2
    col1, col2 = st.columns([5,4])
    with col1:
        sub_title = '''How can I Collect the Data?'''
        st.markdown(f"<p style='text-align: justify; font-size: 34px; color: #00c9a4; font-weight: 700'>{sub_title}</p>", unsafe_allow_html=True)
        desc = '''We harness the power of Kaggle, a leading platform for open datasets and data science competitions, to source diverse and high-quality datasets for our website. This ensures our users can confidently perform robust analyses and visualizations on LinkedIn data.'''
        st.markdown(f"<p style='text-align: justify; font-size: 16px; color: #555555; align-item: center; margin: auto'>{desc}</p>", unsafe_allow_html=True)
        st.title('')
        def redirect_button(url: str, text: str = None, color="#00c9a4"):
            m = st.markdown(
                f"""
                <style>
                div.stButton > button:first-child {{
                    background-color: {color};
                    color: white;
                    height: 3em;
                    width: 12em;
                    border-radius: 20px;
                    font-size: 20px;
                    font-weight: 500;
                    display: inline-block;
                    text-decoration: none;
                    border-style: none;
                }}   
                div.stButton > button:hover {{
                    background-color: #2fe3c1;
                    color: white;
                    border: none;
                }}
                div.stButton > button:active {{
                    position: relative;
                    top: 3px;
                    border: none;
                    color: black;
                }}
                </style>
                """
                , unsafe_allow_html=True
            )
            st.markdown(
                f"""
                <a href="{url}" target="_self">
                    <div class="stButton">
                        <button>{text}</button>
                    </div>
                </a>
                """
                , unsafe_allow_html=True
            )
        redirect_button("https://www.kaggle.com/datasets/arshkon/linkedin-job-postings/data", "Go to Kaggle")

    with col2:
        st_lottie("https://lottie.host/f10df395-fcfa-45d5-a917-85ccf6be3c0e/iBSlzFGPKP.json")
    
    #section 3
    st.markdown("<hr style='border: 1px solid #cccccc; margin-top: 100px'>", unsafe_allow_html=True)
    sub_title = '''THANK YOU!'''
    st.markdown(f"<p style='text-align: center; font-size: 60px; color: #00c9a4; font-weight: 700; letter-spacing: 2px'>{sub_title}</p>", unsafe_allow_html=True)
    desc1 = '''Created by'''
    desc2= '''Mufti Syafi'atun Nafiah || Information Technology, Universitas Negeri Yogyakarta'''
    st.markdown(f"<p style='text-align: center; font-size: 18px; color: #555555; width: 1000px; align-item: center; margin: auto'>{desc1}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 18px; color: #555555; width: 1000px; align-item: center; margin: auto'>{desc2}</p>", unsafe_allow_html=True)
    social_media_links = """
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            <a href="https://www.linkedin.com/in/muftinafiah/" style="text-decoration: none; color: inherit; margin: 0 15px;">LinkedIn</a>
            <a href="https://www.instagram.com/muftisan_" style="text-decoration: none; color: inherit; margin: 0 15px;">Instagram</a>
            <a href="https://www.behance.net/muftinafiah" style="text-decoration: none; color: inherit; margin: 0 15px;">Behance</a>
        </div>
    """
    st.markdown(social_media_links, unsafe_allow_html=True)