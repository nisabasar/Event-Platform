<template>
  <div class="min-h-screen flex items-center justify-center">
    <div class="w-full max-w-md p-8 bg-gray-800 rounded-lg shadow-lg">
      <h2 class="text-2xl font-bold text-center mb-6">Giriş Yap</h2>
      <form @submit.prevent="login" class="space-y-4">
        <div>
          <label class="block mb-1">Kullanıcı Adı</label>
          <input
            v-model="username"
            type="text"
            class="w-full p-3 rounded bg-gray-700 border border-gray-600 focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <div>
          <label class="block mb-1">Şifre</label>
          <input
            v-model="password"
            type="password"
            class="w-full p-3 rounded bg-gray-700 border border-gray-600 focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <div class="flex justify-between items-center">
          <router-link to="/register" class="text-blue-400 hover:underline">Kayıt Ol</router-link>
          <router-link to="/forgot-password" class="text-blue-400 hover:underline">Şifremi Unuttum</router-link>
        </div>
        <button
          type="submit"
          class="w-full py-3 bg-blue-600 hover:bg-blue-700 rounded text-white font-bold"
        >
          Giriş Yap
        </button>
      </form>
      <p v-if="errorMessage" class="mt-4 text-red-500 text-sm">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  data() {
    return {
      username: "",
      password: "",
      errorMessage: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await api.post("token/", {
          username: this.username,
          password: this.password,
        });

        const { access, refresh } = response.data;
        localStorage.setItem("authToken", access);
        localStorage.setItem("refreshToken", refresh);

        // Kullanıcıyı ana sayfaya yönlendir
        this.$router.push("/home");
      } catch (error) {
        this.errorMessage = "Giriş başarısız. Lütfen bilgilerinizi kontrol edin.";
      }
    },
  },
};
</script>


<style scoped>
/* Arka plan rengini kaldırdık */
body {
  background-color: #f3f4f6;
  color: #1f2937;
}

/* Form kutusunu merkeze alırken ekranın görünümüne uyacak şekilde optimize ettik */
.min-h-screen {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.bg-gray-800 {
  background-color: #2d3748;
}

.text-blue-400:hover {
  text-decoration: underline;
}

</style>
