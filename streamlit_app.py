import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

st.set_page_config(page_title="HugChat - An LLM-powered Streamlit app")

import streamlit as st

# Apply custom styles
st.markdown(
    """
    <style>
        .sidebar {
            background-color: #f9f3eb;
            box-shadow: 0px 2px 6px 0px rgba(0, 0, 0, 0.15);
            border-radius: 5px;
            padding: 20px;
        }

        .sidebar .sidebar-title {
            font-size: 28px;
            font-weight: bold;
            color: #982649;
            margin-bottom: 20px;
        }

        .sidebar .sidebar-about {
            font-size: 18px;
            color: #666666;
            margin-bottom: 20px;
            line-height: 1.6;
        }

        .sidebar .sidebar-link {
            font-size: 16px;
            color: #9e6c4b;
            margin-top: 10px;
        }
    </style>
    """
    , unsafe_allow_html=True
)

# Create a sidebar using Bootstrap components
with st.sidebar:
    st.markdown('<div class="sidebar">', unsafe_allow_html=True)
    st.markdown('<h1 class="sidebar-title">🤗💬 HugChat App</h1>', unsafe_allow_html=True)
    st.markdown(
        """
        <p class="sidebar-about">Welcome to the fancy world of HugChat!</p>
        <p class="sidebar-about">This app is powered by the cutting-edge LLM (Language Model) technology and features a delightful chatbot experience.</p>
        <p class="sidebar-about">Here are the amazing technologies we've used to build this app:</p>
        <ul class="sidebar-about">
            <li>Streamlit</li>
            <li>HugChat</li>
            <li>OpenAssistant/oasst-sft-6-llama-30b-xor LLM model</li>
        </ul>
        <p class="sidebar-about">And the best part? No API key required! Just start chatting and let the magic unfold. ✨</p>
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
