<template>
  <div class="min-h-screen flex items-center justify-center">
    <div class="w-full max-w-md p-8 bg-gray-800 rounded-lg shadow-lg">
      <h2 class="text-2xl font-bold text-center mb-6">Kayıt Ol</h2>
      <form @submit.prevent="register" class="space-y-4">
        <!-- İsim -->
        <div>
          <label class="block mb-1">İsim</label>
          <input
            v-model="form.firstName"
            type="text"
            class="w-full p-3 rounded bg-gray-700 border border-gray-600 focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <!-- Soyisim -->
        <div>
          <label class="block mb-1">Soyisim</label>
          <input
            v-model="form.lastName"
            type="text"
            class="w-full p-3 rounded bg-gray-700 border border-gray-600 focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <!-- Kullanıcı Adı -->
        <div>
          <label class="block mb-1">Kullanıcı Adı</label>
          <input
            v-model="form.username"
            type="text"
            class="w-full p-3 rounded bg-gray-700 border border-gray-600 focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <!-- E-posta -->
        <div>
          <label class="block mb-1">E-posta</label>
          <input
            v-model="form.email"
            type="email"
            class="w-full p-3 rounded bg-gray-700 border border-gray-600 focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <!-- Şifre -->
        <div>
          <label class="block mb-1">Şifre</label>
          <input
            v-model="form.password"
            type="password"
            class="w-full p-3 rounded bg-gray-700 border border-gray-600 focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <!-- Şifre (Tekrar) -->
        <div>
          <label class="block mb-1">Şifre (Tekrar)</label>
          <input
            v-model="form.passwordConfirm"
            type="password"
            class="w-full p-3 rounded bg-gray-700 border border-gray-600 focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <!-- Kayıt Ol Butonu -->
        <button
          type="submit"
          class="w-full py-3 bg-blue-600 hover:bg-blue-700 rounded text-white font-bold"
        >
          Kayıt Ol
        </button>
      </form>
      <!-- Hata Mesajı -->
      <p v-if="errorMessage" class="mt-4 text-red-500 text-sm">
        {{ errorMessage }}
      </p>
      <!-- Giriş Sayfasına Dön Bağlantısı -->
      <div class="mt-6 text-center">
        <router-link to="/login" class="text-blue-400 hover:underline">
          Giriş sayfasına dön
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  data() {
    return {
      form: {
        firstName: "",
        lastName: "",
        username: "",
        email: "",
        password: "",
        passwordConfirm: "",
      },
      errorMessage: "",
    };
  },
  methods: {
    async register() {
      // Şifre ve şifre tekrarını kontrol edin
      if (this.form.password !== this.form.passwordConfirm) {
        this.errorMessage = "Şifreler uyuşmuyor.";
        return;
      }

      try {
        // API'ye kullanıcı oluşturma isteği gönder
        await api.post("users/", {
          username: this.form.username,
          email: this.form.email,
          password: this.form.password,
          first_name: this.form.firstName,
          last_name: this.form.lastName,
        });

        // Başarılı işlem sonrası giriş sayfasına yönlendirme
        this.$router.push("/login");
      } catch (error) {
        // Backend'den gelen hata mesajını kontrol et
        this.errorMessage =
          error.response?.data?.username?.[0] ||
          error.response?.data?.email?.[0] ||
          "Kayıt işlemi başarısız.";
      }
    },
  },
};
</script>

<style scoped>
body {
  background-color: #f3f4f6;
  color: #1f2937;
}

.min-h-screen {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.bg-gray-800 {
  background-color: #2d3748;
}
</style>
