<template>
  <div class="min-h-screen bg-gray-900 text-white p-8">
    <h1 class="text-3xl font-bold mb-8">Etkinlik Oluştur</h1>

    <form @submit.prevent="handleSubmit" class="max-w-2xl space-y-6">
      <!-- Etkinlik İsmi -->
      <div>
        <label class="block mb-2">Etkinlik İsmi</label>
        <input
          v-model="eventForm.title"
          type="text"
          class="w-full p-3 rounded bg-gray-800 border border-gray-700 focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
          required
        />
      </div>

      <!-- Kategori -->
      <div>
        <label class="block mb-2">Kategori</label>
        <select
          v-model="eventForm.category"
          class="w-full p-3 rounded bg-gray-800 border border-gray-700 focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
          required
        >
          <option value="Festival">Festival</option>
          <option value="Konser">Konser</option>
          <option value="Spor">Spor</option>
          <option value="Teknoloji">Teknoloji</option>
          <option value="Sanat">Sanat</option>
          <option value="Eğitim">Eğitim</option>
        </select>
      </div>

      <!-- Tarih ve Saat -->
      <div class="grid grid-cols-2 gap-4">
        <div>
          <label class="block mb-2">Tarih</label>
          <input
            v-model="eventForm.date"
            type="date"
            class="w-full p-3 rounded bg-gray-800 border border-gray-700 focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
            required
          />
        </div>
        <div>
          <label class="block mb-2">Saat</label>
          <input
            v-model="eventForm.time"
            type="time"
            class="w-full p-3 rounded bg-gray-800 border border-gray-700 focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
            required
          />
        </div>
      </div>

      <!-- Süre -->
      <div>
        <label class="block mb-2">Süre (saat)</label>
        <input
          v-model="eventForm.duration"
          type="number"
          min="0.5"
          step="0.5"
          class="w-full p-3 rounded bg-gray-800 border border-gray-700 focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
          required
        />
      </div>

      <!-- Konum -->
      <div>
        <label class="block mb-2">Konum</label>
        <input
          v-model="eventForm.location"
          type="text"
          class="w-full p-3 rounded bg-gray-800 border border-gray-700 focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
          required
        />
      </div>

      <!-- Açıklama -->
      <div>
        <label class="block mb-2">Açıklama</label>
        <textarea
          v-model="eventForm.description"
          rows="4"
          class="w-full p-3 rounded bg-gray-800 border border-gray-700 focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
          required
        ></textarea>
      </div>

      <!-- Butonlar -->
      <div class="flex gap-4">
        <button
          type="submit"
          class="px-6 py-3 bg-blue-600 rounded hover:bg-blue-700 transition-colors"
        >
          Etkinlik Oluştur
        </button>
        <button
          type="button"
          @click="$router.push('/home')"
          class="px-6 py-3 bg-gray-700 rounded hover:bg-gray-600 transition-colors"
        >
          İptal
        </button>
      </div>
    </form>
  </div>
</template>
<script>
import api from "@/services/api";

export default {
  data() {
    return {
      eventForm: {
        title: "",
        category: "",
        date: "",
        time: "",
        duration: "",
        location: "",
        description: "",
      },
    };
  },
  methods: {
    async handleSubmit() {
      try {
        const response = await api.post("events/", this.eventForm);
        console.log("Etkinlik başarıyla oluşturuldu:", response.data);

        // Ana sayfaya yönlendirme
        this.$router.push("/home");
      } catch (error) {
        console.error("Etkinlik oluşturulurken hata oluştu:", error);
      }
    },
  },
};
</script>


