<template>
  <div class="min-h-screen py-8 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md mx-auto bg-gray-800 rounded-lg shadow-lg p-6">
      <h2 class="text-2xl font-bold mb-6 text-center text-gray-100">
        Profil Güncelleme
      </h2>

      <form @submit.prevent="updateProfile" class="space-y-4">
        <!-- Profil Fotoğrafı -->
        <div class="text-center mb-6">
          <div class="relative inline-block">
            <img
              :src="profileImage || '/default-avatar.png'"
              class="w-32 h-32 rounded-full object-cover border-4 border-gray-700"
              alt="Profil Fotoğrafı"
            />
            <label
              class="absolute bottom-0 right-0 bg-blue-600 p-2 rounded-full cursor-pointer hover:bg-blue-700"
            >
              <input
                type="file"
                accept="image/*"
                class="hidden"
                @change="handleImageChange"
              />
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 text-white"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"
                />
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"
                />
              </svg>
            </label>
          </div>
        </div>

        <!-- Kişisel Bilgiler -->
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-gray-300">Ad</label>
            <input
              v-model="profile.firstName"
              type="text"
              class="mt-1 block w-full rounded-md bg-gray-700 border-gray-600 text-gray-100 focus:border-blue-500 focus:ring-blue-500"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-300">Soyad</label>
            <input
              v-model="profile.lastName"
              type="text"
              class="mt-1 block w-full rounded-md bg-gray-700 border-gray-600 text-gray-100 focus:border-blue-500 focus:ring-blue-500"
            />
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-300"
            >Kullanıcı Adı</label
          >
          <input
            v-model="profile.username"
            type="text"
            class="mt-1 block w-full rounded-md bg-gray-700 border-gray-600 text-gray-100 focus:border-blue-500 focus:ring-blue-500"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-300">E-posta</label>
          <input
            v-model="profile.email"
            type="email"
            class="mt-1 block w-full rounded-md bg-gray-700 border-gray-600 text-gray-100 focus:border-blue-500 focus:ring-blue-500"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-300">Telefon</label>
          <input
            v-model="profile.phone"
            type="tel"
            class="mt-1 block w-full rounded-md bg-gray-700 border-gray-600 text-gray-100 focus:border-blue-500 focus:ring-blue-500"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-300">Konum</label>
          <input
            v-model="profile.location"
            type="text"
            class="mt-1 block w-full rounded-md bg-gray-700 border-gray-600 text-gray-100 focus:border-blue-500 focus:ring-blue-500"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-300"
            >Doğum Tarihi</label
          >
          <input
            v-model="profile.birthDate"
            type="date"
            class="mt-1 block w-full rounded-md bg-gray-700 border-gray-600 text-gray-100 focus:border-blue-500 focus:ring-blue-500"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-300"
            >Cinsiyet</label
          >
          <select
            v-model="profile.gender"
            class="mt-1 block w-full rounded-md bg-gray-700 border-gray-600 text-gray-100 focus:border-blue-500 focus:ring-blue-500"
          >
            <option value="male">Erkek</option>
            <option value="female">Kadın</option>
            <option value="other">Diğer</option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-300"
            >İlgi Alanları</label
          >
          <div class="mt-2 space-y-2">
            <label class="inline-flex items-center mx-2">
              <input
                type="checkbox"
                v-model="profile.interests"
                value="spor"
                class="rounded bg-gray-700 border-gray-600 text-blue-600"
              />
              <span class="ml-2 text-gray-300">Spor</span>
            </label>
            <label class="inline-flex items-center mx-2">
              <input
                type="checkbox"
                v-model="profile.interests"
                value="teknoloji"
                class="rounded bg-gray-700 border-gray-600 text-blue-600"
              />
              <span class="ml-2 text-gray-300">Teknoloji</span>
            </label>
            <label class="inline-flex items-center mx-2">
              <input
                type="checkbox"
                v-model="profile.interests"
                value="sanat"
                class="rounded bg-gray-700 border-gray-600 text-blue-600"
              />
              <span class="ml-2 text-gray-300">Sanat</span>
            </label>
            <label class="inline-flex items-center mx-2">
              <input
                type="checkbox"
                v-model="profile.interests"
                value="müzik"
                class="rounded bg-gray-700 border-gray-600 text-blue-600"
              />
              <span class="ml-2 text-gray-300">Müzik</span>
            </label>
          </div>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-300"
            >Yeni Şifre (İsteğe bağlı)</label
          >
          <input
            v-model="profile.newPassword"
            type="password"
            class="mt-1 block w-full rounded-md bg-gray-700 border-gray-600 text-gray-100 focus:border-blue-500 focus:ring-blue-500"
          />
        </div>

        <div class="flex justify-end space-x-3 pt-4">
          <button
            type="button"
            @click="$router.push('/home')"
            class="px-4 py-2 border border-gray-600 rounded-md text-gray-300 hover:bg-gray-700"
          >
            İptal
          </button>
          <button
            type="submit"
            class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
          >
            Kaydet
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const profileImage = ref(null);

const profile = ref({
  id: "",
  username: "",
  email: "",
  firstName: "",
  lastName: "",
  phone: "",
  location: "",
  birthDate: "",
  gender: "",
  interests: [],
  newPassword: "",
});

const handleImageChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      profileImage.value = e.target.result;
    };
    reader.readAsDataURL(file);
  }
};

const updateProfile = async () => {
  try {
    // API çağrısı burada yapılacak
    console.log("Profil güncelleme:", profile.value);
    // Başarılı güncelleme sonrası ana sayfaya yönlendirme
    router.push("/home");
  } catch (error) {
    console.error("Profil güncelleme hatası:", error);
  }
};

onMounted(async () => {
  try {
    // Kullanıcı bilgilerini API'den çekme işlemi burada yapılacak
    // Örnek veri:
    profile.value = {
      id: "1",
      username: "kullanici1",
      email: "ornek@mail.com",
      firstName: "Ad",
      lastName: "Soyad",
      phone: "5551234567",
      location: "İstanbul",
      birthDate: "1990-01-01",
      gender: "male",
      interests: ["teknoloji", "spor"],
      newPassword: "",
    };
  } catch (error) {
    console.error("Profil bilgileri çekme hatası:", error);
  }
});
</script>
