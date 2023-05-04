<template>
  <h1>{{ msg }}</h1>

  <hr />
  <el-button type="primary" @click="handleClick">进入</el-button>

</template>

<script setup lang="ts">
import { ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useMessageStore } from '@/stores'


defineProps<{ msg: string }>()

const count = ref<number>(0)
const store = useMessageStore()
const { message } = storeToRefs(store)

import { useRouter } from 'vue-router'
const router = useRouter()
const handleClick = ():void => {
  router.push('/dashboard')
}
</script>

<style lang="less" scoped>
ul {
  li {
    line-height: 2;
  }
}

blockquote {
  color: var(--c-black);
  background-color: var(--c-gray);
  padding: calc(var(--w-space) / 2);
  border-radius: var(--w-radius-xs);
  p {
    margin: 0;
  }
}

hr {
  width: 60%;
  border-color: var(--c-border);
  margin: var(--w-space) auto;
  opacity: 0.2;
}

a {
  color: #42b983;
}

p {
  margin: 0;
}

code {
  background-color: White;
  padding: 2px 4px;
  border-radius: 4px;
  color: #304455;
}
</style>
