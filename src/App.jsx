import React from "react";
import CityAndStores from "./components/CityAndStores";
import ShoppingPage from "./Pages/ShoppingPage";


const Header = () => (
  <div className="flex flex-col justify-center h-screen text-center">
    <h1 className="text-7xl font-extrabold text-white mb-4">CartiB</h1>
    <p className="text-2xl text-white mb-8">Shop smart, compare fast, and cart it your way!</p>
  </div>
);

const GetStartedButton = () => (
  <button className="px-8 py-4 bg-[#FB6107] text-white font-extrabold rounded-full shadow-md hover:bg-[#ffffff] hover:text-[#FB6107] transition duration-300 ease-in-out">
    <h1 className="text-4xl">Get Started</h1>
  </button>
);

function App() {
  return (
    <>
    
    <div className="app w-full h-screen flex">
      <div className="w-1/2 h-screen bg-[#FB6107] flex z-[-99] items-center justify-center">
        <Header />
      </div>
      <div className="w-1/2 h-screen flex relative justify-center items-center">
        <GetStartedButton />
        
      </div>
      
    </div>
    <div>

      <CityAndStores/>
    </div>
    <div>
      <ShoppingPage/>
    </div>
    </>
  );
}

export default App;





