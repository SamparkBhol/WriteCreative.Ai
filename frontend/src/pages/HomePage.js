import React from 'react';
import Chatbot from '../components/Chatbot';
import './HomePage.css';

const HomePage = () => {
  return (
    <div className="homepage">
      <header className="homepage-header">
        <h1>Welcome to the Creative Writing Assistant</h1>
        <p>Your personal assistant for crafting stories, poems, characters, and scripts.</p>
      </header>
      <main className="homepage-main">
        <Chatbot />
      </main>
      <footer className="homepage-footer">
        <p>&copy; {new Date().getFullYear()} Creative Writing Assistant</p>
      </footer>
    </div>
  );
};

export default HomePage;
