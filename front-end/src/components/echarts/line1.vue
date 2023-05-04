<template>
  <div class="chart" ref="chart"></div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import * as echarts from "echarts";

const chart = ref(null);

onMounted(() => {
  axios.get("http://127.0.0.1:5000/data").then((res) => {
    const { x_data, y_data, title } = res.data;

    const option = {
      backgroundColor: "#000000",
      title: {
        text: title,
        left: "center",
        textStyle: {
            color: '#fff' // 将颜色设置为白色
        }
      },
      tooltip: {
        trigger: "axis",
      },
      xAxis: {
        type: "category",
        data: x_data,
      },
      yAxis: {
        type: "value",
        max: 200
      },
      series: [
        {
          data: y_data,
          type: "line",
          smooth: true,
          color: ["yellow"],
        },
      ],
    };

    const myChart = echarts.init(chart.value);
    myChart.setOption(option);
  });
});
</script>

<style scoped>
.chart {
  width: 100%;
  height: 25vh;
  margin: 1px;
}
</style>
