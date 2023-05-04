<template>
  <v-chart :option="option" autoresize @chart:datazoom="onDataZoom"/>
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
  DataZoomComponent,
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";
import { defineProps, ref, provide, watchEffect, inject, watch } from "vue";
import { useDataZoomStore } from "@/stores/dataZoom";
const dataZoomStore = useDataZoomStore();

const realTime = ref(inject("realTime"));

use([
  CanvasRenderer,
  LineChart,
  TitleComponent,
  GridComponent,
  TooltipComponent,
  LegendComponent,
  GraphicComponent,
  DataZoomComponent,
]);

provide(THEME_KEY, "dark");

const props = defineProps({
  title: String,
  xData: Array,
  yData: Array,
  normal: {
    type: Boolean,
    required: false,
    default: true,
  },
});

const option = ref({
  backgroundColor: "#000",
  title: {
    text: props.title,
    left: "center",
  },
  tooltip: {
    trigger: "axis",
  },
  xAxis: {
    type: "category",
    data: props.xData,
    // type: 'value',
    // name: 'X Axis',
    // axisLabel: {
    //   formatter: '{value}',
    // },
  },
  yAxis: {
    type: "value",
    // name: 'Y Axis',
    // axisLabel: {
    //   formatter: '{value}',
    // },
  },
  series: [
    {
      data: props.yData,
      type: "line",
      color: ["#8bc34a"],
    },
  ],
  dataZoom: {
    type: "slider",
    start: dataZoomStore.start,
    end: dataZoomStore.end,
    show: false,
    height: 15,
    bottom: 20,
    realtime: true,
    filterMode: "none",
  },
  graphic: [
    {
      type: "circle",
      right: "1.5%",
      top: "8%",

      shape: {
        cx: 0,
        cy: 0,
        r: 15,
      },
      style: {
        fill: props.normal ? "#000" : "#FF0000",
      },
    },
  ],
});

// let intervalId: NodeJS.Timeout | null = null;

watchEffect(() => {
  option.value.dataZoom.show = !realTime.value;
  option.value.xAxis.data = props.xData;
  option.value.series[0].data = props.yData;
  VChart?.value?.setOption(option.value);

  // option.value.graphic[0].style.fill = props.normal ? "#000" : "#FF0000";
  // if (!props.normal) {
  //   if (intervalId !== null) {
  //     clearInterval(intervalId);
  //     intervalId = null;
  //   }
  //   let isGreen = true;
  //   intervalId = setInterval(() => {
  //     option.value.graphic[0].style.fill = isGreen ? "yellow" : "#FF0000";
  //     isGreen = !isGreen;
  //   }, 500);
  // } else {
  //   if (intervalId !== null) {
  //     clearInterval(intervalId);
  //     intervalId = null;
  //   }
  // }
});

function onDataZoom(event: any) {
  const newStart = event.start;
  const newEnd = event.end;
  dataZoomStore.setDataZoom(newStart, newEnd);
}

// watch(
//   () => [dataZoomStore.start, dataZoomStore.end],
//   ([start, end]) => {
//     // 更新组件的 option
//     option.value.dataZoom.start = start;
//     option.value.dataZoom.end = end;
//     VChart?.value?.setOption(option.value);
//   }
// );

watch(
  () => [dataZoomStore.start, dataZoomStore.end],
  ([start, end]) => {
    // 更新组件的 option
    option.value.dataZoom.start = start;
    option.value.dataZoom.end = end;
    VChart?.value?.setOption({ dataZoom: option.value.dataZoom }, true);
  }
);


</script>

<style scoped>
.chart {
  width: 100%;
  height: 100%;
}
</style>