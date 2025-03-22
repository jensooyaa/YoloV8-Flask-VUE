<template>
    <div class="content">
        <div class="rows">
            <el-image :src="srcList[0]" :preview-src-list="srcList" fit="fit"></el-image>
            <el-image :src="srcList[1]" :preview-src-list="srcList" fit="fit"></el-image>

        </div>
        <div class="rows">
            <el-image :src="srcList[2]" :preview-src-list="srcList" fit="fit"></el-image>
            <el-image :src="srcList[3]" :preview-src-list="srcList" fit="fit"></el-image>
        </div>
        <div class="rows">
            <el-image :src="srcList[4]" :preview-src-list="srcList" fit="fit"></el-image>
            <el-image :src="srcList[5]" :preview-src-list="srcList" fit="fit"></el-image>
            <!-- <img src="../assets/F1_curve.png" alt=""> -->
        </div>
    </div>
</template>

<script>

export default {
    name: 'Records',
    components: {

    },
    data() {
        return {
            srcList: [
                require('../assets/yolo.png'),
                require('../assets/result.png'),
                require('../assets/F1_curve.png'),
                require('../assets/P_curve.png'),
                require('../assets/PR_curve.png'),
                require('../assets/R_curve.png')
            ]
        }
    },

};
</script>

<style>
.content {
    overflow-y: auto;
}

.rows {
    .el-image {
        margin: 10px;
        border: 10px solid gray;
        /* width: 200px; */
        /* height: 180px; */
    }

    display: flex;

}
</style>