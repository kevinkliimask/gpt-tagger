export async function postFile(file) {
  const data = new FormData();
  data.append("file", file)

  const response = await fetch(process.env.REACT_APP_BACKEND_URL, { method: "POST", body: data });
  return (await response.json()).data;
}
