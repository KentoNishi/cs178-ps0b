## Concepts in Svelte

### Components
Components are the building blocks of Svelte apps--they are reusabe, self-contained, and typically semantically named. Each component is defined in a `.svelte` file. Components can be nested within each other, and can be passed data via props. Components can also emit events to the parent component.

#### Example
##### `App.svelte`:
```html
<script lang="ts">
  import ColoredRectangle from './ColoredRectangle.svelte';
  import ColoredButton from './ColoredButton.svelte';
  import type { Color } from './types';
  let color: Color = Color.red;
</script>

<Rectangle {color} />
<button on:click={() => (color = Color.red)}>
  Set to Red
</button>
<button on:click={() => (color = Color.blue)}>
  Set to Blue
</button>
```
##### `ColoredRectangle.svelte`:
```html
<script lang="ts">
  import type { Color } from './types';
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
```


### Reactivity & Binding
Svelte is a reactive framework, which means the UI is automatically updated when the underlying data in variables changes. 

### Logic Blocks
### Events
### Lifecycle Hooks
