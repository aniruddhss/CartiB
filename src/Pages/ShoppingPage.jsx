import React from 'react'
import SearchBar from '../components/SearchBar';
import CartIcon from '../components/Carticon';

const Header = () => (
    <div className='w-full h-[15%] bg-[#FB6107] flex justify-between items-center relative'>
        <h1 className="text-6xl font-extrabold text-white px-6 py-5">CartiB</h1>
        <div className='mt-2 mr-[20%]'>
        <SearchBar />

        </div>
        <div className='mr-10'>

        <CartIcon/>
        </div>
        
        
    </div>
);
const Bod = () => (
    <div className="w-full h-[85%] bg-white flex flex-col justify-center items-center">
    </div>
);

export default function ShoppingPage() {
  return (
    <div>
        <div className='w-full h-screen'>

            <Header />
            <Bod />
        </div>
    </div>
  )
}
