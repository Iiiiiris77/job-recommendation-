import "../App.css";
import { useEffect, useState } from 'react'
import JobCard from './JobCard.js';
import JobViewSkeleton from './jobViewSkeleton.js'
// import RecommendControlLarge from './recommendControlLarge.js'
function RecommendBody(){
    const [data, setData] = useState([{}])
    const [feed, setFeed] = useState([])
    const [isLoading, setLoading] = useState(true)
    const [info, setInfo] = useState({
      username: 'Yufan', userinfo: 'Software Engineering'
    });
    async function fetchedJobsData() {
        setLoading(true)
        if(info.username===''){
          info.username="Researcher"
          info.userinfo= "New York"
        }
        console.log("/recommend/"+info.username+"/"+info.userinfo)
        const response = await fetch( "/recommend/"+info.username+"/"+info.userinfo)
        if (response.ok) {
          var dataJson = await response.json()
          dataJson = dataJson
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
    return (
        <div>
         
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
export default RecommendBody ;