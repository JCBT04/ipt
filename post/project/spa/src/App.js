import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from 'react'
import axios from 'axios'


function App() {

     const [post, setPost] = useState([])

     useEffect(() => {
          axios.get('http://localhost:8000/api/v1/post/').then(response => {
               console.log(response.data)
          })
     }, [])


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        {
          post.map((obj, index) => <p key={index}>{obj.title}</p>)
        }
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
