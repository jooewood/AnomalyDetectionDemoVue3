<template>
  <div class="home">
    <img alt="Vue logo" :src="anoma" width="500" />
    <HelloWorld msg="异常检测Demo" />
  </div>
</template>

<script setup lang="ts">
import anoma from '@/assets/img/anoma.png'
</script>

<style lang="less" scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--c-text);
  padding: calc(var(--w-space) * 3) 0;
  margin: 0 auto;
  position: absolute;
  left: 50%;
  top:50%;
  transform: translate(-50%,-50%);
}
</style>
