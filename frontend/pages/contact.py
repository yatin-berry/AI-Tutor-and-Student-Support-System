import streamlit as st
import time

def main():
    st.markdown("""
        <style>
        .contact-header {
            text-align: center;
            margin-top: 2rem;
            margin-bottom: 1rem;
            animation: fadeIn 0.8s ease-out;
        }
        .contact-header h1 {
            font-size: 3rem !important;
            background: linear-gradient(135deg, #a8c0ff 0%, #3f2b96 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800 !important;
        }
        .contact-header p {
            color: #94a3b8;
            font-size: 1.1rem;
        }
        </style>
        
        <div class="contact-header">
            <h1>Get in Touch</h1>
            <p>We'd love to hear your feedback or answer any questions.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='main-spacer'></div>", unsafe_allow_html=True)
    
    with st.container():
        _, col_center, _ = st.columns([1, 2, 1])
        
        with col_center:
            # We use a standard Streamlit form to let them submit
            with st.form("contact_form", clear_on_submit=True):
                st.markdown("### 📬 Send us a Message")
                name = st.text_input("Name", placeholder="John Doe")
                email = st.text_input("Email", placeholder="john@example.com")
                subject = st.selectbox("Topic", ["General Inquiry", "Feature Request", "Bug Report", "Other"])
                message = st.text_area("Your Message", placeholder="Type your message here...", height=150)
                
                submitted = st.form_submit_button("Send Message", type="primary", use_container_width=True)
                
                if submitted:
                    if not email or not message:
                        st.error("⚠️ Please provide at least an email and a message.")
                    else:
                        with st.spinner("Sending..."):
                            time.sleep(1.5) # Simulate network delay
                        st.success("✅ Thank you! Your message has been sent successfully.")
                        st.balloons()
