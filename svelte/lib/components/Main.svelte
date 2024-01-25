<script lang="ts">
  import ColoredRectangle from '$lib/components/ColoredRectangle.svelte';
  import { Color } from '$lib/types';
  let color: Color = Color.Red;
</script>

<ColoredRectangle {color} />
<button on:click={() => (color = Color.Red)}>
  Set to Red
</button>
<button on:click={() => (color = Color.Blue)}>
  Set to Blue
</button>
