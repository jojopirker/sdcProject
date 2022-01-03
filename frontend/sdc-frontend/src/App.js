import logo from './logo.svg';
import './App.css';
import DashIntegration from './components/DashIntegrationHack';
import Navigation from './components/Navigation';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";


function App() {
  return (

    <div className="App">
      <Navigation />
      <BrowserRouter>
        <Routes>
          <Route path="/dash-1" element={
            <DashIntegration route={"page-1"} />} />
          <Route path="/dash-2" element={
            <DashIntegration route={"page-2"} />} />
        </Routes>
      </BrowserRouter>
    </div>

  );
}

export default App;
