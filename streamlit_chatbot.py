import streamlit as st
import anthropic
from anthropic import Anthropic
# Get API key from Streamlit secrets (for deployment) or config (for local)
try:
    ANTHROPIC_API_KEY = st.secrets["ANTHROPIC_API_KEY"]
except:
    from config import ANTHROPIC_API_KEY

# Initialize session state early
if "messages" not in st.session_state:
    st.session_state.messages = []

if "model" not in st.session_state:
    st.session_state.model = "claude-sonnet-4-20250514"

if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = "You are a helpful AI Assistant."

if "temperature" not in st.session_state:
    st.session_state.temperature = 0.7

# Page configuration
st.set_page_config(page_title="Claude Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Claude Chatbot")
st.caption("Powered by Claude Sonnet 4")

#Welcome message
if len(st.session_state.messages) == 0:
    with st.chat_message("assistant"):
        st.write("""
        ■ Hello! I'm Claude, an AI assistant created by Anthropic.
        I can help you with:
        - Answering questions
        - Writing and editing
        - Analysis and research
        - Coding and debugging
        - Creative projects
        Just type your message below to get started!
        """)

# Sidebar with controls
with st.sidebar:
    st.header("Controls")
    if st.button("Clear Conversation", type="primary"):
        st.session_state.messages = []
        st.rerun()

    # Export conversation
    if len(st.session_state.messages) > 0:
        # Create text version of conversation
        conversation_text = ""
        for msg in st.session_state.messages:
            role = "You" if msg["role"] == "user" else "Claude"
            conversation_text += f"{role}: {msg['content']}\n\n"
        st.download_button(
            label="Export Conversation",
            data=conversation_text,
            file_name="chat_history.txt",
            mime="text/plain"
        )

    st.divider()

    # System prompt
    st.subheader("System Prompt")
    system_prompt = st.text_area(
        "Set Claude's behavior:",
        value="You are a helpful AI Assistant.",
        height=100,
        help="This tells Claude how to behave"
    )
    st.session_state.system_prompt = system_prompt

    st.divider()

    # Model selection
    st.subheader("Model Settings")
    model = st.selectbox(
        "Choose Claude model:",
        [
            "claude-sonnet-4-20250514",
            "claude-opus-4-1-20250805",
            "claude-opus-3-sonnet-20250729"
        ],
        help="Different models have different capabilities and costs"
    )
    st.session_state.model = model

    # Temperature control
    temperature = st.slider(
        "Temperature (creativity):",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Lower = more focused, Higher = more creative"
    )
    st.session_state.temperature = temperature

    st.divider()

    with st.expander("Tips"):
        st.write("""
            **Getting Better Responses:**
            - Be specific in your questions
            - Provide context when needed
            - Ask follow-up questions
            
            **System Prompt Examples:**
            - "You are a Python tutor"
            - "You are a creative writer"
            - "You are a business analyst"
            
            **Temperature Guide:**
            - 0.0-0.3: Focused, consistent
            - 0.4-0.7: Balanced (default)
            - 0.8-1.0: Creative, varied
        """)

st.divider()

st.subheader("About")
st.write("This chatbot uses Claude Sonnet 4.")
st.write(f"Messages: {len(st.session_state.messages)}")

# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Get Claude's response
    with st.chat_message("assistant"):
        try:
            with st.spinner("Claude is thinking..."):
                # Create Anthropic client
                client = Anthropic(api_key=ANTHROPIC_API_KEY)
                
                # Call Claude API
                response = client.messages.create(
                    model=st.session_state.model,
                    max_tokens=1000,
                    temperature=st.session_state.temperature,
                    system=st.session_state.system_prompt,
                    messages=st.session_state.messages
                )

                # Extract response text
                claude_response = response.content[0].text

                # Display response
                st.write(claude_response)

        except anthropic.APIConnectionError as e:
            st.error("Could not connect to Claude. Check your internet connection.")
            st.session_state.messages.pop() # Remove failed message
            st.stop()
        
        except anthropic.RateLimitError as e:
            st.error("Rate limit reached. Please wait a moment and try again.")
            st.session_state.messages.pop()
            st.stop()
        
        except anthropic.APIStatusError as e:
            st.error(f"API error: {e.status_code} - {e.message}")
            st.session_state.messages.pop()
            st.stop()
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")
            st.session_state.messages.pop()
            st.stop()
        
        # Add assistant response to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": claude_response
        })

        # Rerun to update
        st.rerun()
        st.rerun()
