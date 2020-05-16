<template>
    <div id="main">
        <!--<svg viewBox="0 0 120 120" version="1.1" style="position: absolute"-->
             <!--class="d-none d-lg-block circle"-->
             <!--xmlns="http://www.w3.org/2000/svg">-->
            <!--<circle cx="5" cy="5" r="5" style="color: white;"/>-->
        <!--</svg>-->
        <NavBar></NavBar>
        <b-container class="margin-nav">
            <b-row align-h="center">
                <b-col sm="10" class="mt-3">
                    <b-carousel
                            id="carousel-1"
                            controls
                            indicators
                            background="#ababab"
                            img-width="1024"
                            img-height="480"
                            style="text-shadow: 1px 1px 2px #333;"
                    >
                        <!-- Text slides with image -->
                        <b-carousel-slide
                                caption="First slide"
                                text="Nulla vitae elit libero, a pharetra augue mollis interdum."
                                img-src="https://picsum.photos/1024/480/?image=52"
                        ></b-carousel-slide>

                        <!-- Slides with custom text -->
                        <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54">
                            <h1>Hello world!</h1>
                        </b-carousel-slide>

                        <!-- Slides with image only -->
                        <b-carousel-slide
                                img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>

                        <!-- Slides with img slot -->
                        <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
                        <b-carousel-slide>
                            <template v-slot:img>
                                <img
                                        class="d-block img-fluid w-100"
                                        width="1024"
                                        height="480"
                                        src="https://picsum.photos/1024/480/?image=55"
                                        alt="image slot"
                                >
                            </template>
                        </b-carousel-slide>

                        <!-- Slide with blank fluid image to maintain slide aspect ratio -->
                        <b-carousel-slide caption="Blank Image" img-blank img-alt="Blank image">
                            <p>
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eros
                                felis,
                                tincidunt
                                a tincidunt eget, convallis vel est. Ut pellentesque ut lacus vel interdum.
                            </p>
                        </b-carousel-slide>
                    </b-carousel>
                </b-col>
            </b-row>
            <b-row class="mt-3">
                <b-col class="text-center">
                    <div class="h-font">
                        Why we
                    </div>
                </b-col>
            </b-row>
            <b-row align-h="center">
                <b-col sm="3" align-self="stretch" class="mt-3">
                    <b-card class="border-0 border-radius shadow btn-black cursor-0">
                        <b-card-text>
                            <b-row>
                                <b-col class="text-center font-size-14 snotifyToast__buttons--bold text-nowrap">
                                    simple
                                </b-col>
                            </b-row>
                        </b-card-text>
                    </b-card>
                </b-col>
                <b-col sm="3" align-self="stretch" class="mt-3">
                    <b-card class="border-0 border-radius shadow bg-pink cursor-0">
                        <b-card-text>
                            <b-row>
                                <b-col class="text-center font-size-14 snotifyToast__buttons--bold text-nowrap">
                                    useful
                                </b-col>
                            </b-row>
                        </b-card-text>
                    </b-card>
                </b-col>
                <b-col sm="3" align-self="stretch" class="mt-3">
                    <b-card class="border-0 border-radius shadow bg-blue cursor-0">
                        <b-card-text>
                            <b-row>
                                <b-col class="text-center font-size-14 snotifyToast__buttons--bold text-nowrap">
                                    fast
                                </b-col>
                            </b-row>
                        </b-card-text>
                    </b-card>
                </b-col>
            </b-row>
            <b-row class="mt-3">
                <b-col class="text-center">
                    <div class="h-font">
                        Services
                    </div>
                </b-col>
            </b-row>
            <b-row align-h="center">
                <b-col sm="5" align-self="stretch" class="mt-3 d-flex align-items-stretch">
                    <b-card class="border-0 border-radius shadow">
                        <b-card-text>
                            <b-row class="h-font">
                                <b-col>Dashboard
                                </b-col>
                            </b-row>
                            <hr>
                            <b-row>
                                <b-col>
                                    <b-img :src="require('../assets/note_marketing.png')" fluid></b-img>
                                </b-col>
                            </b-row>
                            <b-row>
                                <b-col class="text-center">
                                    <b-button class="bg-blue border-radius border-0" size="lg">Go to Dashboard
                                    </b-button>
                                </b-col>
                            </b-row>
                        </b-card-text>
                    </b-card>
                </b-col>
                <b-col sm="5" align-self="stretch" class="mt-3 d-flex align-items-stretch ">
                    <b-card class="border-0 border-radius shadow">
                        <b-card-text>
                            <b-row class="h-font">
                                <b-col>Tasks
                                </b-col>
                            </b-row>
                            <hr>
                            <b-row>
                                <b-col>
                                    <b-img :src="require('../assets/tasks.png')" fluid></b-img>
                                </b-col>
                            </b-row>
                            <b-row class="mt-4">
                                <b-col class="text-center mt-5">
                                    <b-button class="bg-pink border-radius border-0" size="lg">Go to Tasks
                                    </b-button>
                                </b-col>
                            </b-row>
                        </b-card-text>
                    </b-card>
                </b-col>
            </b-row>
            <b-row class="mt-3">
                <b-col class="text-center"><p class="text-uppercase h-font">Links</p></b-col>
            </b-row>
            <b-row align-h="center">
                <b-col sm="8">
                    <b-row no-gutters class="text-nowrap" align-h="center">
                        <b-col cols="5" lg="2" class="text-center">
                            <b-button
                                    class="btn-black-invert border-radius border-0 shadow active_bottom_shadow"
                                    size="lg">
                                GitHub
                            </b-button>
                        </b-col>
                        <b-col cols="5" lg="2" class="text-center">
                            <b-button
                                    class="btn-black border-radius border-0 shadow active_bottom_shadow"
                                    size="lg">Gmail
                            </b-button>
                        </b-col>
                        <b-col cols="5" lg="2" class="text-center">
                            <b-button class="bg-blue  border-radius border-0 shadow active_bottom_shadow"
                                      size="lg">VK
                            </b-button>
                        </b-col>
                        <b-col cols="5" lg="2" class="text-center">
                            <b-button class="bg-pink  border-radius border-0 shadow active_bottom_shadow"
                                      size="lg">Heroku
                            </b-button>
                        </b-col>
                    </b-row>
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