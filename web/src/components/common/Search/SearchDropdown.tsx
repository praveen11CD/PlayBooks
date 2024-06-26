import React from "react";
import useSearch from "../../../hooks/useSearch.ts";
import { useDispatch } from "react-redux";
import { addSelected } from "../../../store/features/search/searchSlice.ts";
import { highlightMatch } from "../../../utils/search/highlightMatch.tsx";

function SearchDropdown() {
  const { value, filteredOptions, highlightedIndex, resetState } = useSearch();
  const dispatch = useDispatch();

  return (
    <div className="origin-top-right absolute left-0 mt-2 w-full max-h-36 overflow-scroll rounded-md shadow-lg bg-white z-10">
      <div
        className="py-1"
        role="menu"
        aria-orientation="vertical"
        aria-labelledby="options-menu">
        {filteredOptions.length === 0 && (
          <p className="text-xs font-medium px-4 py-2">No matches found</p>
        )}
        {filteredOptions.map((option, index) => (
          <div
            key={index}
            className={`block px-4 py-2 text-xs hover:bg-gray-100 hover:text-gray-900 cursor-pointer font-medium ${
              index === highlightedIndex ? "bg-gray-200" : ""
            }`}
            role="menuitem"
            onClick={(e) => {
              e.preventDefault();
              dispatch(addSelected(option.label));
              resetState();
            }}>
            {highlightMatch(option.label, value)}
          </div>
        ))}
      </div>
    </div>
  );
}

export default SearchDropdown;
