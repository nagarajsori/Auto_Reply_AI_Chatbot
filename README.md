# 🤖 Auto-Reply AI Chatbot

Welcome to **Naruto**, your not-so-friendly AI chatbot that’s trained to roast your friends in style. This project is a fun twist on AI-powered automation - blending OpenAI’s GPT-3.5-turbo with GUI automation to create a chatbot that reads your chats, understands who said what, and then claps back with hilarious roast replies - automatically.

## 📌 Project Overview

This chatbot is built to **automate conversations** in any chat application by:
- Reading chat messages
- Analyzing who sent the last message
- Generating a **humorous roast-style reply**
- Sending it back - all without you lifting a finger

Naruto does all this using **OpenAI’s GPT model** along with some Python magic (`pyautogui`, `pyperclip`, and more).

## 💡 Key Features

### 🔄 Automated Chat Interaction
- Launches your chat app (e.g., Chrome-based apps)
- Uses `pyautogui` to control mouse and keyboard like a human

### 📋 Chat History Analysis
- Copies and reads the latest chat using `pyperclip`
- Checks who sent the last message (e.g., "Rohan Das")

### 😂 Roast Generation
- Sends chat context to **GPT-3.5-turbo**
- Generates a hilarious comeback if the last sender matches your target

### 📤 Auto-Reply
- Pastes the generated response in the input field
- Sends it like a ninja strike - fast and funny

## 🧠 How It Works (Workflow)

```mermaid
graph TD;
    A[Start & Setup] --> B[Open Chat App via pyautogui];
    B --> C[Copy Chat History];
    C --> D[Analyze Last Message Sender];
    D --> E{Is it "Rohan Das"?};
    E -- Yes --> F[Send to OpenAI API];
    F --> G[Generate Roast];
    G --> H[Paste & Send Reply];
    E -- No --> I[Wait & Re-check];
