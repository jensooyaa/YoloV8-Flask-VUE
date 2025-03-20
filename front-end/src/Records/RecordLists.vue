<template>
    <div style="margin: 10px;">
        <!-- 分页处理 -->
        <el-table :data="list.slice(
            (currentPage - 1) * pageSize,
            currentPage * pageSize
        )
            " stripe border style="width: 100%" max-height="850px" overflow-y: auto>
            <!-- 展示信息 -->
            <el-table-column prop="id" label="检测时间" />
            <el-table-column prop="origin" label="原始图像">
                <template slot-scope="scope">
                    <el-image :src="scope.row.origin" :preview-src-list="scope.row.srcList1"></el-image>
                </template>
            </el-table-column>
            <el-table-column prop="decection" label="检测结果">
                <template slot-scope="scope">
                    <el-image :src="scope.row.decection" :preview-src-list="scope.row.srcList2"></el-image>
                </template>
            </el-table-column>
            <el-table-column prop="type" label="对应模型">
                <template slot-scope="scope">
                    <el-button type="success" plain disabled>{{ scope.row.type }}</el-button>
                </template>
            </el-table-column>
            <el-table-column prop="details" label="检测目标详情">
                <template slot-scope="scope">
                    <div @click="view(scope.row.feature_list)"><el-button type="success" round>查看</el-button></div>
                    <!-- <div class="view" @click="view(scope.row.feature_list)">{{ scope.row.details }}</div> -->
                </template>
            </el-table-column>
        </el-table>
        <!-- 分页 -->
        <el-pagination :current-page="currentPage" :page-size="pageSize" :total="list.length"
            :page-sizes="[5, 10, 15, 20]" layout="total, sizes, prev, pager, next, jumper" :disabled="false"
            @size-change="handleSizeChange" @current-change="handleCurrentChange" />
        <feature class="feature" :feature_list="feature_list" :isShow="isShow" :key="componentKey"></feature>
    </div>
</template>

<script>
import { eventBus } from "../eventBus.js"
import feature from "../components/feature.vue";
export default {
    name: 'Recordlists',
    components: {
        feature
    },
    data() {
        return {
            search: '',
            currentPage: 1,
            pageSize: 5,
            list: [],
            feature_list: [],
            isShow: false,
            componentKey: 0
        }
    },
    methods: {
        searchLink() {

        },
        handleSizeChange(val) {
            this.pageSize = val;
        },
        handleCurrentChange(val) {
            this.currentPage = val;
        },
        view(val) {
            this.feature_list = val;
            this.isShow = true;
            this.componentKey++;
        }
    },
    created() {
        const storedData = localStorage.getItem('recordsList');
        if (storedData) {
            this.list = JSON.parse(storedData);
        }
    },
}

</script>


<style>
/* 设置表头背景色 */
.el-table thead.is-group th,
.el-table thead:not(.is-group) th {
    background-color: #f0f9eb;
}

/* 设置 el-table 行的高度 */
.el-table .el-table__row {
    height: 150px;
}

.view:hover {
    color: orangered;
}

.feature {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
</style>