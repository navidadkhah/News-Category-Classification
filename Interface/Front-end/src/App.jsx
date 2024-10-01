import axios from "axios";
import './App.css'
// import { Here } from "./here";
import { useState } from "react";

function App() {
  const [data, setData] = useState("");
  const [output, setoutput] = useState("");
  const handleChange = (e) => {
    setData(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setData(e.target.value);
    if (data === "") {
      alert("Please enter a text");
    } 
    else {
      data.replace("/", "");
      let api = `http://127.0.0.1:5000/pos/${data}`;
      axios
        .get(api)
        .then(function (response) {
          // handle success
          console.log(response.data["predict"]);
          setoutput("Politics");
        })
        .catch(function (error) {
          // handle error
          console.log(error);
        })
        .finally(function () {
          // always executed
        });
      setoutput("Sport");
    }
  };
  return (
    <div className="homepage">
      <h1 className="title">Welcome to the news category recognition</h1>
      <form className="infoForm">
        <div className="form">
          <label htmlFor="search-bar" className="lable">
            please enter your text:
          </label>
          <textarea
            type="texrarea"
            placeholder="Enter your text..."
            className="infoInput"
            name="firstName"
            onChange={(e) => handleChange(e)}
            value={data}
          />
          <button className="button" onClick={handleSubmit}>
            submit
          </button>
        </div>
      </form>
      {output ? <p className="output">the above news category is: {output}</p>:<p></p>}
    </div>
    // <div>
    //   <Here />
    // </div>
  );
}

export default App;
