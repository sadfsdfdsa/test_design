<template>
    <div id="main">
        <NavBar></NavBar>
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
                                <b-form-input class="border-radius border-0"
                                              placeholder="Enter your email address"></b-form-input>
                            </b-input-group>
                        </b-col>
                    </b-row>
                    <b-row class="text-center" align-h="center">
                        <b-col class="text-center" sm="10">
                            <b-input-group class="mt-3">
                                <b-form-input class="border-radius border-0"
                                              placeholder="Enter a password" type="password"></b-form-input>
                            </b-input-group>
                        </b-col>
                    </b-row>
                    <b-row class="text-center" align-h="center">
                        <b-col class="text-center" sm="10">
                            <b-input-group class="mt-3">
                                <b-form-input class="border-radius border-0 bg-blue text-white"
                                              type="password"></b-form-input>
                            </b-input-group>
                        </b-col>
                    </b-row>
                    <hr>
                    <b-row class="text-center" align-h="center">
                        <b-col class="text-center mt-3" sm="6">
                            <b-form-checkbox
                                    id="checkbox-1"
                                    name="checkbox-1"
                                    value="accepted"
                                    unchecked-value="not_accepted"
                            >
                                I accept the terms and use
                            </b-form-checkbox>
                        </b-col>
                        <b-col class="text-center mt-3" sm="6">
                            <b-button size="lg" pill class="border-0 bg-pink active_bottom_shadow">Create account
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
    </div>
</template>

<script>
    import NavBar from "../components/NavBar";
    import Footer from "../components/Footer";

    export default {
        name: "SignUpView",
        components: {Footer, NavBar}
    }
</script>

<style scoped>

</style>