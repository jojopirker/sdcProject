import './App.css';
import DashIntegration from './components/DashIntegrationHack';
import Navigation from './components/Navigation';
import GeneralInformation from './components/GeneralInformation';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import APIOverview from './components/APIOverview';

function App() {
  return (

    <div className="App">
      <Navigation />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={
            <GeneralInformation />} />
          <Route path="/dash-1" element={
            <DashIntegration route={"page-1"} />} />
          <Route path="/dash-2" element={
            <DashIntegration route={"page-2"} />} />
          <Route path="/apiOverview" element={
            <APIOverview />} />
        </Routes>
      </BrowserRouter>
    </div>

  );
}
export default App;
