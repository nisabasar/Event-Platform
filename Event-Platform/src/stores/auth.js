import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: null,
    role: null, // user veya admin
  }),
  actions: {
    setAuth(token, role) {
      this.token = token;
      this.role = role;
    },
    clearAuth() {
      this.token = null;
      this.role = null;
    },
  },
});
