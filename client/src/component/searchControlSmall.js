import "../App.css";
import {
    FiMapPin,
    FiMoon,
    FiSearch,
    FiSun,
  } from "react-icons/fi";

function SearchControlSmall() {
    return (
      <div className="  md:hidden  ">
        <div className="max-w-full bg-white  dark:bg-cardColor shadow-sm ml-10 mr-10 rounded-md absolute top-10 right-0 left-0 grid grid-cols-1 px-4 py-5  mt-6 sm:mx-20">
          <div className="flex justify-between">
            <div className="flex place-items-center  flex-grow">
              <FiSearch className="inline-block text-primary text-2xl" />
              <input
                className="flex-grow mx-2 h-7 outline-none dark:bg-cardColor dark:text-gray-400 text-black"
                type="text"
                placeholder="Filter by text"
              />
            </div>
            <button className="bg-primary text-white font-bold text-xl px-2 py-2 rounded-md justify-self-end inline-block ">
              <FiSearch />
            </button>
          </div>
        </div>
      </div>
    );
  }
  
export default SearchControlSmall;
  