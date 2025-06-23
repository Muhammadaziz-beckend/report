import { useEffect, useState } from "react";
import SimpleBackdrop from "../components/UI/buttons/Loading";
import Get from "../utils/routes/get";
import { useParams } from "react-router-dom";
import Config from "../utils/data";
import Patch from "../utils/routes/patch";

const EditObject = () => {
  const { id } = useParams();
  const { token } = Config();

  const [open, setOpen] = useState(false);
  const [name, setName] = useState("");

  const handelOpen = () => setOpen(true);
  const handelClose = () => setOpen(false);

  console.log(id);

  const getObject = () => {
    handelOpen();

    try {
      Get(`objects/${id}/`, token).then((r) => {
        if (r?.status === 200) {
          setName(r?.data?.name);
        }
      });
    } finally {
      handelClose();
    }
  };

  useEffect(() => {
    getObject();
  }, [id]);

  const handelSubmit = () => {
    event.preventDefault();

    const formData = new FormData(event.target);

    handelOpen();

    try {
      Patch(`objects/${id}/`, formData, token).then((r) => {
        if (r?.status === 200) {
            location.href = "/"
        }
      });
    } finally {
      handelClose();
    }
  };

  return (
    <>
      <form className="form" method="path" onSubmit={handelSubmit}>
        <div className="from_container">
          <h2>Изменения Объекта</h2>

          <div class="form-floating mb-3">
            <input
              type="text"
              className="form-control"
              id="floatingInput"
              placeholder="name"
              name="name"
              value={name}
              required
              onChange={(e) => setName(e.target.value)} // ← вот это добавь
            />
            <label for="floatingInput">Name objects</label>
          </div>

          <SimpleBackdrop open={open} text={"Изменить"} />
        </div>
      </form>
    </>
  );
};

export default EditObject;
