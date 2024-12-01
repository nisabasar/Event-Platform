<template>
  <div class="flex items-center justify-center h-screen bg-gray-900">
    <div class="w-96 bg-gray-800 p-6 rounded-lg shadow-lg">
      <h2 class="text-2xl text-center text-white font-bold mb-6">
        Şifre Sıfırlama
      </h2>
      <form @submit.prevent="handleResetPassword">
        <div class="mb-4">
          <label for="email" class="block text-sm text-gray-400 mb-2">
            E-posta Adresiniz
          </label>
          <input
            v-model="email"
            type="email"
            id="email"
            class="w-full px-3 py-2 bg-gray-700 text-white rounded focus:outline-none"
            required
          />
        </div>
        <button
          type="submit"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded"
        >
          Şifre Sıfırlama Bağlantısı Gönder
        </button>
      </form>
      <div v-if="successMessage" class="mt-4 text-green-500 text-sm">
        {{ successMessage }}
      </div>
      <div v-if="errorMessage" class="mt-4 text-red-500 text-sm">
        {{ errorMessage }}
      </div>
      <div class="text-center mt-6">
        <button
          @click="goToLogin"
          class="text-sm text-blue-400 hover:text-blue-300"
        >
          Giriş sayfasına dön
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      successMessage: "",
      errorMessage: "",
    };
  },
  methods: {
    handleResetPassword() {
      // Burada şifre sıfırlama mantığı uygulanacak
      if (this.email) {
        // Örnek başarılı durum
        this.successMessage =
          "Şifre sıfırlama bağlantısı e-posta adresinize gönderildi.";
        this.errorMessage = "";

        // Gerçek uygulamada burada API çağrısı yapılacak
        setTimeout(() => {
          this.$router.push("/login");
        }, 3000);
      } else {
        this.errorMessage = "Lütfen geçerli bir e-posta adresi girin.";
        this.successMessage = "";
      }
    },
    goToLogin() {
      this.$router.push("/login");
    },
  },
};
</script>
