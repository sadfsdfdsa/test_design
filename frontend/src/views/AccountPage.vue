<template>
    <!--     style="background-color: #f4f7f6; min-height: 100vh;"-->
    <div id="main">
        <b-container fluid v-if="this.user.login===true">
            <b-row>
                <b-col class="text-center banner-section-2">
                    <div style="color: white;" class="margin-nav">
                        <h1 style="font-size: 6em">Account</h1>
                        <div style="font-size: 2em">User | {{this.user.name}}</div>
                    </div>
                </b-col>
            </b-row>
            <b-container>
                <b-row class="mt-2">
                    <b-col cols="12" sm="6">
                        <b-card style="border-left: 3px solid dodgerblue;"
                                class="border-radius-none shadow left-hover-border active_bottom_shadow">
                            <b-row>
                                <b-col class="h-font">
                                    Account
                                </b-col>
                            </b-row>
                            <b-row class="navbar-item-font" align-h="start">
                                <b-col class="text-left navbar-item-font">
                                    {{user.name}}
                                </b-col>
                            </b-row>
                        </b-card>
                    </b-col>
                    <b-col cols="12" sm="6">
                        <b-card style="border-left: 3px solid mediumpurple;"
                                class="border-radius-none shadow left-hover-border active_bottom_shadow">
                            <b-row no-gutters>
                                <b-col sm="12">
                                    <b-row>
                                        <b-col class="h-font">
                                            Service
                                        </b-col>
                                    </b-row>
                                    <b-row>
                                        <b-col>
                                            <a href="https://hse-onlecture.herokuapp.com/tasks" target="_blank"><span
                                                    class="navbar-item">Tasks</span></a>
                                        </b-col>
                                        <b-col>
                                            <b-badge variant="success">Active</b-badge>
                                        </b-col>
                                    </b-row>
                                    <b-row>
                                        <b-col>
                                            <a href="https://hse-onlecture.herokuapp.com/" target="_blank"><span
                                                    class="navbar-item">Dashboard</span></a>
                                        </b-col>
                                        <b-col>
                                            <b-badge variant="success">Active</b-badge>
                                        </b-col>
                                    </b-row>
                                </b-col>
                            </b-row>
                        </b-card>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col cols="12" sm="6">
                        <b-card style="border-left: 3px solid #aaaaaa;"
                                class="border-radius-none shadow left-hover-border active_bottom_shadow">
                            <b-row>
                                <b-col class="h-font">
                                    Actions
                                </b-col>
                            </b-row>
                            <b-row no-gutters>
                                <b-col align-self="start">
                                    <b-button @click="unlogin" class="btn-black navbar-item-font">
                                        Sign out
                                    </b-button>
                                    <b-button @click="unlogin" class="btn-black navbar-item-font ml-1">
                                        Reset password
                                    </b-button>
                                </b-col>
                            </b-row>
                        </b-card>
                    </b-col>
                </b-row>
            </b-container>
        </b-container>
        <Footer class="mt-5">
        </Footer>
    </div>
</template>

<script>
    import Footer from "../components/Footer";

    export default {
        name: "AccountPage",
        components: {Footer},
        props: ['user'],
        data: () => ({}),
        methods: {
            unlogin() {
                this.$emit('do_unlogin')
                this.$router.push({path: '/signin'})
            }
        },
        created() {
            // if (this.user.login === false) {
            //     this.$router.push({path: '/signin', query: {redirect_to: "/account"}})
            // }
        }

    }
</script>

<style scoped>

</style>