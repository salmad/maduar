import streamlit as st
import pandas as pd
from utils.openai_utils import get_openai_response

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

st.title("🎈 Darin Maduar app")

st.write('I will give some examples to get you started, more here [docs.streamlit.io](https://docs.streamlit.io/)')
st.write('btw the app is deployed to darin.maduar.org')


st.divider()

st.title("The app has 4 Tabs")



# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["Simple Examples" ,"Keyword Research",
                                   "Competitor Research", "Text formatting"])

st.divider()

with tab1:
    

    # example of making an input
    parameter = st.text_input("input something and it will save it into variable")
    some_list = [f'{i}_{parameter}' for i in range(4)]

    st.bar_chart(data=pd.DataFrame({'data':range(4),'parameter_name':some_list}), x='parameter_name',y='data')


    st.write('other input objects')
    options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
    )

    st.write("You selected:", options)



with tab2:
    st.header("Keyword Research")
    seed_keyword = st.text_input("Enter a seed keyword:")
    if st.button("Submit", key='keyword_submit'):
        if seed_keyword:
            # Generate and display the table
            df = generate_dummy_data(seed_keyword)
            st.dataframe(df)
            st.text("table can be sorted, searched and downloaded")
        else:
            st.warning("Please enter a keyword")

with tab3:
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

with tab4:
    st.header("Examples")
    # header examples
    st.title("examples")
    st.write("# examples 2")
    st.write("## examples 3")
    st.write("### examples 4")





# st.button(label='Play with openai')
# st.write('I will use some openai functionality here')

# what_user_said = st.chat_input('Say something to chat gpt')


# system_prompt= 'be very funny through saying stupid things. fun is what love. soviet union is proud of you'
# response = get_openai_response(what_user_said)

# st.write(response)


