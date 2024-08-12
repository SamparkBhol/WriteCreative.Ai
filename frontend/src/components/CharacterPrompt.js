import React, { useState } from 'react';
import axios from 'axios';
import './Prompt.css';

const CharacterPrompt = () => {
  const [prompt, setPrompt] = useState('');
  const [generatedCharacter, setGeneratedCharacter] = useState('');

  const handleGenerateCharacter = async () => {
    if (prompt.trim()) {
      try {
        const response = await axios.post('/api/character/generate', { prompt });
        setGeneratedCharacter(response.data.character);
      } catch (error) {
        setGeneratedCharacter('Oops! Something went wrong while generating your character.');
      }
    }
  };

  return (
    <div className="prompt-container">
      <h2>Character Generator</h2>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your character prompt here..."
      />
      <button onClick={handleGenerateCharacter}>Generate Character</button>
      {generatedCharacter && <div className="generated-content">{generatedCharacter}</div>}
    </div>
  );
};

export default CharacterPrompt;
