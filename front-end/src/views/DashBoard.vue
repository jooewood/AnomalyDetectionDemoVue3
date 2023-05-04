<template>
  <HeadMenu />
  <div class="container">
    <div class="sidebar">
      <el-input
        placeholder="批次搜索"
        prefix-icon="el-icon-search"
        clearable
        size="mini"
      ></el-input>
      <el-scrollbar height="1069px">
        <div v-for="(item, index) in buttonList" :key="index">
          <el-button
            class="sidebar-button"
            type="primary"
            color="#000"
            size="medium"
            @click="updateBatchNumber(index)"
            >{{ item }}</el-button
          >
        </div>
      </el-scrollbar>
    </div>
    <div class="content">
      <div class="scrollbar">
        <p>{{ currentTime }}</p>
        <p>当前批次: {{ batchNumber }} / 70</p>
        <div style="display: flex; align-items: center">
          <p
            style="
              margin-right: 10px;
              font-size: 16px;
              color: var(--el-text-color-primary);
            "
          >
            同步
          </p>
          <el-switch
            v-model="syncVar"
            style="
              margin-right: 10px;
            "
            inline-prompt
            active-text="开"
            inactive-text="关"
          />
          <p
            style="
              margin-right: 10px;
              font-size: 16px;
              color: var(--el-text-color-primary);
            "
          >
            实时
          </p>
          <el-switch
            v-model="realTime"
            inline-prompt
            active-text="开"
            inactive-text="关"
          />
        </div>
      </div>
      <chartContainer :key="batchNumber" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, provide, watch, getCurrentInstance } from "vue";
import HeadMenu from "@/components/HeadMenu.vue";
import chartContainer from "@/components/chartContainer.vue";
const realTime = ref(true); // control the mode of picture (dynamic or static)
provide("realTime", realTime);
const syncVar = ref(true)
provide("syncVar", syncVar)

const batchNumber = ref(0); // store the batch number
function updateBatchNumber(number: number) {
  batchNumber.value = number;
}
provide("batchNumber", batchNumber);

const buttonList = ref([]);
const prefix = "青霉素IEEV";
const batchSize = 70;

for (let i = 1; i <= batchSize; i++) {
  buttonList.value.push(`${prefix}${i.toString().padStart(3, "0")}生产批次`);
}

const currentTime = ref("");
function updateTime() {
  const date = new Date();
  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  const day = date.getDate();
  const hour = date.getHours();
  const minute = date.getMinutes();
  const second = date.getSeconds();

  currentTime.value = `${year}年${month}月${day}日 ${hour}:${minute}:${second}`;
}

// 每隔1秒钟更新一次时间
setInterval(updateTime, 1000);
</script>

<style>
/* 侧边栏按钮样式 */
.sidebar {
  width: 15%;
  background-color: #ffffff;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  margin: 1px;
}
.sidebar-button {
  width: 100%;
  margin: 1px;
}

/* 菜单栏下面的 Flex 容器 */
.container {
  display: flex;
  flex-direction: row;
}

/* 菜单栏下面右侧放图的容器 */
.content {
  background-color: #ffffff;
  width: 85%;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  gap: 1px;
  margin: 1px;
}

.scrollbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 45px;
  margin: 4px;
  text-align: center;
  border-radius: 1px;
  background: var(--el-color-primary-light-9);
  color: var(--el-text-color);
  font-size: 18px;
  padding: 0 20px;
}
</style>
