import React, { useState } from 'react';
import axios from 'axios';
import './Prompt.css';

const StoryPrompt = () => {
  const [prompt, setPrompt] = useState('');
  const [generatedStory, setGeneratedStory] = useState('');

  const handleGenerateStory = async () => {
    if (prompt.trim()) {
      try {
        const response = await axios.post('/api/story/generate', { prompt });
        setGeneratedStory(response.data.story);
      } catch (error) {
        setGeneratedStory('Oops! Something went wrong while generating your story.');
      }
    }
  };

  return (
    <div className="prompt-container">
      <h2>Story Generator</h2>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your story prompt here..."
      />
      <button onClick={handleGenerateStory}>Generate Story</button>
      {generatedStory && <div className="generated-content">{generatedStory}</div>}
    </div>
  );
};

export default StoryPrompt;
