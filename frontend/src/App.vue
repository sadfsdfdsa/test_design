<template>
    <div>
        <NavBar :user="user"></NavBar>
        <router-view @do_login="login_user" @do_unlogin="unlogin_user" :user="user"></router-view>
        <vue-snotify></vue-snotify>
    </div>
</template>

<script>
    import NavBar from "./components/NavBar";

    export default {
        components: {NavBar},
        data: () => ({
            user: {
                login: false,
                name: "empty"
            }
        }),
        methods: {
            login_user(user) {
                this.user.login = true;
                this.user.name = user.name;
                this.$store.commit('set_login', true)
                this.$store.commit('set_username', user.name)
            },
            unlogin_user() {
                this.user.login = false;
                this.user.name = "";
                this.$store.commit('set_login', false)
                this.$store.commit('set_username', "")
            }
        },
        created() {
            if (localStorage.getItem(this.$store.state.LSV.login) != null) {
                this.user.login = JSON.parse(localStorage.getItem(this.$store.state.LSV.login))
                this.user.name = localStorage.getItem(this.$store.state.LSV.username)
                this.$store.commit('set_login', this.user.login)
            } else {
                localStorage[this.$store.state.LSV.login] = 'false'
            }
        }
    }
</script>

<style lang="scss">
    @import "~vue-snotify/styles/material.css";
    @import "css/main.css";
</style>
