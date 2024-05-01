export async function postFile(data, numberOfTags, model) {
  const url = new URL(process.env.REACT_APP_BACKEND_URL);
  url.searchParams.set("count", numberOfTags);
  url.searchParams.set("model", model);
  console.log(data);
  const response = await fetch(url, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ data }),
  });
  return (await response.json()).data;
}
