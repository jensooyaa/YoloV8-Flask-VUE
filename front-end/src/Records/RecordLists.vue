<template>
    <div style="margin: 10px;">
        <!-- 分页处理 -->
        <el-table :data="showList.slice(
            (currentPage - 1) * pageSize,
            currentPage * pageSize
        )
            " stripe border style="width: auto" max-height="850px" overflow-y: auto>
            <!-- 展示信息 -->
            <!-- <el-table-column prop="id" label="检测时间" /> -->
            <el-table-column prop="id" label="检测时间" fit>
                <template slot="header">
                    <div style="display: flex;">
                        <!-- <div> 时间</div> -->
                        <el-date-picker size="small" v-model="chooseTimeRange" type="datetimerange" style="width: auto"
                            range-separator="至" :start-placeholder="startTime" :end-placeholder="endTime">
                        </el-date-picker>
                    </div>
                </template>
            </el-table-column>
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
                    <div>
                        <el-button type="success" round @click="view(scope.row.feature_list)">查看</el-button>
                        <el-button type="danger" round @click="deleteItem(scope.row.id)">删除</el-button>
                    </div>
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
// import { eventBus } from "../eventBus.js"
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
            visible: false,
            list: [],//原始数据
            showList: [],//展示数据
            feature_list: [],
            isShow: false,
            componentKey: 0,
            startTime: "开始时间",
            endTime: "结束时间",
            chooseTimeRange: '',
            showDialog: false
        }
    },
    methods: {
        handleSizeChange(val) {
            this.pageSize = val;
        },
        handleCurrentChange(val) {
            this.currentPage = val;
        },
        view(val) {
            this.feature_list = val;
            this.isShow = true;
            this.visible = true;
            this.componentKey++;
            this.showDialog = true;
        },

        deleteItem(id) {

            this.$confirm('此操作将永久删除该记录, 是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                this.isShow = false;
                this.list = this.list.filter((item) => item.id !== id)
                localStorage.setItem('recordsList', JSON.stringify(this.list));

                this.$message({
                    type: 'success',
                    message: '删除成功!'
                });
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消删除'
                });
            });
        },
        formatDate(date) {
            const year = date.getFullYear();
            const month = String(date.getMonth() + 1).padStart(2, '0');
            const day = String(date.getDate()).padStart(2, '0');
            const hours = String(date.getHours()).padStart(2, '0');
            const minutes = String(date.getMinutes()).padStart(2, '0');
            const seconds = String(date.getSeconds()).padStart(2, '0');

            return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
        },

    },
    created() {
        const storedData = localStorage.getItem('recordsList');
        if (storedData) {
            this.list = JSON.parse(storedData);
        }
    },
    watch: {
        chooseTimeRange(newValue) {
            console.log("newValue", newValue)
            const start = this.formatDate(newValue[0]);
            const end = this.formatDate(newValue[1]);
            this.showList = this.list;
            this.showList = this.showList.filter((item) => new Date(item.id) >= new Date(start) && new Date(item.id) <= new Date(end));
            // location.reload();
        },
        list(newValue) {
            this.showList = newValue;
        }
    }
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