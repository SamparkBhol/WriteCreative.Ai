import React, { useState } from 'react';
import axios from 'axios';
import './Prompt.css';

const PoetryPrompt = () => {
  const [prompt, setPrompt] = useState('');
  const [generatedPoetry, setGeneratedPoetry] = useState('');

  const handleGeneratePoetry = async () => {
    if (prompt.trim()) {
      try {
        const response = await axios.post('/api/poetry/generate', { prompt });
        setGeneratedPoetry(response.data.poetry);
      } catch (error) {
        setGeneratedPoetry('Oops! Something went wrong while generating your poem.');
      }
    }
  };

  return (
    <div className="prompt-container">
      <h2>Poetry Generator</h2>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your poetry prompt here..."
      />
      <button onClick={handleGeneratePoetry}>Generate Poetry</button>
      {generatedPoetry && <div className="generated-content">{generatedPoetry}</div>}
    </div>
  );
};

export default PoetryPrompt;
