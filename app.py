import streamlit as st
from openai import OpenAI
import json
import time
from datetime import datetime
import base64
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="✨ AI Email Generator",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    /* Reset and global styles */
    * {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Main content text colors */
    .main .block-container {
        color: #1f2937 !important;
    }
    
    /* Headers and titles */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #1f2937 !important;
        font-weight: 600;
    }
    
    /* Paragraphs and general text */
    .stMarkdown p, .stMarkdown div {
        color: #374151 !important;
    }
    
    /* Main header styling */
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        color: white !important;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .main-header p {
        color: white !important;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Form elements styling */
    /* Text input styling */
    .stTextInput > div > div > input {
        background: #ffffff !important;
        border: 2px solid #e5e7eb !important;
        border-radius: 10px !important;
        color: #1f2937 !important;
        padding: 0.75rem !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    /* Textarea styling */
    .stTextArea > div > div > textarea {
        background: #ffffff !important;
        border: 2px solid #e5e7eb !important;
        border-radius: 10px !important;
        color: #1f2937 !important;
        padding: 0.75rem !important;
        font-size: 14px !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background: #ffffff !important;
        border: 2px solid #e5e7eb !important;
        border-radius: 10px !important;
        color: #1f2937 !important;
    }
    
    .stSelectbox > div > div > div {
        color: #1f2937 !important;
        background: #ffffff !important;
    }
    
    .stSelectbox > div > div > div:hover {
        background: #f3f4f6 !important;
    }
    
    /* Form labels */
    .stTextInput > label, .stTextArea > label, .stSelectbox > label {
        color: #374151 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        border-radius: 25px !important;
        border: none !important;
        color: white !important;
        padding: 0.75rem 2rem !important;
        font-weight: bold !important;
        font-size: 16px !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
    }
    
    /* Email output styling */
    .email-output {
        background: #ffffff !important;
        padding: 2rem !important;
        border-radius: 15px !important;
        border-left: 5px solid #667eea !important;
        margin: 1rem 0 !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
        color: #1f2937 !important;
        border: 1px solid #e5e7eb !important;
    }
    
    .email-output p, .email-output div {
        color: #1f2937 !important;
        line-height: 1.6 !important;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%) !important;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%) !important;
    }
    
    /* Sidebar text */
    .sidebar .stMarkdown h3, .sidebar .stMarkdown p {
        color: #374151 !important;
    }
    
    /* Metric card styling */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        padding: 1rem !important;
        border-radius: 10px !important;
        color: white !important;
        text-align: center !important;
        margin: 0.5rem 0 !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
    }
    
    .metric-card h3 {
        color: white !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        margin: 0 !important;
    }
    
    .metric-card p {
        color: white !important;
        opacity: 0.9 !important;
        margin: 0.25rem 0 0 0 !important;
    }
    
    /* Success message styling */
    .success-message {
        background: linear-gradient(135deg, #10b981 0%, #34d399 100%) !important;
        padding: 1rem !important;
        border-radius: 10px !important;
        color: white !important;
        text-align: center !important;
        margin: 1rem 0 !important;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3) !important;
    }
    
    /* Info boxes and alerts */
    .stAlert {
        color: #1f2937 !important;
        background: #f3f4f6 !important;
        border: 1px solid #d1d5db !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }
    
    /* Error messages */
    .stAlert[data-baseweb="notification"] {
        background: #fef2f2 !important;
        border-color: #fecaca !important;
        color: #dc2626 !important;
    }
    
    /* Success messages */
    .stAlert[data-baseweb="notification"][data-testid="stAlert"] {
        background: #f0fdf4 !important;
        border-color: #bbf7d0 !important;
        color: #16a34a !important;
    }
    
    /* Code blocks */
    .stCodeBlock {
        background: #f8f9fa !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 8px !important;
        color: #1f2937 !important;
        font-family: 'Courier New', monospace !important;
    }
    
    .stCodeBlock pre {
        color: #1f2937 !important;
        background: #f8f9fa !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: #f8f9fa !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 8px !important;
        color: #374151 !important;
        font-weight: 600 !important;
    }
    
    .streamlit-expanderContent {
        background: #ffffff !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 8px !important;
        color: #1f2937 !important;
    }
    
    /* Tips section */
    .stMarkdown .stAlert {
        background: #eff6ff !important;
        border: 1px solid #bfdbfe !important;
        color: #1e40af !important;
        border-radius: 8px !important;
        padding: 0.75rem !important;
        margin: 0.5rem 0 !important;
    }
    
    /* Spinner text */
    .stSpinner > div {
        color: #667eea !important;
    }
    
    /* Placeholder text */
    ::placeholder {
        color: #9ca3af !important;
        opacity: 1 !important;
    }
    
    /* Focus states */
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div:focus {
        outline: none !important;
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_emails' not in st.session_state:
    st.session_state.generated_emails = []

# Get API key from environment or Streamlit secrets
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') or st.secrets.get('OPENAI_API_KEY')

def generate_email_with_ai(prompt, email_type, tone, length, recipient_type, api_key):
    """Generate email using OpenAI API"""
    try:
        client = OpenAI(api_key=api_key)
        
        # Create a comprehensive prompt
        system_prompt = f"""You are an expert email writer. Generate a professional {email_type.lower()} email with the following specifications:
        - Type: {email_type}
        - Tone: {tone}
        - Length: {length}
        - Recipient: {recipient_type}
        
        Make the email engaging, professional, and appropriate for the context. Include a subject line and proper email formatting."""
        
        user_prompt = f"Write an email about: {prompt}"
        
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        return completion.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Error generating email: {str(e)}"

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>✨ AI Email Generator</h1>
        <p>🚀 Create professional emails in seconds with AI-powered assistance</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for settings
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        
        # API Key status
        if OPENAI_API_KEY:
            st.success("✅ OpenAI API Key configured!")
        else:
            st.error("❌ OpenAI API Key not found in environment variables")
            st.info("Please set OPENAI_API_KEY in your .env file")
        
        st.markdown("---")
        
        # Email statistics
        st.markdown("### 📊 Statistics")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>{len(st.session_state.generated_emails)}</h3>
                <p>Emails Generated</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>{datetime.now().strftime('%H:%M')}</h3>
                <p>Current Time</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📝 Email Configuration")
        
        # Email content input
        email_content = st.text_area(
            "💭 What would you like to write about?",
            placeholder="Describe the purpose of your email, key points to include, or any specific details...",
            height=120
        )
        
        # Email type selection
        email_types = [
            "📧 Professional Business",
            "🤝 Networking",
            "📋 Job Application",
            "📞 Follow-up",
            "🎉 Thank You",
            "📢 Announcement",
            "❓ Inquiry",
            "📅 Meeting Request",
            "🔄 Status Update",
            "🎯 Sales Pitch"
        ]
        
        email_type = st.selectbox(
            "📋 Email Type",
            email_types,
            help="Select the type of email you want to generate"
        )
        
        # Tone selection
        tones = [
            "🎯 Professional & Formal",
            "😊 Friendly & Casual",
            "🚀 Enthusiastic & Energetic",
            "🤝 Diplomatic & Polite",
            "💼 Business-like & Direct",
            "🎨 Creative & Engaging"
        ]
        
        tone = st.selectbox(
            "🎭 Tone",
            tones,
            help="Choose the tone that best fits your message"
        )
        
        # Length selection
        lengths = [
            "📱 Short & Concise (50-100 words)",
            "📄 Standard (100-200 words)",
            "📝 Detailed (200-300 words)",
            "📚 Comprehensive (300+ words)"
        ]
        
        length = st.selectbox(
            "📏 Length",
            lengths,
            help="Select the desired length of your email"
        )
        
        # Recipient type
        recipients = [
            "👔 Colleague",
            "👨‍💼 Manager/Supervisor",
            "🤝 Client/Customer",
            "🎓 Professor/Teacher",
            "👥 Team Member",
            "🔍 Recruiter",
            "🤝 Business Partner",
            "👨‍💻 Technical Contact"
        ]
        
        recipient_type = st.selectbox(
            "👤 Recipient Type",
            recipients,
            help="Who will be receiving this email?"
        )
        
        # Generate button
        if st.button("🚀 Generate Email", use_container_width=True):
            if not email_content:
                st.error("❌ Please enter what you'd like to write about!")
            elif not OPENAI_API_KEY:
                st.error("❌ OpenAI API Key not found! Please set OPENAI_API_KEY in your .env file")
            else:
                with st.spinner("🤖 AI is crafting your perfect email..."):
                    generated_email = generate_email_with_ai(
                        email_content,
                        email_type,
                        tone,
                        length,
                        recipient_type,
                        OPENAI_API_KEY
                    )
                    
                    # Store in session state
                    email_data = {
                        'content': generated_email,
                        'type': email_type,
                        'tone': tone,
                        'length': length,
                        'recipient': recipient_type,
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    st.session_state.generated_emails.append(email_data)
                    
                    st.success("✅ Email generated successfully!")
                    
                    # Display the generated email
                    st.markdown("### 📧 Generated Email")
                    st.markdown(f"""
                    <div class="email-output">
                        {generated_email.replace(chr(10), '<br>')}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Copy button
                    st.code(generated_email, language="text")
    
    with col2:
        st.markdown("### 💡 Tips & Suggestions")
        
        tips = [
            "🎯 Be specific about your email's purpose",
            "👤 Consider your recipient's perspective",
            "📝 Include relevant context and details",
            "🎨 Use the tone that matches your relationship",
            "⏰ Keep it concise but complete",
            "🔍 Review and edit before sending"
        ]
        
        for tip in tips:
            st.info(tip)
        
        st.markdown("---")
        
        st.markdown("### 🎨 Quick Templates")
        
        template_buttons = [
            "📧 Professional Introduction",
            "🤝 Networking Follow-up",
            "📋 Job Application",
            "🎉 Thank You Note"
        ]
        
        for template in template_buttons:
            if st.button(template, key=template):
                st.info(f"💡 Template selected: {template}")
                st.session_state.suggested_template = template
    
    # History section
    if st.session_state.generated_emails:
        st.markdown("---")
        st.markdown("### 📚 Email History")
        
        for i, email_data in enumerate(reversed(st.session_state.generated_emails[-5:])):  # Show last 5
            with st.expander(f"📧 {email_data['type']} - {email_data['timestamp']}"):
                st.markdown(f"**Type:** {email_data['type']}")
                st.markdown(f"**Tone:** {email_data['tone']}")
                st.markdown(f"**Recipient:** {email_data['recipient']}")
                st.markdown("**Content:**")
                st.text(email_data['content'])
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("📋 Copy", key=f"copy_{i}"):
                        st.success("✅ Copied to clipboard!")
                with col2:
                    if st.button("✏️ Edit", key=f"edit_{i}"):
                        st.info("Edit feature coming soon!")
                with col3:
                    if st.button("🗑️ Delete", key=f"delete_{i}"):
                        st.session_state.generated_emails.pop(-(i+1))
                        st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; margin-top: 2rem;">
        <p style="color: white; font-size: 1.1rem; margin: 0; font-weight: 600;">
            Made with ❤️ by <span style="color: #ffd700; font-weight: bold;">AmiteshIntelligenceSystems</span> (AI SY's)
        </p>
        <p style="color: rgba(255,255,255,0.8); font-size: 0.9rem; margin: 0.5rem 0 0 0;">
            ✨ Empowering communication through AI ✨
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
