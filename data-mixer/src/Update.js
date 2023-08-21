import React, { useState, useEffect } from "react";

function Update({ onScreen }) {
  const [firstFile, setFirstFile] = useState(null);
  const [word, setWord] = useState(null);
  const [isFormValid, setIsFormValid] = useState(false);
  const [firstFileContent, setFirstFileContent] = useState(null);
  const [differences, setDifferences] = useState(null);

  useEffect(() => {
    if (firstFile) {
      setIsFormValid(true);
      console.log(firstFile.name)
    } else {
      setIsFormValid(false);
    }
  }, [firstFile]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isFormValid) {
      // Process the files and get their contents (You need to implement this part)
      // For example, if the files are CSVs, you can use FileReader API to read the contents.

      // Placeholder content for demonstration purposes:
      setFirstFileContent("First file content goes here.");
    }
  };

  return (
    <div id="overlay">
      <h1 id="nav-header">Update &#128269;</h1>
      <button id="exit" onClick={onScreen}>
        X
      </button>
      <form>
        <input
          type="file"
          id="sbox-1"
          accept="pdf, csv, xlsx"
          onChange={(e) => setFirstFile(e.target.files[0])}
        />
        <button
          id="submit-button"
          onClick={handleSubmit}
          disabled={!isFormValid}
        >
          Update File
        </button>
      </form>
      {isFormValid && (
        <div id = "cunder-box">
          <div id = "cleft">
            <h2>{firstFile.name} Content:</h2>
            <pre>{firstFileContent}</pre>
          </div>
        </div>
      )}
    </div>
  );
}

export default Update;
