import React from "react";

function TodoItem({ todo, deleteTodo }) {
  return (
    <li>
      {todo.task}
      <button onClick={() => deleteTodo(todo.id)}>❌</button>
    </li>
  );
}

export default TodoItem;
