import { FileUploader } from "react-drag-drop-files";
import { useState } from "react";

import "./App.css";
import { postFile } from "./api/postFile";

function App() {
  const [tags, setTags] = useState(null);
  const [error, setError] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = async (file) => {
    try {
      setIsLoading(true);
      setTags(await postFile(file));
    } catch (e) {
      setError(e);
      console.error(e);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="content">
      <FileUploader handleChange={handleChange} name="file" types={["csv"]} />
      {tags && (
        <>
          <div>
            <h3>English tags:</h3>
            <p>{tags.english.join(", ")}</p>
          </div>
          <div>
            <h3>Estonian tags:</h3>
            <p>{tags.estonian.join(", ")}</p>
          </div>
        </>
      )}
      {isLoading && <span>Loading...</span>}
      {error && <span>{error.toString()}</span>}
    </div>
  );
}

export default App;
