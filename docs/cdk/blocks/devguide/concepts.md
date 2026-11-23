---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/concepts.html
---

# AWS CDK Blocks concepts

This topic explains the key concepts you need to understand when building applications with AWS CDK Blocks.

## CDK Blocks
<a name="concepts-building-blocks"></a>

A **CDK Block** is an npm package for a single capability. Each CDK Block packages a CDK Construct for the infrastructure, an interface, and the interface’s AWS and local implementations into one package. When you create a CDK Block in your code, CDK Blocks sets up the matching AWS resources, wires permissions, and gives you a local implementation for development.

For example, `KVStore` is a CDK Block for key-value storage. A single instantiation gives you:
+ A DynamoDB table (provisioned automatically during deployment)
+  AWS SDK integration (used at runtime in Lambda)
+ A local store (used during local development)

```typescript
import { KVStore, Scope } from 'aws-cdk-blocks';

const scope = new Scope('my-app');
const cache = new KVStore<{ name: string }>(scope, 'cache', {});

// Same API works locally and in production
await cache.put('user:123', { name: 'Alice' });
const user = await cache.get('user:123');
```

## Scope
<a name="concepts-scope"></a>

A **Scope** is a namespace container for CDK Blocks. Every CDK Block must be instantiated within a scope. The scope provides identity and grouping. Each CDK Block’s full identifier (`fullId`) joins its scope ID and the ID you provide with `-`.

```typescript
const scope = new Scope('my-app');
const users = new KVStore(scope, 'users', {});   // Full ID: my-app-users
const sessions = new KVStore(scope, 'sessions', {}); // Full ID: my-app-sessions
```

In a deployed app, the full ID also starts with the stack name, for example `my-stack-my-app-users`. Resource names and the local `.bb-data/` folders are derived from it, so scopes keep resource names unique and predictable across your application.

**Warning**
Renaming a CDK Block ID (the second argument to the constructor) or its scope changes its full ID. On the next deployment, the CDK Block gets a new, empty AWS resource, and your app no longer sees the old data. What happens to the old resource depends on the removal policy. With `BlocksPresets.production`, stateful resources such as `KVStore`, `Database`, and `FileBucket` use a `RETAIN` policy, so the old resource is removed from the stack but kept in your account. With `BlocksPresets.sandbox`, the old resource is deleted along with its data. Always treat CDK Block IDs as immutable once deployed.

## The app definition
<a name="concepts-ifc-layer"></a>

The **app definition** is your backend entry point, the `cdk-blocks/index.ts` file. This is where you instantiate CDK Blocks and define your API. Each CDK Block includes a CDK Construct, so CDK Blocks creates CDK infrastructure from this code. To change what a CDK Block creates or add other resources, use the [CDK layer](#concepts-cdk-layer).

```typescript
// cdk-blocks/index.ts - the app definition
import { ApiNamespace, Scope, KVStore, Auth } from 'aws-cdk-blocks';

const scope = new Scope('my-app');

// Infrastructure is derived from these instantiations
const auth = new Auth(scope, 'auth');
const todos = new KVStore<{ title: string; done: boolean }>(scope, 'todos', {});

// API methods are callable from the frontend
export const api = new ApiNamespace(scope, 'api', (context) => ({
  async createTodo(title: string) {
    const user = await auth.requireAuth(context);
    await todos.put(`${user.userSub}:${title}`, { title, done: false });
  },
}));

// Exposes sign-up, sign-in, and sign-out to the frontend
export const authApi = auth.createApi();
```

The app definition serves three purposes simultaneously:
+  **Local development**: CDK Blocks resolve to local implementations
+  **Deployment**: CDK Blocks resolve to CDK Constructs that define your infrastructure
+  **Production runtime**: CDK Blocks resolve to AWS SDK integrations running in Lambda

## Conditional exports
<a name="concepts-conditional-exports"></a>

CDK Blocks uses **Node.js conditional exports** to route the same `import` statement to different implementations depending on the execution context. This is the mechanism that makes a single codebase work across local development, deployment, and production.

When you write `import { KVStore } from 'aws-cdk-blocks'`, the resolved file depends on context:

| Context | Resolved implementation | What happens |
| --- | --- | --- |
| Local development | In-memory and filesystem | Your app runs entirely on localhost |
| CDK synthesis | CDK Construct (DynamoDB table) | Infrastructure is defined for CloudFormation |
| Lambda runtime |  AWS SDK (DynamoDB client) | Real AWS service calls in production |
| TypeScript/IDE | Type definitions | Full IntelliSense and type checking |

You never need to configure conditional exports manually. CDK Blocks sets up the build system to select the correct implementation for each context automatically.

## ApiNamespace
<a name="concepts-api-namespace"></a>

An **ApiNamespace** defines type-safe backend methods that your frontend can call directly. It’s the bridge between your backend logic and your client code.

```typescript
// Backend: define the API
export const api = new ApiNamespace(scope, 'api', (context) => ({
  async greet(name: string) {
    return { message: `Hello, ${name}!` };
  },
}));
```

```typescript
// Frontend: call the API directly
import { api } from 'cdk-blocks';

const result = await api.greet('World');
// result.message === 'Hello, World!'
// TypeScript knows the return type
```

There is no code generation, no API client initialization, and no URL configuration. The frontend import is type-safe. If you change the backend method signature, TypeScript reports errors in the frontend immediately.

Locally, `ApiNamespace` routes calls through a local HTTP server. In production, calls go through API Gateway to Lambda.

## BlocksContext
<a name="concepts-context"></a>

The **BlocksContext** is the request/response object provided to `ApiNamespace` handlers. CDK Blocks that need HTTP-level access (such as authentication CDK Blocks reading cookies or setting headers) accept `BlocksContext` as a parameter.

```typescript
export const api = new ApiNamespace(scope, 'api', (context) => ({
  async protectedAction() {
    // Auth blocks use context to read headers/cookies
    const user = await auth.requireAuth(context);
    return { username: user.username };
  },
}));
```

You don’t construct `BlocksContext` yourself. It’s provided automatically by the framework for each incoming request.

Every `ApiNamespace` method is a public endpoint until it calls `requireAuth`. Creating an `Auth` Block does not protect any method by itself. To make every method of a namespace require a session, define it with `auth.protect`. The local implementation does not check auth either, so a method you forget to gate still passes every local test.

## The CDK layer
<a name="concepts-cdk-layer"></a>

The **CDK layer** is the file `cdk-blocks/index.cdk.ts`. In a standalone project, it creates your stack and gives you direct access to CDK Constructs. Use it when you need to:
+ Add AWS resources that don’t have a CDK Block (such as Amazon SNS topics)
+ Configure custom domains or other environment-specific settings
+ Integrate CDK Blocks into an existing CDK application

```typescript
// cdk-blocks/index.cdk.ts
import * as cdk from 'aws-cdk-lib';
import * as sns from 'aws-cdk-lib/aws-sns';
import { BlocksStack, BlocksPresets, registerConfig } from 'aws-cdk-blocks/cdk';
import { getStackName } from 'aws-cdk-blocks/scripts';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));

const app = new cdk.App();
const sandboxMode = app.node.tryGetContext('sandboxMode') === 'true';
const projectRoot = app.node.tryGetContext('projectRoot') || process.cwd();

const stack = await BlocksStack.create(app, getStackName({ sandbox: sandboxMode, projectRoot }), {
  backendHandlerPath: join(__dirname, 'index.handler.ts'),
  backendCDKPath: join(__dirname, 'index.ts'),
  defaults: sandboxMode ? BlocksPresets.sandbox : BlocksPresets.production,
});

// Add any CDK construct alongside your Blocks
const topic = new sns.Topic(stack, 'alerts');
topic.grantPublish(stack.executionRole);
registerConfig(stack, 'ALERTS_TOPIC_ARN', topic.topicArn);
```

All compute in your app shares one execution role, `stack.executionRole`, so a grant to it applies to every function. `registerConfig` passes a value to your runtime code, which reads it as `process.env.ALERTS_TOPIC_ARN`. Pass absolute paths to `BlocksStack.create`. A relative `backendCDKPath` resolves against the current working directory, not against this file.

For background work, use the `AsyncJob` and `CronJob` Blocks instead of adding queues or schedules in the CDK layer.

Every project needs this file. In a standalone project, `cdk.json` points the CDK app at it, and CDK Blocks does not generate one if it is missing. The project templates include it.

## Local development
<a name="concepts-local-development"></a>

When you run `npm run dev`, CDK Blocks starts your entire application locally:
+ CDK Blocks use local implementations (file-backed stores, a local user pool, embedded databases)
+ The application runs on `http://localhost:3000` with hot reload
+ No AWS account, no internet connection, and no cloud costs required

Local data persists in a `.bb-data/` directory at your project root. Each CDK Block gets its own subdirectory.

## Sandbox deployments
<a name="concepts-sandbox"></a>

A **sandbox** is a fast, ephemeral deployment to AWS for testing against real services. When you run `npm run sandbox`:
+ CDK Blocks deploys your backend to Lambda with hot-swapping
+ CDK Blocks resolve to real AWS services (DynamoDB, API Gateway, etc.)
+ Each developer gets an isolated sandbox identified by a unique ID
+ Remove it with `npm run sandbox:destroy`

Sandboxes are useful when you need to test behavior that differs between local implementations and real services, such as DynamoDB query performance or IAM permission boundaries.

## Terminology reference
<a name="concepts-terminology"></a>

| Term | Definition |
| --- | --- |
| CDK Block | An npm package for a single capability that includes a CDK Construct for its infrastructure, its runtime code, and a local implementation. |
| Scope | A namespace container that provides identity to CDK Blocks. |
| App definition | The backend entry point (`cdk-blocks/index.ts`) where CDK Blocks are instantiated and APIs are defined. Infrastructure is derived from this code. |
| CDK layer | The file (`cdk-blocks/index.cdk.ts`) that creates your stack in a standalone project and gives you direct CDK access for custom infrastructure. |
| ApiNamespace | A core primitive that defines type-safe RPC methods callable from the frontend. It is not a CDK Block. |
| BlocksContext | The request/response context object provided to API handlers. |
| Conditional exports | Node.js mechanism that routes imports to different files based on execution context. |
| Sandbox | A fast, ephemeral AWS deployment for testing against real services. |
| Local implementation | A version of a CDK Block that runs on your machine without AWS, backed by memory, the filesystem, or an embedded engine such as PGlite. |
