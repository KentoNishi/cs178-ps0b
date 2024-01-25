<script lang="ts">
  import ColoredRectangle from '$lib/components/ColoredRectangle.svelte';
  import { Color } from '$lib/types';
	import { onDestroy, onMount } from 'svelte';
  let color: Color = Color.Red;
  onMount(() => console.log('Mounted!'));
  onDestroy(() => console.log('Unmounted!'));
</script>

<ColoredRectangle {color} on:customEvent={e => console.log(e)} />
<button on:click={() => (color = Color.Red)}>
  Set to Red
</button>
<button on:click={() => (color = Color.Blue)}>
  Set to Blue
</button>
<p>
  The button is
  {#if color === Color.Red}
    red
  {:else}
    blue
  {/if}
</p>
