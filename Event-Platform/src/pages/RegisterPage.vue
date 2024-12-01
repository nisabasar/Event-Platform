<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-900 text-white">
    <div class="w-full max-w-md bg-gray-800 p-8 rounded-lg shadow-lg">
      <h2 class="text-3xl font-bold text-center mb-6">Kayıt Ol</h2>
      <form @submit.prevent="handleRegister" class="space-y-6">
        <!-- Kullanıcı Adı -->
        <div>
          <label class="block text-sm font-medium mb-2">Kullanıcı Adı</label>
          <input
            v-model="form.username"
            type="text"
            placeholder="Kullanıcı adınızı girin"
            class="w-full px-4 py-3 rounded-md bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        <!-- E-posta -->
        <div>
          <label class="block text-sm font-medium mb-2">E-posta</label>
          <input
            v-model="form.email"
            type="email"
            placeholder="E-posta adresinizi girin"
            class="w-full px-4 py-3 rounded-md bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        <!-- Telefon -->
        <div>
          <label class="block text-sm font-medium mb-2">Telefon</label>
          <input
            v-model="form.phone"
            type="tel"
            placeholder="Telefon numaranızı girin"
            class="w-full px-4 py-3 rounded-md bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <!-- Şifre -->
        <div>
          <label class="block text-sm font-medium mb-2">Şifre</label>
          <input
            v-model="form.password"
            type="password"
            placeholder="Şifrenizi oluşturun"
            class="w-full px-4 py-3 rounded-md bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        <!-- Şifre Tekrar -->
        <div>
          <label class="block text-sm font-medium mb-2">Şifre Tekrar</label>
          <input
            v-model="form.password2"
            type="password"
            placeholder="Şifrenizi tekrar girin"
            class="w-full px-4 py-3 rounded-md bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        <!-- Cinsiyet -->
        <div>
          <label class="block text-sm font-medium mb-2">Cinsiyet</label>
          <select
            v-model="form.gender"
            class="w-full px-4 py-3 rounded-md bg-gray-700 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          >
            <option value="">Lütfen bir seçenek seçin</option>
            <option value="male">Erkek</option>
            <option value="female">Kadın</option>
            <option value="other">Diğer</option>
          </select>
        </div>

        <!-- İlgi Alanları -->
        <div>
          <label class="block text-sm font-medium mb-2">İlgi Alanları</label>
          <div class="space-y-2">
            <label class="inline-flex items-center">
              <input
                type="checkbox"
                value="Spor"
                v-model="form.interests"
                class="rounded bg-gray-700 border-gray-600 text-blue-500"
              />
              <span class="ml-2">Spor</span>
            </label>
            <label class="inline-flex items-center">
              <input
                type="checkbox"
                value="Teknoloji"
                v-model="form.interests"
                class="rounded bg-gray-700 border-gray-600 text-blue-500"
              />
              <span class="ml-2">Teknoloji</span>
            </label>
            <label class="inline-flex items-center">
              <input
                type="checkbox"
                value="Sanat"
                v-model="form.interests"
                class="rounded bg-gray-700 border-gray-600 text-blue-500"
              />
              <span class="ml-2">Sanat</span>
            </label>
          </div>
        </div>

        <!-- Kayıt Ol Butonu -->
        <div>
          <button
            type="submit"
            class="w-full py-3 bg-blue-600 rounded-md hover:bg-blue-700 transition-colors font-bold"
          >
            Kayıt Ol
          </button>
        </div>
      </form>

      <p class="text-center mt-6">
        Zaten bir hesabınız var mı?
        <router-link to="/login" class="text-blue-400 hover:underline">Giriş Yap</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  data() {
    return {
      form: {
        username: "",
        email: "",
        phone: "",
        password: "",
        password2: "",
        gender: "other",
        interests: [],
      },
    };
  },
  methods: {
    async handleRegister() {
      if (this.form.password !== this.form.password2) {
        alert("Şifreler uyuşmuyor!");
        return;
      }

      try {
        const response = await api.post("register/", this.form);
        if (response && response.data) {
          alert("Kayıt başarılı! Giriş yapabilirsiniz.");
          this.$router.push("/login");
        }
      } catch (error) {
        if (error.response && error.response.data) {
          console.error("Kayıt hatası:", error.response.data);
          alert(
            error.response.data.gender?.[0] ||
              error.response.data.detail ||
              "Kayıt başarısız. Lütfen bilgilerinizi kontrol edin."
          );
        } else {
          console.error("Kayıt hatası:", error);
          alert("Sunucuya bağlanılamadı. Lütfen daha sonra tekrar deneyin.");
        }
      }
    },
  },
};
</script>

<style>
body {
  background-color: #1f2937;
  color: #f3f4f6;
}
</style>
