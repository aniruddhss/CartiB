import React, { useState } from "react";

const SearchBar = () => {
  const [searchTerm, setSearchTerm] = useState("");

  const handleInputChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSearch = (event) => {
    event.preventDefault(); // Prevent default form submission
    console.log("Searching for:", searchTerm);
    // Optionally clear the search term after search
    setSearchTerm("");
  };

  return (
    <div className="flex justify-center items-center py-6">
      <form className="flex w-3/4 md:w-1/2 lg:w-1/3" onSubmit={handleSearch}>
        {/* Search Input */}
        <input
          type="text"
          placeholder="Search for items..."
          value={searchTerm}
          onChange={handleInputChange}
          aria-label="Search input"
          className="flex-grow px-10 py-3 pl-4 text-gray-700 bg-white border border-none rounded-l-full shadow-md focus:outline-none focus:border-[#FB6107]"
        />
        {/* Search Button */}
        <button
          type="submit" // Change to type="submit"
          aria-label="Search button"
          className="px-10 bg-[#FFFFFF] text-[#FB6107] font-bold rounded-r-full hover:bg-[#FB6107] hover:text-white transition duration-300 ease-in-out focus:outline-[#FFFFFF]"
        >
          Search
        </button>
      </form>
    </div>
  );
};

export default SearchBar;