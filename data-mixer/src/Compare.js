import React, { useState, useEffect } from "react";

function Compare({ onScreen }) {
  const [firstFile, setFirstFile] = useState(null);
  const [secondFile, setSecondFile] = useState(null);
  const [isFormValid, setIsFormValid] = useState(false);
  const [firstFileContent, setFirstFileContent] = useState(null);
  const [secondFileContent, setSecondFileContent] = useState(null);
  const [differences, setDifferences] = useState(null);

  useEffect(() => {
    if (firstFile && secondFile) {
      setIsFormValid(true);
      console.log(firstFile.name, secondFile.name)
    } else {
      setIsFormValid(false);
    }
  }, [firstFile, secondFile]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (isFormValid) {
      // Process the files and get their contents (You need to implement this part)
      // For example, if the files are CSVs, you can use FileReader API to read the contents.

      // Placeholder content for demonstration purposes:
      setFirstFileContent("First file content goes here.");
      setSecondFileContent("Second file content goes here.");
    }
  };

  return (
    <div id="overlay">
      <h1 id="nav-header">Compare &#128203;</h1>
      <button id="exit" onClick={onScreen}>
        X
      </button>
      <form>
        <input
          type="file"
          id="cbox-1"
          name="avatar"
          accept="pdf, csv, xlsx"
          onChange={(e) => setFirstFile(e.target.files[0])}
        />
        <input
          type="file"
          id="cbox-2"
          name="avatar"
          accept="pdf, csv, xlsx"
          onChange={(e) => setSecondFile(e.target.files[0])}
        />
        <button
          id="submit-button"
          onClick={handleSubmit}
          disabled={!isFormValid}
        >
          Compare Files
        </button>
      </form>
      {isFormValid && (
        <div id = "cunder-box">
          <div id = "cleft">
            <h2>{firstFile.name} Content:</h2>
            <pre>{firstFileContent}</pre>
          </div>
          <div id="cmid">Number of differences from both files</div>
          <div id ="crigt">
            <h2>{secondFile.name} Content:</h2>
            <pre>{secondFileContent}</pre>
          </div>
        </div>
      )}
    </div>
  );
}

export default Compare;
