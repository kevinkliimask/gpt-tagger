// This function was written with the help of ChatGPT https://chat.openai.com/share/5512d600-82ba-4343-97bf-1dd6bcb5df7b
export const readCsv = (file) => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();

    reader.onload = (event) => {
      const content = event.target.result;
      const lines = content.split("\n").slice(0, 10)
      const dataArray = lines.map((line) => line.split(","));

      resolve(dataArray);
    };

    reader.onerror = (error) => {
      reject(error);
    };

    reader.readAsText(file);
  });
};
