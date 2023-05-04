<template>
  <Chart
    class="chart"
    v-if="t"
    :title="t"
    :xData="xData"
    :yData="yData"
    :x_mark="props.x_mark"
  />
</template>
<script setup>
import { ref, inject, watch, watchEffect } from "vue";
import axios from "axios";

import Chart from "@/components/echarts/line3.vue";

const props = defineProps({
  title: String,
  x_data: Array,
  y_data: Array,
  x_mark: {
    type: Array,
    required: false,
  },
});

const realTime = ref(inject("realTime"));

const xData = ref([]);
const yData = ref([]);
const t = ref("");
t.value = props.title;

const windowSize = 300;
const windowStep = 1;

const state = ref({
  count: 0,
  timer: null, // 添加一个timer属性
});

let i = windowSize - windowStep;

const updateChart = (x_data, y_data, r) => {
  if (r) {
    clearInterval(state.timer);
    xData.value = x_data.slice(0, windowSize);
    yData.value = y_data.slice(0, windowSize);
    state.timer = setInterval(() => {
      i = (i + windowStep) % x_data.length;
      xData.value.splice(0, 1);
      xData.value.push(x_data[i]);
      yData.value.splice(0, 1);
      yData.value.push(y_data[i]);
    }, 100);
  } else {
    clearInterval(state.timer);
    xData.value = x_data;
    yData.value = y_data;
  }
};

watchEffect(() => {
  updateChart(props.x_data, props.y_data, realTime.value);
});

function getRandomBoolean() {
  // generate a random number between 0 and 1
  const randomNum = Math.random();
  // if the number < 0.9, return true
  if (randomNum < 1) {
    return true;
  } else {
    // else return flase
    return false;
  }
}

const normal = ref(true);
normal.value = getRandomBoolean();
</script>
<style scoped>
.chart {
  width: 24.85%;
  height: 25vh;
  margin: 1px;
}
</style>
