<template>
    <div id="main">
        <!--        <NavBar></NavBar>-->
        <b-container class="margin-nav">
            <b-row class="mt-5"></b-row>
            <b-row class="text-center mt-5" align-h="center">
                <b-col class="mt-5 text-center" sm="6" cols="12">
                    <b-row class="mt-5">
                        <b-col class="h-font">Sign In</b-col>
                    </b-row>
                    <b-row class="text-center" align-h="center">
                        <b-col class="text-center" sm="10">
                            <b-input-group class="mt-3">
                                <b-form-input class=" border-0 input-underline" autofocus v-model="input.email"
                                              placeholder="Enter your email address"></b-form-input>
                            </b-input-group>
                        </b-col>
                    </b-row>
                    <b-row class="text-center" align-h="center">
                        <b-col class="text-center" sm="10">
                            <b-input-group class="mt-3">
                                <b-form-input class=" border-0 input-underline" v-model="input.pass"
                                              placeholder="Enter a password" type="password"></b-form-input>
                            </b-input-group>
                        </b-col>
                    </b-row>
                    <b-row class="text-center mt-2" align-h="center" align-v="center">
                        <b-col class="text-center mt-3" sm="6">
                            <b-form-checkbox
                                    id="checkbox-1"
                                    name="checkbox-1"
                                    :value="true"
                                    :unchecked-value="false"
                                    v-model="input.remember_flag"
                            >
                                Remember me
                            </b-form-checkbox>
                        </b-col>
                        <b-col class="text-center mt-3" sm="6">
                            <b-button size="md" pill class="border-0 btn-black-invert" @click="login">Login
                            </b-button>
                        </b-col>
                    </b-row>
                    <!--<b-row class="text-left" align-h="start">-->
                    <!--<b-col class="text-left ml-5" sm="2">-->
                    <!--<b-img src="https://cdn.auth0.com/blog/googleoauth/logo.png"-->
                    <!--fluid center class="shadow border-radius active_bottom_shadow cursor"-->
                    <!--alt="Responsive image"></b-img>-->
                    <!--</b-col>-->
                    <!--</b-row>-->
                </b-col>
            </b-row>
        </b-container>
        <Footer class="fixed-bottom">
        </Footer>
    </div>
</template>

<script>
    import Footer from "../components/Footer";

    export default {
        name: "SignIn",
        components: {Footer},
        props: ['user'],
        data: () => ({
            input: {
                pass: "",
                email: "",
                remember_flag: false
            },
        }),
        methods: {
            login() {
                if (this.input.pass && this.input.email) {
                    let tmp = {
                        name: "Artem Shuvaev"
                    }
                    this.$emit('do_login', tmp)
                    this.$router.push({path: this.$route.query.redirect_to ? this.$route.query.redirect_to : '/'})
                    return;
                }
                this.$snotify.warning('Complete all fields')
            }
        },
        created() {
        }
    }
</script>

<style scoped>

</style>