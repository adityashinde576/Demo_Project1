import React, { useEffect, useState } from "react";
import TodoList from "../components/TodoList";

function Home() {
  const [todos, setTodos] = useState([]);
  const [task, setTask] = useState("");

  // Load all todos from Flask
  useEffect(() => {
    fetch("http://127.0.0.1:5000/todos")
      .then(res => res.json())
      .then(data => setTodos(data))
      .catch(err => console.error("Error:", err));
  }, []);

  const addTodo = () => {
    if (!task.trim()) return;
    fetch("http://127.0.0.1:5000/todos", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ task }),
    })
      .then(res => res.json())
      .then(newTodo => setTodos([...todos, newTodo]));
    setTask("");
  };

  const deleteTodo = (id) => {
    fetch(`http://127.0.0.1:5000/todos/${id}`, { method: "DELETE" })
      .then(() => setTodos(todos.filter(t => t.id !== id)));
  };

  return (
    <div className="home">
      <h2>📝 To-Do List</h2>
      <div className="input-section">
        <input
          value={task}
          onChange={(e) => setTask(e.target.value)}
          placeholder="Enter a task"
        />
        <button onClick={addTodo}>Add</button>
        <button>demo testing</button>
      </div>

      <TodoList todos={todos} deleteTodo={deleteTodo} />
    </div>
  );
}

export default Home;
