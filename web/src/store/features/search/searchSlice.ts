import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { RootState } from "../../index.ts";

interface SearchState {
  value: string;
  isOpen: boolean;
  filteredOptions: any[];
  selected: string[];
  highlightedIndex: number;
  options: any[];
}

const initialState: SearchState = {
  value: "",
  isOpen: false,
  filteredOptions: [],
  selected: [],
  highlightedIndex: 0,
  options: [],
};

const searchSlice = createSlice({
  name: "search",
  initialState,
  reducers: {
    setValue: (state, action: PayloadAction<string>) => {
      state.value = action.payload;
      state.highlightedIndex = 0;
    },
    setIsOpen: (state, action: PayloadAction<boolean>) => {
      state.isOpen = action.payload;
    },
    setFilteredOptions: (state, action: PayloadAction<string[]>) => {
      state.filteredOptions = action.payload;
    },
    setSelected: (state, action: PayloadAction<string[]>) => {
      state.selected = action.payload;
    },
    addSelected: (state, { payload }: PayloadAction<string>) => {
      if (!state.selected.includes(payload)) {
        state.selected.push(payload);
      }
    },
    removeSelected: (state, action: PayloadAction<string>) => {
      state.selected = state.selected?.filter(
        (item) => item !== action.payload,
      );
    },
    setHighlightedIndex: (state, action: PayloadAction<number>) => {
      state.highlightedIndex = action.payload;
    },
    setOptions: (state, action: PayloadAction<string[]>) => {
      state.options = action.payload;
    },
  },
});

export const {
  setValue,
  setIsOpen,
  setFilteredOptions,
  setSelected,
  addSelected,
  removeSelected,
  setHighlightedIndex,
  setOptions,
} = searchSlice.actions;

export default searchSlice.reducer;

export const searchSelector = (state: RootState) => state.search;
