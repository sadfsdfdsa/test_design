<template>
    <div id="main">
        <NavBar></NavBar>
        <b-container class="margin-nav">
            <b-row align-h="center">
                <b-col sm="8" class="mt-3">
                    <div class="mt-3">
                        <b-row>
                            <b-col align-self="center">
                                <b-card no-body class="border-0 shadow border-radius">
                                    <b-row no-gutters>
                                        <b-col md="6">
                                            <b-card-img src="https://picsum.photos/400/400/?image=20" alt="Image"
                                                        class="border-radius-left"></b-card-img>
                                        </b-col>
                                        <b-col md="6">
                                            <b-row>
                                                <b-col>
                                                    <b-card-body>
                                                        <b-row>
                                                            <b-col class="h-font"><h3>Dashboard update</h3>
                                                            </b-col>
                                                        </b-row>
                                                        <b-card-text>
                                                            This is a wider card with supporting text as a natural
                                                            lead-in to
                                                            additional content.
                                                            This content is a little bit longer.
                                                        </b-card-text>
                                                        <b-row>
                                                            <b-col>
                                                                <div class="font-weight-light text-muted">Author:
                                                                    Shuvaev
                                                                    Artem
                                                                </div>
                                                            </b-col>
                                                        </b-row>
                                                        <b-row>
                                                            <b-col class="text-right">
                                                                <b-button class="bg-pink border-0" pill>Read more
                                                                </b-button>
                                                            </b-col>
                                                        </b-row>
                                                    </b-card-body>
                                                </b-col>
                                            </b-row>
                                        </b-col>
                                    </b-row>
                                </b-card>
                            </b-col>
                        </b-row>
                    </div>
                </b-col>
            </b-row>
            <b-row align-h="center" class="mt-3">
                <b-col sm="8" class="mt-3">
                    <div class="mt-3">
                        <b-row>
                            <b-col align-self="center">
                                <b-card no-body class="border-0 shadow border-radius">
                                    <b-row no-gutters>
                                        <b-col md="6">
                                            <b-row>
                                                <b-col>
                                                    <b-card-body>
                                                        <b-row>
                                                            <b-col class="h-font"><h3>Tasks update</h3>
                                                            </b-col>
                                                        </b-row>
                                                        <b-card-text>
                                                            This is a wider card with supporting text as a natural
                                                            lead-in to
                                                            additional content.
                                                            This content is a little bit longer.
                                                        </b-card-text>
                                                        <b-row>
                                                            <b-col>
                                                                <div class="font-weight-light text-muted">Author:
                                                                    Shuvaev
                                                                    Artem
                                                                </div>
                                                            </b-col>
                                                        </b-row>
                                                        <b-row>
                                                            <b-col class="text-right">
                                                                <b-button class="bg-blue border-0" pill>Read more
                                                                </b-button>
                                                            </b-col>
                                                        </b-row>
                                                    </b-card-body>
                                                </b-col>
                                            </b-row>
                                        </b-col>
                                        <b-col md="6">
                                            <b-card-img src="https://picsum.photos/600/600/?image=25" alt="Image"
                                                        class="border-radius-right"></b-card-img>
                                        </b-col>
                                    </b-row>
                                </b-card>
                            </b-col>
                        </b-row>
                    </div>
                </b-col>
            </b-row>
        </b-container>
        <Footer class="mt-5"></footer>
    </div>
</template>

<script>
    import note from "../assets/note_marketing.png";

    import NavBar from "../components/NavBar";
    import Footer from "../components/Footer";

    export default {
        components: {Footer, NavBar},
        data: () => ({
            imgs: {
                note_img: note
            }
        }),

    }
</script>

<style>

</style>