<template>
  <nav
    v-if="!isAuthPage"
    class="fixed top-0 left-0 right-0 flex items-center justify-between px-6 h-16 bg-slate-900 text-white shadow-lg z-50"
  >
    <!-- Sol taraf - Logo -->
    <div class="flex-none">
      <router-link
        to="/home"
        class="text-xl font-bold text-white hover:text-blue-400 transition-colors duration-300"
      >
        EventP
      </router-link>
    </div>

    <!-- Orta kısım - Navigasyon Linkleri -->
    <div class="flex-1 flex justify-center items-center space-x-8">
      <router-link
        to="/admin"
        class="text-gray-300 hover:text-white transition-colors duration-300"
        active-class="text-white"
      >
        Admin Sayfası
      </router-link>
      <router-link
        to="/chat"
        class="text-gray-300 hover:text-white transition-colors duration-300"
        active-class="text-white"
      >
        Sohbet Sayfası
      </router-link>
    </div>

    <!-- Sağ taraf - Profil İkonu -->
    <div class="flex-none">
      <router-link
        to="/profile"
        class="w-10 h-10 rounded-full bg-gray-700 flex items-center justify-center hover:bg-gray-600 transition-colors duration-300"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
          />
        </svg>
      </router-link>
    </div>
  </nav>

  <!-- Navbar'ın yüksekliği kadar boşluk bırakma -->
  <div v-if="!isAuthPage" class="h-16"></div>
</template>

<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();

// Kimlik doğrulama sayfalarında navbar'ı gizlemek için
const isAuthPage = computed(() => {
  return ["/login", "/register", "/forgot-password", "/"].includes(route.path);
});
</script>
