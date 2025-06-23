import { useState } from "react";
import { ToastContainer, toast } from "react-toastify";
import Button from "@mui/material/Button";

import "../static/css/login.css";
import Post from "../utils/routes/post.js";
import Data from "../utils/data.jsx";
import { useNavigate } from "react-router-dom";
import SimpleBackdrop from "../components/UI/buttons/Loading.jsx";

const Login = () => {
  const navigate = useNavigate();
  const { setToken } = Data();

  const [open, setOpen] = useState(false);

  const handelSubmit = () => {
    event.preventDefault();

    const formData = new FormData(event.target);

    if (!formData.get("phone")) {
      return toast.error("Имя не было указен!");
    } else if (!formData.get("password")) {
      return toast.error("Пароль не было указен!");
    }

    handleOpen();
    try {
      Post("auth/login", formData).then((r) => {
        console.log(r?.data);
        if (r?.status === 200 || r?.status === 201) {
          setToken(r?.data);

          navigate("/");
        } else if (r?.status === 400) {
          toast.error("Пароль или номер телефона неверны!");
        } else {
          console.log(r?.data);

          toast.error("Что-то пошло не так!");
        }
      });
    } finally {
      handleClose();
    }
  };

  const handleClose = () => {
    setOpen(false);
  };
  const handleOpen = () => {
    setOpen(true);
  };

  const [phone, setPhone] = useState("Тел");

  const handlePhoneChange = (e) => {
    let input = e.target.value;

    // Убираем всё, кроме цифр
    const onlyNumbers = input.replace(/\D/g, "");

    // Всегда добавляем +996 в начале
    if (!onlyNumbers.startsWith("996")) {
      input = "+996" + onlyNumbers.replace(/^996/, "");
    } else {
      input = "+" + onlyNumbers;
    }

    setPhone(input);
  };

  return (
    <>
      <form method="post" className="form_auth" onSubmit={handelSubmit}>
        <div className="container">
          <h2>Login</h2>

          <label className="label_form">
            <input
              type="tel"
              placeholder="Тел (+996)"
              name="phone"
              value={phone}
              onChange={handlePhoneChange}
              required
            />
          </label>

          <label className="label_form">
            <input
              type="password"
              name="password"
              placeholder="Пароль"
              required
            />
          </label>

          <SimpleBackdrop open={open} none_button={true}/>
        </div>
      </form>
      <ToastContainer />
    </>
  );
};

export default Login;
