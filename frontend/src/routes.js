import Index from "./views/Index.vue";
import SignUpView from "./views/SignUpPage";
import SignInPage from "./views/SignInPage";


const routes = [
    {
        path: "/",
        component: Index,
        name: "indexPage",
        meta: {}
    },
    {
        path: "/signup",
        component: SignUpView,
        name: "signupPage",
        meta: {}
    },
        {
        path: "/signin",
        component: SignInPage,
        name: "signinPage",
        meta: {}
    },
];

export default routes;