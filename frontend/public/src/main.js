function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function sendMessage() {
    var messageInput = document.getElementById('message-input');
    var messageContainer = document.getElementById('message-container');

    var userMessage = messageInput.value.trim();
    if (userMessage === '') {
        return;
    }

    // Create a chat bubble for user message
    var userBubble = document.createElement('div');
    userBubble.className = 'chat-bubble user-bubble';
    userBubble.textContent = userMessage;

    // Append the user message bubble to the message container
    messageContainer.appendChild(userBubble);

    // Clear the message input
    messageInput.value = '';

    // For now, let's add an empty chat bubble for the chatbot response
    var botBubble = document.createElement('div');
    botBubble.className = 'chat-bubble bot-bubble';
    botBubble.textContent = ''; // Leave it empty for now

    // Append the chatbot response bubble to the message container
    messageContainer.appendChild(botBubble);
}