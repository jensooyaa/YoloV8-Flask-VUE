// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import axios from 'axios'
import Element from 'element-ui'
import echarts from "echarts";
import router from './router/index.js'
Vue.prototype.$echarts = echarts;
import '../node_modules/element-ui/lib/theme-chalk/index.css'
import '../src/assets/style.css'
import './theme/index.css'
// import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// import ElementPlus from 'element-plus'
// import 'element-plus/dist/index.css'
Vue.use(Element)
// Vue.use(ElementPlus)

Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.prototype.$http = axios

// // 全局注册组件
Vue.component("App", App);

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    render: h => h(App)
})
