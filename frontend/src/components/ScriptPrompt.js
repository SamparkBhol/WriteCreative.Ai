import React, { useState } from 'react';
import axios from 'axios';
import './Prompt.css';

const ScriptPrompt = () => {
  const [prompt, setPrompt] = useState('');
  const [generatedScript, setGeneratedScript] = useState('');

  const handleGenerateScript = async () => {
    if (prompt.trim()) {
      try {
        const response = await axios.post('/api/script/generate', { prompt });
        setGeneratedScript(response.data.script);
      } catch (error) {
        setGeneratedScript('Oops! Something went wrong while generating your script.');
      }
    }
  };

  return (
    <div className="prompt-container">
      <h2>Script Generator</h2>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your script prompt here..."
      />
      <button onClick={handleGenerateScript}>Generate Script</button>
      {generatedScript && <div className="generated-content">{generatedScript}</div>}
    </div>
  );
};

export default ScriptPrompt;
