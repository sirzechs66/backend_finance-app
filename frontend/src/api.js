export async function fetchUsers() {
  const res = await fetch(`${import.meta.env.VITE_API_URL}/users/`);
  return res.json();
}
