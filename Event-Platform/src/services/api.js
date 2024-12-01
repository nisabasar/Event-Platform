import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
});

// Authorization başlığını sadece oturum açmış kullanıcılar için ekleyin
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("authToken"); // LocalStorage'da token saklandığını varsayıyoruz
  if (token && config.url !== "register/") {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
