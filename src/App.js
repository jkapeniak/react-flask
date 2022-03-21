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
              
              console.log("posted successfully")

              console.log(response.data)

              console.log("Course")

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
  const [name, setName] = useState('cis x x x');

  const [course, setCourse] = useState('');




  function handlePostQuery(query){

    var myParams = {
        data: query
    }
  
    if (query !== "") {
        axios.post('http://131.104.49.112/api/query', myParams)
            .then(function(response){
                
                console.log("posted successfully")

                console.log(response.data)
                setCourse(JSON.stringify(response.data));

                // console.log(JSON.stringify({ x: 5, y: 6 }));


  
                console.log("Course")
  
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
    
    const handleSubmit = (e) => {
    
        e.preventDefault();

        console.log(`Form submitted, ${name}`);   
        
        console.log({name})
        
        handlePostQuery({name})

    }


  useEffect(() => {
    fetch('http://131.104.49.112/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="App" style={{ background: "#61dafb" }}>
      {/* <header className="App-header">

        ... no changes in this part ...

        <p>The current time is {currentTime}.</p>
      </header> */}

    <p style={{ background: "#61dafb" }}>The current time is {currentTime}.</p>

    
    <p>The current data is {course}.</p>

      <div>
      <h1>
        Example input: cis x x x  
      </h1>
      <form onSubmit = {handleSubmit}>
            <input onChange = {(e) => setName(e.target.value)} value = {name}></input>
            <button type = 'submit'>Click to submit</button>
        </form>

      </div>
      

    </div>
  );
}




export default App;
