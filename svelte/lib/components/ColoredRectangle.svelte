<script lang="ts">
  import type { Color } from '$lib/types';
  export let color: Color;
</script>

<div class:red={color === Color.red} class:blue={color === Color.blue} />

<style>
  div {
    width: 100px;
    height: 100px;
  }
  .red {
    background-color: red;
  }
  .blue {
    background-color: blue;
  }
</style>
