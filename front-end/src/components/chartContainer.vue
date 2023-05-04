<template>
  <div class="chart-container">
    <div class="y">
      <LineChart :title="t" :x_data="x" :y_data="y" :key="t" />
      <el-result :icon="iconName" :title="iconTitle"></el-result>
    </div>
    <el-collapse v-model="activeCollapse">
      <el-collapse-item title="传感器监测详情" name="1">
        <div>
          <el-scrollbar height="800px">
            <div class="charts-row">
              <LineChart
                class="chart-item"
                v-for="k in keys.slice()"
                :key="k"
                :title="k"
                :x_data="x"
                :y_data="data_dict[k]"
              />
            </div>
          </el-scrollbar>
        </div>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script setup lang="ts">
import {
  ref,
  inject,
  watch,
  provide,
  onBeforeMount,
  nextTick,
  computed,
} from "vue";
import axios from "axios";
import LineChart from "@/components/drawSensor.vue";

const batchNumber = ref(inject("batchNumber"));
const isDataLoaded = ref(false);
const activeCollapse = ref(["1"]);

const normal = ref(false);

const iconName = computed(() => (normal.value ? "success" : "error"));
const iconTitle = computed(() => (normal.value ? "正常" : "异常"));

const keys = ref([]);
const data_dict = ref({});
const y = ref([]);
const x = ref([]);
const t = ref("Penicillin concentration(P:g/L)");
const XmarkLine = ref([]);
const XmarkArea = ref([]);
provide("XmarkLine", XmarkLine);
provide("XmarkArea", XmarkArea);

onBeforeMount(() => {
  const apiUrl = `http://127.0.0.1:5000/api/data/${batchNumber.value}`;
  axios.get(apiUrl).then((res) => {
    keys.value = Object.keys(res.data);
    data_dict.value = res.data;
    y.value = res.data["Penicillin concentration(P:g/L)"];
    x.value = res.data["Time (h)"];

    XmarkLine.value = res.data["markLine"];
    XmarkArea.value = res.data["markArea"];

    normal.value = res.data["normal"];
    keys.value.splice(keys.value.indexOf("normal"), 1);
    keys.value.splice(keys.value.indexOf("markLine"), 1);
    keys.value.splice(keys.value.indexOf("markArea"), 1);
    keys.value.splice(keys.value.indexOf("Penicillin concentration(P:g/L)"), 1);
    keys.value.splice(keys.value.indexOf("Batch_ref"), 1);
    keys.value.splice(keys.value.indexOf("Time (h)"), 1);
    isDataLoaded.value = true;
  });
});
</script>

<style lang="less" scoped>
.charts-row {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
.chart-container {
  margin: 1px;
}

.y {
  display: flex;
  flex-direction: row;
}

.chart-item {
  flex-basis: 24.5%;
  box-sizing: border-box;
  margin: 1px;
}
</style>
