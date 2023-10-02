import './App.css';
import React, {useEffect,useState} from "react";
import Body from './component/body.js';
import RecommendBody from './component/recommendBody.js'
import Header from './component/header.js';

function App() {
  const[hasBar, setBar] = useState({searchBody: true});
  useEffect(() => {
    // console.log(hasBar.searchBody)
  }, [hasBar])
  return (
    <div className="bg-gray-100 dark:bg-bcakground h-full">
      <Header changeBody = {setBar}/>
      {hasBar.searchBody ? <Body/>: <RecommendBody/>}
      
    </div>
  );
}

export default App;
