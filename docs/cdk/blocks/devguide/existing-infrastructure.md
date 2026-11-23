---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/existing-infrastructure.html
---

# Integrating with existing infrastructure

 AWS CDK Blocks is designed to work with existing AWS infrastructure. Whether you have an existing CDK application, pre-deployed resources, or a mix of both, you can adopt CDK Blocks incrementally without rewriting your infrastructure.

## Choosing a pattern
<a name="existing-patterns-overview"></a>

CDK Blocks provides five patterns for integrating with existing infrastructure. Choose based on your situation:

| Pattern | Effort | Use when | Local support |
| --- | --- | --- | --- |
| CDK in CDK Blocks | Low | No CDK Block exists for the resource you need | ❌ Manual |
|  `fromExisting`  | Lowest | A CDK Block exists and you have a pre-deployed resource | ✅ Automatic |
| Custom CDK Block | Medium | You’re repeating the same resource pattern in multiple places | ✅ Automatic |
| Vendorize | Low | A CDK Block that AWS provides is almost right but needs CDK changes | ✅ Automatic |
| Infrastructure outside the AWS CDK | High | Your team has to manage a resource, or the whole backend, with Terraform or another tool it already uses | ✅ Automatic |

## Pattern 1: CDK in CDK Blocks
<a name="existing-cdk-in-blocks"></a>

Use raw CDK Constructs alongside CDK Blocks. CDK Blocks gives you two shapes for this:

 ** `BlocksStack` **: A standalone CloudFormation stack containing the CDK Blocks Lambda and API Gateway. Use for new projects or when you want CDK Blocks isolated in its own deployment unit.

 ** `BlocksBackend` **: A CDK Construct you drop into an existing stack. Use when you already have stacks and want CDK Blocks to live alongside your other resources.

Both expose `executionRole`, the one IAM role that all CDK Blocks compute in the app shares. Grant permissions to it. To pass a value such as a resource ARN to your code, call `registerConfig(scope, key, value)` from `aws-cdk-blocks/cdk`. At runtime, the value is available as `process.env[key]`.

### Example: BlocksStack with an SNS topic
<a name="example-blocksstack-with-an-sns-topic"></a>

This example adds an Amazon Simple Notification Service (Amazon SNS) topic, a resource that has no CDK Block.

```typescript
// cdk-blocks/index.cdk.ts
import * as cdk from 'aws-cdk-lib';
import * as sns from 'aws-cdk-lib/aws-sns';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { BlocksPresets, BlocksStack, registerConfig } from 'aws-cdk-blocks/cdk';

const __dirname = dirname(fileURLToPath(import.meta.url));

const app = new cdk.App();
const stack = await BlocksStack.create(app, 'my-app', {
  backendHandlerPath: join(__dirname, 'index.handler.ts'),
  backendCDKPath: join(__dirname, 'index.ts'),
  defaults: BlocksPresets.production,
});

const topic = new sns.Topic(stack, 'alerts');
topic.grantPublish(stack.executionRole);
registerConfig(stack, 'ALERTS_TOPIC_ARN', topic.topicArn);
```

```typescript
// cdk-blocks/index.ts
import { Scope, ApiNamespace } from 'aws-cdk-blocks';
import { SNSClient, PublishCommand } from '@aws-sdk/client-sns';

const scope = new Scope('my-app');
const sns = new SNSClient({});

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async sendAlert(message: string) {
    await sns.send(new PublishCommand({
      TopicArn: process.env.ALERTS_TOPIC_ARN,
      Message: message,
    }));
    return { ok: true };
  },
}));
```

Like every `ApiNamespace` method, `sendAlert` is a public endpoint until you add an auth check.

For background work, don’t wire up a raw queue or schedule. Use [AsyncJob](bb-realtime-async.md#bb-async-job) or [CronJob](bb-realtime-async.md#bb-cron-job), which provision the infrastructure and run locally.

### Example: BlocksBackend inside an existing stack
<a name="example-blocksbackend-inside-an-existing-stack"></a>

Use a static factory method because `BlocksBackend.create()` is asynchronous and constructors cannot use `await`:

```typescript
// my-existing-stack.ts
import * as cdk from 'aws-cdk-lib';
import * as sns from 'aws-cdk-lib/aws-sns';
import { BlocksBackend, BlocksPresets, registerConfig } from 'aws-cdk-blocks/cdk';

export class MyApiStack extends cdk.Stack {
  static async create(scope: cdk.App, id: string, props?: cdk.StackProps) {
    const stack = new MyApiStack(scope, id, props);

    // Your existing resources
    const topic = new sns.Topic(stack, 'alerts');

    // Drop Blocks in as a Construct
    const blocks = await BlocksBackend.create(stack, 'BlocksApi', {
      backendHandlerPath: './cdk-blocks/index.handler.ts',
      backendCDKPath: './cdk-blocks/index.ts',
      defaults: BlocksPresets.production,
    });

    topic.grantPublish(blocks.executionRole);
    registerConfig(blocks, 'ALERTS_TOPIC_ARN', topic.topicArn);
    return stack;
  }
}
```

Relative `backendHandlerPath` and `backendCDKPath` values resolve against the directory you run synth from.

Run synth with the `cdk` condition, for example `"app": "npx tsx -C cdk bin/app.ts"` in `cdk.json`, or `NODE_OPTIONS="--conditions=cdk" npx cdk synth`. The `npm run deploy` and `npm run sandbox` scripts set it for you. Without it, every CDK Block import resolves to its local implementation and produces no infrastructure, so `create()` stops with a `Missing --conditions=cdk` error.

### Tradeoffs
<a name="tradeoffs"></a>
+ ✅ Full access to any AWS resource with plain CDK and SDK
+ ❌ No local implementation. `npm run dev` will call real AWS unless you stub the SDK yourself
+ ❌ No type-level guarantee that config values such as `process.env.ALERTS_TOPIC_ARN` exist

If you find yourself repeating this pattern, consider creating a [custom CDK Block](custom-building-blocks.md) instead.

## Pattern 2: fromExisting
<a name="existing-from-existing"></a>

Some CDK Blocks can wrap a pre-deployed AWS resource. The CDK Block provides its typed API and local implementation, but skips provisioning. You keep ownership of the resource.

These CDK Blocks support it. Pass the factory method’s result as the option in the Factory method column, such as `table` for `KVStore`. `AppSetting.fromExisting` is different: it returns the setting itself.

| Block | Factory method | Wraps |
| --- | --- | --- |
|  `KVStore`  |  `table: KVStore.fromExisting(tableName)`  | Existing DynamoDB table. Pass a `key` that matches the table’s key schema. |
|  `FileBucket`  |  `bucket: FileBucket.fromExisting(bucketName)`  | Existing S3 bucket |
|  `Database`  |  `cluster: DatabaseCluster.fromExisting({ name, ca? })`  | Existing PostgreSQL database, with its tables and data. `0` stores its connection string. The deploy runs the files in `migrationsPath` on it. For more information, see [Existing PostgreSQL databases](bb-data-storage.md#bb-database-existing). |
|  `Auth`  |  `userPool: Auth.fromExisting(userPoolId, clientId?)`  | Existing Cognito user pool. CDK Blocks adds its own app client to the pool. With `allowBearerAuth: true`, it also accepts access tokens from the app client that you pass as `clientId`. |
|  `AppSetting`  |  `AppSetting.fromExisting(scope, id, { name })`  | Existing AWS Systems Manager Parameter Store parameter |
|  `Secret`  |  `secret: Secret.fromExisting(secretArn)`  | Existing Secrets Manager secret |
|  `Metrics`  |  `metrics: Metrics.fromExisting(namespace)`  | Existing CloudWatch namespace |

### Example
<a name="example"></a>

```typescript
// cdk-blocks/index.ts
import { Scope, KVStore, ApiNamespace } from 'aws-cdk-blocks';
import { z } from 'zod';

const scope = new Scope('my-app');

const sessions = new KVStore(scope, 'sessions', {
  schema: z.object({ sessionId: z.string(), userId: z.string() }),
  key: { partitionKey: 'sessionId' },
  table: KVStore.fromExisting('my-legacy-sessions-table'),
});

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async getSession(token: string) {
    return sessions.get({ sessionId: token });
  },
}));
```

### Tradeoffs
<a name="tradeoffs-2"></a>
+ ✅ Local development still works. `npm run dev` keeps data in files under `.bb-data/`, not in the real resource. A `Database` on an existing database is the exception: it connects to that database
+ ✅ IAM permissions are granted automatically to the shared execution role
+ ✅ Same typed API as a resource that CDK Blocks manages
+ ❌ Limited to the CDK Block’s API surface. If you need features the CDK Block doesn’t expose, use Pattern 1
+ ❌ Cross-account resources require manual IAM (fall back to Pattern 1)

The wrapped resource can come from any tool.

## Pattern 3: Custom CDK Block
<a name="existing-custom-bb"></a>

When you’re repeating Pattern 1 for the same resource type, wrap it in a custom CDK Block. This gives you a typed API, a local implementation, and reusability.

See [Creating custom CDK Blocks](custom-building-blocks.md) for a complete guide to authoring CDK Blocks.

### When to use
<a name="when-to-use"></a>
+ You have ≥2 callers using the same resource pattern
+ You want `npm run dev` to work without AWS for this resource
+ You want type-safe call sites instead of raw `process.env` \+ SDK

## Pattern 4: Vendorize
<a name="existing-vendorize"></a>

If a CDK Block that AWS provides is *almost* right but needs CDK changes you can’t get upstream quickly, you can copy its source into your project:

```bash
npm run vendorize -- @aws-cdk-blocks/bb-kv-store
```

This copies the CDK Block source into your monorepo. You now own it. Modify the CDK, runtime, or local implementation as needed.

### Tradeoffs
<a name="tradeoffs-3"></a>
+ ✅ Full control over the CDK Block implementation
+ ✅ Local implementations, types, and API surface all still work
+ ❌ You’re responsible for maintenance. Upstream updates require manual re-sync
+ ❌ Only use when a custom CDK Block (Pattern 3) or an upstream pull request won’t solve the problem

You can also vendorize a CDK Block without `fromExisting` to point it at a resource that the CDK did not create. Change its `index.cdk.ts` to import the resource instead of creating it.

## Pattern 5: Infrastructure outside the AWS CDK
<a name="existing-outside-cdk"></a>

Each CDK Block’s CDK code (`index.cdk.ts`) creates its resources and grants the shared execution role access. It then either names each resource from the CDK Block’s `fullId`, so the runtime can derive the same name, or passes names and ARNs to the runtime as config. Nothing else in the CDK Block depends on the CDK: the runtime entry (`index.aws.ts`), the local implementation, local development and the typed client work the same whoever created the infrastructure. So a tool other than the CDK can provide the infrastructure, as long as it provides the same contract.

Two shapes work:

| Shape | CDK still owns | Your tool owns |
| --- | --- | --- |
| Hybrid | The app shell (execution role, Lambda function, API Gateway) and most CDK Blocks | One or more CDK Blocks' resources, through `fromExisting` (Pattern 2) or a vendorized CDK Block (Pattern 4) |
| No CDK | Nothing | The app shell and every CDK Block’s resources, grants and config |

The contract differs by CDK Block. A KVStore needs only a table with the right name and the key schema of its `key` option (or the string partition key `_bkv_pk` without one), which the execution role can read and write. An AsyncJob needs a queue, config, and an event source mapping on the backend function with settings that match its options. A Database needs config and its migrations run.

### When to use
<a name="when-to-use-2"></a>
+ A resource, or the whole backend, has to be managed by Terraform or another tool your team already uses
+ You want to keep the CDK Blocks app code, local implementations and typed client without deploying through the CDK

### When not to use
<a name="when-not-to-use"></a>
+  `fromExisting` (Pattern 2) already covers the resource and the CDK can keep deploying everything else
+ You are not prepared to keep names, config keys, IAM grants, and CDK Block options in sync by hand

### Tradeoffs
<a name="tradeoffs-4"></a>
+ ✅ Your infrastructure tool manages the resources, with its own state, review and drift detection
+ ✅ App code, local implementations and the typed client do not change
+ ❌ You keep the contract in sync by hand: derived names, config keys, IAM grants, and options such as AsyncJob’s `maxRetries`. A mismatch usually shows up at runtime as an error in the function’s logs, not at deploy time
+ ❌ With no CDK, you replace `npm run deploy`, `npm run sandbox` and `npm run destroy` with your own steps
+ ❌ When a CDK Block changes its contract in a new version, you update your infrastructure to match

## Raw HTTP routes and webhooks
<a name="existing-raw-route"></a>

 `ApiNamespace` methods are JSON-RPC calls from your frontend. When another system must call a fixed URL, such as a payment provider sending webhooks, use `RawRoute`. You get the request and set the response yourself.

```typescript
// cdk-blocks/index.ts
import { createHmac, timingSafeEqual } from 'node:crypto';
import { ApiError, RawRoute, Scope, Secret } from 'aws-cdk-blocks';

const scope = new Scope('my-app');
const signingKey = new Secret(scope, 'webhook-signing-key');

new RawRoute(scope, 'payments-webhook', {
  method: 'POST',
  path: '/webhooks/payments',
  handler: async ({ request, response }) => {
    const body = await request.text();
    const key = await signingKey.get();
    if (!key) throw new ApiError('Webhook signing key is not set', 503);

    const expected = Buffer.from(createHmac('sha256', key).update(body).digest('hex'));
    const received = Buffer.from(request.headers.get('x-signature') ?? '');
    if (received.length !== expected.length || !timingSafeEqual(received, expected)) {
      throw new ApiError('Invalid signature', 401);
    }

    const event = JSON.parse(body) as { type: string };
    console.log('Payment event:', event.type);
    response.status = 200;
    response.send({ received: true });
  },
});
```

 `RawRoute` takes these options:
+  `method`: `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, or `OPTIONS`.
+  `path`: `/health` matches exactly, `/users/{id}` captures one segment into `request.params.id`, and `/files/ ` captures the rest of the path into `request.params['`. If you omit `path`, it is built from the IDs of any scopes between your top-level scope and the route, plus the route ID. Set `path` explicitly for URLs that other systems depend on.
+  `handler`: Receives `request` (`headers`, `text()`, `json()`, `url`, `params`) and `response` (`status`, `headers`, `send()`). The response `Content-Type` defaults to `application/json`.

CDK Blocks serves the route from the same origin as your API, both in `npm run dev` and when deployed. It needs no extra infrastructure. You cannot register `/`, `/aws-blocks`, or a path under `/aws-blocks/api`, and you cannot register the same method and path twice.

A raw route has no auth of its own, so check a signature or token in the handler. If the handler throws an `ApiError`, the response uses its status and the body `{ "error": message }`. An error that you create with `blocksError()` keeps its message and adds its `name` to the body. Any other error becomes an HTTP 500 with the body `{ "error": "Internal error" }`, and the full error goes only to the server log.
