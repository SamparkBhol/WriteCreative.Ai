import React, { useState } from 'react';
import axios from 'axios';
import './StoryPage.css';

const StoryPage = () => {
  const [prompt, setPrompt] = useState('');
  const [story, setStory] = useState('');
  const [loading, setLoading] = useState(false);

  const generateStory = async () => {
    if (!prompt.trim()) return;

    setLoading(true);
    try {
      const response = await axios.post('/api/story/generate', { prompt });
      setStory(response.data.story);
    } catch (error) {
      setStory('An error occurred while generating the story. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="story-page">
      <header className="page-header">
        <h2>Story Generator</h2>
        <p>Enter a prompt below to generate a captivating story.</p>
      </header>
      <main className="page-content">
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your story prompt here..."
          rows="6"
        />
        <button onClick={generateStory} disabled={loading}>
          {loading ? 'Generating...' : 'Generate Story'}
        </button>
        {story && <div className="generated-story">{story}</div>}
      </main>
    </div>
  );
};

export default StoryPage;
