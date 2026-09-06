---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/additional-utilities.html
---

# Bundling, TypeScript, and source maps for the `APPSYNC_JS` runtime
<a name="additional-utilities"></a>

TypeScript enhances AWS AppSync development by providing type safety and early error detection. You can write TypeScript code locally and transpile it to JavaScript before using it with the `APPSYNC_JS` runtime. The process starts with installing TypeScript and configuring tsconfig.json for the `APPSYNC_JS` environment. You can then use bundling tools like esbuild to compile and bundle the code.

You can leverage custom and external libraries in your handler and function code, as long as they comply with `APPSYNC_JS` requirements. Bundling tools combine code into a single file for use in AWS AppSync. Source maps can be included to aid debugging.

## Leveraging libraries and bundling your code
<a name="using-external-libraries"></a>

In your handler code, you can leverage both custom and external libraries so long as they comply with the `APPSYNC_JS` requirements. This makes it possible to reuse existing code in your application. To make use of libraries that are defined by multiple files, you must use a bundling tool, such as [esbuild](https://esbuild.github.io/), to combine your code in a single file that can then be saved to your AWS AppSync namespace handler code.

When bundling your code, keep the following in mind:
+ `APPSYNC_JS` only supports ECMAScript modules (ESM).
+ `@aws-appsync/*` modules are integrated into `APPSYNC_JS` and should not be bundled with your code.
+ The `APPSYNC_JS` runtime environment is similar to NodeJS in that code does not run in a browser environment.
+ You can include an optional source map. However, do not include the source content.

  To learn more about source maps, see [Using source maps](#source-maps).

For example, to bundle your handler code located at `src/appsync/onPublish.js`, you can use the following esbuild CLI command:

```
$ esbuild --bundle \
--sourcemap=inline \
--sources-content=false \
--target=esnext \
--platform=node \
--format=esm \
--external:@aws-appsync/utils \
--outdir=out/appsync \
 src/appsync/onPublish.js
```

## Building your code and working with TypeScript
<a name="working-with-typescript"></a>

[TypeScript](https://www.typescriptlang.org/) is a programming language developed by Microsoft that offers all of JavaScript’s features along with the TypeScript typing system. You can use TypeScript to write type-safe code and catch errors and bugs at build time before saving your code to AWS AppSync. The `@aws-appsync/utils` package is fully typed.

The `APPSYNC_JS` runtime doesn't support TypeScript directly. You must first transpile your TypeScript code to JavaScript code that the `APPSYNC_JS` runtime supports before saving your code to AWS AppSync. You can use TypeScript to write your code in your local integrated development environment (IDE), but note that you cannot create TypeScript code in the AWS AppSync console.

To get started, make sure you have [TypeScript](https://www.typescriptlang.org/download) installed in your project. Then, configure your TypeScript transcompilation settings to work with the `APPSYNC_JS` runtime using [TSConfig](https://www.typescriptlang.org/tsconfig). Here’s an example of a basic `tsconfig.json` file that you can use:

```
// tsconfig.json
{
  "compilerOptions": {
    "target": "esnext",
    "module": "esnext",
   "noEmit": true,
   "moduleResolution": "node",
  }
}
```

You can then use a bundling tool like esbuild to compile and bundle your code. For example, given a project with your AWS AppSync code located at `src/appsync`, you can use the following command to compile and bundle your code:

```
$ esbuild --bundle \
--sourcemap=inline \
--sources-content=false \
--target=esnext \
--platform=node \
--format=esm \
--external:@aws-appsync/utils \
--outdir=out/appsync \
 src/appsync/**/*.ts
```

### Using generics in TypeScript
<a name="working-with-typescript-generics"></a>

You can use generics with several of the provided types. For example, you can write a handler that makes use of the `√`≈. In your IDE, type definitions and auto-complete hints will guide you into properly using the available utilities.

```
import type { EventOnPublishContext, IncomingEvent, OutgoingEvent } from "@aws-appsync/utils"
import * as ddb from '@aws-appsync/utils/dynamodb'

type Message = {
  id: string;
  text: string;
  owner: string;
  likes: number
}

type OnP<T = any> = {
  request: (ctx: EventOnPublishContext<T>) => unknown,
  response: (ctx: EventOnPublishContext<T>) => OutgoingEvent[] | IncomingEvent[]
}

export const onPublish: OnP<Message> = {
  request(ctx) {
    const msg = ctx.events[0]
    return ddb.update<Message>({
      key: { owner: msg.payload.owner, id: msg.payload.id },
      update: msg.payload,
      condition: { id: { attributeExists: true } }
    })
  },
  response: (ctx) => ctx.events
}
```

## Linting your bundles
<a name="using-lint-with-bundles"></a>

You can automatically lint your bundles by importing the `esbuild-plugin-eslint` plugin. You can then enable it by providing a `plugins` value that enables eslint capabilities. Below is a snippet that uses the esbuild JavaScript API in a file called `build.mjs`:

```
/* eslint-disable */
import { build } from 'esbuild'
import eslint from 'esbuild-plugin-eslint'
import glob from 'glob'
const files = await glob('src/**/*.ts')

await build({
  format: 'esm',
  target: 'esnext',
  platform: 'node',
  external: ['@aws-appsync/utils'],
  outdir: 'dist/',
  entryPoints: files,
  bundle: true,
  plugins: [eslint({ useEslintrc: true })],
})
```

## Using source maps
<a name="source-maps"></a>

You can provide an inline source map (`sourcemap`) with your JavaScript code. Source maps are useful for when you bundle JavaScript or TypeScript code and want to see references to your input source files in your logs and runtime JavaScript error messages.

Your `sourcemap` must appear at the end of your code. It is defined by a single comment line that follows the following format:

```
//# sourceMappingURL=data:application/json;base64,<base64 encoded string>
```

The following is an example of a source map:

```
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsibGliLmpzIiwgImNvZGUuanMiXSwKICAibWFwcGluZ3MiOiAiO0FBQU8sU0FBUyxRQUFRO0FBQ3RCLFNBQU87QUFDVDs7O0FDRE8sU0FBUyxRQUFRLEtBQUs7QUFDM0IsU0FBTyxNQUFNO0FBQ2Y7IiwKICAibmFtZXMiOiBbXQp9Cg==
```

Source maps can be created with esbuild. The example below shows you how to use the esbuild JavaScript API to include an inline source map when code is built and bundled:

```
import { build } from 'esbuild'
import eslint from 'esbuild-plugin-eslint'
import glob from 'glob'
const files = await glob('src/**/*.ts')

await build({
  sourcemap: 'inline',
  sourcesContent: false,

  format: 'esm',
  target: 'esnext',
  platform: 'node',
  external: ['@aws-appsync/utils'],
  outdir: 'dist/',
  entryPoints: files,
  bundle: true,
  plugins: [eslint({ useEslintrc: true })],
})
```

In the preceeding example, the `sourcemap` and `sourcesContent` options specify that a source map should be added in line at the end of each build but should not include the source content. As a convention, we recommend not including source content in your `sourcemap`. You can disable this in esbuild by setting `sources-content` to `false`.

To illustrate how source maps work, review the following example in which handler code references helper functions from a helper library. The code contains log statements in the handler code and in the helper library:

**./src/channelhandler.ts** (your handler)

```
import { EventOnPublishContext }  from "@aws-appsync/utils";
 import { mapper }  from "./lib/mapper";

 exportfunction onPublish ( ctx: EventOnPublishContext ) {
   return ctx.events.map(mapper)
}
```

**./lib/helper.ts** (a helper file)

```
import { IncomingEvent, OutgoingEvent } from "@aws-appsync/utils";

export function mapper(event: IncomingEvent, index: number) {
  console.log(`-> mapping: event ${event.id}`)
  return {
    ...event,
    payload: { ...event.payload, mapped: true },
    error: index % 2 === 0 ? 'flip flop error' : null
  } as OutgoingEvent
}
```

When you build and bundle the handler file, your handler code will include an inline source map. When your handler runs, entries will appear in the CloudWatch logs.
