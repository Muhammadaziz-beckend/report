const Add = ({ href }) => {
  return (
    <button onClick={() => (location.href = href)} className="add">
      +
    </button>
  );
};

export default Add;
