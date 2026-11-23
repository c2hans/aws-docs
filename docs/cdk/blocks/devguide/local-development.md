---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/local-development.html
---

# Local development

Your whole app runs on your machine. When you run `npm run dev`, your entire application runs on your local machine: backend, frontend, database, authentication, and background jobs. You don’t need an AWS account, AWS credentials, an internet connection, or a running container daemon. The only prerequisite is Node.js version 22 or later.

Every CDK Block ships with a local implementation that exposes the same typed API as its AWS counterpart. At GA, each CDK Block runs locally on its own built-in implementation, so your app works without an AWS account. [AWS Emulator](https://docs.aws.amazon.com/emulator/latest/userguide/what-is-service.html) support for AWS CDK Blocks is planned.

A few things need a network connection, because they call the real service:
+ An `Auth` provider that signs in with a real identity provider.
+ A `Database` on an existing PostgreSQL database (`DatabaseCluster.fromExisting()`).
+ An `Agent` whose `model.local` names a hosted model. An Amazon Bedrock model in `model.local` also needs AWS credentials.

This page explains how local development works, what each CDK Block maps to locally, and how to use local implementations to test your application.

## How local development works
<a name="local-development-how-it-works"></a>

### Conditional exports
<a name="local-development-conditional-exports"></a>

Every CDK Block is an npm package with several implementations behind a single import. CDK Blocks uses [Node.js conditional exports](https://nodejs.org/api/packages.html#conditional-exports) to route the same `import` statement to the right implementation for the execution context. For example, the `KVStore` package declares:

```json
{
  "exports": {
    ".": {
      "browser": "./dist/index.browser.js",
      "cdk": {
        "types": "./dist/index.cdk.d.ts",
        "default": "./dist/index.cdk.js"
      },
      "aws-runtime": "./dist/index.aws.js",
      "types": "./dist/index.mock.d.ts",
      "default": "./dist/index.mock.js"
    }
  }
}
```

| Context | Export condition | What resolves |
| --- | --- | --- |
| Local development |  `default`  | The local implementation. Your code runs in-process on your machine, backed by the filesystem, in-memory state, or an embedded engine. |
| Deployment (CDK synthesis) |  `cdk`  | CDK Constructs that define the CDK Block’s AWS infrastructure. |
| Production runtime (Lambda) |  `aws-runtime`  | The AWS SDK implementation that calls real AWS services. |
| Browser |  `browser`  | The client-side code bundled into your frontend. |

The local implementation is the default resolution, so any Node.js process that imports your backend gets the local implementations automatically. This includes the dev server, your test runner, and any script you run. You don’t turn on a local mode. The local implementation is used whenever no deployment context applies. CDK Blocks applies the `aws-runtime` condition only when it bundles your backend for Lambda, so the AWS SDK is never loaded during local development.

You never configure this yourself. CDK Blocks sets up the build system to select the correct implementation for each context automatically.

Local implementations are for local development only. If a backend is bundled without the `aws-runtime` condition, it loads the local implementations instead of the AWS ones. To catch this, a CDK Block’s local implementation checks where it runs when it loads, and throws an error on compute that CDK Blocks deployed. The error starts with `A Building Block mock entry (first detected: <package>) was loaded in a deployed environment`. It explains how to set the `aws-runtime` condition. The package it names is the first CDK Block whose check ran, which can be a CDK Block that another CDK Block uses. CDK Blocks detects a deployed environment from the `BLOCKS_CONFIG_BUCKET` and `BLOCKS_CONFIG_KEY` environment variables, which it sets on every compute it provisions. On compute that CDK Blocks does not provision, the check does nothing, so the `aws-runtime` condition is your only protection there.

### The dev server
<a name="local-development-dev-server"></a>

 `npm run dev` starts a local dev server in watch mode:
+ Your backend runs in-process. There is no separate compute to provision, and code changes reload automatically.
+ In templates with a frontend, open `http://localhost:3000`. The dev server listens on that port and forwards page requests to your frontend dev server (Vite or Next.js), which runs on port 3100.
+ The templates without a frontend (`backend`, `api-only`, `sql`, `cron`, and `observability`) serve only the API, on port 3001. In an Amplify project, CDK Blocks adds `npm run blocks:dev` instead of `npm run dev`; it also serves the API on port 3001, and `npm run blocks:stop` stops it.
+  `ApiNamespace` calls route through the local HTTP server with the same request and response semantics as Amazon API Gateway in production, including `BlocksContext`, cookies, and headers.
+  `Realtime` channels connect over a WebSocket served by the dev server.
+  `CronJob` schedules fire while the dev server is running.

The dev server listens on `127.0.0.1` only, so other machines on your network cannot reach it. This matters because it serves your whole API against local data. Anyone who can reach the port can create an account, or sign in as any user through a `stubIdp()` provider of an `Auth` Block. They can then read or change that data. To reach the dev server from a container or a remote development machine, set `BLOCKS_DEV_HOST`. For example, `BLOCKS_DEV_HOST=0.0.0.0 npm run dev` listens on every interface and prints a warning. Anyone who can reach that interface can call your API, so do this only where you control access to the port.

To stop a dev server that is running in another terminal or in the background, run `npm run dev:stop`. It stops the server by the process ID that `npm run dev` recorded in the project, so it never stops unrelated processes. If the server uses a port other than 3000, pass the port. For example, in a template without a frontend, run:

```bash
npm run dev:stop -- --port 3001
```

### Where local state lives
<a name="local-development-state"></a>

CDK Blocks that persist data write to a `.bb-data/` directory in the directory where you start the dev server, which is your project root. Most CDK Block instances get their own subdirectory, named after the CDK Block’s full ID: its scope ID joined to its parent scope IDs with `-`. For example, `new KVStore(new Scope('my-app'), 'orders')` writes to `.bb-data/my-app-orders/`. `AppSetting` and `Secret` values share one file, `.bb-data/settings.json`.

This has three practical benefits:
+ Data persists across restarts. Stop and restart the dev server, and your users, files, and table rows are still there.
+ You can inspect the state directly. The data is stored as plain files, so you can open your `EmailClient` outbox or a `KVStore’s contents in your editor.
+ You can reset at any time. Delete `.bb-data/`, or a single CDK Block’s subdirectory, to start from a clean state.

Keep `.bb-data/` out of version control. Scaffolded CDK Blocks applications add it to `.gitignore` for you.

## What each Block maps to locally
<a name="local-development-block-mapping"></a>

Every CDK Block exposes the same typed API locally and on AWS. The following table shows what backs that API in each environment.

| Block | Locally | On AWS  |
| --- | --- | --- |
|  `Auth`  | A local user pool in `.bb-data/`. Sign-up, sign-in, password reset, MFA, and passkey flows work without any AWS calls, and verification codes go to the `codeDelivery` callback. On a `store: 'builtin'` Block, a `type: 'oidc'` provider talks to the real identity provider, so register the local callback URL `http://localhost:3000/aws-blocks/auth/callback` with it. A `stubIdp()` provider signs in test users offline without credentials. Social, SAML, and OIDC providers on the default store need a deployed user pool, so their sign-in is unavailable under `npm run dev`  | An Amazon Cognito user pool with your configured options, or no user pool with `store: 'builtin'`. `stubIdp()` providers work in sandbox deployments only, and synth fails if any other deployment uses one |
|  `KVStore`  | File-backed store in `.bb-data/` with the same key and index query semantics. The dev server keeps the store in memory and reads its file only when it creates the store, so another process that uses the same `.bb-data/` directory, such as a second dev server or a script, does not see its writes and can overwrite them | DynamoDB table, with Global Secondary Indexes for its `indexes`  |
|  `Database`  | PGlite, an embedded WebAssembly PostgreSQL engine, running in-process with data in `.bb-data/` and one schema per CDK Block. Supports migrations, transactions, and Row Level Security. A `dsql` cluster also enforces Amazon Aurora DSQL’s SQL rules and transaction limits, so unsupported SQL fails locally instead of at deploy time | Aurora DSQL, or Aurora PostgreSQL Serverless v2 for an `aurora` cluster |
|  `FileBucket`  | A directory in `.bb-data/`, mirroring S3 API behavior including presigned upload/download URLs | S3 bucket |
|  `Realtime`  | Typed pub/sub over a WebSocket served by the local dev server | API Gateway WebSocket API with DynamoDB connection management |
|  `AsyncJob`  | In-process queue. Handlers execute inside the dev server, and failed jobs retry up to `maxRetries` attempts (default 3). With `trackStatus: true`, `getStatus()` and `waitUntilComplete()` report the same states as in production: `queued`, `processing`, `complete`, and `failed`  | SQS queue with a dead-letter queue, consumed by the app’s default compute or by the `Compute` you assign |
|  `CronJob`  | In-process scheduler. `rate` and `cron` schedules fire on Node.js timers while the dev server runs, and each trigger is logged to the terminal | Amazon EventBridge Scheduler schedule that invokes a Lambda function |
|  `Agent`  | A canned, keyword-based provider that returns predictable responses without a real model, API key, or cloud cost. You can alternatively point an `openai-api` provider at Ollama or any OpenAI-compatible endpoint | An Amazon Bedrock AgentCore Runtime runs the agent loop and streams over a `Realtime` WebSocket. It calls Amazon Bedrock models, by default `BedrockModels.BALANCED` through a global inference profile. The runtime is billed for vCPU and memory while a session runs |
|  `KnowledgeBase`  | A local text index built over your documents in `.bb-data/`, so retrieval works offline | Amazon Bedrock Knowledge Bases with automatic ingestion, chunking, and embedding |
|  `EmailClient`  | Emails are captured to a local outbox (`.bb-data/…​/emails.json`) instead of being sent, so you can inspect what your application tried to send | Amazon SES |
|  `AppSetting`  | Values in `.bb-data/settings.json`  | SSM Parameter Store (SecureString when `secret: true`) |
|  `Secret`  | Plaintext values in `.bb-data/settings.json`, with the previous version in `.bb-data/secret-versions.json`. Never use real credentials locally. As in production, a `Secret` is read-only unless you set `allowRuntimeWrite: true`, so set a local value by editing `settings.json`  |  AWS Secrets Manager secret |
|  `Logger`  | Structured logs to your terminal, using the same code path as production | Same output, captured by CloudWatch Logs. Entries include the X-Ray trace ID when the runtime provides one. To add a request ID, use `log.child({ requestId })`  |
|  `Metrics`  | EMF-formatted JSON to your terminal, using the same code path as production | Same output, captured as CloudWatch metrics |
|  `Tracer`  | Traces recorded to files in `.bb-data/` for local inspection |  AWS X-Ray distributed tracing |
|  `Dashboard`  | Not available locally. The dashboard route (`/aws-blocks/dashboard` by default) responds with HTTP 503 and a message directing you to deploy, because there is no CloudWatch dashboard to render | CloudWatch dashboard organized by compute, with health and logs sections, traces when the app has a `Tracer`, and widgets for the metrics you list in `metricConfigs`  |
|  `Compute`  | No compute is provisioned. Every handler runs in-process in the dev server, whatever compute you assign it to |  AWS Lambda function for a `serverless` compute, or an Amazon ECS service on AWS Fargate for a `container` compute |

Note two things about this table:
+  `Logger` and `Metrics` run the same code in both environments. Only the destination of the output differs: what you see in your terminal locally is what CloudWatch captures in production.
+ The data CDK Blocks use real database engines locally. `Database` runs actual PostgreSQL through PGlite, and on a `dsql` cluster it also validates your SQL against Aurora DSQL restrictions, so incompatible SQL fails on your machine instead of during a deployment.

## Testing with local implementations
<a name="local-development-testing"></a>

Local implementations also form the basis for testing. A typical CDK Blocks test setup has three levels: unit tests for your business logic, integration tests against local implementations, and end-to-end tests against a sandbox. The first two levels run entirely on your machine.

### Unit test business logic with CDK Blocks as parameters
<a name="local-development-testing-unit"></a>

Extract business logic from your API handlers into pure functions that accept CDK Block instances as parameters. Type each parameter with only the CDK Block methods the function calls, using `Pick`. The function then depends only on that part of the CDK Block’s typed interface, so you can test it with a standard test runner such as Vitest, without starting the dev server:

```typescript
// orders.ts - testable without the full framework
import { ApiError, type KVStore } from 'aws-cdk-blocks';

export interface OrderInput {
  title: string;
}

export interface Order extends OrderInput {
  id: string;
  userId: string;
}

// Depend only on the KVStore methods you call, so a test can pass a small stub.
export type OrderStore = Pick<KVStore<Order>, 'put'>;

export async function createOrder(store: OrderStore, userId: string, input: OrderInput): Promise<Order> {
  if (!input.title) throw new ApiError('Title required', 400);
  const order: Order = { id: crypto.randomUUID(), ...input, userId };
  await store.put(`${userId}:${order.id}`, order);
  return order;
}
```

```typescript
// orders.test.ts
import { it, expect, vi } from 'vitest';
import { createOrder, type OrderStore } from './orders.js';

it('creates an order', async () => {
  const testStore: OrderStore = { put: vi.fn(async () => {}) };
  const result = await createOrder(testStore, 'user-1', { title: 'Test' });
  expect(result.title).toBe('Test');
  expect(testStore.put).toHaveBeenCalledWith(`user-1:${result.id}`, result);
});
```

The real `KVStore` satisfies `OrderStore`, so your API handler passes its store to `createOrder` unchanged.

For more information about structuring your application this way, see [Testing](best-practices.md#bp-testing) in Best practices.

### Integration test against local implementations
<a name="local-development-testing-fast"></a>

For tests that cover CDK Block behavior itself, run your application with `npm run dev` and test against it. CDK Blocks resolve to their local implementations automatically.

Projects created from most templates include such a test in `test/e2e.test.ts`. It uses the Node.js test runner (`node:test`) and calls your API through the same typed client as your frontend. Run it with `npm run test:e2e`. It uses a dev server that is already running, or starts one.
+ Tests run in milliseconds because everything is in-process.
+ Stateful CDK Blocks behave realistically: conditional writes on `KVStore` fail when they should, `Database` enforces your migrations and Row Level Security, and an `AsyncJob` with `trackStatus: true` records each job’s status transitions.
+ Tests run anywhere Node.js runs, including CI, without AWS credentials.

### Control and inspect state through `.bb-data/`
<a name="local-development-testing-state"></a>

Because local state is plain files, your tests can seed and assert on it directly:
+ Reset between tests or runs by deleting `.bb-data/` or one CDK Block’s subdirectory.
+ Assert on side effects that are hard to observe in the cloud. For example, `EmailClient` writes every email to a local outbox file. A test can trigger a password reset and then read the outbox to verify the message content.

### Test against a sandbox
<a name="local-development-testing-sandbox"></a>

Local implementations match the behavior of their AWS counterparts at the API level, but some things can only be verified against real services: IAM permission boundaries, service quotas and throttling, DynamoDB query performance at scale, or real model output from Amazon Bedrock.

For those cases, deploy a [sandbox](concepts.md#concepts-sandbox) with `npm run sandbox` and run the same tests against it. A sandbox is a fast, ephemeral deployment to AWS that each developer gets in isolation. A useful pattern is to parameterize your end-to-end tests by target environment, so the same test suite runs against `localhost` during development and against a sandbox URL before you ship:

| Run against | Use for |
| --- | --- |
| Local dev server | Day-to-day development, fast feedback, CI on every commit |
| Sandbox deployment | IAM and permission verification, performance characteristics, service-specific behavior, real AI model responses |
| Production deployment | Smoke tests after release |

Do most of your development and testing against local implementations, and use a sandbox when you need to verify the behavior of the AWS services themselves.

For more information about how CDK Blocks are structured, see [Conditional exports](concepts.md#concepts-conditional-exports). For deploying to AWS, see [Deploy to AWS](deploy-to-aws.md).
