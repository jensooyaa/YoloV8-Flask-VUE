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
            <el-table-column prop="type" label="对应模型" />
            <el-table-column prop="details" label="检测目标详情" />
            <el-table-column>
                <!-- 查询框 根据户主姓名查询 -->
                <template #header>
                    <el-input v-model="search" size="small" placeholder="请输入查询内容" @blur="searchLink" />
                </template>
            </el-table-column>
        </el-table>
        <!-- 分页 -->
        <el-pagination :current-page="currentPage" :page-size="pageSize" :total="list.length"
            :page-sizes="[5, 10, 15, 20]" layout="total, sizes, prev, pager, next, jumper" :disabled="false"
            @size-change="handleSizeChange" @current-change="handleCurrentChange" />
    </div>
</template>

<script>
import { eventBus } from "../eventBus.js"
export default {
    name: 'Recordlists',
    components: {
        // RecordLists
    },
    data() {
        return {
            search: '',
            currentPage: 1,
            pageSize: 5,
            list: []
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
</style>