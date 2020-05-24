<template>
    <b-container class="fixed-top" fluid="true" style="background-color: rgba(255, 255, 255, .7);">
        <b-row align-h="center">
            <b-col sm="12" lg="8">
                <b-navbar toggleable="lg">
                    <b-row class="navbar-row" align-v="center">
                        <b-col class="text-left" lg="6" md="10">
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
                        <b-col class="text-uppercase" lg="4">
                            <b-collapse id="nav-text-collapse" is-nav>
                                <div class="mr-4">
                                    <a href="https://hse-onlecture.herokuapp.com/" target="_blank"><span
                                            class="navbar-item">Dashboard</span></a>
                                </div>
                                <div class="mr-4">
                                    <a href="https://hse-onlecture.herokuapp.com/tasks" target="_blank"><span
                                            class="navbar-item">Tasks</span></a>
                                </div>
                                <div class="mr-4">
                                    <router-link to="/" tag="div" class="navbar-item">Blog</router-link>
                                </div>
                                <div class="mr-4">
                                    <router-link to="/test" tag="div" class="navbar-item">Test</router-link>
                                </div>
                                <div class="mr-4 navbar-item-font" style="border-right: 2px solid #333;">
                                    &#8203;
                                </div>
                                <div class="mr-4" v-if="!this.user.login">
                                    <router-link to="/signin" tag="b-button"
                                                 class="text-nowrap btn-black border-radius  border-0 active_bottom_shadow text-uppercase navbar-item-font">
                                        sign in
                                    </router-link>
                                </div>
                                <div class="mr-4" v-if="!this.user.login">
                                    <router-link to="/signup" tag="b-button"
                                                 class="text-nowrap btn-black-invert border-0 border-radius text-uppercase navbar-item-font">
                                        sign up
                                    </router-link>
                                </div>
                                <div class="mr-4" v-else>
                                    <router-link to="/account" tag="div"
                                                 class="text-nowrap navbar-item border-0 text-uppercase">
                                        {{this.user.name}}
                                    </router-link>
                                </div>
                            </b-collapse>
                        </b-col>
                    </b-row>
                </b-navbar>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
    export default {
        name: "NavBar",
        props: ['user']
    }
</script>

<style scoped>

</style>