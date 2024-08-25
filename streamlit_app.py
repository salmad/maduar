import streamlit as st
import pandas as pd

# Function to generate dummy data for demonstration
def generate_dummy_data(keyword):
    '''
    this is for dummy data
    '''
    return pd.DataFrame({
        'Keyword': [keyword + ' 1', keyword + ' 2', keyword + ' 3'],
        'CPC': [1.5, 2.0, 2.5],
        'Search Volume': [1000, 1500, 2000]
    })

def generate_competitor_data(keywords):
    '''
    this is for dummy data
    '''
    return pd.DataFrame({
        'Competitor': [keyword + ' Competitor' for keyword in keywords],
        'Ranking': (range(0,len(keywords))),
        'Other Parameter': [f'{i}_param' for i in range(0,len(keywords))]
    })

st.title("examples")
st.write("# examples 2")
st.write("## examples 3")
st.write("### examples 4")


parameter = st.text_input("input field to save into variable")
some_list = [f'{i}_{parameter}' for i in range(4)]

st.bar_chart(data=pd.DataFrame({'data':range(4),'parameter_name':some_list}), x='parameter_name',y='data')


st.divider()

st.title("Streamlit App with Two Tabs")



# Create tabs
tab1, tab2 = st.tabs(["Keyword Research", "Competitor Research"])

st.divider()

with tab1:
    st.header("Keyword Research")
    seed_keyword = st.text_input("Enter a seed keyword:")
    if st.button("Submit", key='keyword_submit'):
        if seed_keyword:
            # Generate and display the table
            df = generate_dummy_data(seed_keyword)
            st.dataframe(df)
        else:
            st.warning("Please enter a keyword")

with tab2:
    st.header("Competitor Research")
    keywords_input = st.text_area("Enter keywords separated by commas:")
    if st.button("Submit", key='competitor_submit'):
        keywords = [keyword.strip() for keyword in keywords_input.split(',') if keyword.strip()]
        if keywords:
            # Generate and display the table
            df = generate_competitor_data(keywords)
            st.dataframe(df)
        else:
            st.warning("Please enter at least one keyword")



st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
