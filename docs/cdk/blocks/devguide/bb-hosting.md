---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/bb-hosting.html
---

# Hosting

The Hosting construct provides frontend deployment with server-side rendering (SSR) support. Hosting auto-detects your frontend framework (Next.js, Nuxt and other Nitro-based frameworks, Astro, SvelteKit, or SPA) and provisions the required AWS resources. Import from `aws-cdk-blocks/cdk` and use in your CDK layer file (`cdk-blocks/index.cdk.ts`).

Locally, the development server serves your frontend at `http://localhost:3000` with hot reload. On AWS, Hosting provisions an Amazon CloudFront distribution with an Amazon S3 origin, AWS Lambda compute for SSR, an optional AWS WAF, Amazon CloudWatch alarms, and DNS records. Hosting also supports custom domains and skew protection during rolling deployments. CloudFront is the default front door. You can choose a different one with the `frontDoor` prop. For more information, see [Front door](#bb-hosting-front-door).

Use Hosting in the CDK layer, not in the app definition. The `npm run deploy` command deploys Hosting. A plain sandbox (`npm run sandbox`) deploys only your backend, and `npm run sandbox:preview` deploys a sandbox that includes Hosting in a fast preview shape. Hosting itself does not check for a sandbox. The project template’s CDK layer file decides when to add Hosting. For more information, see [Basic usage](#bb-hosting-usage).

## What Hosting provisions
<a name="bb-hosting-provisions"></a>

On AWS, a single `Hosting` construct with the default front door provisions these frontend resources:
+  **Amazon CloudFront** – a global content delivery network (CDN) distribution that serves your site from edge locations close to your users
+  **Amazon S3** – an origin bucket that stores your static assets (HTML, CSS, JavaScript, images)
+  ** AWS Lambda** – server-side rendering (SSR) compute for framework routes that render on the server. Applies to SSR frameworks only. Hosting skips this resource for single-page applications (SPAs) and static sites.
+  **Custom domains with TLS** – optional Amazon Route 53 records and an AWS Certificate Manager (ACM) certificate for your own domain over HTTPS
+  ** AWS WAF** – optional web application firewall rules, including rate limiting
+  **Amazon CloudWatch monitoring** – alarms for the Amazon CloudFront 5xx error rate, SSR AWS Lambda errors and throttles, image optimization AWS Lambda errors, and the revalidation dead-letter queue depth (enabled by default)
+  **Skew protection** – cookie-based pinning that keeps a user’s session on a single build during rolling deployments (enabled by default)

When you provide the `api` prop, the front door also proxies backend API requests through the same domain as your frontend. With the default front door, Hosting adds Amazon CloudFront behaviors for this. Your frontend calls the API with relative URLs (for example, `/aws-blocks/…​`). Because the frontend and API share a single origin, you avoid cross-origin resource sharing (CORS) concerns.

## Supported frameworks
<a name="bb-hosting-frameworks"></a>

Hosting detects your framework from the `dependencies`, `devDependencies`, and `peerDependencies` in your `package.json` and selects the matching adapter. SSR frameworks deploy with AWS Lambda compute. SPA frameworks deploy as static assets that Amazon CloudFront serves from an Amazon S3 origin.

| Framework | Rendering | Detected from |
| --- | --- | --- |
| Next.js | SSR |  `next` in dependencies |
| Nuxt | SSR |  `nuxt` or `nitropack` in dependencies |
| Astro | Static or SSR |  `astro` in dependencies |
| Nitro-based (SolidStart, TanStack Start, and others) | SSR |  `@solidjs/start`, `@tanstack/start`, `nitropack`, or one of the other packages on Hosting’s fixed Nitro list, in dependencies. For a Nitro-based framework that is not detected, set `framework: 'nitro'`  |
| SvelteKit 2 | SSR |  `@sveltejs/kit` in dependencies |
| React, Vue, Svelte, Angular (SPA) | Static single-page application | None of the above (falls back to the SPA/static adapter) |

If more than one package matches, the first match in this order wins: Next.js, Nitro-based, Astro, SvelteKit. For SvelteKit, Hosting builds your app with `@sveltejs/adapter-node` and runs the resulting server on AWS Lambda. If your `svelte.config.js` sets no adapter, Hosting replaces the file with one that uses `adapter-node` for the duration of the build, then restores your original. If it sets any other adapter, including `adapter-auto`, synthesis fails with `SvelteKitIncompatibleAdapterError`. Switch to `adapter-node` or remove the adapter.

Framework detection is automatic. To override it, set the `framework` prop explicitly. It accepts `nextjs`, `nuxt`, `nitro`, `astro`, `sveltekit`, `spa`, and `static`. Use `spa` for a single-page app that routes on the client, and `static` for a multi-page static site.

```typescript
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));

new Hosting(stack, 'Web', {
  root: join(__dirname, '..'),
  framework: 'nextjs',
});
```

For a framework that Hosting does not support, pass your own adapter function with the `customAdapter` prop.

For the full list of supported framework versions and native platform clients, see [Supported platforms](supported-platforms.md).

## Basic usage
<a name="bb-hosting-usage"></a>

Before you begin, make sure you have a CDK layer file (`cdk-blocks/index.cdk.ts`) and a frontend app with a `package.json` in your project.

Add Hosting to your CDK layer file. At minimum, provide the `root` path to your frontend app and a `buildCommand`. Pass your backend stack as `api` to serve the frontend and API from the same domain.

The following example has the same shape as the CDK layer file that `npm create @aws-cdk-blocks/blocks-app` generates:

```typescript
// cdk-blocks/index.cdk.ts
import * as cdk from 'aws-cdk-lib';
import { BlocksPresets, BlocksStack, Hosting, HostingPresets } from 'aws-cdk-blocks/cdk';
import { getStackName } from 'aws-cdk-blocks/scripts';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));

const app = new cdk.App();
const sandboxMode = app.node.tryGetContext('sandboxMode') === 'true';
const previewMode = app.node.tryGetContext('previewMode') === 'true';
const projectRoot = app.node.tryGetContext('projectRoot') || process.cwd();

const stackName = getStackName({ sandbox: sandboxMode, projectRoot });
export const blocksStack = await BlocksStack.create(app, stackName, {
  backendHandlerPath: join(__dirname, 'index.handler.ts'),
  backendCDKPath: join(__dirname, 'index.ts'),
  defaults: sandboxMode ? BlocksPresets.sandbox : BlocksPresets.production,
});

// Hosting for `npm run deploy` and `npm run sandbox:preview`.
// A plain `npm run sandbox` deploys the backend only.
if (!sandboxMode || previewMode) {
  new Hosting(blocksStack, 'Hosting', {
    ...(previewMode ? HostingPresets.preview : HostingPresets.production),
    root: join(__dirname, '..'),
    buildCommand: 'npm run build',
    api: blocksStack,
  });
}
```

The example does the following:
+ It defines ` dirnamedirname` is not defined by default.
+ It names the stack with `getStackName()`, which ends the name in `-prod` for a deploy and in your sandbox ID for a sandbox, so a sandbox never overwrites your production stack.
+ It adds Hosting only for `npm run deploy` (`sandboxMode` is not set) and for `npm run sandbox:preview` (`previewMode` is set). Without this check, every sandbox would deploy Hosting too.
+ It spreads `HostingPresets.preview` for a preview sandbox and `HostingPresets.production` otherwise. For more information, see [Preview deployments](#bb-hosting-preview).

Omit the `api` prop to deploy a static-only site with no backend. If you already built your app, omit `buildCommand` and Hosting deploys the existing output.

The `Hosting` construct exposes the resources it creates as public readonly members, so you can reference them elsewhere in your CDK layer:

| Member | Description |
| --- | --- |
|  `bucket`  | The Amazon S3 bucket storing static assets. |
|  `distribution`  | The Amazon CloudFront distribution serving the site. Available only with the default CloudFront front door or the stacked door. With any other front door, reading it throws `FrontDoorNotCloudFrontError`; use `url` instead. |
|  `url`  | The public URL of the deployed site. |
|  `ssrFunction`  | The primary SSR AWS Lambda function, when the framework uses SSR. |
|  `ssrWebFunction`  | The SSR server, when `compute.type` is `'web-function'`. Set instead of `ssrFunction`. |
|  `buildCacheBucket`  | The build-cache Amazon S3 bucket, when `buildCache.enabled` is `true`. |
|  `monitoring`  | With the CloudFront front door, when monitoring is enabled, an object with `alarms` (every Amazon CloudWatch alarm Hosting created) and `alarmTopics` (the Amazon Simple Notification Service topics the alarms notify). |

## Front door
<a name="bb-hosting-front-door"></a>

The front door is the service that receives your users' requests and routes them to your static assets, SSR compute, and API. By default, Hosting uses an Amazon CloudFront distribution. To use a different front door, set the `frontDoor` prop:

|  `frontDoor` value | Serves your app through | Use it when | Settings it accepts in `features`  |
| --- | --- | --- | --- |
| Omitted, `'cloudfront'`, or `{ features }`  | Amazon CloudFront, a global CDN with an edge cache (the default) | Your app is public, has users in many places, and needs the edge cache, skew protection, or geo restriction |  `domain`, `waf`, `logging`, `monitoring`, `skewProtection`, `priceClass`, `contentSecurityPolicy`, `geoRestriction`, `ssrDefaultTtl`, `cacheKeyCookies`, `cacheKeyHeaders`, `responseHeadersPolicy`, `quotas`  |
|  `{ kind: 'alb' }`  | A regional Application Load Balancer in a VPC (Hosting creates a VPC unless you pass `vpc`). No edge cache. Set `internal: true` for a private load balancer in private subnets. A VPC that you pass must have private subnets for this. With `features.domain`, the load balancer serves HTTPS at your domain, using `certificate` if you pass one. Without a domain, it serves plain HTTP. | Your load balancer must be in a VPC, or your app must be private |  `domain`, `waf`, `logging`, `monitoring`  |
|  `{ kind: 'apiGateway' }`  | Amazon API Gateway, with no VPC and no edge cache. Set `api: 'http'` (the default) for an HTTP API or `api: 'rest'` for a REST API. A REST API needs `domain`. Pass `certificate` to use your own regional certificate for the domain. | You want inexpensive serverless hosting with no VPC or CDN, such as previews and small apps |  `domain`  |
|  `{ kind: 'stacked', edge: 'cloudfront', router: 'alb' }`  | An Amazon CloudFront edge in front of an Application Load Balancer. The edge serves static files from Amazon S3 and sends dynamic requests through the load balancer, which accepts traffic only from the edge. Takes `vpc`, `internal`, and `certificate`, as the `alb` door does. Without `features.router.domain`, the hop from the edge to the load balancer is plain HTTP, and synthesis warns about it for an internet-facing load balancer. | You want the CloudFront edge, with dynamic traffic through a load balancer that only the edge can reach |  `edge: { waf, contentSecurityPolicy }` and `router: { domain, waf, logging, monitoring }`  |
|  `{ kind: 'custom', door }`  | A front door you write with `defineFrontDoor()` from `@aws-cdk-blocks/hosting/constructs`. Hosting passes the settings to your door as `input.features` and does not apply them itself, except that `logging` also controls the access logs of the asset bucket. | A platform team shares one front door across many apps |  `domain`, `waf`, `logging`, `monitoring`, `geoRestriction`, `skewProtection`  |
|  `'none'`  | An Amazon S3 static website over HTTP. Static sites and SPAs only. Your frontend calls the API from a different origin. | You serve a static demo over plain HTTP | None |

The following behavior differs from the default CloudFront front door:
+  **Edge features** – the `alb` and `apiGateway` front doors have no edge cache, skew protection, or geo restriction. The stacked front door has the edge cache, but no skew protection or geo restriction.
+  **File size limit** – the `alb` and `apiGateway` front doors serve static files through an AWS Lambda proxy that returns the whole file, base64 encoded, in its response. The response limit is 1 MB behind an Application Load Balancer and 6 MB behind API Gateway, and base64 encoding makes each file about a third larger. The proxy measures a compressible file after gzip compression. Synthesis lists the files over the limit in an `AssetExceedsProxyLimit` warning.
+  **Buffered server responses** – the HTTP API buffers SSR responses, with a limit of about 6 MB each. The Application Load Balancer, including the one behind the stacked front door, also buffers them, with a limit of 1 MB. A REST API streams them.
+  **Next.js middleware and edge routes** – middleware runs only behind the CloudFront front door. Edge routes (`runtime: 'edge'`) need the CloudFront front door, or `edgeRoutes: 'regional'` behind the HTTP API, which is the default there. Otherwise, synthesis fails. The Next.js server streams its responses, so synthesis also fails behind the `alb` and stacked front doors, with `StreamingServerNeedsStreamingDoorError`.

Every built-in front door answers 404 for a missing static file. Behind every built-in front door except `'none'`, a multi-page static site with no 404 page of its own gets a default 404 page.

Pass the settings for the chosen front door in `features`. A setting the front door does not implement is a type error. The following example keeps the default CloudFront front door and turns on AWS WAF:

```typescript
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));

new Hosting(blocksStack, 'Web', {
  root: join(__dirname, '..'),
  buildCommand: 'npm run build',
  api: blocksStack,
  frontDoor: {
    features: {
      waf: { enabled: true },
    },
  },
});
```

The following example serves the same app behind an API Gateway HTTP API instead:

```typescript
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));

new Hosting(blocksStack, 'Web', {
  root: join(__dirname, '..'),
  buildCommand: 'npm run build',
  api: blocksStack,
  frontDoor: { kind: 'apiGateway' },
});
```

A custom front door is an object with a `service` ID and a `build` function. Hosting calls `build` once at synthesis, after it creates the bucket, compute, and API. The `url` that `build` returns becomes your app’s address. Hosting does not check that your door applies `features`. It checks only that the door’s routing reaches the static assets and the API (`wiringCheck`, on by default). The check sees routing wired with the `cf` helpers from `@aws-cdk-blocks/hosting/constructs`. If you wire routing another way, declare it with `cf.recordWired()` or set `wiringCheck: false`. The same module also exports the asset proxy and API proxy helpers that the built-in doors use.

```typescript
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { defineFrontDoor } from '@aws-cdk-blocks/hosting/constructs';

const __dirname = dirname(fileURLToPath(import.meta.url));

const myDoor = defineFrontDoor({
  service: 'my-door',
  build(scope, { app, origins, features }) {
    // app: routes, SPA fallback, redirects, header rules, error pages
    // origins: assets (bucket and build prefix), server, image, api
    // features: the settings from frontDoor.features
    // ...create the door...
    return { url: 'https://app.example.com' };
  },
});

new Hosting(blocksStack, 'Web', {
  root: join(__dirname, '..'),
  buildCommand: 'npm run build',
  api: blocksStack,
  frontDoor: { kind: 'custom', door: myDoor },
});
```

## Preview deployments
<a name="bb-hosting-preview"></a>

 `HostingPresets` holds two preset groups of Hosting props. Spread one into the props first, then add or override props after it:
+  `HostingPresets.production` sets nothing, so you get the defaults: the CloudFront front door, image optimization, incremental regeneration, Lambda@Edge for Next.js edge routes, and a new build ID for every deploy.
+  `HostingPresets.preview` is a fast, inexpensive shape for temporary environments such as previews of pull requests. It sets `frontDoor: { kind: 'apiGateway' }` (an API Gateway HTTP API, with no CloudFront), `imageOptimization: false`, `incrementalRegeneration: false`, `edgeRoutes: 'regional'`, and `buildId: 'fixed'`. Routing, server rendering, prerendered pages, cookie sign-in, and the API keep working. Server responses are buffered, with a limit of about 6 MB each. A preview has no CDN, AWS WAF, or skew protection, serves images unoptimized, and has the file size limit of the `apiGateway` front door. Its URL is public, and Hosting adds no authentication to it.

To keep one preview setting at its default, override it after the spread:

```typescript
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));

new Hosting(blocksStack, 'Hosting', {
  ...HostingPresets.preview,
  imageOptimization: true,
  root: join(__dirname, '..'),
  api: blocksStack,
});
```

 `imageOptimization: false` and `edgeRoutes: 'regional'` need the API Gateway HTTP API front door. `buildId: 'fixed'` is not available behind the CloudFront front door or the stacked front door. This is because the edge cache would keep serving files that each deploy overwrites. When a setting does not fit the front door, synthesis fails with `UnsupportedHostingSettingError`.

 `npm run sandbox:preview` deploys a sandbox with Hosting in the preview shape, when your CDK layer file is set up as in [Basic usage](#bb-hosting-usage). It deploys once, prints the site URL, and exits. It does not watch for changes or start a local server. Run it again to redeploy. A change that touches only backend code is hotswapped. The plain sandbox commands deploy the same stack without Hosting, so running `npm run sandbox` after a preview removes the preview site. Remove a preview sandbox with `npm run sandbox:destroy`. For a pull request preview, run `npm run sandbox:preview` from CI, and run `npm run sandbox:destroy` when the pull request closes. Keep `.cdk-blocks-sandbox/sandbox-id.txt` between the two runs, such as in a CI cache, because it names the sandbox stack.

## Custom domains
<a name="bb-hosting-domains"></a>

Configure a custom domain with `frontDoor.features.domain`. With the default CloudFront front door, the ACM certificate must be in the `us-east-1` AWS Region. This requirement applies regardless of where you deploy the rest of your stack.

You can set up a domain in two ways.

 **Amazon Route 53 (automatic)** – provide a `hostedZone` you control. Hosting looks the zone up, so the stack needs `env: { account, region }`, or you also pass the zone’s `hostedZoneId`. Hosting requests a DNS-validated ACM certificate and creates the A and AAAA alias records automatically:

```typescript
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));

new Hosting(blocksStack, 'Web', {
  root: join(__dirname, '..'),
  buildCommand: 'npm run build',
  api: blocksStack,
  frontDoor: {
    features: {
      domain: {
        domainName: 'app.example.com',
        hostedZone: 'example.com',
      },
    },
  },
});
```

The following fragments go inside `frontDoor.features`. To serve both an apex domain and its `www` subdomain, pass an array of domain names and set `wwwRedirect`:

```typescript
domain: {
  domainName: ['example.com', 'www.example.com'],
  hostedZone: 'example.com',
  wwwRedirect: 'toApex',
}
```

 **Bring your own DNS (manual)** – if you manage DNS outside Amazon Route 53, omit `hostedZone` and supply a pre-validated `certificate` in `us-east-1`. Hosting does not create DNS records. Instead, it outputs the Amazon CloudFront distribution domain name. Point a CNAME (or an ALIAS/ANAME record for an apex domain) at that domain name:

```typescript
domain: {
  domainName: ['app.example.com'],
  certificate: myPreValidatedCert, // ACM certificate in us-east-1
}
```

**Note**
If you provide neither a hosted zone nor a certificate, synthesis fails fast with a `MissingCertificateError` rather than waiting on an unvalidated certificate at deploy time. A certificate outside `us-east-1` fails with an `InvalidCertificateRegionError`.

## SSR compute
<a name="bb-hosting-compute"></a>

For SSR frameworks, tune the AWS Lambda function that renders your server-side routes with the `compute` prop. Hosting ignores this prop for SPA and static deployments.

```typescript
import * as cdk from 'aws-cdk-lib';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));

new Hosting(blocksStack, 'Web', {
  root: join(__dirname, '..'),
  buildCommand: 'npm run build',
  framework: 'nextjs',
  api: blocksStack,
  compute: {
    memorySize: 2048,
    timeout: cdk.Duration.seconds(30),
  },
});
```

| Option | Default | Description |
| --- | --- | --- |
|  `type`  |  `'lambda'`  | Where the SSR server runs: `'lambda'` or `'web-function'`. See **Lambda Web Functions** after this table. |
|  `webFunction`  | None | Tuning for Lambda Web Functions, such as `maxEnvironments`. Used only when `type` is `'web-function'`. |
|  `memorySize`  | 1024 |  AWS Lambda memory size, in MB. |
|  `timeout`  | 30 seconds |  AWS Lambda timeout. Accepts a `cdk.Duration` or a plain number of seconds. |
|  `reservedConcurrency`  | None | Reserved concurrent executions for the SSR AWS Lambda function. |
|  `imageOptimization.reservedConcurrency`  | None | Reserved concurrency for the image-optimization AWS Lambda function. Left unreserved by default so deployments succeed on fresh AWS accounts. |
|  `logRetention`  | One month | Amazon CloudWatch log retention for the SSR AWS Lambda function. |

 **Lambda Web Functions** – set `compute.type` to `'web-function'` to run your framework’s own Node.js server directly on AWS Lambda Web Functions. One execution environment serves many concurrent requests, which means fewer cold starts and lower cost for SSR that mostly waits on I/O. Web Functions work with Next.js, Nuxt and other Nitro-based frameworks, Astro, and SvelteKit. They need the default CloudFront front door and one of these Regions: `us-east-1`, `us-east-2`, `us-west-2`, `ap-northeast-1`, `eu-west-1`. With another front door, synthesis fails with `UnsupportedComputeFrontDoorError`. `memorySize` and `reservedConcurrency` do not apply; tune the server with `webFunction` instead:

```typescript
compute: {
  type: 'web-function',
  webFunction: { maxEnvironments: 20 },
},
```

## Security
<a name="bb-hosting-security"></a>

Hosting provides several controls for protecting your distribution. Set the WAF, Content Security Policy, and geo-restriction settings inside `frontDoor.features`.

 **WAF** – enable AWS WAF with the `waf` setting to add managed protections and rate limiting. You can also associate an existing WebACL by ARN (the WebACL must be in `us-east-1`):

```typescript
waf: {
  enabled: true,
  rateLimit: 1000, // requests per 5-minute window per IP
}
```

 **Content Security Policy** – set `contentSecurityPolicy` to override the restrictive default `Content-Security-Policy` header. Hosting applies its security headers, including this one, to the API and auth paths it proxies as well as to your site:

```typescript
contentSecurityPolicy: "default-src 'self'; img-src 'self' data:;",
```

 **Geo-restriction** – use `geoRestriction` to restrict access by country. Set `countries` to an array of ISO country codes and `type` to `'allowlist'` (allow only those countries) or `'denylist'` (block them):

```typescript
geoRestriction: { type: 'allowlist', countries: ['US', 'CA', 'GB'] },
```

**Warning**
Hosting writes values from `backendConfig` to `/.cdk-blocks-sandbox/config.json` and injects them into the `BLOCKS_CONFIG` AWS Lambda environment variable. Both locations are publicly accessible. Do not include secrets, API keys, or other sensitive configuration. For sensitive values, use the `environment` prop with `secret()`, as described next.

 **Secrets and configuration for SSR code** – the `environment` prop sets environment variables on every regional compute function, including image optimization. Lambda@Edge functions do not get them. A plain string is stored as is, in the CloudFormation template and the function configuration. A `secret('KEY')` value is stored in AWS Secrets Manager, and a `config('KEY')` value in AWS Systems Manager Parameter Store. For those, Hosting injects only the location of the value, never the value, and grants the function read access to it. The variable name must match the key:

```typescript
import { config, secret } from 'aws-cdk-blocks/cdk';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));

new Hosting(blocksStack, 'Web', {
  root: join(__dirname, '..'),
  buildCommand: 'npm run build',
  api: blocksStack,
  environment: {
    FEATURE_FLAG: 'on',
    PAYMENTS_API_KEY: secret('PAYMENTS_API_KEY'),
    SUPPORT_EMAIL: config('SUPPORT_EMAIL'),
  },
});
```

In your SSR code, read the values with `await getSecret('PAYMENTS_API_KEY')` and `await getConfig('SUPPORT_EMAIL')` from `@aws-cdk-blocks/hosting`. Locally, each getter reads `process.env` first, so you can put the value in a `.env` file.

## Operations
<a name="bb-hosting-operations"></a>

Hosting includes operational features to keep deployments observable and reliable.

 **Monitoring** – Amazon CloudWatch alarms are enabled by default. They cover the Amazon CloudFront 5xx error rate, SSR AWS Lambda errors and throttles, image optimization AWS Lambda errors, and the revalidation dead-letter queue depth. Hosting creates the Amazon SNS topics the alarms notify. If your stack sets `env: { account, region }` and is not in `us-east-1`, the CloudFront alarm and its topic are created in `us-east-1`. Without `env`, they are created in your stack, and synth prints a warning. With the CloudFront front door, the construct’s `monitoring` member exposes the alarms as `monitoring.alarms` and the topics as `monitoring.alarmTopics`. To get notified, add email or URL subscriptions in `frontDoor.features`:

```typescript
import { EmailSubscription } from 'aws-cdk-lib/aws-sns-subscriptions';
```

```typescript
monitoring: { subscriptions: [new EmailSubscription('ops@example.com')] },
```

Set `monitoring: { enabled: false }` to opt out.

 **Skew protection** – enabled by default. During a rolling deployment, viewers who started a session continue to receive assets from the same build. This prevents asset mismatches. Set `skewProtection: { enabled: false }` in `frontDoor.features` to disable it. Hosting keeps superseded builds in Amazon S3 for 30 days. Change this with the `buildRetentionDays` prop.

 **Access logging** – enabled by default. Amazon CloudFront access logs go to a dedicated Amazon S3 bucket. Use the `logging` setting in `frontDoor.features` to change how long logs are kept, or set `logging: { enabled: false }` to turn them off:

```typescript
logging: { enabled: true, retentionDays: 90 },
```

 **Build cache** – enable `buildCache` to preserve framework build caches (such as `.next/cache`) between deployments in an Amazon S3 bucket, reducing cold-build times in CI:

```typescript
buildCache: { enabled: true },
```

## Configuration reference
<a name="bb-hosting-reference"></a>

The following table summarizes the top-level `Hosting` properties. All properties except `root` are optional. Deprecated properties still work and are merged into `frontDoor.features`. For more information, see [Front door](#bb-hosting-front-door).

**Note**
The top-level props `domain`, `waf`, `logging`, `monitoring`, `skewProtection`, `priceClass`, `contentSecurityPolicy`, `geoRestriction`, `ssrDefaultTtl`, `cacheKeyCookies`, `cacheKeyHeaders`, and `quotas` are deprecated aliases for the `frontDoor.features` settings of the same name. Setting the same setting both ways fails synthesis with `FrontDoorSettingConflictError`. A top-level prop that the chosen front door does not implement fails synthesis with `UnsupportedFrontDoorSettingError`.

| Property | Default | Description |
| --- | --- | --- |
|  `root`  | None (required) | Path to the frontend app root directory. Required. |
|  `buildCommand`  | None | Shell command to build the frontend during CDK synthesis. Omit if you pre-built the app. |
|  `framework`  | Auto-detected | Framework type. Overrides detection from `package.json`. |
|  `buildOutputDir`  | Auto-detected | Path to the build output directory. |
|  `customAdapter`  | None | Your own adapter function, for a framework Hosting does not support. |
|  `basePath`  | None | URL prefix for the entire site (for example, `/app`). |
|  `api`  | None | Backend stack to proxy through the same domain (single-origin, no CORS). |
|  `backendConfig`  | None | Extra config merged into `config.json`. Publicly accessible, so do not include secrets. |
|  `compute`  | See [SSR compute](#bb-hosting-compute)  |  AWS Lambda compute configuration for SSR frameworks. |
|  `environment`  | None | Environment variables for SSR compute. Values are plain strings, `secret()`, or `config()`. See [Security](#bb-hosting-security). |
|  `frontDoor`  | Amazon CloudFront | The front door and its `features` settings. See [Front door](#bb-hosting-front-door). |
|  `imageOptimization`  |  `true`  | Set `false` to build no image optimization function. Setting it to `false` needs the API Gateway HTTP API front door. |
|  `incrementalRegeneration`  |  `true`  | Set `false` to skip the Next.js incremental regeneration resources. Prerendered pages are still served but never regenerate. |
|  `edgeRoutes`  |  `'edge'` (`'regional'` behind the API Gateway HTTP API front door) | Where Next.js edge routes run: Lambda@Edge (`'edge'`) or regional AWS Lambda functions (`'regional'`). |
|  `buildId`  |  `'per-deploy'`  |  `'fixed'` keeps the build ID while the build output is unchanged, so a redeploy can skip uploads. Not available behind CloudFront. |
|  `domain`  | None | Deprecated. Use `frontDoor.features.domain`. Custom domain configuration. |
|  `waf`  | Disabled | Deprecated. Use `frontDoor.features.waf`. AWS WAF configuration. |
|  `priceClass`  |  `PRICE_CLASS_100`  | Deprecated. Use `frontDoor.features.priceClass`. Amazon CloudFront price class. |
|  `geoRestriction`  | None | Deprecated. Use `frontDoor.features.geoRestriction`. Country allow or deny list for the distribution. |
|  `buildCache`  | Disabled | Amazon S3-backed framework build cache. |
|  `errorPages`  | None | Custom 404/500 HTML pages. Incompatible with SPA client-side routing. |
|  `logging`  | Enabled for CloudFront and asset bucket logs. With the ALB front door, ALB access logs are off unless you set it | Deprecated. Use `frontDoor.features.logging`. Amazon CloudFront access logging. |
|  `monitoring`  | Enabled | Deprecated. Use `frontDoor.features.monitoring`. Amazon CloudWatch alarms wired to Amazon SNS topics. |
|  `skewProtection`  | Enabled | Deprecated. Use `frontDoor.features.skewProtection`. Cookie-based build pinning during rolling deployments. |
|  `buildRetentionDays`  | 30 | Days to keep superseded builds in Amazon S3. The current build is never removed. |
|  `retainOnDelete`  |  `false`  | Retain the Amazon S3 bucket when you delete the stack. |

For the full construct API, adapter internals, and advanced configuration, see the [Hosting package source code on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/hosting).
