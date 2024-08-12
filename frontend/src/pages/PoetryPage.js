import React, { useState } from 'react';
import axios from 'axios';
import './PoetryPage.css';

const PoetryPage = () => {
  const [prompt, setPrompt] = useState('');
  const [poetry, setPoetry] = useState('');
  const [loading, setLoading] = useState(false);

  const generatePoetry = async () => {
    if (!prompt.trim()) return;

    setLoading(true);
    try {
      const response = await axios.post('/api/poetry/generate', { prompt });
      setPoetry(response.data.poetry);
    } catch (error) {
      setPoetry('An error occurred while generating the poetry. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="poetry-page">
      <header className="page-header">
        <h2>Poetry Generator</h2>
        <p>Enter a prompt below to generate a beautiful poem.</p>
      </header>
      <main className="page-content">
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your poetry prompt here..."
          rows="6"
        />
        <button onClick={generatePoetry} disabled={loading}>
          {loading ? 'Generating...' : 'Generate Poetry'}
        </button>
        {poetry && <div className="generated-poetry">{poetry}</div>}
      </main>
    </div>
  );
};

export default PoetryPage;
