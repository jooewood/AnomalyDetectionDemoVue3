<template>
  <div ref="chartContainer" style="width: 800px; height: 400px"></div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch, provide } from "vue";
import * as echarts from "echarts";
import { useDataZoomStore } from "@/stores/dataZoom";

const chartContainer = ref(null);
let chartInstance: any;

const dataZoomStore = useDataZoomStore();

const markLineIndices = [1, 3, 5]; 
const markLineData = markLineIndices.map((index) => {
  return {
    xAxis: index,
  };
});

const XmarkArea = ref([[1, 2], [5, 6]]);

function generateMarkAreaData() {
  return XmarkArea.value.map(([start, end]) => {
    return [
      { xAxis: start },
      { xAxis: end },
    ];
  });
}

onMounted(() => {
  chartInstance = echarts.init(chartContainer.value, "dark");

  const option = {
    title: {
      text: "xxx",
      left: "center",
    },
    xAxis: {
      type: "category",
      data: [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
      ],
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        data: [120, 200, 150, 80, 70, 110, 130, 90, 100, 180, 220, 250],
        type: "line",
        markLine: {
          data: markLineData,
          symbol: "none",
          
          label: {
            formatter: 'Index: {c}',
          },
        },
        markArea: {
          data: generateMarkAreaData(),
        },
      },
    ],
    dataZoom: [
      {
        type: "slider",
        start: dataZoomStore.start,
        end: dataZoomStore.end,
        realtime: true,
        filterMode: "none",
      },
    ],
  };

  chartInstance.setOption(option);

  chartInstance.on("dataZoom", (params: any) => {
    dataZoomStore.setDataZoom(params.start, params.end);
  });
});

watch(
  () => [dataZoomStore.start, dataZoomStore.end],
  ([start, end]) => {
    chartInstance.dispatchAction({
      type: "dataZoom",
      start,
      end,
    });
  }
);

onUnmounted(() => {
  chartInstance.dispose();
});
</script>
