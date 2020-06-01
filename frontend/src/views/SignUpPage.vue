<template>
    <div id="main">
        <!--        <NavBar></NavBar>-->
        <b-container class="margin-nav">
            <b-row class="mt-5"></b-row>
            <b-row class="text-center mt-5" align-h="center">
                <b-col class="mt-5 text-center" sm="6" cols="12">
                    <b-row class="mt-5">
                        <b-col class="h-font">Sign Up</b-col>
                    </b-row>
                    <b-row class="text-center" align-h="center">
                        <b-col class="text-center" sm="10">
                            <b-input-group class="mt-3">
                                <b-form-input class=" border-0 input-underline" v-model="input.username" autofocus trim
                                              placeholder="Create username"></b-form-input>
                            </b-input-group>
                        </b-col>
                    </b-row>
                    <b-row class="text-center" align-h="center">
                        <b-col class="text-center" sm="10">
                            <b-input-group class="mt-3">
                                <b-form-input class="border-0 input-underline" v-model="input.email" trim
                                              placeholder="Enter your email address"></b-form-input>
                            </b-input-group>
                        </b-col>
                    </b-row>
                    <b-row class="text-center" align-h="center">
                        <b-col class="text-center" sm="10">
                            <b-input-group class="mt-3">
                                <b-form-input class=" border-0 input-underline" v-model="input.pass"
                                              @update="input.show_pass_again=true"
                                              placeholder="Enter a password" type="password"></b-form-input>
                            </b-input-group>
                        </b-col>
                    </b-row>
                    <b-row class="text-center" align-h="center" v-if="input.show_pass_again && input.pass.length>0">
                        <b-col class="text-center" sm="10">
                            <b-input-group class="mt-3">
                                <b-form-input class=" border-0 input-underline" placeholder="Password again"
                                              v-model="input.pass_again"
                                              type="password"></b-form-input>
                            </b-input-group>
                        </b-col>
                    </b-row>
                    <b-row class="text-center mt-2" align-h="center" align-v="center">
                        <b-col class="text-center mt-3" sm="5">
                            <b-form-checkbox
                                    class="check-box"
                                    id="checkbox-1"
                                    name="checkbox-1"
                                    :value="true"
                                    :unchecked-value="false"
                                    v-model="input.check_terms">
                                Accept the terms and use
                            </b-form-checkbox>
                        </b-col>
                        <b-col class="text-center mt-3" sm="5">
                            <b-button size="md" pill class="border-0 btn-black-invert" @click="create_account">Create
                                account
                            </b-button>
                        </b-col>
                    </b-row>
                </b-col>
            </b-row>
        </b-container>
        <Footer class="fixed-bottom"></Footer>
    </div>
</template>

<script>
    import Footer from "../components/Footer";

    export default {
        name: "SignUpView",
        components: {Footer},
        props: ['user'],
        data: () => ({
            input: {
                username: "",
                pass: "",
                email: "",
                pass_again: "",
                check_terms: false,
                show_pass_again: false
            }
        }),
        methods: {
            create_account() {
                if (this.input.pass && this.input.email && this.input.pass === this.input.pass_again && this.input.check_terms) {
                    this.$api.post("/signup/", {password: this.input.pass, email: this.input.email, username: this.input.username}).then((data) => {
                        if (data.data.result === "success") {
                            this.$emit('do_login', data.data.data.user, {remember_flag: this.input.remember_flag})
                            localStorage[this.$store.state.LSV.access_token] = data.data.data.access_token;
                            localStorage[this.$store.state.LSV.refresh_token] = data.data.data.refresh_token;
                            localStorage[this.$store.state.LSV.login] = 'true';
                            this.$router.push({path: this.$route.query.redirect_to ? this.$route.query.redirect_to : '/'})
                        } else {
                            this.$snotify.error(data.data.error.msg);
                        }
                    });
                    return;
                }
                this.$snotify.warning('Complete all fields please!')
            }
        },
        created() {
        }
    }
</script>

<style scoped>

</style>