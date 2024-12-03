import React, { useState } from "react";

const MultiSelectDropdown = () => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false); // Tracks dropdown visibility
  const [selectedOptions, setSelectedOptions] = useState([]); // Tracks finalized selections
  const [tempSelected, setTempSelected] = useState([]); // Tracks temporary selections within dropdown
  const options = ["BlinkIt","JioMart","Swiggy Instamart", "Ondoor"]; // Options for the dropdown

  // Toggle dropdown visibility
  const toggleDropdown = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  // Handle checkbox selection
  const handleCheckboxChange = (option) => {
    setTempSelected((prev) =>
      prev.includes(option)
        ? prev.filter((item) => item !== option) // Remove if already selected
        : [...prev, option] // Add if not selected
    );
  };

  // Finalize selections on clicking "Done"
  const handleDone = () => {
    setSelectedOptions(tempSelected);
    setIsDropdownOpen(false);
  };

  // Remove an option from the finalized selections
  const handleRemoveTag = (option) => {
    setSelectedOptions((prev) => prev.filter((item) => item !== option));
    setTempSelected((prev) => prev.filter((item) => item !== option)); // Keep temporary state in sync
  };

  return (
    <div className="flex flex-col items-center">
      <label htmlFor="dropdown" className="mb-2 text-lg font-medium text-gray-700">
        Select Stores
      </label>

      {/* Dropdown Button */}
      <div className="relative w-64">
        <button
          id="dropdown"
          onClick={toggleDropdown}
          className="w-full px-4 py-2 border border-gray-300 rounded-lg bg-white text-gray-700 hover:border-gray-400 focus:outline-none"
        >
          {selectedOptions.length > 0
            ? `Selected (${selectedOptions.length})`
            : "Choose stores"}
        </button>

        {/* Dropdown Menu */}
        {isDropdownOpen && (
          <div className="absolute mt-2 w-full bg-white border border-gray-300 rounded-lg shadow-lg max-h-48 overflow-y-auto z-10">
            {options.map((option) => (
              <div key={option} className="px-4 py-2">
                <label className="flex items-center space-x-2">
                  <input
                    type="checkbox"
                    checked={tempSelected.includes(option)}
                    onChange={() => handleCheckboxChange(option)}
                    className="form-checkbox text-[#FF9F1C] rounded focus:ring-[#FF9F1C]"
                  />
                  <span>{option}</span>
                </label>
              </div>
            ))}
            {/* Done Button */}
            <div className="flex justify-center my-2">
              <button
                onClick={handleDone}
                className="px-4 py-2 bg-[#7CB518] text-white rounded-lg hover:bg-[#5C8001] focus:outline-none"
              >
                Done
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Selected Tags */}
      <div className="mt-4 flex flex-wrap gap-2">
        {selectedOptions.map((option) => (
          <div
            key={option}
            className="flex items-center space-x-2 bg-[#7CB518] text-white px-3 py-1 rounded-full border border-[#7CB518] shadow-sm"
          >
            <span>{option}</span>
            <button
              onClick={() => handleRemoveTag(option)}
              className="font-extrabold hover:text-red-700 transition duration-200 ease-in-out"
            >
              ✕
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MultiSelectDropdown;
