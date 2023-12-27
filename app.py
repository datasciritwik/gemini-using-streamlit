import streamlit as st
import gemini


option = st.sidebar.radio('', ("Tutorial", "Ask Anything"))

if option == "Ask Anything":

    # Streamlit UI
    st.title("Gemini AI")

    # Enter your api key
    api_key = st.text_input("Enter the API Key")

    # User input for prompt
    user_prompt = st.text_area("Enter your prompt here:", height=10)

    # Button to generate response
    if st.button("Generate Response"):
        
        if user_prompt:
            with st.spinner("Generating response..."):
                response = gemini.genetrate(user_prompt, api_key)
            # st.write("AI Response:")
            st.markdown(response)
        else:
            st.warning("Please enter a prompt.")


elif option == "Tutorial":
    st.title('Steps for Creating API')

    # Step I
    st.markdown('- Visit this path **[click](https://makersuite.google.com/app/apikey)**')

    # Step II
    st.markdown('- Click on "Click API key on new project"')

    # Step III
    st.markdown('- Copy and paste API key press ENTER')




# step I    --> Visit this path [page url]
# step II   --> Click on "Click API key on new project"
# step III  --> Copy and paste API ENTER
