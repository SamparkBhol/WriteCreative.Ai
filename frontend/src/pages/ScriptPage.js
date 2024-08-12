import React, { useState } from 'react';
import axios from 'axios';
import './ScriptPage.css';

const ScriptPage = () => {
  const [prompt, setPrompt] = useState('');
  const [script, setScript] = useState('');
  const [loading, setLoading] = useState(false);

  const generateScript = async () => {
    if (!prompt.trim()) return;

    setLoading(true);
    try {
      const response = await axios.post('/api/script/generate', { prompt });
      setScript(response.data.script);
    } catch (error) {
      setScript('An error occurred while generating the script. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="script-page">
      <header className="page-header">
        <h2>Script Generator</h2>
        <p>Enter a prompt below to generate a compelling script.</p>
      </header>
      <main className="page-content">
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your script prompt here..."
          rows="6"
        />
        <button onClick={generateScript} disabled={loading}>
          {loading ? 'Generating...' : 'Generate Script'}
        </button>
        {script && <div className="generated-script">{script}</div>}
      </main>
    </div>
  );
};

export default ScriptPage;
