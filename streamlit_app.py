import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

st.set_page_config(page_title="HugChat - An LLM-powered Streamlit app")
import streamlit as st

# Apply Material theme styles
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #fafafa;
            box-shadow: rgba(0, 0, 0, 0.15) 0px 0px 2px 0px;
            border-radius: 5px;
            padding: 20px;
        }

        .sidebar .sidebar-content .sidebar-title {
            font-size: 24px;
            color: #e91e63;
            margin-bottom: 20px;
        }

        .sidebar .sidebar-content .sidebar-about {
            font-size: 16px;
            color: #333333;
            margin-bottom: 20px;
        }

        .sidebar .sidebar-content .sidebar-link {
            font-size: 14px;
            color: #2196f3;
            margin-top: 10px;
        }
    </style>
    """
    , unsafe_allow_html=True
)

with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-title">🤗💬 HugChat App</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <p class="sidebar-about"><b>About</b></p>
        <p class="sidebar-about">This app is an LLM-powered chatbot built using:</p>
        <ul class="sidebar-about">
            <li>Streamlit</li>
            <li>HugChat</li>
            <li>OpenAssistant/oasst-sft-6-llama-30b-xor LLM model</li>
        </ul>
        <p class="sidebar-about">💡 Note: No API key required!</p>
        """
        , unsafe_allow_html=True
    )
    st.markdown('<p class="sidebar-link">Made with ❤️ by <a href="https://linkedin.com/in/deepak-kn" target="_blank">Deepak</a></p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)



# Generate empty lists for generated and past.
## generated stores AI generated responses
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm HugChat, How may I help you?"]
## past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']
# Layout of input/response containers
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text
## Applying the user input box
with input_container:
    user_input = get_text()

# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chatbot = hugchat.ChatBot()
    response = chatbot.chat(prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
