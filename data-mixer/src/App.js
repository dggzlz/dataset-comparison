import React, { useState } from "react";
import Compare from "./Compare";
import Search from "./Search";

function App() {
  const [showCompare, setShowCompare] = useState(false);
  const [showSearch, setShowSearch] = useState(false); 

  const toggleCompare = () => {
    setShowCompare(!showCompare);
  };

  const toggleSearch = () => {
    setShowSearch(!showSearch);
  };

  return (
    <div id="body">
      {showCompare && <Compare onScreen={toggleCompare} />}
      {showSearch && <Search onScreen={toggleSearch} />} 
      <nav>
        <h1>Data Mixer &#128256;</h1>
        <div id="button-part">
          <button>About</button>
          <button>Update File</button>
          <button onClick={toggleCompare}>Compare File</button>
          <button>Locate Differences</button>
          <button onClick={toggleSearch}>Search Files</button>
          <button>Sorting Files</button>
          <button>Copy Files from other sites</button>
        </div>
      </nav>
      <h1>About</h1>
    </div>
  );
}

export default App;
