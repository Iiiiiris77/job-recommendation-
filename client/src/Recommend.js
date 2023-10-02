import './App.css';
import Header from './component/header.js';
import recommendBody from './component/recommendbody.js';
function recommend(){
    return (
        <div className="bg-gray-100 dark:bg-bcakground h-full">
          <Header/>
          <recommendBody/>

        </div>
      );

}