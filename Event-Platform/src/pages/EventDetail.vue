<template>
  <div class="container mx-auto py-10 px-4">
    <div class="bg-gray-800 p-6 rounded-lg shadow-md">
      <!-- Etkinlik Detayları -->
      <h1 class="text-3xl font-bold text-white mb-4">{{ event.name }}</h1>
      <p class="text-gray-300 mb-4">{{ event.description }}</p>
      <p class="text-gray-300 mb-4">
        <strong>Tarih ve Saat:</strong>
        {{ event.date }} - {{ event.time }}
      </p>
      <p class="text-gray-300 mb-4">
        <strong>Süre:</strong>
        {{ event.duration }}
      </p>
      <p class="text-gray-300 mb-4">
        <strong>Konum:</strong>
        {{ event.location }}
      </p>
      <p class="text-gray-300 mb-4">
        <strong>Kategori:</strong>
        {{ event.category }}
      </p>

      <!-- Harita Bileşeni -->
      <div class="mt-6">
        <Map :location="event.location" />
      </div>

      <!-- Katıl Butonu -->
      <div class="mt-6">
        <button
          @click="joinEvent"
          class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition-colors"
        >
          Etkinliğe Katıl
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { useRoute } from "vue-router";
import { ref, onMounted } from "vue";
import api from "@/services/api";
import Map from "@/components/Map.vue";

export default {
  components: { Map },
  setup() {
    const route = useRoute();
    const event = ref(null);

    // Etkinlik detaylarını API'den al
    onMounted(async () => {
      try {
        const response = await api.get(`events/${route.params.id}`);
        event.value = response.data;
      } catch (error) {
        console.error("Etkinlik detayları alınırken hata oluştu:", error);
      }
    });

    // Etkinliğe katılma fonksiyonu
    const joinEvent = async () => {
      try {
        await api.post("participants/", {
          event: event.value.id,
        });
        alert("Etkinliğe başarıyla katıldınız!");
      } catch (error) {
        console.error("Etkinliğe katılma sırasında hata oluştu:", error);
        alert(
          error.response?.data?.detail ||
            "Etkinliğe katılma sırasında bir hata oluştu."
        );
      }
    };

    return { event, joinEvent };
  },
};
</script>

<style scoped>
.container {
  max-width: 800px;
}
</style>
