/* eslint-disable react-hooks/exhaustive-deps */
import Heading from "../Heading";
import { useEffect } from "react";
import useToggle from "../../hooks/useToggle";
import SuspenseLoader from "../Skeleton/SuspenseLoader";
import TableSkeleton from "../Skeleton/TableLoader";
import InviteUserOverlay from "./InviteUserOverlay";
import UserTable from "./UserTable";
import { useGetAccountUsersQuery } from "../../store/features/auth/api/index.ts";
import usePagination from "../../hooks/usePagination.ts";
import PaginatedTable from "../PaginatedTable.tsx";

const InviteTeam = () => {
  const { isOpen: isActionOpen, toggle } = useToggle();
  const { reset } = usePagination();
  const { data, isLoading, isFetching, refetch } = useGetAccountUsersQuery();
  const total = data?.meta?.total_count;

  const handleInviteUsers = () => {
    toggle();
  };

  useEffect(() => {
    if (!isFetching) refetch();

    return () => {
      reset();
    };
  }, []);

  return (
    <div>
      <Heading
        heading={"Invite Team"}
        onTimeRangeChangeCb={false}
        onRefreshCb={false}
      />
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
          padding: "1.5rem",
          justifyContent: "space-between",
        }}>
        <button
          className="text-sm bg-violet-600 hover:bg-violet-700 px-4 py-2  rounded-lg"
          onClick={handleInviteUsers}
          style={{ color: "white", marginTop: "0px", marginRight: "10px" }}>
          + Invite Users
        </button>
      </div>
      <SuspenseLoader loading={isLoading} loader={<TableSkeleton />}>
        <h1
          style={{
            fontSize: "1.25rem",
            fontWeight: "600",
            color: "#1F2937",
            marginBottom: "1.5rem",
            margin: "0rem 0.5rem 0.5rem 0.5rem",
          }}>
          Active Users
        </h1>
        <PaginatedTable
          renderTable={UserTable}
          data={data?.users}
          total={total}
          tableContainerStyles={
            data?.length ? {} : { maxHeight: "35vh", minHeight: "35vh" }
          }
        />
      </SuspenseLoader>
      <InviteUserOverlay isOpen={isActionOpen} toggleOverlay={toggle} />
    </div>
  );
};

export default InviteTeam;
