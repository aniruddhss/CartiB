import React, { useState } from "react";
import { FaShoppingCart } from "react-icons/fa";

const CartIcon = () => {
  const [cartCount, setCartCount] = useState(0); // Initial cart item count

  // Function to simulate adding items to the cart
  const addItemToCart = () => {
    setCartCount((prevCount) => prevCount + 1);
  };

  return (
    <div className="relative flex items-center space-x-4">
      {/* Cart Icon */}
      <div className="relative">
        <FaShoppingCart size={26} className="text-[#ffffff] cursor-pointer" />
        {cartCount > 0 && (
          <span className="absolute -top-2 -right-2 bg-[#FF9F1C] text-white text-xs font-bold rounded-full px-2 py-0.5">
            {cartCount}
          </span>
        )}
      </div>

      {/* Button to simulate adding to cart */}
      {/* <button
        onClick={addItemToCart}
        className="px-4 py-2 bg-[#FF9F1C] text-white rounded-lg hover:bg-[#e48918] focus:outline-none"
      >
        Add Item
      </button> */}
    </div>
  );
};

export default CartIcon;

