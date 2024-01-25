<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import { Color } from '$lib/types';
  export let color: Color;
  const dispatch = createEventDispatcher();
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div
  class:red={color === Color.Red}
  class:blue={color === Color.Blue}
  on:click={() => dispatch('customEvent', { color })}
/>

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
