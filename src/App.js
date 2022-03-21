import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
const axios = require('axios').default;


function handlePostQuery(query){

  var myParams = {
      data: query
  }

  if (query !== "") {
      axios.post('http://131.104.49.112/api/query', myParams)
          .then(function(response){
              console.log(response);
              console.log("posted successfully")
     //Perform action based on response
      })
      .catch(function(error){
          console.log(error);
     //Perform action based on error
      });
  } else {
      alert("The search query cannot be empty")
  }
}








function App() {
  const [currentTime, setCurrentTime] = useState(0);


  handlePostQuery("very nice how much")

  useEffect(() => {
    fetch('http://131.104.49.112/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">

        ... no changes in this part ...

        <p>The current time is {currentTime}.</p>
      </header>
    </div>
  );
}




export default App;
