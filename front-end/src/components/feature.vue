<template>
    <div v-if="isShow" class="pop">
        <div class="close-button-container" @click="close">
            <el-button type="danger" size="mini">关闭</el-button>
        </div>
        <div style="background-color:#f0f9eb ;">检测目标详情</div>
        <el-table :data="feature_list" height="600px" border text-align: center v-loading="loading"
            element-loading-text="数据正在处理中，请耐心等待" element-loading-spinner="el-icon-loading" lazy>
            <el-table-column label="目标类别" width="300px">
                <template slot-scope="scope">
                    <span>{{ scope.row[2] }}</span>
                </template>
            </el-table-column>
            <el-table-column label="目标大小" width="300px">
                <template slot-scope="scope">
                    <span>{{ scope.row[0] }}</span>
                </template>
            </el-table-column>
            <el-table-column label="置信度" width="300px">
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
            // default: () => false
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
.pop {
    border: 16px solid #f0f9eb;
    /* padding: 50px; */
}

.close-button-container {
    position: absolute;
    top: 10px;
    right: 10px;
    z-index: 1;
}
</style>