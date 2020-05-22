<template>
    <b-container class="fixed-top" fluid="true" style="background-color: white; opacity: 0.7">
        <b-row align-h="center">
            <b-col sm="8">
                <b-container>
                    <b-navbar toggleable="lg">
                        <b-row class="navbar-row" align-v="center">
                            <b-col class="text-left" lg="11">
                                <b-row align-v="center">
                                    <b-col class="text-left" lg="12" cols="10">
                                        <div style="display: inline-block">
                                            <router-link to="/" tag="div" class="cursor h-font text-uppercase">
                                                <span class="brand-animation-pink">On</span>|<span
                                                    class="brand-animation-blue">Testing</span></router-link>
                                        </div>
                                        <!--                                        <span class="badge badge-warning" style="vertical-align: top">Beta</span>-->
                                    </b-col>
                                    <b-col class="text-right" cols="2">
                                        <b-navbar-toggle target="nav-text-collapse"
                                                         class="d-lg-none text-right border-0 bg-white">
                                            <img src="../assets/Hamburger_icon.svg">
                                        </b-navbar-toggle>
                                    </b-col>
                                </b-row>
                            </b-col>
                            <b-col class="text-uppercase">
                                <b-collapse id="nav-text-collapse" is-nav>
                                    <div class="navbar-item mr-4">
                                        <a href="https://hse-onlecture.herokuapp.com/" target="_blank"><span
                                                class="navbar-item">Dashboard.</span></a>
                                    </div>
                                    <div class="navbar-item mr-4">
                                        <a href="https://hse-onlecture.herokuapp.com/tasks" target="_blank"><span
                                                class="navbar-item">Tasks.</span></a>
                                    </div>
                                    <div class="navbar-item mr-4">
                                        <router-link to="/" tag="div" class="navbar-item">Blog.</router-link>
                                    </div>
                                    <div class="navbar-item mr-4">
                                        <router-link to="/test" tag="div" class="navbar-item">Test.</router-link>
                                    </div>
                                    <!--                                    <div class="navbar-item mr-4">-->
                                    <!--                                        <router-link to="/signin" tag="b-button"-->
                                    <!--                                                     class="text-nowrap btn-black border-radius border-0 shadow active_bottom_shadow text-uppercase">-->
                                    <!--                                            sign in-->
                                    <!--                                        </router-link>-->
                                    <!--                                    </div>-->
                                    <!--                                    <div class="navbar-item mr-4">-->
                                    <!--                                        <router-link to="/signup" tag="b-button"-->
                                    <!--                                                     class="text-nowrap btn-black-invert border-0 border-radius text-uppercase active_bottom_shadow">-->
                                    <!--                                            sign up-->
                                    <!--                                        </router-link>-->
                                    <!--                                    </div>-->
                                </b-collapse>
                            </b-col>
                        </b-row>
                    </b-navbar>
                </b-container>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
    export default {
        name: "NavBar",
        methods: {}
    }
</script>

<style scoped>

</style>