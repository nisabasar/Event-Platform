<template>
  <div class="min-h-screen py-8 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md mx-auto bg-gray-800 rounded-lg shadow-lg p-6">
      <h2 class="text-2xl font-bold mb-6 text-center text-gray-100">
        Kullanıcı Profili
      </h2>

      <div class="text-center mb-6">
        <img
          :src="profile.profileImage || '/default-avatar.png'"
          class="w-32 h-32 rounded-full object-cover border-4 border-gray-700"
          alt="Profil Fotoğrafı"
        />
      </div>

      <div class="space-y-4">
        <div>
          <p class="text-lg font-medium text-gray-300">Kullanıcı Adı:</p>
          <p class="text-xl text-gray-100">{{ profile.username }}</p>
        </div>
        <div>
          <p class="text-lg font-medium text-gray-300">E-posta:</p>
          <p class="text-xl text-gray-100">{{ profile.email }}</p>
        </div>
        <div>
          <p class="text-lg font-medium text-gray-300">Puan:</p>
          <p class="text-xl text-gray-100">{{ profile.points }}</p>
        </div>
        <div>
          <p class="text-lg font-medium text-gray-300">Konum:</p>
          <p class="text-xl text-gray-100">{{ profile.location || 'Belirtilmedi' }}</p>
        </div>
        <div>
          <p class="text-lg font-medium text-gray-300">İlgi Alanları:</p>
          <ul class="list-disc list-inside text-gray-100">
            <li v-for="interest in profile.interests" :key="interest">
              {{ interest }}
            </li>
          </ul>
        </div>
      </div>

      <div class="mt-6 flex justify-end">
        <button
          @click="editProfile"
          class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
        >
          Profili Düzenle
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  data() {
    return {
      profile: {
        username: "",
        email: "",
        points: 0,
        profileImage: "",
        location: "",
        interests: [],
      },
    };
  },
  async created() {
    try {
      const response = await api.get("users/me/");
      this.profile = response.data;
    } catch (error) {
      console.error("Profil bilgileri alınırken hata oluştu:", error);
    }
  },
  methods: {
    editProfile() {
      this.$router.push("/edit-profile");
    },
  },
};
</script>

<style>
body {
  background-color: #1f2937;
  color: #f3f4f6;
}

::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #374151;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb {
  background: #4b5563;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #6b7280;
}
</style>
