import streamlit as st

st.title("Echo Chatbot")

#initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

#Display all messages 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#Chat input
user_input = st.chat_input("Type a message...")

if user_input:
    # add user message to history
    st.session_state.messages.append({
        "role": "user", 
        "content": user_input
    })

    #create echo response
    echo_response = f"You said: {user_input}"

    #Add bot response to history
    st.session_state.messages.append({
        "role": "assistant", 
        "content": echo_response
    })   

    # Rerun to show new messages
    st.rerun()


