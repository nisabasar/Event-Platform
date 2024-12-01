<template>
  <div class="container mx-auto py-16">
    <div v-if="event" class="bg-gray-800 rounded-lg p-8 shadow-md">
      <h1 class="text-3xl font-bold mb-6">{{ event.name }}</h1>
      <p class="text-gray-300 mb-6">{{ event.description }}</p>

      <div class="space-y-4 text-gray-400">
        <!-- Tarih -->
        <div class="flex items-center space-x-2">
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
        <div class="flex items-center space-x-2">
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
        <div class="flex items-center space-x-2">
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

        <!-- Kategori -->
        <div class="flex items-center space-x-2">
          <span class="bg-gray-700 px-3 py-1 rounded-full text-sm">{{
            event.kategori
          }}</span>
        </div>
      </div>
    </div>
    <div v-else class="text-center text-gray-400">
      <p>Etkinlik bilgisi bulunamadı.</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ["id"],
  data() {
    return {
      event: null, // Etkinlik bilgisi
    };
  },
  created() {
    // URL'den gelen `id` parametresine göre etkinliği bul
    const allEvents = [
      {
        id: "ETK001",
        name: "Geleneksel Bahar Festivali",
        date: "20 Nisan 2024",
        saat: "14:00",
        description:
          "Baharın gelişini kutlamak için düzenlenen renkli bir festival. Canlı müzik, yemek stantları ve çeşitli aktiviteler sizleri bekliyor.",
        duration: "3 saat",
        konum: "Maltepe Sahil Etkinlik Alanı",
        kategori: "Festival",
      },
      {
        id: "ETK002",
        name: "Sezen Aksu Konseri",
        date: "15 Mayıs 2024",
        saat: "20:30",
        description:
          "Türk pop müziğinin divası Sezen Aksu, en sevilen şarkılarıyla sizlerle buluşuyor.",
        duration: "2 saat",
        konum: "Harbiye Açık Hava Tiyatrosu",
        kategori: "Konser",
      },
      {
        id: "ETK003",
        name: "Belgrad Ormanı Doğa Yürüyüşü",
        date: "22 Nisan 2024",
        saat: "09:00",
        description:
          "Profesyonel rehber eşliğinde, doğayla iç içe sağlıklı bir yürüyüş deneyimi.",
        duration: "4 saat",
        konum: "Belgrad Ormanı Neşet Suyu Girişi",
        kategori: "Spor",
      },
      {
        id: "ETK004",
        name: "Teknoloji ve İnovasyon Fuarı",
        date: "1 Haziran 2024",
        saat: "10:00",
        description:
          "Yapay zeka, robotik ve dijital dönüşüm alanındaki en son yeniliklerin sergilendiği kapsamlı fuar.",
        duration: "3 gün",
        konum: "İstanbul Kongre Merkezi",
        kategori: "Teknoloji",
      },
      {
        id: "ETK005",
        name: "Modern Türk Mutfağı Workshop",
        date: "18 Mayıs 2024",
        saat: "13:00",
        description:
          "Ünlü şef eşliğinde modern Türk mutfağının inceliklerini öğrenin.",
        duration: "2 saat",
        konum: "Gastronomi Akademisi",
        kategori: "Eğitim",
      },
      {
        id: "ETK006",
        name: "Hamlet - Modern Yorumlama",
        date: "25 Haziran 2024",
        saat: "20:00",
        description:
          "Shakespeare'in ölümsüz eseri Hamlet'in modern bir yorumu ile karşınızda.",
        duration: "2.5 saat",
        konum: "Zorlu PSM",
        kategori: "Sanat",
      },
    ];
    this.event = allEvents.find((event) => event.id === this.id);
  },
};
</script>
