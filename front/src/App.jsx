import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import "./static/css/style.css";
import "./static/css/from.css";
import Login from "./pages/Login";
import Main from "./pages/Main";
import AddObjects from "./pages/AddObjects";
import EditObject from "./pages/EditObjects";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/login/" element={<Login />} />
        <Route path="/" element={<Main />} />
        <Route path="/add/objects/" element={<AddObjects />} />
        <Route path="/edit/objects/:id" element={<EditObject />} />
      </Routes>
    </Router>
  );
};

export default App;
