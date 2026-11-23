---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/best-practices.html
---

# Best practices for AWS CDK Blocks

This topic covers best practices for structuring, securing, testing, and scaling AWS CDK Blocks applications.

## Project structure
<a name="bp-project-structure"></a>

Organize your backend code for clarity and maintainability.

 **Keep the app definition thin.** Your `cdk-blocks/index.ts` should contain CDK Block instantiations and API definitions. Move complex business logic into separate modules.

```typescript
// cdk-blocks/index.ts - thin orchestration layer
import { ApiNamespace, Scope, KVStore } from 'aws-cdk-blocks';
import { createOrder, listOrders, type Order, type OrderInput } from './orders.js';

const scope = new Scope('my-app');
const store = new KVStore<Order>(scope, 'orders', {});

export const api = new ApiNamespace(scope, 'api', (context) => ({
  createOrder: (input: OrderInput) => createOrder(store, context, input),
  listOrders: () => listOrders(store, context),
}));
```

```typescript
// cdk-blocks/orders.ts - business logic, testable in isolation
import type { BlocksContext, KVStore } from 'aws-cdk-blocks';

export interface OrderInput { title: string }
export interface Order extends OrderInput { id: string; userId: string }

export async function createOrder(store: KVStore<Order>, context: BlocksContext, input: OrderInput) {
  // validation, business rules, persistence
}
```

 **Use a single Scope per application.** Multiple scopes in one backend create separate resource namespaces, which adds complexity without benefit for most applications.

 **Co-locate related CDK Blocks.** If your app has distinct domains (orders, users, notifications), group them logically but keep them in the same app definition file unless the file becomes unwieldy.

## Error handling
<a name="bp-error-handling"></a>

CDK Blocks sends an error’s `name` and message to the frontend only for errors it knows are safe to show: an `ApiError`, or an error created with `blocksError()`. Any other error thrown in an API method, including a plain `Error` with a custom `name`, reaches the client as a nameless error with status 500 and the message `Internal error`. Throw an `ApiError` with a name to enable structured error handling on the client.

```typescript
// Backend
import { ApiError } from 'aws-cdk-blocks';

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async getItem(id: string) {
    const item = await store.get(id);
    if (!item) {
      throw new ApiError(`Item ${id} not found`, 404, { name: 'NotFoundError' });
    }
    return item;
  },
}));
```

```typescript
// Frontend
import { api } from 'cdk-blocks';
import { isBlocksError } from 'aws-cdk-blocks/client';

try {
  await api.getItem('abc');
} catch (err) {
  if (isBlocksError(err, 'NotFoundError')) {
    // Handle not found
  }
}
```

 **Best practices for errors:**
+ Throw `ApiError(message, status, { name })` with a descriptive name (`NotFoundError`, `ValidationError`, `UnauthorizedError`). Avoid a plain `Error`, because its name and message never reach the client.
+ For validation errors, throw `ApiError(message, 400)` so the client gets the message and a 400 status.
+ In frontend code, import `isBlocksError` from `aws-cdk-blocks/client`. The main `aws-cdk-blocks` entry exports nothing in a browser build.
+ Never expose internal details (stack traces, AWS resource ARNs) in error messages. The `Error.cause` property stays server-side and is never sent to the client.
+ Let unhandled errors bubble up. CDK Blocks returns them as generic 500 responses without leaking internals.

## Authentication and authorization
<a name="bp-authentication"></a>

 **Always validate the user in every API method that accesses user data.** Don’t rely on frontend-only checks. Every `ApiNamespace` method is a public endpoint until it calls `requireAuth`. The local implementation does not check auth either, so a method you forget to gate still passes every local test.

```typescript
export const api = new ApiNamespace(scope, 'api', (context) => ({
  async getMyData() {
    // Always authenticate server-side
    const user = await auth.requireAuth(context);
    return store.get(`user:${user.userSub}`);
  },
}));
```

 **Scope data access by user.** Use the user’s stable ID (`user.userSub`) as a key prefix to prevent users from accessing each other’s data. It stays the same for the user’s lifetime. Don’t key data on an email address, which a user can change.

```typescript
// Good: scoped to user
await store.put(`${user.userSub}:${itemId}`, data);

// Bad: no user scoping - any authenticated user can access any item
await store.put(itemId, data);
```

 **Make protection the default.** Define namespaces that hold signed-in methods with `auth.protect`, so each method runs only after the session check. Gate admin methods with `requireRole` or the `role` option of `auth.protect`.

 **Choose where users live before the first deploy.** The `Auth` Block keeps users in an Amazon Cognito user pool by default. Use `store: 'builtin'` when an OIDC provider is the only source of users. Changing the ID of a deployed CDK Block, or switching it from the default store to `store: 'builtin'`, removes its user pool and every user in it.

## Local development
<a name="bp-local-development"></a>

 **Develop locally first.** Use `npm run dev` as your primary development loop. Only deploy to a sandbox when you need to test behavior specific to real AWS services.

 **Understand local implementation limitations.** Local implementations replicate the API surface but not all production behavior:

| Block | Local behavior | Production difference |
| --- | --- | --- |
|  `KVStore`  | Local filesystem store |  `query()`, `scan()`, `getBatch()`, and index reads are eventually consistent. `get()` is strongly consistent by default. |
|  `Database`  | PGlite (embedded PostgreSQL), one statement or transaction at a time | Concurrent transactions on Aurora DSQL can fail at commit, which local runs don’t reproduce. An `aurora` cluster at `minCapacity: 0` takes about 20 seconds to resume |
|  `Auth`  | Local user pool in `.bb-data/`. Social, SAML, and OIDC providers on the default store can’t sign in | Sessions and users are not portable between local and deployed environments. Cognito sends codes by email |
|  `Realtime`  | Local WebSocket server | API Gateway WebSocket has connection limits and message size limits |

 **Clear local data when needed.** Delete the `.bb-data/` directory to reset all local state:

```bash
rm -rf .bb-data
```

## Testing
<a name="bp-testing"></a>

 **Unit test your business logic independently.** Extract logic from API handlers into pure functions that accept CDK Block instances as parameters.

```typescript
// orders.ts - testable without the full framework
import { ApiError, type KVStore } from 'aws-cdk-blocks';

export interface OrderInput { title: string }
export interface Order extends OrderInput { id: string; userId: string }

export async function createOrder(store: KVStore<Order>, userId: string, input: OrderInput) {
  if (!input.title) throw new ApiError('Title required', 400);
  const order: Order = { id: crypto.randomUUID(), ...input, userId };
  await store.put(`${userId}:${order.id}`, order);
  return order;
}
```

```typescript
// orders.test.ts
import type { KVStore } from 'aws-cdk-blocks';
import { createOrder, type Order } from './orders.js';

it('creates an order', async () => {
  const mockStore = { put: vi.fn(), get: vi.fn() };
  const result = await createOrder(mockStore as unknown as KVStore<Order>, 'user-1', { title: 'Test' });
  expect(result.title).toBe('Test');
  expect(mockStore.put).toHaveBeenCalled();
});
```

 **Integration test locally.** Run your full application with `npm run dev` and test the API endpoints. Local implementations are deterministic and fast.

 **End-to-end test with sandbox.** For critical paths, deploy to a sandbox and run tests against real AWS services to catch behavior differences.

## Performance
<a name="bp-performance"></a>

 **Minimize CDK Block instantiations.** Each CDK Block maps to AWS resources that you deploy and manage. CDK Blocks creates DynamoDB tables with on-demand billing, so an extra table costs little while idle. Each one is still another resource to deploy, monitor, and back up. Don’t create a new `KVStore` for every data type. Use key prefixes to partition data within a single store.

```typescript
// Good: one store, partitioned by prefix
const store = new KVStore(scope, 'data', {});
await store.put(`users:${id}`, userData);
await store.put(`orders:${id}`, orderData);

// Avoid: a separate store for each entity (more resources to deploy and manage)
const userStore = new KVStore(scope, 'users', {});
const orderStore = new KVStore(scope, 'orders', {});
```

 **Declare a key for query-heavy workloads.** If you need to list or sort records, or read them by other attributes, give the `KVStore` a `schema` and a `key`, and add `indexes`. A `query()` reads one partition, which is more efficient than a `scan()` of the whole table.

 **Keep API methods focused.** By default, every `ApiNamespace` method in your app runs on one shared AWS Lambda function. To give a namespace more memory, pass a `Compute` Block in the namespace’s `compute` option. Avoid methods that do too many things. Split them into focused operations.

## Deployment
<a name="bp-deployment"></a>

 **Use sandbox for development, full deploy for production.** Sandboxes use Lambda hot-swapping for speed but aren’t suitable for production traffic.

 **Set up separate AWS accounts** for development, staging, and production. CDK Blocks deploys the same code to any account. The resources are derived from your code, not from environment-specific configuration.

 **Configure environment-specific settings in the CDK layer.** Custom domains, VPC configuration, and other environment differences belong in `cdk-blocks/index.cdk.ts`, not in your runtime code.

```typescript
// cdk-blocks/index.cdk.ts
const isProd = process.env.DEPLOY_ENV === 'production';

const stack = await BlocksStack.create(app, stackName, {
  backendHandlerPath: join(__dirname, 'index.handler.ts'),
  backendCDKPath: join(__dirname, 'index.ts'),
  defaults: isProd ? BlocksPresets.production : BlocksPresets.sandbox,
});

if (isProd) {
  // Production-only: custom domain, WAF, etc.
  new Hosting(stack, 'Hosting', {
    root: join(__dirname, '..'),
    api: stack,
    frontDoor: {
      features: {
        domain: {
          domainName: 'app.example.com',
          hostedZone: 'example.com',
          hostedZoneId: 'Z0123456789EXAMPLE',
        },
      },
    },
  });
}
```

## Working with coding agents
<a name="bp-ai-development"></a>

CDK Blocks gives coding agents guidance. Steering files ship with each CDK Block.

To get the best results from coding agents:
+  **Keep your app definition clean and readable.** Coding agents use it as context to understand your app.
+  **Use descriptive CDK Block IDs.** `new KVStore(scope, 'user-sessions', {})` gives agents more context than `new KVStore(scope, 's1', {})`.
+  **Write JSDoc comments on API methods.** Agents use these to understand intent when generating frontend code.
+  **Install CDK Block packages.** Their `README.md` and type definitions in `node_modules` provide agents with API documentation and usage examples.
+  **Use the Agent Block for AI capabilities.** The Agent Block provides tool calling, HITL approval, and conversation persistence. Locally, it uses a canned provider for predictable testing without API keys.

### Example prompt for coding agents
<a name="example-prompt-for-coding-agents"></a>

The following prompt shows how a coding agent can add several capabilities in one request:

```
Add a FileBucket for user avatars, an AsyncJob that generates thumbnails on upload, and a Realtime channel that notifies the UI when processing completes.
```
