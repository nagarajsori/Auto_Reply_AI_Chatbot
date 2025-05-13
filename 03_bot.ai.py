import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
  api_key="<Your Key Here>",
)

def is_last_message_from_sender(chat_log, sender_name="Naveen"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False

# Step 1: Click on the chrome icon at coordinates (971, 1051)
pyautogui.click(971, 1051)
time.sleep(1)  # Wait for any UI to respond

while True:
    time.sleep(5)
    # Step 2: Drag to select text
    pyautogui.moveTo(735, 280)
    pyautogui.dragTo(862, 958, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(1040, 963)

    # Step 4: Get text from clipboard
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named Nagaraj who speaks Kannada, English as well as Hindi. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not start like this [21:02, 12/5/2025] Amma: "},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(1150, 1965)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')