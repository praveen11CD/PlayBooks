/* eslint-disable react-hooks/exhaustive-deps */
import Heading from "../../Heading.js";
import { useEffect, useState } from "react";
import SuspenseLoader from "../../Skeleton/SuspenseLoader.js";
import TableSkeleton from "../../Skeleton/TableLoader.js";
import ExecutionsTable from "./ExecutionsTable.jsx";
import Search from "../../common/Search/index.tsx";
import { useSearchQuery } from "../../../store/features/search/api/searchApi.ts";

const context = "WORKFLOW_EXECUTION";

const WorkflowExecutionList = () => {
  const [pageMeta, setPageMeta] = useState({ limit: 10, offset: 0 });
  const { data, isFetching, refetch } = useSearchQuery({
    context,
    ...pageMeta,
  });
  const workflowsList = data?.workflow_executions;
  const total = data?.meta?.total_count;

  useEffect(() => {
    if (!isFetching) refetch(pageMeta);
  }, [pageMeta]);

  const pageUpdateCb = (page) => {
    setPageMeta(page);
  };

  return (
    <div>
      <Heading
        heading={"Workflow Executions"}
        onTimeRangeChangeCb={false}
        onRefreshCb={false}
      />
      <main className="flex flex-col gap-4 p-2 pt-4">
        <Search
          context={context}
          limit={pageMeta.limit}
          offset={pageMeta.offset}
        />
        <SuspenseLoader loading={isFetching} loader={<TableSkeleton />}>
          <ExecutionsTable
            workflowsList={workflowsList}
            total={total}
            pageSize={pageMeta ? pageMeta?.limit : 10}
            pageUpdateCb={pageUpdateCb}
            tableContainerStyles={
              workflowsList?.length
                ? {}
                : { maxHeight: "35vh", minHeight: "35vh" }
            }
            refreshTable={refetch}></ExecutionsTable>
        </SuspenseLoader>
      </main>
    </div>
  );
};

export default WorkflowExecutionList;
