<template>
    <div id="main">
<!--        <NavBar></NavBar>-->
        <div id="sub_main">
            <b-container class="margin-nav" style="position: absolute">
                <b-row>
                    <b-col cols="3">
                        <b-row>
                            <b-col>
                                Timer 0 = infinity time (seconds):
                                <b-input placeholder="time" v-model="game_settings.game_timer"></b-input>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col>
                                Interval for creating new items (ms):
                                <b-input placeholder="interval" v-model="game_settings.timeout_creating"></b-input>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col>
                                Interval for item live (seconds):
                                <b-input placeholder="live seconds" v-model="game_settings.seconds_live"></b-input>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col>
                                <b-checkbox placeholder="live seconds" v-model="game_settings.use_letters"
                                            :value="true"
                                            :unchecked-value="false">
                                    Add letters ({{Array.from(new
                                    Set(this.letters_variants_string.split(''))).join(',')}})
                                </b-checkbox>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col>
                                <b-checkbox placeholder="live seconds" v-model="game_settings.use_only_letters"
                                            :value="true"
                                            :unchecked-value="false">
                                    Spawning only letters
                                </b-checkbox>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col>
                                Keys:
                                <b-input placeholder="interval" v-model="letters_variants_string"></b-input>
                            </b-col>
                        </b-row>
                    </b-col>
                    <b-col class="text-center" cols="2">
                        <b-row>
                            <b-col>
                                <b-button @click="stop" variant="danger" size="lg">Stop</b-button>
                                <b-button @click="start" variant="success" size="lg">Start</b-button>

                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col>
                                <div class="font-weight-light text-muted">Enter to start game
                                </div>
                            </b-col>
                        </b-row>
                    </b-col>
                    <b-col cols="2" class="text-center">
                        <h3>Time: {{this.show_timer}}s</h3>
                    </b-col>
                    <b-col cols="2" class="text-center">
                        <h3 style="color: green">Kills: {{this.game_counter_kill}}</h3>
                    </b-col>
                    <b-col cols="2" class="text-center">
                        <h3 style="color: red">Loses: {{this.game_counter_lose}}</h3>
                    </b-col>
                </b-row>
                <b-row style="padding-left: 60%;" align-v="center">
                    <b-col v-for="(letter, index) in letters.slice(0, 4)" :key="index" :cols="index===0?6:2"
                           @click="remove_ball(index)" class="text-center">
                        <div :style="'font-size: '+(index===0?12:3)+'em; '+(index===0?'border-bottom: 10px solid '+show_border_color+';':'')"
                             class="text-capitalize">
                            <strong>{{letter.letter}}</strong>
                        </div>
                    </b-col>
                </b-row>
            </b-container>
            <div v-for="(boll, index) in bolls" :key="index"
                 @click="remove_ball(index)"
                 :style="boll.style">
                {{boll.time}} <h1>{{boll.letter}}</h1>
            </div>
        </div>
    </div>
</template>

<script>
    import NavBar from "../components/NavBar";

    export default {
        name: "Test",
        components: {NavBar},
        data: () => ({
            bolls: [],
            letters: [],
            active_screen: {
                width: 0,
                height: 0
            },

            show_timer: 0,
            show_border_color: "black",

            game_is_active: false,
            game_counter_kill: 0,
            game_counter_lose: 0,
            game_settings: {
                timeout_creating: 350,
                seconds_live: 10,
                use_letters: true,
                use_only_letters: true,
                letter_spawning_chance: 0.3,
                game_timer: 10
            },
            game_intervals: {
                creating_balls: null,
                removing_balls: null,
                removing_letters: null,
                timer_gui: null,
                timer_stopping: null
            },
            letters_variants: [
                'q', 'w', 'e', 'r'
            ],
            letters_variants_string: "qwer"
        }),
        methods: {
            start() {
                if (this.game_is_active) {
                    this.stop();
                }

                this.game_is_active = true;
                this.bolls = [];
                this.letters = [];
                this.letters_variants = Array.from(new Set(this.letters_variants_string.split('')))
                this.game_counter_kill = 0;
                this.game_counter_lose = 0;
                if (this.game_settings.use_only_letters) {
                    this.game_settings.letter_spawning_chance = 1000;
                    this.game_settings.use_letters = true;
                    this.game_intervals.removing_letters = setInterval(this.remove_letters_by_time, 1000);
                    window.addEventListener('keypress', this.event_keypress)
                }

                this.game_intervals.creating_balls = setInterval(this.create_balls, parseInt(this.game_settings.timeout_creating))
                this.game_intervals.removing_balls = setInterval(this.remove_balls_by_time, 1000)

                if (parseInt(this.game_settings.game_timer) > 0) {
                    this.game_settings.game_timer = parseInt(this.game_settings.game_timer);
                    this.game_intervals.timer_stopping = setTimeout(this.stop, 1000 * (this.game_settings.game_timer + 1))
                    this.show_timer = this.game_settings.game_timer
                    this.game_intervals.timer_gui = setInterval(this.timer_interval_gui, 1000)
                }
            },
            timer_interval_gui() {
                this.show_timer--;
            },

            stop() {
                this.game_is_active = false;

                clearTimeout(this.game_intervals.timer_stopping);
                clearInterval(this.game_intervals.timer_gui)
                clearInterval(this.game_intervals.creating_balls);
                clearInterval(this.game_intervals.removing_balls);
                clearInterval(this.game_intervals.removing_letters)
                window.removeEventListener("keypress", this.event_keypress);
            },
            event_keypress(event) {
                if (this.letters[0].letter === event.key) {
                    this.remove_letter(0, true)

                    this.show_border_color = "green";
                    setTimeout(this.unset_color, 300)

                    return;
                }

                this.show_border_color = "red";
                setTimeout(this.unset_color, 300)

                this.game_counter_lose++;
            },
            unset_color() {
                this.show_border_color = "black";
            },

            remove_ball(index, by_user = true) {
                this.game_is_active ? (by_user ? this.game_counter_kill++ : this.game_counter_lose++) : false;
                this.$delete(this.bolls, index)
            },
            remove_letter(index, by_user = true) {
                this.game_is_active ? (by_user ? this.game_counter_kill++ : this.game_counter_lose++) : false;
                this.$delete(this.letters, index)
            },
            create_balls() {
                // 90 navbar height

                let tmp_letter = "";
                let tmp_w = 0;
                let tmp_h = 0;
                let tmp_style = '';

                this.game_settings.use_letters ? ((Math.floor(Math.random() * Math.floor(100))) <= 100 * this.game_settings.letter_spawning_chance ?
                    tmp_letter = this.letters_variants[((Math.floor(Math.random() * Math.floor(this.letters_variants.length))))] : false) : false;
                if (tmp_letter === '') {
                    tmp_w = Math.floor(Math.random() * Math.floor(this.active_screen.width));
                    tmp_h = 90 + Math.floor(Math.random() * Math.floor(this.active_screen.height - 200));
                    tmp_style = "position: absolute; height: 50px; width: 50px; border-radius: 50px; background: red; " +
                        "margin-top: " + tmp_h + "px;" +
                        " margin-left: " + tmp_w + "px;"

                    this.bolls.push({
                        letter: tmp_letter,
                        time: this.game_settings.seconds_live,
                        style: tmp_style
                    });
                } else {
                    tmp_w = this.active_screen.width / 2;
                    tmp_h = this.active_screen.height / 2;

                    this.letters.push({
                        letter: tmp_letter,
                        time: this.game_settings.seconds_live,
                    });
                }
            },
            remove_balls_by_time() {
                for (let i = 0; i < this.bolls.length; i++) {
                    this.bolls[i].time--;
                    if (this.bolls[i].time <= 0) {
                        this.remove_ball(i, false);
                    }
                }
            },
            remove_letters_by_time() {
                for (let i = 0; i < this.letters.length; i++) {
                    this.letters[i].time--;
                    if (this.letters[i].time <= 0) {
                        this.remove_letter(i, false);
                    }
                }
            },

            control_keys(event) {
                if (event.key === 'Enter') {
                    this.start()
                    return;
                }
                if (event.key === "Escape") {
                    this.stop();
                }

            }
        },
        created() {
            this.active_screen.width = window.innerWidth - 100;
            this.active_screen.height = window.innerHeight - 100;

            window.addEventListener('keyup', this.control_keys)
        }
    }
</script>

<style scoped>

</style>