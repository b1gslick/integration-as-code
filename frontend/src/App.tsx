import React, { useEffect, useState } from "react";
import "./App.css";

const App = () => {
  const [largeData, setLargeData] = useState("");
  const [readWrite, setReadWrite] = useState(false);

  useEffect(() => {
    if (!readWrite) {
      getLargeData(0);
    } else {
      postLargeData(largeData);
    }
  });

  const getLargeData = (id: number) => {
    fetch(`${process.env.BACKEND}`, {
      method: "GET",
      headers: {
        "X-RapidAPI-Key": "your-api-key",
        "X-RapidAPI-Host": "jokes-by-api-ninjas.p.rapidapi.com",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        setLargeData(data[0].joke);
        console.log(data);
      })
      .catch((error) => console.log(error));
  };
  const postLargeData = (data: string) => {};

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    event.preventDefault();
    let inputValue = event.target.value;
    console.log(event.target.value); // You will the value here. you can simply pass the value to the function
  };

  const handleLargeData = (event: any) => {
    setLargeData(event.target.value);
  };
  const onToggle = (ev: React.ChangeEvent<HTMLInputElement>) => {
    const value = (ev.target as HTMLInputElement).checked;
    setReadWrite(value);
  };
  return (
    <div className="App">
      <input type={"checkbox"} onChange={onToggle} checked={readWrite}></input>
      <input type={"text"} onChange={handleInputChange}></input>
      <textarea
        value={largeData}
        disabled={!readWrite}
        onChange={handleLargeData}
      ></textarea>
      <button disabled={!readWrite} name="save">
        Save data
      </button>
    </div>
  );
};

export default App;
