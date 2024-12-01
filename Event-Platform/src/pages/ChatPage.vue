Koyu Temalı Etkinlik Sohbet Sayfası

<template>
  <div class="flex flex-col h-screen bg-gray-800">
    <!-- Üst Başlık -->
    <header class="bg-gray-900 shadow-lg p-4">
      <div class="max-w-7xl mx-auto">
        <div class="flex items-center justify-between">
          <div>
            <h1 class="text-2xl font-bold text-gray-100">{{ etkinlikAdi }}</h1>
            <p class="text-sm text-gray-400">Etkinlik Sohbet Alanı</p>
          </div>
          <div class="flex items-center space-x-4">
            <span class="text-sm text-gray-400">
              {{ katilimciSayisi }} Katılımcı
            </span>
          </div>
        </div>
      </div>
    </header>

    <!-- Ana Sohbet Alanı -->
    <div class="flex-1 overflow-hidden">
      <div class="max-w-7xl mx-auto h-full p-4">
        <div class="bg-gray-900 rounded-lg shadow-lg h-full flex flex-col">
          <!-- Mesaj Geçmişi -->
          <div
            class="flex-1 overflow-y-auto p-4 space-y-4"
            ref="messageContainer"
          >
            <div
              v-for="mesaj in mesajlar"
              :key="mesaj.id"
              :class="[
                'flex',
                mesaj.kullaniciId === kullaniciId
                  ? 'justify-end'
                  : 'justify-start',
              ]"
            >
              <div
                :class="[
                  'max-w-[70%] rounded-lg p-3',
                  mesaj.kullaniciId === kullaniciId
                    ? 'bg-blue-600 text-gray-100'
                    : 'bg-gray-700 text-gray-100',
                ]"
              >
                <div class="flex items-center space-x-2">
                  <span class="font-medium">{{ mesaj.kullaniciAdi }}</span>
                  <span class="text-xs opacity-70">
                    {{ formatTarih(mesaj.tarih) }}
                  </span>
                </div>
                <p class="mt-1">{{ mesaj.icerik }}</p>
              </div>
            </div>
          </div>

          <!-- Mesaj Gönderme Alanı -->
          <div class="border-t border-gray-700 p-4">
            <form @submit.prevent="mesajGonder" class="flex space-x-4">
              <input
                v-model="yeniMesaj"
                type="text"
                placeholder="Mesajınızı yazın..."
                class="flex-1 rounded-lg bg-gray-700 border-gray-600 text-gray-100 px-4 py-2 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 placeholder-gray-400"
              />
              <button
                type="submit"
                class="bg-blue-600 text-gray-100 px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-gray-900"
              >
                Gönder
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  data() {
    return {
      eventId: null,
      messages: [],
      newMessage: "",
    };
  },
  methods: {
    async fetchMessages() {
      try {
        const response = await api.get(`messages/?event=${this.eventId}`);
        this.messages = response.data;
      } catch (error) {
        console.error("Mesajları alırken hata oluştu:", error);
      }
    },
    async sendMessage() {
      try {
        await api.post("messages/", {
          event: this.eventId,
          content: this.newMessage,
        });
        this.newMessage = "";
        this.fetchMessages();
      } catch (error) {
        console.error("Mesaj gönderilirken hata oluştu:", error);
      }
    },
  },
  created() {
    this.eventId = this.$route.params.id;
    this.fetchMessages();
  },
};
</script>


<style>
/* Sayfa geneli için koyu tema stilleri */
body {
  background-color: #1f2937;
  color: #f3f4f6;
}

/* Scrollbar stilini özelleştirme */
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
