import streamlit as st
import pandas as pd
from utils.openai_utils import get_openai_response

# App Title
st.title("Unlock Your Startup Potential")

# Foldable section 1: Gifting Text
with st.expander("A Special Gift Just for You"):
    st.markdown(
        """
        **Хеллоу Даша,**

        What if I told you that everything you’ve been struggling with around coding—designing fancy UIs, battling with deployment, feeling stuck—is all a complete waste of your time? Seriously, forget it. You don’t need any of that to launch your next big thing.
        
        **Here’s the ugly truth:** most people are breaking their backs learning skills they don’t need, and it’s keeping them stuck. But you’re about to bypass all of that.
        
        I’m giving you a gift that will allow you to create killer apps and launch them without ever touching a line of frontend code or figuring out deployment. How? Because this tool I’ve built for you does it all—effortlessly.

        **Here’s why this matters:** Every minute you spend struggling with UI design or deployment is a minute you’re not spending on your genius. It’s time to unleash your true potential, using just the skills you already have.

        **This isn’t just another tool**—it’s a revolution. You’re about to step into a world where you get to focus on what you do best (writing Python), and let everything else fall into place. No more tutorials, no more dead ends. Just pure, unfiltered creation.

        **This is your unfair advantage**—a way to shortcut your way to startup success without the usual headaches. So, are you ready to dominate and have a blast doing it? Let’s make those ideas reality.

        Happy birthday, sister. This is probably the most nerdy gift you have ever received.
          """
    )

# Foldable section 2: Getting Started Guide
with st.expander("Getting Started Guide"):
    st.markdown(
        """
        **Welcome to the future of app development, where your Python skills are the star of the show!**
        Here's the deal: building apps usually means dealing with a lot of stuff you don't care about—like designing user interfaces 
        and figuring out how to deploy your app to the web. But why bother with all that when you can just focus on writing awesome Python code?
        
        \nThis app (not just one) is designed to let you do exactly that. It's simple:
        
        \n1. **Setup dev environment in 1 click**: Go to your github repo https://github.com/salmad/maduar. Click on \"Code\" and got to "Code spaces". 
        And hit plus. You will be able to see and edit code in familiar VS Code editor.
        Make sure Dr. Mad invited you to all necessary projects on github. If you are reading this most likely your ```maduardar``` github account was invited.
        I found that you can use github's code spaces to code/test without having to download code locally.
        
        \n2. **Setup prod environment**: you will have railway.app access which is used for your deployment. But i hope you will rarely use it.
        You can use the domain, deployment services and OpenAI API for as long as you need (API pass word will be sent to your email in the form of .env file. Put it in your repo to execute code locally).

        \n3. **How to run apps**: 
        First install all packages using terminal: ```pip install -r requirements.txt```.
        Next I created apps for you.
            \n    3.1. One is **Streamlit** app can be run by typing the following command in terminal of the main folder: ```streamlit run streamlit_app.py```. Use streamlit for things like jupyter notebook, where your charts etc. will be deployed. Once you launch the command you will get an option to open the app in browser. This is not all, I created another app for you.
            \n    3.2. Another one is for **custom or traditional API request**. Look at file called fastapi_app.py.
            To run it, type ```python fastapi_app.py``` in your comand line and you can open another app in browser. Special bonus 🎁🤩🤑 is if you type "/landing_page" you will get a landing page. Change the text and it is yours.

        \n4. **Write Your Python Code**: For that you have a document like this (streamlit_app.py) and another file (fastapi_app.py) with pre-built template.
        To get how fast api works launch the local website with ```/docs``` or ```/redoc```. Documentation for your APIs will apear automatically as you write them.

        \n5. **Push to GitHub, Deploy Instantly**: Want to share your creation with the world? Just push your code to GitHub, 
        and boom—it’s deployed. All in VS code editor. No servers, no headaches.  

        \n Ok, that's it.

        \nThis is the fastest, easiest way to turn your ideas into reality. Build that app, launch that startup, 
        or just have a blast playing around with your own creations. And remember, the only limit is your imagination—so dream big and code with confidence!
        """
    )

# Footer
st.markdown("---")
st.markdown("**Get started now and turn your Python skills into something extraordinary!**")


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
                                   "Competitor Research", "Killer open ai functionality"])

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
    # st.header("Examples")
    st.write("### Killer example: chatgpt")
    st.write("i used markdown formatting for the previous")
    with st.form("openai_form"):
        st.write("Talk to chat gpt here")
        user_message = st.text_input('Type here')
        # what_user_said = st.chat_input('Say something to chat gpt')

        # Every form must have a submit button.
        submitted = st.form_submit_button("ask ai")


        if submitted:
            system_prompt= 'be very funny through saying stupid things. fun is what love. soviet union is proud of you'
            response = get_openai_response(system_prompt=system_prompt,user_prompt=user_message)
            st.write(response)
    