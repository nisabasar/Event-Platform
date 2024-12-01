<template>
  <div class="container mx-auto py-16">
    <div class="flex flex-col items-center">
      <h1 class="text-3xl font-bold mb-8">Etkinlik Önerileri</h1>

      <!-- Kategori Filtreleme -->
      <div class="flex gap-4 mb-8">
        <button
          v-for="kategori in kategoriler"
          :key="kategori"
          class="px-4 py-2 rounded-full text-sm bg-gray-700 hover:bg-gray-600 transition-colors"
          :class="secilenKategori === kategori ? 'bg-blue-600' : ''"
          @click="kategoriFiltrele(kategori)"
        >
          {{ kategori }}
        </button>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
        <div
          v-for="event in filtrelenmisEtkinlikler"
          :key="event.id"
          class="bg-gray-800 rounded-lg p-6 shadow-md hover:shadow-xl transition-all duration-300"
        >
          <div class="flex justify-between items-start mb-4">
            <h2 class="text-xl font-bold">{{ event.name }}</h2>
            <span class="bg-gray-700 px-3 py-1 rounded-full text-sm">
              {{ event.kategori }}
            </span>
          </div>

          <p class="text-gray-300 mb-4">{{ event.description }}</p>

          <div class="space-y-3 mb-4">
            <!-- Tarih ve Saat -->
            <div class="flex items-center space-x-2 text-gray-400">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                />
              </svg>
              <span>{{ event.date }} - {{ event.saat }}</span>
            </div>

            <!-- Süre -->
            <div class="flex items-center space-x-2 text-gray-400">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
              <span>{{ event.duration }}</span>
            </div>

            <!-- Konum -->
            <div class="flex items-center space-x-2 text-gray-400">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                />
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                />
              </svg>
              <span>{{ event.konum }}</span>
            </div>
          </div>

          <div class="flex justify-between items-center">
            <router-link
              :to="{ name: 'EventDetail', params: { id: event.id } }"
            >
              <button
                class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition-colors duration-300"
              >
                Katıl
              </button>
            </router-link>

            <span class="text-sm text-gray-400">#{{ event.id }}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="mt-12 flex justify-center">
      <router-link to="/create-event">
        <button
          class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition-colors duration-300"
        >
          Etkinlik Oluştur
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  data() {
    return {
      events: [],
      kategoriler: ["Tümü", "Festival", "Konser", "Spor", "Teknoloji", "Sanat", "Eğitim"],
      secilenKategori: "Tümü",
    };
  },
  computed: {
    filtrelenmisEtkinlikler() {
      if (this.secilenKategori === "Tümü") {
        return this.events;
      }
      return this.events.filter((event) => event.kategori === this.secilenKategori);
    },
  },
  methods: {
    async fetchEvents() {
      try {
        const response = await api.get("events/");
        this.events = response.data;
      } catch (error) {
        console.error("Etkinlikleri alırken hata oluştu:", error);
      }
    },
    kategoriFiltrele(kategori) {
      this.secilenKategori = kategori;
    },
  },
  created() {
    this.fetchEvents();
  },
};
</script>


<style>
/* Önceki stil kodunuz aynen kalacak */
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
