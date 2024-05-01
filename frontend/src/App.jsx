import { FileUploader } from "react-drag-drop-files";
import { useState } from "react";

import "./App.css";
import { postFile } from "./api/postFile";
import { readCsv } from "./utils/csvReader";

const NUMBER_OF_TAGS = [3, 4, 5, 6, 7, 8, 9, 10];
const MODELS = ["gpt-3.5-turbo", "gpt-4"];
const FILE_TYPES = ["csv"];

function App() {
  const [tags, setTags] = useState(null);
  const [selectedNumberOfTags, setSelectedNumberOfTags] = useState(NUMBER_OF_TAGS[0]);
  const [selectedModel, setSelectedModel] = useState(MODELS[0]);

  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = async (file) => {
    try {
      setTags(null);
      setError(null);
      setIsLoading(true);

      const csvData = await readCsv(file);
      setTags(await postFile(csvData, selectedNumberOfTags, selectedModel));
    } catch (e) {
      setError(e);
      console.error(e);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="content">
      <div className="card">
        <h2>Dataset tagger</h2>
        <div className="selections">
          <div>
            <span>Number of tags:</span>
            <select defaultValue={selectedNumberOfTags} onChange={(e) => setSelectedNumberOfTags(e.target.value)}>
              {NUMBER_OF_TAGS.map((val) => (
                <option value={val}>{val}</option>
              ))}
            </select>
          </div>
          <div>
            <span>Model:</span>
            <select defaultValue={selectedModel} onChange={(e) => setSelectedModel(e.target.value)}>
              {MODELS.map((val) => (
                <option value={val}>{val}</option>
              ))}
            </select>
          </div>
        </div>
        <div className="upload">
          <FileUploader handleChange={handleChange} name="file" types={FILE_TYPES} />
        </div>
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
    </div>
  );
}

export default App;
