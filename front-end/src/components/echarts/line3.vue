<template>
  <div class="chart" ref="chartContainer"></div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watchEffect, watch, inject } from "vue";
import * as echarts from "echarts";
import { useDataZoomStore } from "@/stores/dataZoom";
const dataZoomStore = useDataZoomStore();

const realTime = ref(inject("realTime"));
const XmarkLine = ref(inject("XmarkLine"));
const XmarkArea = ref(inject("XmarkArea"));

function generateMarkAreaData() {
  return XmarkArea.value.map(([start, end]) => {
    return [{ xAxis: start }, { xAxis: end }];
  });
}

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

const chartContainer = ref(null);
let chartInstance;

const createMarkLines = () => {
  return XmarkLine.value.map((index) => {
    return {
      xAxis: index,
      lineStyle: {
        color: "#FF0000",
        // type: "solid",
      },
    };
  });
};

const option = ref({
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
  },
  yAxis: {
    type: "value",
  },
  series: [
    {
      data: props.yData,
      type: "line",
      color: ["#8bc34a"],
      markLine: {
        data: createMarkLines(),
        symbol: "none",
        label: {
          show: false,
        },
      },
      markArea: {
        data: generateMarkAreaData(),
      },
    },
  ],
  dataZoom: {
    type: "slider",
    start: dataZoomStore.start,
    end: dataZoomStore.end,
    show: !realTime.value,
    height: 25,
    bottom: 15,
    realtime: true,
    filterMode: "none",
  },
});

onMounted(() => {
  chartInstance = echarts.init(chartContainer.value, "dark");
  chartInstance.setOption(option.value);
  chartInstance.on("dataZoom", (params: any) => {
    dataZoomStore.setDataZoom(params.start, params.end);
  });
});

const updateChart = (xData, yData, markLines) => {
  if (!chartInstance) return;

  chartInstance.setOption({
    xAxis: {
      data: xData,
    },
    series: [
      {
        data: yData,
        markLine: {
          data: markLines,
        },
      },
    ],
  });
};

watch(
  [() => props.xData, () => props.yData, () => XmarkLine.value],
  ([xData, yData, XmarkLine]) => {
    updateChart(xData, yData, createMarkLines());
  },
  { immediate: true, deep: true }
);

watch(
  () => XmarkArea.value,
  () => {
    if (!chartInstance) return;

    chartInstance.setOption({
      series: [
        {
          markArea: {
            data: generateMarkAreaData(),
          },
        },
      ],
    });
  },
  { immediate: true, deep: true }
);

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

watch(
  () => realTime.value,
  (newValue) => {
    chartInstance.setOption({
      dataZoom: {
        show: !newValue,
      },
    });
  }
);

onUnmounted(() => {
  chartInstance.dispose();
});
</script>

<style scoped>
.chart {
  width: 100%;
  height: 25vh;
}
</style>
