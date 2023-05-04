<template>
  <Chart
    class="chart"
    v-if="t"
    :title="t"
    :xData="xData"
    :yData="yData"
    :normal="normal"
  />
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

import Chart from "@/components/echarts/line2.vue";

const xData = ref([]);
const yData = ref([]);
const t = ref("");

const windowSize = 10; // 滑动窗口的长度
const windowStep = 1; // 滑动窗口的步长

axios.get("http://127.0.0.1:5000/data").then((res) => {
  const { x_data, y_data, title } = res.data;
  xData.value = x_data.slice(0, windowSize);
  yData.value = y_data.slice(0, windowSize);
  t.value = title;
  let i = windowSize - windowStep;
  setInterval(() => {
    i = (i + windowStep) % x_data.length;
    xData.value.splice(0, 1);
    xData.value.push(x_data[i]);
    yData.value.splice(0, 1);
    yData.value.push(y_data[i]);
  }, 1000); // 间隔为 1 秒钟
});

function getRandomBoolean() {
  // 生成一个在 0 到 1 之间的随机数
  const randomNum = Math.random();
  // 如果随机数小于 0.9，返回 true，有 90% 的概率返回 true
  if (randomNum < 0.9) {
    return true;
  } else {
    // 否则返回 false，有 10% 的概率返回 false
    return false;
  }
}

const normal = ref(true);
normal.value = getRandomBoolean();

</script>

<style scoped>
.chart {
  width: 24%;
  height: 25vh;
  margin: 1px;
}
</style>
