// src/App.vue
<template>
  <div>
    <Navbar v-if="!isLoginOrRegister" />
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";

export default {
  name: "App",
  components: {
    Navbar,
  },
  computed: {
    isLoginOrRegister() {
      return this.$route.path === "/login" || this.$route.path === "/register";
    },
  },
};
</script>

<style>
body {
  background-color: #1f2937;
  color: #f3f4f6;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
