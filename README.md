# ✨ AI Email Generator

A modern and stylish Streamlit application that generates professional emails using AI. Create compelling emails in seconds with customizable options for type, tone, length, and recipient.

## 🚀 Features

- **🤖 AI-Powered Generation**: Uses OpenAI's GPT-4o for intelligent email creation
- **🎨 Modern UI**: Beautiful gradient design with emojis and modern styling
- **📋 Multiple Email Types**: Professional business, networking, job applications, and more
- **🎭 Customizable Tone**: Choose from professional, friendly, enthusiastic, and other tones
- **📏 Length Options**: Short, standard, detailed, or comprehensive emails
- **👤 Recipient Targeting**: Optimized for different recipient types
- **📚 Email History**: Save and manage your generated emails
- **💡 Smart Tips**: Built-in suggestions for better email writing
- **📊 Statistics**: Track your email generation activity

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd email-generator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables**:
   - Create a `.env` file in the project root
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`
   - Get your API key from [OpenAI Platform](https://platform.openai.com/)
   - Keep your API key secure and never share it publicly

   Example `.env` file:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

## 🚀 Usage

### **Local Development**

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**:
   - The app will open at `http://localhost:8501`

3. **Generate Emails**:
   - Describe what you want to write about
   - Select email type, tone, length, and recipient
   - Click "Generate Email" to create your AI-powered email

### **Deploy to Streamlit Cloud**

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and set main file to `app.py`
   - Click "Deploy"

3. **Configure Secrets**:
   - In your app settings, go to "Secrets"
   - Add your OpenAI API key:
   ```toml
   OPENAI_API_KEY = "sk-your-actual-api-key-here"
   ```

4. **Your app will be live** at: `https://your-app-name.streamlit.app`

## 📧 Email Types Available

- 📧 Professional Business
- 🤝 Networking
- 📋 Job Application
- 📞 Follow-up
- 🎉 Thank You
- 📢 Announcement
- ❓ Inquiry
- 📅 Meeting Request
- 🔄 Status Update
- 🎯 Sales Pitch

## 🎭 Tone Options

- 🎯 Professional & Formal
- 😊 Friendly & Casual
- 🚀 Enthusiastic & Energetic
- 🤝 Diplomatic & Polite
- 💼 Business-like & Direct
- 🎨 Creative & Engaging

## 📏 Length Options

- 📱 Short & Concise (50-100 words)
- 📄 Standard (100-200 words)
- 📝 Detailed (200-300 words)
- 📚 Comprehensive (300+ words)

## 👤 Recipient Types

- 👔 Colleague
- 👨‍💼 Manager/Supervisor
- 🤝 Client/Customer
- 🎓 Professor/Teacher
- 👥 Team Member
- 🔍 Recruiter
- 🤝 Business Partner
- 👨‍💻 Technical Contact

## 💡 Tips for Better Emails

- 🎯 Be specific about your email's purpose
- 👤 Consider your recipient's perspective
- 📝 Include relevant context and details
- 🎨 Use the tone that matches your relationship
- ⏰ Keep it concise but complete
- 🔍 Review and edit before sending

## 🔧 Customization

The application uses custom CSS for modern styling. You can modify the appearance by editing the CSS section in `app.py`.

## 📊 Features

- **Real-time Statistics**: Track emails generated and current time
- **Email History**: View, copy, and manage previously generated emails
- **Quick Templates**: Pre-defined templates for common email types
- **Responsive Design**: Works on desktop and mobile devices
- **Session Management**: Emails persist during your session

## 🔒 Security

- API keys are loaded from environment variables (not stored in the app)
- No data is transmitted to external servers except OpenAI API calls
- All communication with OpenAI is encrypted
- The `.env` file is excluded from version control

## 🐛 Troubleshooting

**Common Issues:**

1. **API Key Error**: Make sure you have a valid OpenAI API key with sufficient credits
2. **Environment Variable Not Found**: Ensure your `.env` file is in the project root and contains `OPENAI_API_KEY=your_key`
3. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
4. **Streamlit Not Found**: Install Streamlit with `pip install streamlit`

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions, please open an issue on the repository.

---

**Happy Email Writing! ✨📧** 