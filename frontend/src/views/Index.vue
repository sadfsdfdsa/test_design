<template>
    <!--    <div id="main" style="background-color: #f4f7f6;">-->
    <div id="main">
        <NavBar></NavBar>
        <b-container fluid>
            <b-row>
                <b-col class="text-center banner-section">
                    <div style="color: white;" class="margin-nav">
                        <h1 style="font-size: 6em">Header</h1>
                        <div style="font-size: 2em">New York | 04.04.2001</div>
                    </div>
                </b-col>
            </b-row>
            <b-row align-h="center" class="mt-2">
                <b-col style="font-family: 'Helvetica Neue'" class="font-size-14" sm="6">
                    <h1 class="text-center">Sub header</h1>
                    <p> Erat magnis a vitae sapien fermentum tincidunt vel cum elit. Mollis
                        dictum elit eu neque metus ad fermentum in eleifend quam netus Varius ridiculus, eu curabitur eu
                        pretium.</p>
                    <h2>Test</h2>
                    <p>Varius Nisl sollicitudin lorem. Elit malesuada malesuada hac mi. Facilisi penatibus ad neque
                        vehicula Nascetur curabitur nunc sapien tempus orci ut. Consequat sit, nulla sociosqu massa.
                        Rhoncus, dui nunc nunc duis aliquet mi dapibus consequat phasellus fringilla vulputate.</p>

                    <p>Pulvinar facilisis convallis maecenas nec hymenaeos praesent. Nisl eleifend justo quam etiam
                        gravida
                        varius ridiculus magnis auctor. Platea vestibulum aenean elementum ullamcorper. Sodales nascetur
                        duis molestie. At ut vestibulum pharetra mus etiam ligula laoreet.</p>
                    <b-img src="https://images.adsttc.com/media/images/5a42/a9f1/b22e/38db/4100/039c/newsletter/BeFunky_Collage.jpg?1514318318"
                           fluid></b-img>
                    <h2>More info</h2>
                    <p> Pulvinar facilisis convallis maecenas nec hymenaeos praesent. Nisl eleifend justo quam etiam
                        gravida
                        varius ridiculus magnis auctor. Platea vestibulum aenean elementum ullamcorper. Sodales nascetur
                        duis molestie. At ut vestibulum pharetra mus etiam ligula laoreet.</p>
                </b-col>
            </b-row>
            <b-row align-h="center" class="mt-2">
                <b-col sm="6">
                    <hr>
                    <b-button size="lg" class="btn-black">See more</b-button>
                </b-col>
            </b-row>
            <b-row class="mt-4" align-h="center">
                <b-col class="text-center banner-section-1" sm="8">
                    <div style="color: white;" class="margin-nav">
                        <h1 style="font-size: 6em">Main Header</h1>
                        <div style="font-size: 2em">Place | Date</div>
                    </div>
                </b-col>
            </b-row>
            <b-row align-h="center">
                <b-col style="font-family: 'Helvetica Neue'" class="font-size-14" sm="6">
                    <h1 class="text-center">Theme of themes</h1>
                    Nulla nullam ultrices eleifend tempor. Eros. Feugiat ad ultricies
                    condimentum risus malesuada tempor potenti rhoncus sem penatibus pharetra ultrices congue imperdiet
                    semper arcu velit per erat justo ridiculus parturient Cum non parturient primis venenatis litora
                    amet hymenaeos, rhoncus rutrum aptent leo porta interdum primis urna. Orci. Auctor aptent conubia
                    amet inceptos at cras lacus curabitur tristique nisl elit phasellus ante conubia pede luctus
                    praesent gravida ullamcorper montes est nunc, curabitur class malesuada magna enim hendrerit.
                    Adipiscing mus. Lacus lacinia inceptos. Metus morbi est at tellus cras.<br>

                    Augue. Ad molestie ullamcorper ornare magnis vulputate. Nonummy, in erat a tempor laoreet cursus
                    consequat enim. Mus eget suscipit natoque dignissim condimentum rutrum penatibus. Cubilia nibh
                    Dignissim duis, vestibulum nibh turpis elementum diam. Ultrices magnis tincidunt augue lacinia augue
                    malesuada quam proin aenean pretium viverra dui sociis. Felis porta tempus. Lorem consectetuer
                    aptent erat fusce, sollicitudin aenean pellentesque iaculis. Fames, nisl non mattis nostra posuere,
                    morbi fermentum laoreet nam. Venenatis praesent varius varius. Amet mollis dignissim phasellus etiam
                    cum.
                </b-col>
            </b-row>
            <b-row align-h="center" class="mt-2">
                <b-col sm="6">
                    <hr>
                    <b-button size="lg" class="btn-black">See more</b-button>
                </b-col>
            </b-row>
        </b-container>
        <Footer class="mt-5 mb-2"></footer>
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

<style scoped>

</style>