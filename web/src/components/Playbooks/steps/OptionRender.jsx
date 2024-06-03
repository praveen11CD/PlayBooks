import React from "react";
import { useDispatch } from "react-redux";
import { updateStep } from "../../../store/features/playbook/playbookSlice.ts";
import SelectComponent from "../../SelectComponent";
import ValueComponent from "../../ValueComponent";
import MultiSelectDropdown from "../../common/MultiSelectDropdown/index.tsx";
import useIsPrefetched from "../../../hooks/useIsPrefetched.ts";

export default function OptionRender({ data, removeErrors, task, stepIndex }) {
  const dispatch = useDispatch();
  const isPrefetched = useIsPrefetched();

  const handleChange = (...args) => {
    if (data.handleChange) {
      data.handleChange(...args);
    } else {
      dispatch(updateStep({ index: stepIndex, key: data.key, value: args[0] }));
    }

    removeErrors(data.key);
  };

  const isValidUrl = (url) => {
    try {
      new URL(url);
      return true;
    } catch (e) {
      return false;
    }
  };

  const handleTextAreaChange = (e) => {
    const val = e.target.value;
    if (data.handleChange) {
      data.handleChange(e);
    } else {
      dispatch(updateStep({ index: stepIndex, key: data.key, value: val }));
    }

    removeErrors(data.key);
  };

  const multiSelectChange = (...args) => {
    if (data.handleChange) {
      data.handleChange(...args);
    } else {
      dispatch(updateStep({ index: stepIndex, key: data.key, value: args[0] }));
    }

    removeErrors(data.key);
  };

  const error = data.key
    ? task.showError && !data.selected && !task[`${data.key}`]
    : false;

  switch (data.type) {
    case "options":
      // if (!(data.options?.length > 0)) return;
      return (
        <div className={`flex flex-col`}>
          <p
            style={{
              fontSize: "13px",
              color: "#676666",
            }}>
            <b>{data.label}</b>
          </p>
          <SelectComponent
            key={data.key}
            data={data.options ?? []}
            placeholder={`Select ${data.label}`}
            onSelectionChange={handleChange}
            selected={data.selected ?? task[`${data.key}`]}
            searchable={true}
            disabled={isPrefetched || data.disabled}
            error={error}
            containerClassName={"w-56"}
            {...data.additionalProps}
          />
        </div>
      );
    case "text-row":
    case "text":
      return (
        <div
          className={`flex ${
            data.type === "text"
              ? "flex-col"
              : "flex-row items-center justify-center gap-2"
          } ${data.type === "text" ? "" : "mt-2"}`}>
          <p
            style={{
              marginTop: data.type === "text" ? "10px" : "",
              fontSize: "13px",
              color: "#676666",
            }}>
            <b>{data.label}</b>
          </p>
          <ValueComponent
            key={data.key}
            placeHolder={`Enter ${data?.label}`}
            valueType={"STRING"}
            onValueChange={handleChange}
            value={data.selected || task[`${data.key}`]}
            error={error}
            disabled={isPrefetched}
            {...data.additionalProps}
          />
        </div>
      );
    case "multiline":
      return (
        <div key={data.key} className="flex flex-col w-full">
          <p className="mt-2 text-sm text-gray-500">
            <b>{data.label}</b>
          </p>
          <textarea
            className={
              "w-full border border-gray-300 p-1 rounded mt-1 text-sm resize-none text-[#676666] h-32"
            }
            rows={4}
            value={data.value ?? data.selected ?? task[`${data.key}`]}
            onChange={handleTextAreaChange}
            disabled={isPrefetched || data.disabled}
            style={error ? { borderColor: "red" } : {}}
          />
        </div>
      );

    case "button":
      return (
        <button
          className="p-1 border-2 w-fit border-purple-500 hover:bg-purple-500 text-purple-500 hover:text-white transition-all rounded cursor-pointer leading-none"
          onClick={data.handleClick}>
          {data.label}
        </button>
      );

    case "iframe-render":
      return (
        <>
          {
            isValidUrl(data.value) ? (  
              <iframe
                src={data.value}
                title="iframe"
                className="w-full h-full"
                style={{ height: "500px", marginTop: "10px", border: "1px solid #ccc"}}
                allowFullScreen
              />
            ) : (
              <p style={{ color: "red", marginTop: "10px", fontSize: '12px' }} >Invalid URL</p>
            )
          }
        </>
      );

    case "multi-select":
      // if (!(data.options?.length > 0)) return;
      return (
        <div key={data.id}>
          <MultiSelectDropdown
            label={data.label}
            options={data.options}
            error={data.error}
            disabled={isPrefetched || data.disabled}
            additionalProps={data.additionalProps}
            placeholder={data.placeholder}
            selectedDisplayKey={data.selectedDisplayKey}
            multiSelectChange={multiSelectChange}
            selectedValuesKey={data.selectedValuesKey ?? data.key}
            task={task}
          />
        </div>
      );
    default:
      return;
  }
}
