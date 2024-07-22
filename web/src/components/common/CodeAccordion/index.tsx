import React, { forwardRef } from "react";
import Editor from "react-simple-code-editor";
import hljs from "highlight.js/lib/core";
import python from "highlight.js/lib/languages/python";
import json from "highlight.js/lib/languages/json";
import { CodeAccordionPropTypes, LanguageTypes } from "./types/index.ts";
import isJSONString from "./utils/isJSONString.ts";

hljs.registerLanguage("python", python as any);
hljs.registerLanguage("json", json as any);

const CodeAccordion = forwardRef<HTMLDivElement, CodeAccordionPropTypes>(
  ({ code, language, label, onValueChange = () => {} }, ref) => {
    const value =
      language === LanguageTypes.JSON
        ? isJSONString(code)
          ? JSON.parse(JSON.stringify(code, null, 2))
          : JSON.stringify(code, null, 2)
        : code;

    return (
      <div ref={ref}>
        <p className="font-semibold text-violet-500 text-xs">{label}</p>
        <Editor
          value={value}
          className="border rounded outline-none max-h-[150px] !overflow-y-auto"
          onValueChange={onValueChange}
          highlight={(code: string) =>
            hljs.highlight(code, {
              language,
            }).value
          }
          disabled
          padding={10}
          style={{
            fontFamily: '"Fira code", "Fira Mono", monospace',
            fontSize: 12,
          }}
        />
      </div>
    );
  },
);

export default CodeAccordion;
