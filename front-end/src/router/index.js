// 导入Vue和VueRouter
import Vue from 'vue'
import VueRouter from 'vue-router'

// 安装VueRouter为Vue的插件
Vue.use(VueRouter)

// 导入需要通过路由展示的组件
import Home from '../home/index.vue'
import Detection from "../detection/index.vue"
import Records from "../Records/index.vue"
import Model from "../Model/index.vue"

// 创建路由实例
const router = new VueRouter({
    routes: [

        // 定义路由规则，path为匹配的路径，component为对应的展示组件
        {
            path: '/home',
            component: Home,
            children: [
                {
                    path: "Detection",
                    name: "Detection",
                    component: Detection,
                    meta: {
                        title: "目标检测",
                    }
                },
                {
                    path: "Records",
                    name: "Records",
                    component: Records,
                    meta: {
                        title: "记录管理",
                    }
                },
                {
                    path: "Model",
                    name: "Model",
                    component: Model,
                    meta: {
                        title: "模型信息",
                    }
                },

                {
                    path: '', // 当访问 /home 时，默认重定向到 /home/Detection
                    redirect: 'Detection'
                }
            ]
        },
        {
            // 根路径
            path: "/",
            // 重定向 自动被重定向/login
            redirect: "/home"
        }
    ]
})

// 导出路由实例
export default router