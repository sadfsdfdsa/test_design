import Snotify, {SnotifyPosition} from "vue-snotify";
import BootstrapVue from "bootstrap-vue";
import VueRouter from "vue-router";
import Vuex from "vuex";
import Vue from 'vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import routes from "./routes.js";
import App from "./App.vue";
import api from "./utils/api.js";

Vue.use(BootstrapVue);
Vue.use(VueRouter);
Vue.use(Vuex);
Vue.use(Snotify, {
    toast: {
        position: SnotifyPosition.rightTop,
        timeout: 3000
    }
});

// you may call it in components with this.$api
Vue.prototype.$api = api;

const store = new Vuex.Store({
    state: {
        login: false,
        username: "",

        LSV: {
            login: "login",
            username: "username",
            access_token: "access_token",
            refresh_token: "refresh_token"

        }
    },
    mutations: {
        set_login(state, login = false) {
            state.login = login;
            localStorage[state.LSV.login] = login;
        },
        set_username(state, username) {
            state.username = username;
            localStorage[state.LSV.username] = username;
        }

    }
});

const router = new VueRouter({
    routes,
    mode: "history",
    scrollBehavior: () => ({y: 0})
});

new Vue({
    el: "#app",
    router,
    store,
    render: f => f(App)
});
