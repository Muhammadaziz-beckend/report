import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import "./static/css/style.css";
import Login from "./pages/Login";
import Main from "./pages/Main";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/login/" element={<Login />} />
        <Route path="/" element={<Main />} />
      </Routes>
    </Router>
  );
};

export default App;
