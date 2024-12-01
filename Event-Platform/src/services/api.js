import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/", // Backend URL
  headers: {
    "Content-Type": "application/json",
  },
});

// Token’i her istek için otomatik eklemek
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("authToken");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
