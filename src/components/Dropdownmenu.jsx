import React, { useState } from 'react';

const CityDropdown = () => {
  const [selectedCity, setSelectedCity] = useState(''); // State to store selected city
  const cities = ['Bhopal,Madhya Pradesh']; // List of cities

  const handleChange = (event) => {
    setSelectedCity(event.target.value); // Update state with the selected city
  };

  return (
    <div className="flex flex-col items-center">
      {/* Label */}
      <label htmlFor="city-select" className="text-lg font-medium mb-2 text-gray-700">
        Select a City
      </label>

      {/* Dropdown */}
      <select
        id="city-select"
        value={selectedCity}
        onChange={handleChange}
        className="px-4 py-2 border border-gray-300 rounded-lg text-gray-700 text-center focus:outline-none focus:ring-2 focus:ring-[#FB6107]"
      >
        <option value="" disabled>
          Choose a City 
        </option>
        {cities.map((city) => (
          <option key={city} value={city}>
            {city}
          </option>
        ))}
      </select>

      {/* Display Selected City */}
      {selectedCity && (
        <p className="mt-4 text-gray-700">
          You selected: <span className="font-bold">{selectedCity}</span>
        </p>
      )}
    </div>
  );
};

export default CityDropdown;
