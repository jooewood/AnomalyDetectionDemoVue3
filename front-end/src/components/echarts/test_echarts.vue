<template>
  <div class="chart">
    <v-chart class="chart" :option="option" autoresize />
  </div>
</template>
<script setup lang="ts">
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { LineChart } from "echarts/charts";
import {
  TitleComponent,
  GridComponent,
  TooltipComponent,
  LegendComponent,
  GraphicComponent,
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";
import { defineProps, ref, provide, watchEffect } from "vue";

use([
  CanvasRenderer,
  LineChart,
  TitleComponent,
  GridComponent,
  TooltipComponent,
  LegendComponent,
  GraphicComponent,
]);

provide(THEME_KEY, "dark");

const props = defineProps({
  normal: {
    type: Boolean,
    required: false,
    default: false,
  },
});

const option = ref({
  // backgroundColor: "#000",
  title: {
    text: "XXX",
    left: "center",
  },
  tooltip: {
    trigger: "axis",
  },
  xAxis: {
    type: "category",
    data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
  },
  yAxis: {
    type: "value",
  },
  series: [
    {
      data: [820, 932, 901, 934, 1290, 1330, 1320],
      type: "line",
      color: ["yellow"],
    },
  ],
  graphic: [
    {
      type: "circle",
      right: "2.5%",
      top: "5%",

      shape: {
        cx: 0,
        cy: 0,
        r: 15,
      },
      style: {
        fill: props.normal ? "#8bc34a" : "#FF0000",
      },
    },
  ],
});

let intervalId: NodeJS.Timeout | null = null;

watchEffect(() => {
  option.value.graphic[0].style.fill = props.normal ? "#8bc34a" : "#FF0000";
  if (!props.normal) {
    if (intervalId !== null) {
      clearInterval(intervalId);
      intervalId = null;
    }
    let isGreen = true;
    intervalId = setInterval(() => {
      option.value.graphic[0].style.fill = isGreen ? "#8bc34a" : "#FF0000";
      isGreen = !isGreen;
    }, 500);
  } else {
    if (intervalId !== null) {
      clearInterval(intervalId);
      intervalId = null;
    }
  }
});
</script>
<style>
.chart {
  width: 400px;
  height: 400px;
}
</style>
