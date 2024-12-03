import React from 'react'
import CityDropdown from './Dropdownmenu';
import MultiSelectDropdown from './Multiselectdropdown';

const Header = () => (
    <div className='w-full h-[15%] bg-[#FB6107] flex'>
        <h1 className="text-6xl font-extrabold text-white px-6 py-5">CartiB</h1>
    </div>
  );
const Bod = () => (
    <div className="w-full h-[85%] bg-white flex flex-col justify-center items-center">
        <div className='flex space-x-[20vw] mb-[10%]'> 
            <CityDropdown />
            <MultiSelectDropdown />
        </div>
            <StartShoppingButton/>
    </div>
);
const StartShoppingButton = () => (
    <button className="px-8 py-4 bg-[#FB6107] text-white font-extrabold rounded-full shadow-md hover:bg-[#ffffff] hover:text-[#FB6107] transition duration-300 ease-in-out">
      <h1 className="text-lg">Start Shopping</h1>
    </button>
  );

function CityAndStores() {
  return (
    <div className='w-full h-screen'>
        <Header/>
        <Bod/>
        
        

    </div>
  )
}

export default CityAndStores