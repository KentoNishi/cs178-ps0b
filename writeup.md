## Some Concepts in Svelte

### Components
Components are the building blocks of Svelte apps--they are reusabe, self-contained, and typically semantically named. Each component is defined in a `.svelte` file. Components can be nested within each other, and can be passed data via props. Components can also emit events to the parent component. They are most useful for code separation.

#### Example
##### `ColoredRectangle.svelte`:
```html
<script lang="ts">
  import { Color } from '$lib/types';
  export let color: Color;
</script>

<div class:red={color === Color.Red} class:blue={color === Color.Blue} />

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

##### `types.ts`:
```ts
export enum Color {
  Red = "red",
  Blue = "blue",
};
```

### Reactivity
Svelte is a reactive framework, which means the UI is automatically updated when the underlying data in variables changes. Reactive variables can be passed to components as props (or even two-way bound), and the value of the variable will be synced between the parent and child component.

##### `Main.svelte`:
```html
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
```

### Logic Blocks
Logic blocks can be used to conditionally and declaratively render content. The contents of logic blocks are automatically updated when the underlying data changes. Some common logic blocks are `#if`, `#each`, and `#await`.

#### Example
##### `Main.svelte`:
```html
...

<p>
  The button is
  {#if color === Color.Red}
    red
  {:else}
    blue
  {/if}
</p>
```

### Events
Events can be emitted from components and listened to by parent components. Events are especially useful for tracking user interactions with the UI. For example, Svelte implements the `on:click` event for most native HTML elements (like `button`, `div`, `input`, etc.). Svelte also allows programmers to define custom events.

#### Example
##### `Main.svelte`:
```html
...

<ColoredRectangle {color} on:customEvent={e => console.log(e)} />

...
```

##### `ColoredRectangle.svelte`:
```html
<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  ...
  const dispatch = createEventDispatcher();
</script>

<div
  class:red={color === Color.Red}
  class:blue={color === Color.Blue}
  on:click={() => dispatch('customEvent', { color })}
/>
```

### Lifecycle Hooks
Svelte provides component lifecycle hooks which can be used to run code at specific points in the lifecycle. Some common hooks include `onMount` and `onDestroy`. `onMount` is called when the component is first mounted to the DOM, and `onDestroy` is called when the component is removed from the DOM. These hooks are critical for initializing and cleaning up resources.

#### Example
##### `Main.svelte`:
```html
<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  ...
  onMount(() => console.log('Mounted!'));
  onDestroy(() => console.log('Unmounted!'));
</script>
...
```

