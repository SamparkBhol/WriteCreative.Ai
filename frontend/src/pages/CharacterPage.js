import React, { useState } from 'react';
import axios from 'axios';
import './CharacterPage.css';

const CharacterPage = () => {
  const [prompt, setPrompt] = useState('');
  const [character, setCharacter] = useState('');
  const [loading, setLoading] = useState(false);

  const generateCharacter = async () => {
    if (!prompt.trim()) return;

    setLoading(true);
    try {
      const response = await axios.post('/api/character/generate', { prompt });
      setCharacter(response.data.character);
    } catch (error) {
      setCharacter('An error occurred while generating the character. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="character-page">
      <header className="page-header">
        <h2>Character Generator</h2>
        <p>Enter a prompt below to create an intriguing character.</p>
      </header>
      <main className="page-content">
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your character prompt here..."
          rows="6"
        />
        <button onClick={generateCharacter} disabled={loading}>
          {loading ? 'Generating...' : 'Generate Character'}
        </button>
        {character && <div className="generated-character">{character}</div>}
      </main>
    </div>
  );
};

export default CharacterPage;
