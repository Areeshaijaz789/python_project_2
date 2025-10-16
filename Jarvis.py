import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel
from openai import OpenAI

# 🔑 Replace with your actual OpenAI API key
OPENAI_API_KEY = "sk-..."  

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

class JarvisApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Jarvis - Coding Assistant")
        self.layout = QVBoxLayout()

        # 🧠 Chat display area
        self.chat_log = QTextEdit()
        self.chat_log.setReadOnly(True)

        # ✏️ Input field
        self.input = QLineEdit()
        self.input.setPlaceholderText("Ask me anything...")

        # 🚀 Button to send messages
        self.send_button = QPushButton("Ask Jarvis")

        # 🕐 Status label
        self.status = QLabel("")

        # Add widgets to layout
        self.layout.addWidget(self.chat_log)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.send_button)
        self.layout.addWidget(self.status)
        self.setLayout(self.layout)

        # Connect actions
        self.send_button.clicked.connect(self.send_message)
        self.input.returnPressed.connect(self.send_message)

        # 💅 Styling
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-family: Segoe UI;
                font-size: 14px;
            }
            QTextEdit {
                background-color: #2d2d2d;
                border: 1px solid #3c3c3c;
                border-radius: 8px;
                padding: 8px;
            }
            QLineEdit {
                background-color: #2d2d2d;
                border: 1px solid #3c3c3c;
                border-radius: 6px;
                padding: 8px;
            }
            QPushButton {
                background-color: #0078d7;
                border: none;
                padding: 10px;
                border-radius: 6px;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
            QLabel {
                color: #cccccc;
            }
        """)

    def send_message(self):
        user_text = self.input.text().strip()
        if not user_text:
            return

        # Show user message
        self.chat_log.append(f"You: {user_text}")
        self.input.clear()
        self.status.setText("Jarvis is thinking...")

        # Get AI response
        response = self.get_ai_response(user_text)
        self.chat_log.append(f"Jarvis: {response}\n")
        self.status.setText("")

        # Save chat to file
        self.save_chat_history(f"You: {user_text}\nJarvis: {response}\n")

    def get_ai_response(self, prompt):
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {str(e)}"

    def save_chat_history(self, text):
        """💾 Save chat to a local file"""
        with open("jarvis_chat_history.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JarvisApp()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec_())
