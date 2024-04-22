import { FileUploader } from "react-drag-drop-files";

import { postFile } from "../api/postFile";

const fileTypes = ["csv"];

function DragDrop({ onChange, onError }) {
  const handleChange = async (file) => {
    try {
      onChange(await postFile(file));
    } catch (e) {
      onError(e);
      console.error(e)
    }
  };

  return <FileUploader handleChange={handleChange} name="file" types={fileTypes} />;
}

export default DragDrop;
