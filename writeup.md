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

## Some Concepts in Flask

### App Object
The `Flask` class is the main object of a Flask application. Once instantiated to a variable typically named `app`, the object can be used to register routes and run the application.

#### Example
##### `app.py`:
```py
from flask import Flask
app = Flask(__name__)

...

if __name__ == '__main__':
    app.run(debug=True)
```

### Routes
Routes are the URLs which the application responds to. They are registered to the `app` object using the `@app.route` decorator. The decorator takes a URL path and an optional list of HTTP methods (if empty, it defaults to GET). The function under the decorator is called when the route is requested. The route URL can also contain variable parts, which are passed to the function as arguments.

#### Example
##### `app.py`:
```py
...
@app.route('/add', methods=['POST'])
def add_todo():
    ...

@app.route('/remove/<int:index>')
def remove_todo(index):
    ...
```

### Request Object
The `request` object contains information about the request sent to the server. The object provides access to the request method, headers, body, query string, and form data. The object is often used to access the form data sent from a POST request.

#### Example
##### `app.py`:
```py
...
def add_todo():
    todo_item = request.form.get('todo_item')
    if todo_item:
        todos.append({'task': todo_item, 'completed': False})
    ...
```

### HTML Templates
Flask uses the Jinja templating engine to render dynamic/conditional content, with somewhat similar syntax to Svelte. Templates are stored in the `templates` directory and are rendered with the `render_template` function. Templates can use variables within double brackets (`{{}}`), and values for the variables can be passed as keyword arguments to `render_template`. Note that the content is not automatically reactive, and requires a page refresh to update (or a `redirect` call).

#### Example
##### `app.py`:
```py
...
@app.route('/')
def index():
    return render_template('base.html', todos=todos)
...
```

##### `base.html`:
```html
...
    {% for item in todos %}
      <span>{{ item.task }}</span>
    {% endfor %}
...
```

## Debugging

### Svelte
I am a DIEHARD Svelte enthusiast. I used Vue until about 4 years ago, when I discovered Svelte. I have been using Svelte for all of my personal projects ever since, and some of my apps have become somewhat popular. For example, my Chrome extensions built with Svelte have tens of thousands of weekly users ([link](https://github.com/LiveTL/LiveTL)), and it even received a [MadeWithSvelte entry](https://madewithsvelte.com/livetl). Some of my commissioned Svelte websites have also been viewed millions of times.

When running my Svelte application, I set up a SvelteKit project with the `npm create svelte@latest .` command. However, during the setup process, I mistakenly opted into the Svelte 5 beta compiler. This led to dev mode being completely broken, and I was unable to run the application. I spent some time checking the debug logs, and found a warning from Vite about the Svelte compiler version. After I realized my mistake, I re-ran the command to reinitialize the project with the compiler version downgraded to `4.2.7`, and the application ran as expected. 

### Flask
I have also used Flask fairly extensively in the past, but most of my use came from serving either REST APIs or static assets. I was not aware that Flask had a templating engine, so I learned a lot about it as I went through the tutorial.

When I was initially following the tutorial linked for the Flask todo app in the assignment description ([link](LINK)), I had an error like the following:
```
RuntimeError: Working outside of application context.
```

To fix the issue, I navigated to Google and found the appropriate Flask documentation page describing the [Application Context](https://flask.palletsprojects.com/en/3.0.x/appcontext/#manually-push-a-context). From here, I learned that the app's context must be pushed before using the database. To fix the issue, I simply added this line with the `with` statement within my `if __name__ == '__main__'` block, and the code ran as expected.

Afterwards, I wanted to write my own ultra-simple todo app to get a better understanding of Jinja templates. To do so, I completely got rid of the database and just used a list of dictionaries to store the todo items. I also wrote my own routes to support adding, checking off, and removing todo items. 