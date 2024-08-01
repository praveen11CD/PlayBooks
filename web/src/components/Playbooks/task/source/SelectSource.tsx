import { useDispatch, useSelector } from "react-redux";
import { updateSource } from "../../../../store/features/playbook/playbookSlice.ts";
import useIsPrefetched from "../../../../hooks/playbooks/useIsPrefetched.ts";
import { InputTypes } from "../../../../types/inputs/inputTypes.ts";
import CustomInput from "../../../Inputs/CustomInput.tsx";
import useCurrentTask from "../../../../hooks/playbooks/task/useCurrentTask.ts";
import { commonKeySelector } from "../../../../store/features/common/commonSlice.ts";

function SelectSource({ id }) {
  const { connectorOptions } = useSelector(commonKeySelector);
  const [task, currentStepId] = useCurrentTask(id);
  const dispatch = useDispatch();
  const isPrefetched = useIsPrefetched();

  function handleSourceChange(id) {
    dispatch(updateSource({ id: currentStepId, value: id }));
  }

  return (
    <div className="flex flex-col">
      <CustomInput
        label="Data Source"
        options={connectorOptions}
        inputType={InputTypes.DROPDOWN}
        value={task?.source ?? ""}
        handleChange={handleSourceChange}
        disabled={!!isPrefetched}
      />
    </div>
  );
}

export default SelectSource;
