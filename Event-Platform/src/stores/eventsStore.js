import { defineStore } from "pinia";

export const useEventsStore = defineStore("events", {
  state: () => ({
    events: [
      {
        id: "ETK001",
        name: "Geleneksel Bahar Festivali",
        date: "20 Nisan 2024",
        saat: "14:00",
        description:
          "Baharın gelişini kutlamak için düzenlenen renkli bir festival.",
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
    ],
  }),
  actions: {
    addEvent(newEvent) {
      // Etkinlik nesnesini uygun formata çevir
      const formattedEvent = {
        id: newEvent.id,
        name: newEvent.title,
        date: new Date(newEvent.datetime).toLocaleDateString("tr-TR", {
          day: "numeric",
          month: "long",
          year: "numeric",
        }),
        saat: new Date(newEvent.datetime).toLocaleTimeString("tr-TR", {
          hour: "2-digit",
          minute: "2-digit",
        }),
        description: newEvent.description,
        duration: `${newEvent.duration} saat`,
        konum: newEvent.location,
        kategori: newEvent.category,
      };
      this.events.push(formattedEvent);
    },
  },
});
