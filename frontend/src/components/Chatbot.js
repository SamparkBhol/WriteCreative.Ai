import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Chatbot.css';

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    // Initial greeting from the chatbot
    setMessages([{ text: 'Hello! I’m your Creative Writing Assistant. What can I help you with today?', sender: 'bot' }]);
  }, []);

  const handleSend = async () => {
    if (input.trim()) {
      const userMessage = { text: input, sender: 'user' };
      setMessages([...messages, userMessage]);

      try {
        const response = await axios.post('/api/chatbot/respond', { message: input });
        const botMessage = { text: response.data.response, sender: 'bot' };
        setMessages([...messages, userMessage, botMessage]);
      } catch (error) {
        const errorMessage = { text: 'Sorry, I’m having trouble processing your request.', sender: 'bot' };
        setMessages([...messages, userMessage, errorMessage]);
      }
      setInput('');
    }
  };

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSend();
    }
  };

  return (
    <div className="chatbot-container">
      <div className="chat-window">
        <div className="messages">
          {messages.map((message, index) => (
            <div key={index} className={`message ${message.sender}`}>
              {message.text}
            </div>
          ))}
        </div>
        <div className="input-container">
          <input
            type="text"
            placeholder="Type a message..."
            value={input}
            onChange={handleInputChange}
            onKeyPress={handleKeyPress}
          />
          <button onClick={handleSend}>Send</button>
        </div>
      </div>
    </div>
  );
};

export default Chatbot;
