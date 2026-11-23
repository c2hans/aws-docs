---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/supported-platforms.html
---

# Supported platforms

 AWS CDK Blocks supports web, desktop, and mobile platforms. Your backend API is defined once in TypeScript, and type-safe clients are available for every supported platform.

## Web frameworks
<a name="platforms-web"></a>

CDK Blocks auto-detects your web framework and configures the development server and deployment pipeline accordingly. The following frameworks are supported:

| Framework | Minimum version | Notes |
| --- | --- | --- |
| Next.js | 15.x | Full SSR support with automatic route detection and middleware handling. If your project does not install a Next.js build adapter package itself (the `nextjs` template does), Hosting uses a pinned one. The pinned adapter supports Next.js 15.5.18 or a later 15.x release, and Next.js 16.2.6 or later. |
| Nuxt | 4.x | SSR via Nitro adapter with automatic server routes |
| Astro | 4.x | Static and SSR modes supported. Supported range: Astro 4 through 7. |
| SolidStart | 1.x | Via Nitro adapter |
| TanStack Start | 1.x | Via Nitro adapter |
| SvelteKit | 2.x | SSR via `@sveltejs/adapter-node`. If your `svelte.config.js` sets no adapter, Hosting adds `adapter-node` for the build. Any other adapter fails synthesis. |
| React (SPA) | 18.x | Static single-page application, any build tool (Vite, Create React App) |
| Vue (SPA) | 3.x | Static single-page application via Vite |
| Svelte (SPA) | 4.x | Static single-page application via Vite |
| Angular (SPA) | 17.x | Static single-page application. Angular 17 and later write the build to a nested folder, so set `buildOutputDir` (for example, `dist/my-app/browser`). |

For SPA frameworks, CDK Blocks serves static assets from CloudFront with S3 origin. For SSR frameworks (Next.js, Nuxt, Astro SSR, SvelteKit, SolidStart, TanStack Start), CDK Blocks deploys server-side rendering via Lambda compute.

Framework detection is automatic based on the dependencies, dev dependencies, and peer dependencies in your `package.json`. You can override it explicitly in your Hosting configuration.

## Native and mobile platforms
<a name="platforms-native"></a>

CDK Blocks generates typed native clients from your backend API via OpenRPC codegen. You define your API once in TypeScript, and codegen produces a typed client for each native platform on top of that platform’s SDK.

| SDK | Platforms | Distribution |
| --- | --- | --- |
| Swift | iOS 16 or later, macOS 13 or later | Swift Package Manager |
| Kotlin (Kotlin Multiplatform) | Android (API level 23 or later), iOS, and the JVM (for example, desktop apps) | Maven/Gradle |
| Dart (Flutter) | iOS, Android, web, and desktop. Dart 3.11 or later, and Flutter 3.41 or later for `blocks_runtime_flutter`  | Dart packages `blocks_runtime`, `blocks_codegen`, and `blocks_runtime_flutter`  |

### How native codegen works
<a name="how-native-codegen-works"></a>

The build pipeline generates an OpenRPC specification (`cdk-blocks/blocks.spec.json`) from your `ApiNamespace` methods. Native codegen tools read this specification to produce typed SDKs for each platform.

The codegen pipeline has two layers:

 **Platform SDK** (hand-written, built once per platform)
Handles transport (HTTP JSON-RPC), authentication (cookie management, token injection), Realtime hydration (WebSocket connections), and FileBucket hydration (presigned URL operations).

 **Generated typed facade** (app-specific, produced by codegen)
One typed method per `ApiNamespace` method. Calls into the platform SDK’s transport layer. Contains no transport logic.

To generate the specification:

```bash
npx blocks-generate-spec
```

This reads `cdk-blocks/index.ts` and writes `cdk-blocks/blocks.spec.json`. Scaffolded apps run it with `npm run spec`. To regenerate it on every build, add it to your build script:

```json
{
  "scripts": {
    "build:spec": "blocks-generate-spec",
    "build": "npm run build:spec && tsc && vite build"
  }
}
```

### Writing APIs for native compatibility
<a name="writing-apis-for-native-compatibility"></a>

TypeScript method signatures produce correct native types automatically. For richer types (format constraints, enums), use Zod schemas:
+ Plain TypeScript types (tier 2): correct base types inferred from method signatures
+ Zod schemas (tier 1): full JSON Schema with constraints (`format: uuid`, `maxLength`, `minLength`). Schema detection requires Zod 4.
+ If neither is detected, parameters emit as `unknown` (generates `Any` in native clients)

For best results, use explicit return types and Zod validation on complex inputs.

## Hosting and deployment
<a name="platforms-hosting"></a>

CDK Blocks provides `Hosting` (import from `aws-cdk-blocks/cdk`) for deploying your frontend alongside your backend. Hosting provisions:
+  **Amazon CloudFront** distribution with global edge caching (the default front door; you can choose another)
+  **Amazon S3** origin for static assets
+  **Lambda compute** for server-side rendering (SSR frameworks only)
+  **Optional WAF** integration for security rules
+  **Custom domains** with automatic DNS and TLS
+  **Skew protection** during rolling deployments

Hosting deploys your frontend when you run `npm run deploy`. A plain sandbox deploys only your backend, and `npm run sandbox:preview` adds Hosting in a fast preview shape. For more information, see [Basic usage](bb-hosting.md#bb-hosting-usage) in the Hosting chapter.

### Framework auto-detection
<a name="framework-auto-detection"></a>

Hosting detects your framework from the `dependencies`, `devDependencies`, and `peerDependencies` in `package.json`. It checks in this order and uses the first match:
+  `next` → Next.js adapter
+  `nuxt`, `nitropack`, `@solidjs/start`, `@tanstack/start`, or one other package on Hosting’s fixed Nitro list → Nitro adapter. For any other Nitro-based framework, set `framework: 'nitro'`
+  `astro` → Astro adapter
+  `@sveltejs/kit` → SvelteKit adapter
+ None of the above → SPA/static adapter

Override detection by setting `framework` explicitly in your Hosting configuration.
