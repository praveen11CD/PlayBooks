/* eslint-disable react-hooks/exhaustive-deps */
import { useState } from "react";
import { Tooltip } from "@mui/material";
import styles from "../playbooks.module.css";
import { Launch } from "@mui/icons-material";
import Notes from "./Notes.jsx";
import DeleteIcon from "@mui/icons-material/Delete";
import PlayArrowIcon from "@mui/icons-material/PlayArrow";
import { useDispatch, useSelector } from "react-redux";
import {
  addExternalLinks,
  changeProgress,
  deleteStep,
  toggleExternalLinkVisibility,
  updateStep,
} from "../../../store/features/playbook/playbookSlice.ts";
import { getTaskFromStep } from "../../../utils/parser/playbook/stepsToplaybook.ts";
import { getStepTitle } from "../utils.jsx";
import ExternalLinks from "./ExternalLinks.jsx";
import { rangeSelector } from "../../../store/features/timeRange/timeRangeSlice.ts";
import { useExecutePlaybookMutation } from "../../../store/features/playbook/api/index.ts";
import Query from "./Query.jsx";

function Step({ step, index }) {
  const [addQuery, setAddQuery] = useState(
    step?.isPrefetched ?? step.source ?? false,
  );
  const [outputs, setOutputs] = useState([]);
  const dispatch = useDispatch();
  const timeRange = useSelector(rangeSelector);
  const [triggerExecutePlaybook] = useExecutePlaybookMutation();

  const updateCardByIndex = (key, value) => {
    dispatch(
      updateStep({
        index,
        key,
        value,
      }),
    );
  };

  function handleDeleteClick(index) {
    dispatch(deleteStep(index));
  }

  const queryForStepTask = async (step, cb) => {
    if (Object.keys(step.errors ?? {}).length > 0) {
      cb({}, false);
      return;
    }

    let body = {
      playbook_task_definition: getTaskFromStep(step),
      meta: {
        time_range: timeRange,
      },
    };

    if (
      Object.keys(body?.playbook_task_definition?.documentation_task ?? {})
        .length > 0
    ) {
      cb(
        {
          step: step,
          data: null,
          timestamp: new Date().toTimeString(),
          title: getStepTitle(step),
        },
        true,
      );
      return;
    }

    try {
      const response = await triggerExecutePlaybook(body).unwrap();
      cb(
        {
          step: step,
          data: response,
          timestamp: new Date().toTimeString(),
          title: getStepTitle(step),
        },
        true,
      );
    } catch (e) {
      updateCardByIndex("outputError", e.err ?? e.message);
      console.error(e);
      cb(
        {
          error: e.err,
        },
        false,
      );
    }
  };

  const handleExecute = () => {
    dispatch(changeProgress({ index: index, progress: true }));

    updateCardByIndex("outputLoading", true);
    updateCardByIndex("showOutput", true);
    updateCardByIndex("outputError", null);
    updateCardByIndex("output", null);
    updateCardByIndex("showError", false);

    queryForStepTask(step, function (res) {
      if (Object.keys(res ?? {}).length > 0) {
        if (res.err) {
          updateCardByIndex("showOutput", true);
          updateCardByIndex("outputLoading", false);
          return;
        }
        setOutputs([res, ...outputs]);
        updateCardByIndex("showOutput", true);
        updateCardByIndex("output", res);
        updateCardByIndex("outputLoading", false);
        changeCardExecutionProgressStatus(false);
      } else {
        updateCardByIndex("showError", true);
        updateCardByIndex("showOutput", false);
        updateCardByIndex("outputLoading", false);
      }
    });
  };

  function changeCardExecutionProgressStatus(status) {
    dispatch(changeProgress({ index, status }));
  }

  const toggleExternalLinks = () => {
    dispatch(toggleExternalLinkVisibility({ index }));
  };

  const setLinks = (links) => {
    dispatch(addExternalLinks({ index, externalLinks: links }));
  };

  return (
    <div className={styles["step-card"]}>
      <div
        className={styles["step-card-content"]}
        style={{ paddingBottom: "0px" }}>
        <div className={styles["step-name"]}>
          {step.isPrefetched && step.description && (
            <div className={styles.head}>
              <div className={styles.extLinks}>
                {step.externalLinks?.map((link, i) => (
                  <a
                    key={i}
                    href={link.url}
                    target="_blank"
                    rel="noreferrer"
                    className={styles.extLink}>
                    {link?.name || link.url} <Launch />
                  </a>
                ))}
              </div>
            </div>
          )}
        </div>
        <div className={styles["step-section"]}>
          <div className={styles["step-info"]}>
            <div>
              {/* <SelectOne
                options={options}
                selected={step.stepType}
                onChange={(id) => {
                  dispatch(setStepType({ index, stepType: id }));
                }}
              /> */}
              <div
                className={styles["addConditionStyle"]}
                onClick={() => setAddQuery(true)}>
                <b className="add_data">{!addQuery ? "+ Add Data" : "Data"}</b>
              </div>

              {addQuery && <Query step={step} index={index} />}
              {/* <HandleSelectedType
                selectedId={step.stepType}
                step={step}
                index={index}
              /> */}
            </div>
          </div>
          <Notes step={step} index={index} />
          <div className={styles["step-buttons"]}>
            {step.source && (
              <button
                className={styles["pb-button"]}
                onClick={() => handleExecute(index)}>
                <Tooltip title="Run this Step">
                  <>
                    Run <PlayArrowIcon />
                  </>
                </Tooltip>
              </button>
            )}
            <button
              className={styles["pb-button"]}
              onClick={() => handleDeleteClick(index)}>
              <Tooltip title="Remove this Step">
                <DeleteIcon />
              </Tooltip>
            </button>
          </div>
          {!step.isPrefetched && (
            <div>
              <div>
                <div
                  className={styles["addConditionStyle"]}
                  onClick={toggleExternalLinks}>
                  <b className="ext_links">
                    {step.showExternalLinks ? "-" : "+"}
                  </b>{" "}
                  Add External Links
                </div>

                {step.showExternalLinks && (
                  <ExternalLinks
                    links={step.externalLinks}
                    setLinks={setLinks}
                  />
                )}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Step;
