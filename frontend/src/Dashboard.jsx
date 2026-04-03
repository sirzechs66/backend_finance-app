import { useEffect, useState } from 'react';
import { fetchUsers } from './api';

export default function Dashboard({ onLogout }) {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    fetchUsers().then(setUsers);
  }, []);
  return (
    <div className="dashboard-container">
      <header>
        <h1>Finance Dashboard</h1>
        <button className="logout-btn" onClick={onLogout}>Logout</button>
      </header>
      <section className="user-list-section">
        <h2>Users</h2>
        <ul className="user-list">
          {users.map(u => (
            <li key={u.id} className="user-item">{u.username} ({u.email})</li>
          ))}
        </ul>
      </section>
    </div>
  );
}
