import Header from "../components/headers/Headers";
import ListObjects from "../components/main/ListObjects";
import Add from "../components/UI/buttons/Add";

const Main = () => {
  return (
    <>
      <Header />
      <ListObjects />

      <div className="button_add">
        <Add href={"add/objects"} />
      </div>
    </>
  );
};

export default Main;
