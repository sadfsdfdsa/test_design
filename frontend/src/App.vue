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
            },

            login_count: 0
        }),
        methods: {
            login_user(user, options = {}) {
                this.user.login = true;
                this.user.name = user.name;
                this.$store.commit('set_login', true)
                this.$store.commit('set_username', user.name)
                if (options.remember_flag === false) {
                    localStorage.removeItem(this.$store.state.LSV.access_token);
                    localStorage.removeItem(this.$store.state.LSV.refresh_token);
                }
            },
            unlogin_user() {
                this.user.login = false;
                this.user.name = "";
                localStorage.removeItem(this.$store.state.LSV.access_token);
                localStorage.removeItem(this.$store.state.LSV.refresh_token);
                this.$store.commit('set_login', false)
                this.$store.commit('set_username', "")
            }
        },
        created() {
            if (localStorage.getItem(this.$store.state.LSV.access_token) != null) {
                this.$api.post("/login/", {}, {headers: {"Authorization": 'Bearer ' + localStorage[this.$store.state.LSV.access_token]}}).then((data) => {
                    if (data.data.result === "success") {
                        this.login_user(data.data.data.user)
                        localStorage[this.$store.state.LSV.access_token] = data.data.data.access_token;
                        localStorage[this.$store.state.LSV.refresh_token] = data.data.data.refresh_token;
                        localStorage[this.$store.state.LSV.login] = 'true';
                        this.login_count = 0;
                    } else {
                        if (data.status === 401 && localStorage.getItem(this.$store.state.LSV.refresh_token) != null && this.login_count < 5) {
                            this.$api.post("/refresh/", {}, {headers: {"Authorization": 'Bearer ' + localStorage[this.$store.state.LSV.refresh_token]}}).then((data) => {
                                if (data.data.result === "success") {
                                    localStorage[this.$store.state.LSV.access_token] = data.data.data.access_token;
                                    this.login_count++;
                                    this.created();
                                }
                            });
                        } else {
                            this.$snotify.error(data.data.error.msg);
                        }
                    }
                });
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
