export async function postFile(file, numberOfTags, model) {
  const data = new FormData();
  data.append("file", file)

  const url = new URL(process.env.REACT_APP_BACKEND_URL);
  url.searchParams.set("count", numberOfTags);
  url.searchParams.set("model", model);

  const response = await fetch(url, { method: "POST", body: data });
  return (await response.json()).data;
}
