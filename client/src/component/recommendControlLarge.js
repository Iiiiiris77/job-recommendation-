import 'bootstrap/dist/css/bootstrap.css';
import "../App.css";
import { useState } from "react";
import DropdownButton from 'react-bootstrap/DropdownButton';
import Dropdown from 'react-bootstrap/Dropdown';
import Form from 'react-bootstrap/Form';

const RecommendControlLarge = ({changeInfo}) => {

  const [inputValue, setInputValue] = useState({
    rolename: '', location: '', date_posted: '', remote_jobs_only: false, employment_type:' '
  })

  const searchClickHandler = () => {
    changeInfo({
      rolename: inputValue.rolename,
      location: inputValue.location,
      date_posted: inputValue.date_posted, 
      remote_jobs_only: inputValue.remote_jobs_only, 
      employment_type: inputValue.employment_type
    })
 }

 const handleRoleChange = (event) => {
    setInputValue({
      rolename: event.target.value, 
      location: inputValue.location, 
      date_posted: inputValue.date_posted, 
      remote_jobs_only: inputValue.remote_jobs_only, 
      employment_type: inputValue.employment_type
    });
  }

  const handleLocChange = (event) => {
    // console.log(event)
    setInputValue({
      rolename: inputValue.rolename, 
      location: event.target.value,
      date_posted: inputValue.date_posted, 
      remote_jobs_only: inputValue.remote_jobs_only, 
      employment_type: inputValue.employment_type
    });
  }
  const handleDataChange = (event) => {
    setInputValue({
      rolename: inputValue.rolename, 
      location: inputValue.location, 
      date_posted: event, 
      remote_jobs_only: inputValue.remote_jobs_only, 
      employment_type: inputValue.employment_type
    });
  }
  const handleEmployChange = (event) => {
    setInputValue({
      rolename: inputValue.rolename, 
      location: inputValue.location, 
      date_posted: inputValue.date_posted,
      remote_jobs_only: inputValue.remote_jobs_only, 
      employment_type: event
    });
  }
  const handleRemoteChange = (event) => {
    // console.log(event.target.checked)
    setInputValue({
      rolename: inputValue.rolename, 
      location: inputValue.location, 
      date_posted: inputValue.date_posted,
      remote_jobs_only: event.target.checked, 
      employment_type: inputValue.employment_type
    });
  }


    return (
      <div className="hidden md:block">
        <div className="max-w-full bg-white dark:bg-cardColor shadow-sm ml-10 mr-10 rounded-md absolute top-20 right-0 left-0 grid grid-cols-6 gap-4 px-4  mt-6 ">
          <div className="flex align-middle place-items-center border-r border-gray-300 dark:border-gray-700 py-7 flex-grow ">
            {/* <FiSearch className="inline-block  text-primary text-2xl" /> */}
            <input
              className="flex-grow mx-2 h-7 outline-none dark:bg-cardColor dark:text-gray-400 text-black"
              type="text"
              placeholder="Role Name"
              onChange={handleRoleChange}
            />
          </div>
          <div className="flex align-middle place-items-center border-r border-gray-300 dark:border-gray-700 py-3 ">
            {/* <FiMapPin className="inline-block  text-primary text-2xl" />  */}
            <input
              className="flex-grow mx-2 h-7 outline-none dark:bg-cardColor dark:text-gray-400 text-black"
              type="text"
              placeholder="Loc(City, State)"
              onChange={handleLocChange}
            />
          </div> 
          {/* <div className="justify-between  flex align-middle place-items-center"> */}
            {/* <div className="flex  place-items-center"> */}
            <div className="flex align-middle place-items-center border-r border-gray-300 dark:border-gray-700 py-3 ">
              <DropdownButton title="Date Posted" onSelect={handleDataChange}>
                <Dropdown.Item eventKey='past_24_hours'>
                  past 24 hours
                </Dropdown.Item>
                <Dropdown.Item eventKey='past_week'>
                  past week
                </Dropdown.Item>
                <Dropdown.Item eventKey='past_month'>
                 past  month
                </Dropdown.Item>
                <Dropdown.Item eventKey='any'>
                 any
                </Dropdown.Item>
              </DropdownButton>
            </div>

            {/* <div className="flex  place-items-center"> */}
            <div className="flex align-middle place-items-center border-r border-gray-300 dark:border-gray-700 py-3 ">
              <DropdownButton title="Work Type" onSelect={handleEmployChange}>
                <Dropdown.Item eventKey='FULLTIME'>
                full time 
                </Dropdown.Item>
                <Dropdown.Item eventKey='CONTRACTOR'>
                contractor
                </Dropdown.Item>
                <Dropdown.Item eventKey='PARTTIME'>
                part time
                </Dropdown.Item>
                <Dropdown.Item eventKey='INTERN'>
                intern
                </Dropdown.Item>
              </DropdownButton>
            </div>

            <div className="flex  place-items-center">
            <Form.Check 
            type="checkbox"
            id="Remote Only"
            label="Remote Only"
            onChange={handleRemoteChange}
          />

              </div>
            <button 
            className="bg-primary text-white font-bold text-xl px-8 py-2 rounded-md justify-self-end md:px-5 lg:px-8 hover:bg-primaryLight"
            onClick={searchClickHandler}>
              Search
            </button>
          {/* </div> */}
        </div>
      </div>
    );
  }
  export default RecommendControlLarge;