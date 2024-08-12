import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Chatbot from './components/Chatbot';
import StoryPrompt from './components/StoryPrompt';
import PoetryPrompt from './components/PoetryPrompt';
import CharacterPrompt from './components/CharacterPrompt';
import ScriptPrompt from './components/ScriptPrompt';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import './App.css';

const App = () => {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Switch>
          <Route path="/" exact component={Chatbot} />
          <Route path="/story" component={StoryPrompt} />
          <Route path="/poetry" component={PoetryPrompt} />
          <Route path="/character" component={CharacterPrompt} />
          <Route path="/script" component={ScriptPrompt} />
        </Switch>
        <Footer />
      </div>
    </Router>
  );
};

export default App;
