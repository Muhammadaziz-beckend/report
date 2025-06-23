import { useState } from "react";

import SimpleBackdrop from "../components/UI/buttons/Loading";
import Post from "../utils/routes/post";
import Config from "../utils/data";
import { useNavigate } from "react-router-dom";

const AddObjects = () => {
  const { token } = Config();
  const navigate = useNavigate();

  const [open, setOpen] = useState(false);

  const handelOpen = () => setOpen(true);
  const handelClose = () => setOpen(false);

  const handelSubmit = () => {
    event.preventDefault();

    const formData = new FormData(event.target);

    try {
      handelOpen();
      Post("objects/", formData, token).then((r) => {
        if (r?.status === 201) {
          navigate("/");
        } else {
          console.log(r);
        }
      });
    } finally {
      handelClose();
    }
  };

  return (
    <>
      <form method="post" className="form" onSubmit={handelSubmit}>
        <div className="from_container">
          <h2>Добавить объект</h2>

          <div className="form-floating">
            <input
              name="name"
              type="text"
              className="form-control"
              id="floatingInput"
              placeholder="Названия"
              required
            />
            <label for="floatingInput">Названия</label>
          </div>

          <button
            type="submit"
            className="btn btn-primary btn_submit"
          >
            Создать
          </button>
        </div>
      </form>
      <SimpleBackdrop open={open} none_button={false} />
    </>
  );
};

export default AddObjects;
