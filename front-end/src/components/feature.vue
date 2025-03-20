<template>
    <div v-if="isShow" style="padding: 10px;">
        <div class="close-button-container" @click="close">
            <el-button type="danger" size="mini">关闭</el-button>
        </div>
        <el-table :data="feature_list" height="500px" border style="width: 750px; text-align: center"
            v-loading="loading" element-loading-text="数据正在处理中，请耐心等待" element-loading-spinner="el-icon-loading" lazy>
            <el-table-column label="目标类别" width="250px">
                <template slot-scope="scope">
                    <span>{{ scope.row[2] }}</span>
                </template>
            </el-table-column>
            <el-table-column label="目标大小" width="250px">
                <template slot-scope="scope">
                    <span>{{ scope.row[0] }}</span>
                </template>
            </el-table-column>
            <el-table-column label="置信度" width="250px">
                <template slot-scope="scope">
                    <span>{{ scope.row[1] }}</span>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
    name: "feature",
    data() {
        return {};
    },
    props: {
        feature_list: {
            type: Array,
            default: () => []
        },
        isShow: {
            type: Boolean,
            default: () => false
        }
    },
    methods: {
        close() {
            this.isShow = false
        }
    }

};
</script>

<style>
.close-button-container {
    position: absolute;
    top: 10px;
    right: 10px;
    z-index: 1;
}
</style>