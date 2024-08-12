import axios from 'axios';

// Base configuration for axios
const api = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Function to generate story based on prompt
export const generateStory = async (prompt) => {
  try {
    const response = await api.post('/story/generate', { prompt });
    return response.data.story;
  } catch (error) {
    console.error('Error generating story:', error);
    throw error;
  }
};

// Function to generate poetry based on prompt
export const generatePoetry = async (prompt) => {
  try {
    const response = await api.post('/poetry/generate', { prompt });
    return response.data.poetry;
  } catch (error) {
    console.error('Error generating poetry:', error);
    throw error;
  }
};

// Function to generate character based on prompt
export const generateCharacter = async (prompt) => {
  try {
    const response = await api.post('/character/generate', { prompt });
    return response.data.character;
  } catch (error) {
    console.error('Error generating character:', error);
    throw error;
  }
};

// Function to generate script based on prompt
export const generateScript = async (prompt) => {
  try {
    const response = await api.post('/script/generate', { prompt });
    return response.data.script;
  } catch (error) {
    console.error('Error generating script:', error);
    throw error;
  }
};

// Export the axios instance for custom requests
export default api;
