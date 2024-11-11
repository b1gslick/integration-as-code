import React, { useEffect, useState } from "react";
import LargeData, { LargeDataType } from "./api/requests";
import "./App.css";

const App = () => {
  const [largeData, setLargeData] = useState("");
  const [readWrite, setReadWrite] = useState(false);
  const [allRowsData, setAllRowsData] = useState(Array<LargeDataType>);
  const [isNew, setIsNew] = useState(false);
  const [currentId, setCurrentId] = useState("");
  // const url = process.env.BACKEND;
  const url = "http://localhost:8000";
  const redisHost = "";
  const redisPort = 0;
  const ld = new LargeData(url, redisHost, redisPort);

  useEffect(() => {
    fetchAllRows();
  }, []);

  const fetchAllRows = async () => {
    setAllRowsData(await ld.getAll());
  };

  const handleLargeData = (event: any) => {
    setLargeData(event.target.value);
  };
  const onToggle = (ev: React.ChangeEvent<HTMLInputElement>) => {
    const value = (ev.target as HTMLInputElement).checked;
    setReadWrite(value);
  };
  const postData = async () => {
    if (isNew) {
      await ld.postLargeData(largeData);
    } else {
      await ld.updateLargeData(largeData, currentId);
    }
  };
  const selectedRow = async (ev: any) => {
    setIsNew(false);
    setCurrentId(ev.target.value[0]);
    if (ev.target.value[0] === "") {
      setIsNew(true);
    }
    setLargeData(ev.target.value[1]);
  };

  return (
    <div className="App">
      <div>
        <label htmlFor="select"></label>
        <select className="select__large_data" onChange={selectedRow}>
          <option key={0} value={""}>
            new post
          </option>
          {allRowsData.map((row) => {
            return (
              <option key={row.id} value={[row.hash, row.big_data]}>
                {row.hash}
              </option>
            );
          })}
        </select>
      </div>

      <div>
        <input
          type={"checkbox"}
          onChange={onToggle}
          checked={readWrite}
        ></input>
      </div>
      <div>
        <textarea
          value={largeData}
          disabled={!readWrite}
          onChange={handleLargeData}
        ></textarea>
      </div>
      <div>
        <button disabled={!readWrite} name="save" onClick={postData}>
          Save data
        </button>
      </div>
    </div>
  );
};

export default App;
