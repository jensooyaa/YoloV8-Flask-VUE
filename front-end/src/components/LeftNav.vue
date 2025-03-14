<template>
    <div class="left-nav">
        <div class="first-item" @click="navigateTo('/home/Model')">
            模型信息
        </div>
        <div @click="navigateTo('/home/Detection')">
            目标检测
        </div>
        <div @click="navigateTo('/home/Records')">
            记录管理
        </div>

    </div>
</template>

<script>
export default {
    name: 'LeftNav',
    methods: {
        navigateTo(path) {
            this.$router.push(path);
        }
    }
};

</script>

<style scoped>
.left-nav {
    width: 300px;
    background-color: #21B3B9;
    height: 100%;

    div {
        height: 100px;
        padding: 2px;
        color: white;
        font-size: 30px;
        border-bottom: 5px solid white;
        line-height: 100px;
    }

    div:hover {
        color: chocolate;
    }


}
</style>