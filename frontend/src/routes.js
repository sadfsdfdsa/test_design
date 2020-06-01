import Index from "./views/Index.vue";
import SignUpView from "./views/SignUpPage";
import SignInPage from "./views/SignInPage";
import Test from "./views/Test";
import AccountPage from "./views/AccountPage";
import Platform from "./views/Platform";


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
    {
        path: "/test",
        component: Test,
        name: "testPage",
        meta: {}
    },
    {
        path: "/account",
        component: AccountPage,
        name: "accountPage",
        meta: {}
    },
    {
        path: "/platform",
        component: Platform,
        name: "platformPage",
        meta: {}
    },
];

export default routes;