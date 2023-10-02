import "../App.css";

import { FaToggleOff, FaToggleOn } from "react-icons/fa";
import {
  FiMapPin,
  FiMoon,
  FiSearch,
  FiSun,
} from "react-icons/fi";
import SearchControlSmall from './searchControlSmall.js';
import SearchControlLarge from './searchControlLarge.js';
import React, {useState} from "react";

function Header({changeBody}) {
// function Header() {

  const[hasBar, setBar] = useState(true);
  const handleClick = (e) => {
    // console.log(e)
    setBar(e)
    changeBody({searchBody: !hasBar})
  }

  return (
    <div className="container max-w-full relative">
      <header className="bg-primary space-x-4 pl-8 pr-4 pb-8 pt-4 flex place-content-between ">
        <div className="inline-block text-3xl font-bold text-white">
          <button onClick = {() => handleClick(true)}>{hasBar ? <strong>search</strong> : 'search |'}</button>
          <button onClick = {() => handleClick(false)}>{!hasBar ? <strong>recommendation</strong> : '| recommendation'}</button>
        </div>
        <div className="inline-block text-3xl font-bold text-white">
          {/* <button onClick = {() => setBar(false)}>profile</button> */}
        </div>
        <Toggle />
      </header>
    </div>
  );
}
class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = { isToggleOn: true };

    // This binding is necessary to make `this` work in the callback
    this.handleClick = this.handleClick.bind(this);
    console.log(this.state.isDisplay);
  }

  handleClick() {
    this.setState((prevState) => ({
      isToggleOn: !prevState.isToggleOn,
    }));
    if(this.state.isToggleOn){
      document.documentElement.classList.add('dark')
    }else{
      document.documentElement.classList.remove('dark')
    }
  }

  render() {
    var isDisplay = this.state.isToggleOn;
    let toggleButton;
    if (isDisplay) {
      toggleButton = <FaToggleOn className={"inline-block  text-2xl"} />;
    } else {
      toggleButton = <FaToggleOff className={"inline-block text-2xl "} />;
    }
    return (
      <div className="object object-right space-x-2 text-white text-sm items-center flex">
        <FiMoon className="inline-block" />
        <button
          className="outline-none m-0 text-3xl focus:outline-none self-center mb-2"
          onClick={this.handleClick}
        >
          {toggleButton}
        </button>
        <FiSun className="inline-block" />
      </div>
    );
  }
}



export default Header;
