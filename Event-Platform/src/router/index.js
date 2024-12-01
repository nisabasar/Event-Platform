import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../pages/HomePage.vue";
import EventDetail from "../pages/EventDetail.vue";
import ProfilePage from "../pages/ProfilePage.vue";
import AdminPage from "../pages/AdminPage.vue";
import ChatPage from "../pages/ChatPage.vue";
import LoginPage from "../pages/LoginPage.vue";
import RegisterPage from "../pages/RegisterPage.vue";
import CreateEventPage from "../pages/CreateEventPage.vue";
import ForgotPassword from "../pages/ForgotPassword.vue";

const routes = [
  { path: "/", redirect: "/login" },
  { path: "/login", component: LoginPage },
  { path: "/register", component: RegisterPage },
  { path: "/forgot-password", component: ForgotPassword },
  { path: "/home", component: HomePage },
  {
    path: "/event/:id",
    name: "EventDetail",
    component: EventDetail,
    props: true,
  },
  { path: "/profile", component: ProfilePage },
  { path: "/admin", component: AdminPage },
  { path: "/chat", component: ChatPage },
  { path: "/create-event", component: CreateEventPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
