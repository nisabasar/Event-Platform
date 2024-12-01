import { createRouter, createWebHistory } from "vue-router";

import LoginPage from "@/pages/LoginPage.vue";
import RegisterPage from "@/pages/RegisterPage.vue";
import HomePage from "@/pages/HomePage.vue";
import ProfilePage from "@/pages/ProfilePage.vue";
import EventDetailPage from "@/pages/EventDetail.vue";
import CreateEventPage from "@/pages/CreateEventPage.vue";
import ChatPage from "@/pages/ChatPage.vue";
import ForgotPassword from "@/pages/ForgotPassword.vue"; // Eksik import eklendi

const routes = [
  { path: "/", name: "login", component: LoginPage },
  { path: "/login", name: "login", component: LoginPage }, 
  { path: "/register", name: "register", component: RegisterPage },
  { path: "/home", name: "home", component: HomePage },
  { path: "/profile", name: "profile", component: ProfilePage },
  { path: "/event/:id", name: "eventDetail", component: EventDetailPage, props: true },
  { path: "/create-event", name: "createEvent", component: CreateEventPage },
  { path: "/forgot-password", name: "forgotPassword", component: ForgotPassword },
  { path: "/chat/:eventId", name: "chat", component: ChatPage, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
