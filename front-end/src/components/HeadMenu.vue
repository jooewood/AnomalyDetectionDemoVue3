<template>
  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    background-color="#000000"
    text-color="#fff"
    active-text-color="#ffd04b"
    @select="handleSelect"
  >
    <el-menu-item index="1">Monitor.AI</el-menu-item>
    <el-sub-menu index="2">
      <template #title>解决方案</template>
      <el-menu-item index="2-1">设备监测</el-menu-item>
      <el-menu-item index="2-2">行为监测</el-menu-item>
      <el-menu-item index="2-3">异常预警</el-menu-item>
    </el-sub-menu>
    <el-menu-item index="3">经典案例</el-menu-item>
    <el-menu-item index="3">联系我们</el-menu-item>
    <el-menu-item index="4">关于明度</el-menu-item>

    <div class="search-box">
      <el-input
        placeholder="全局搜索"
        prefix-icon="el-icon-search"
        clearable
        size="mini"
      ></el-input>
    </div>
  </el-menu>
</template>

<script setup lang="ts"></script>

<style scoped>
/* 顶部菜单样式 */
.el-menu-demo {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

/* 顶部搜索框样式 */
.search-box {
  display: flex;
  align-items: center;
  margin-left: auto;
  margin-right: 20px;
}
</style>
