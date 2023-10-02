import "../App.css";
function JobViewSkeleton() {
    return (
      <div className='p-8 pt-0 mx-auto bg-white   my-4  dark:bg-cardColor rounded-md shadow animate-pulse dark:bg-very-dark-blue w-76  w-full '>
        <div
          className={
            'text-white font-b  absolute grid w-12 h-12 p-2 transform -translate-y-1/2 place-items-center rounded-2xl bg-gray-400'
          }
        ></div>
        <div className='flex items-center pt-12 text-base leading-5 text-dark-grey'>
          <p className='w-6/12 h-4 bg-gray-400 rounded'></p>
        </div>
        <div className='mt-3'>
          <h2 className='w-8/12 h-4 text-lg  leading-6 bg-gray-400 rounded text-very-dark-blue dark:text-white'></h2>
        </div>
        <div>
          <p className='w-5/12 h-4 mt-3 text-base font-normal leading-5 bg-gray-400 rounded text-dark-grey'></p>
        </div>
        <div>
          <p className='w-3/12 h-4 mt-10 text-sm  bg-gray-400 rounded text-violet'></p>
        </div>
      </div>
    )
  }
  export default JobViewSkeleton ;