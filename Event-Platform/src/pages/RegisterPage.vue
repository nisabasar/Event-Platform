<template>
  <div class="flex items-center justify-center h-screen bg-gray-900">
    <div class="w-96 bg-gray-800 p-6 rounded-lg shadow-lg">
      <h2 class="text-2xl text-center text-white font-bold mb-6">Kayıt Ol</h2>
      <form @submit.prevent="handleRegister">
        <div class="mb-4">
          <label for="username" class="block text-sm text-gray-400 mb-2"
            >Kullanıcı Adı</label
          >
          <input
            v-model="user.username"
            type="text"
            id="username"
            class="w-full px-3 py-2 bg-gray-700 text-white rounded focus:outline-none"
            required
          />
        </div>
        <div class="mb-4">
          <label for="password" class="block text-sm text-gray-400 mb-2"
            >Şifre</label
          >
          <input
            v-model="user.password"
            type="password"
            id="password"
            class="w-full px-3 py-2 bg-gray-700 text-white rounded focus:outline-none"
            required
          />
        </div>
        <div class="mb-4">
          <label for="firstName" class="block text-sm text-gray-400 mb-2"
            >Ad</label
          >
          <input
            v-model="user.firstName"
            type="text"
            id="firstName"
            class="w-full px-3 py-2 bg-gray-700 text-white rounded focus:outline-none"
            required
          />
        </div>
        <div class="mb-4">
          <label for="lastName" class="block text-sm text-gray-400 mb-2"
            >Soyad</label
          >
          <input
            v-model="user.lastName"
            type="text"
            id="lastName"
            class="w-full px-3 py-2 bg-gray-700 text-white rounded focus:outline-none"
            required
          />
        </div>
        <div class="mb-4">
          <label for="birthDate" class="block text-sm text-gray-400 mb-2"
            >Doğum Tarihi</label
          >
          <input
            v-model="user.birthDate"
            type="date"
            id="birthDate"
            class="w-full px-3 py-2 bg-gray-700 text-white rounded focus:outline-none"
            required
          />
        </div>
        <div class="mb-4">
          <label for="gender" class="block text-sm text-gray-400 mb-2"
            >Cinsiyet</label
          >
          <select
            v-model="user.gender"
            id="gender"
            class="w-full px-3 py-2 bg-gray-700 text-white rounded focus:outline-none"
          >
            <option value="Erkek">Erkek</option>
            <option value="Kadın">Kadın</option>
            <option value="Diğer">Diğer</option>
          </select>
        </div>
        <div class="mb-4">
          <label for="email" class="block text-sm text-gray-400 mb-2"
            >E-posta Adresi</label
          >
          <input
            v-model="user.email"
            type="email"
            id="email"
            class="w-full px-3 py-2 bg-gray-700 text-white rounded focus:outline-none"
            required
          />
        </div>
        <div class="mb-4">
          <label for="phone" class="block text-sm text-gray-400 mb-2"
            >Telefon Numarası</label
          >
          <input
            v-model="user.phone"
            type="tel"
            id="phone"
            class="w-full px-3 py-2 bg-gray-700 text-white rounded focus:outline-none"
          />
        </div>
        <div class="mb-4">
          <label for="interests" class="block text-sm text-gray-400 mb-2"
            >İlgi Alanları</label
          >
          <textarea
            v-model="user.interests"
            id="interests"
            class="w-full px-3 py-2 bg-gray-700 text-white rounded focus:outline-none"
          ></textarea>
        </div>
        <div class="mb-4">
          <label for="profilePicture" class="block text-sm text-gray-400 mb-2"
            >Profil Fotoğrafı</label
          >
          <input
            type="file"
            id="profilePicture"
            @change="handleFileUpload"
            class="w-full px-3 py-2 bg-gray-700 text-white rounded focus:outline-none"
          />
        </div>
        <button
          type="submit"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded"
        >
          Kayıt Ol
        </button>

        <button
          type="button"
          @click="handleCancel"
          class="w-full bg-gray-600 hover:bg-gray-700 text-white py-2 rounded mt-4"
        >
          İptal
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {
        username: "",
        password: "",
        firstName: "",
        lastName: "",
        birthDate: "",
        gender: "Erkek",
        email: "",
        phone: "",
        interests: "",
        profilePicture: null,
      },
    };
  },
  methods: {
    handleRegister() {
      console.log("Kayıt bilgileri:", this.user);
      // Burada API çağrısı ya da veri kaydı yapılabilir
      alert("Kayıt başarıyla tamamlandı!");
      this.$router.push("/login");
    },
    handleCancel() {
      this.$router.push("/"); // İptal butonuna basıldığında /home'a yönlendirir
    },
    handleFileUpload(event) {
      this.user.profilePicture = event.target.files[0];
    },
  },
};
</script>

<style scoped>
/* Stil ayarları isteğe bağlı */
</style>
