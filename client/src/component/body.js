import "../App.css";
import SearchControlSmall from './searchControlSmall.js';
import SearchControlLarge from './searchControlLarge.js';
import { useEffect, useState } from 'react'
import JobCard from './JobCard.js';
import JobViewSkeleton from './jobViewSkeleton.js'
function Body(){
    const [data, setData] = useState([{}])
    const [feed, setFeed] = useState([])
    const [isLoading, setLoading] = useState(true)
    const [info, setInfo] = useState({
      rolename: '', location: '', date_posted: '', remote_jobs_only: false, employment_type:' '
    });

    async function fetchedJobsData() {
      setLoading(true)
      // const response = await fetch("/search/software engineer/New York/any/false/fulltime")
      // US location
      // detail into apply link
      if(info.rolename===''){
        info.rolename="Data Scientist"
        info.location= "United States"
        info.date_posted="any time"
        info.remote_jobs_only= 'n'
        info.employment_type="FULLTIME"
      }
      console.log("/search/"+info.rolename+"/"+info.location+"/"+info.date_posted+"/"+info.remote_jobs_only+"/"+info.employment_type)
      const response = await fetch( "/search/"+info.rolename+"/"+info.location+"/"+info.date_posted+"/"+info.remote_jobs_only+"/"+info.employment_type)
      if (response.ok) {
        var dataJson = await response.json()
        dataJson = dataJson.data
        // dataJson = dataJson
        // Extract title, author and post id:
        console.log(dataJson)
        const posts = dataJson.map(post => {
          return {
            title: post.job_title,
            author: post.job_publisher,
            id: post.job_id
          }
      })
      // Save posts to feed state:
      
      setFeed(posts)
      setData(dataJson)
      setLoading(false)
      
    }
  }

    useEffect(() => {
      // Invoke the fetchedJobsData function:
      fetchedJobsData()
      }, []);
      
    useEffect(() => {
      console.log('info', info)
      fetchedJobsData()
    }, [info])

    return (
      <div>
        <SearchControlSmall /> 
        <SearchControlLarge changeInfo={setInfo} />
       
        <div className=" grid grid-cols-1 sm:grid-cols-1  md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-4 gap-4 mt-20 px-9 md:px-9 sm:px-20 ">

            {isLoading ? [1,2,3,4,5,6,7,8,9,10,11,12].map(val => {
                return <JobViewSkeleton/>
            }) :  feed.map(job => {
               return data.map(job => <JobCard key={job.job_id} job={job}/>)
          })}
           {/* Mock Jobs Data */}
           {/* {Data.map(job => <JobCard key={job.id} job={job}/>)} */}
          

        </div>
      </div>

    );
}


 
export default Body ;