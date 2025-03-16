<template>
    <div class="left-nav">
        <div class="first-item" @click="navigateTo('/home/Model')">
            <i class="el-icon-s-grid"></i>
            模型信息
        </div>
        <div @click="navigateTo('/home/Detection')">
            <i class="el-icon-camera-solid"></i>
            目标检测
        </div>
        <div @click="navigateTo('/home/Records')">
            <i class=" el-icon-s-operation"></i>
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
    color: white;
    /* background-image: url(../assets/image.png); */

    div {
        height: 100px;
        padding: 2px;
        font-size: 35px;
        border-bottom: 5px solid white;
        line-height: 100px;
    }

    div:hover {
        color: chocolate;
    }


}
</style>