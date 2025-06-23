import { NavLink } from "react-router-dom";
import { useEffect, useState } from "react";

import "../../static/css/listObjects.css";
import Get from "../../utils/routes/get.js";
import Edit from "../../static/image/edit.svg";
import Delete from "../../static/image/delete.svg";
import Config from "../../utils/data";

const ListObjects = () => {
  const { token } = Config();
  const [objects, setObjects] = useState([]);

  const getObjects = () => {
    Get("objects/", token).then((r) => {
      if (r?.status == 200) {
        setObjects(r?.data);
      }
    });
  };

  useEffect(() => {
    getObjects();
  }, [token]);

  return (
    <>
      <div className="list_objects">
        <div className="container">
          <div className="list_objects_items">
            {objects.map((item) => {
              return (
                <>
                  <div className="object" key={item?.id}>
                    <NavLink to={`objects/${item?.id}/`} className="left">
                      <h3 className="top">{item?.name}</h3>
                      <p className="bottom">{Math.ceil(item?.amount_money)} сом</p>
                    </NavLink>
                    <div className="right">
                      <NavLink  to={`edit/objects/${item.id}`} className="edit">
                        <img src={Edit} alt="edit" />
                      </NavLink>
                      <NavLink className="delete">
                        <img src={Delete} alt="delete" />
                      </NavLink>
                    </div>
                  </div>
                </>
              );
            })}
          </div>
        </div>
      </div>
    </>
  );
};

export default ListObjects;
