import { defineStore } from 'pinia';

export const useDataZoomStore = defineStore({
  id: 'dataZoom',

  state: () => ({
    start: 0,
    end: 100,
  }),

  actions: {
    setDataZoom(start: number, end: number) {
      this.start = start;
      this.end = end;
    },
  },
});
