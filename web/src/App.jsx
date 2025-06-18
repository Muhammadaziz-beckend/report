import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import "./static/css/style.css";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<>hello</>} />
      </Routes>
    </Router>
  );
};

export default App;
