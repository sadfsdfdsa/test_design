<template>
    <div id="main">
        <b-container class="margin-nav">
            <b-row>
                <b-col>
                    <b-button v-b-toggle.sidebar-1 class="btn-black">Guide</b-button>
                    <b-sidebar id="sidebar-1" title="Sidebar" shadow>
                        <div class="px-3 py-2">
                            <p>
                                Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis
                                in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.
                            </p>
                            <b-img src="https://picsum.photos/500/500/?image=54" fluid></b-img>
                        </div>
                    </b-sidebar>
                </b-col>
            </b-row>
            <b-row>
                <b-col sm="2">
                    <b-nav vertical class="w-10 border-bottom">
                        <b-nav-item active>Active</b-nav-item>
                        <b-nav-item>Link</b-nav-item>
                        <b-nav-item-dropdown
                                id="my-nav-dropdown"
                                text="Dropdown"
                                toggle-class="nav-link-custom">
                            <b-dropdown-item>One</b-dropdown-item>
                            <b-dropdown-item>Two</b-dropdown-item>
                            <b-dropdown-divider></b-dropdown-divider>
                            <b-dropdown-item>Three</b-dropdown-item>
                        </b-nav-item-dropdown>
                        <b-nav-item>Another Link</b-nav-item>
                    </b-nav>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
    export default {
        name: "Platform"
    }
</script>

<style scoped>

</style>