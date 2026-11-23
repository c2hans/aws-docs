---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/custom-building-blocks.html
---

# Creating custom CDK Blocks

When the AWS CDK Blocks that AWS provides don’t cover your use case, or when you want every app team to start from your own standards, create a custom CDK Block. A custom CDK Block packages infrastructure, runtime logic, and a local implementation into a single reusable module. Platform developers share custom CDK Blocks with their app teams through npm.

## Use cases for custom CDK Blocks
<a name="custom-bb-when"></a>

Create a custom CDK Block when:
+ You’re repeating the same AWS resource \+ SDK boilerplate across multiple API methods
+ You want local development support for a resource that doesn’t have a built-in CDK Block
+ You want to share a reusable capability across projects or app teams

Don’t create a custom CDK Block when:
+ You only need the resource in one place. Use the [The CDK layer](concepts.md#concepts-cdk-layer) directly instead
+ A built-in CDK Block already does what you need

## Create a Block with the scaffolder
<a name="custom-bb-scaffold"></a>

Start with the `@aws-cdk-blocks/create-block` scaffolder. It generates a complete CDK Block package that builds and passes its tests before you change anything:

```bash
npm create @aws-cdk-blocks/block@latest Notifications
```

Pass the class name in PascalCase, without a `BB` prefix. The package is named `bb-` plus the name in kebab case, for example `@my-org/bb-notifications`.

What the scaffolder does depends on where you run it:

| Where you run it | Result |
| --- | --- |
| Inside an npm workspaces repository | Creates `packages/bb-<name>`, adds it to the root `workspaces`, runs `npm install`, then builds and tests the new package. Your app can import it without publishing. Your app code is not changed. The npm scope comes from the name in the root `package.json`, or is `app` if that name has no scope. |
| Anywhere else | Creates a standalone `@<scope>/bb-<name>` package in `./bb-<name>` and runs `npm install` in it. The scope defaults to `your-org`. |

| Option | Meaning |
| --- | --- |
|  `--scope <npm-scope>`  | npm scope for the package name |
|  `--dir <path>`  | Target directory for a standalone package |
|  `--yes`, `-y`  | Skip the confirmation prompt |
|  `--skip-install`  | Don’t run `npm install`  |
|  `--skip-verify`  | Don’t build and test the package afterward |
|  `--dry-run`  | Print what would be generated, and write nothing |

The generated code is a skeleton with one example method (`echo`) and `TODO` markers. Replace it with your CDK Block’s API. The rest of this page walks through each file, using an email notifications CDK Block as the example.

## Block structure
<a name="custom-bb-structure"></a>

A CDK Block is an npm package with one entry for each place its code runs:

```
bb-notifications/
├── src/
│   ├── index.mock.ts
│   ├── index.aws.ts
│   ├── index.cdk.ts
│   ├── index.browser.ts
│   ├── types.ts
│   ├── errors.ts
│   ├── version.ts
│   ├── index.test.ts
│   └── parity.test.ts
├── scripts/
│   └── generate-version.mjs
├── package.json
├── tsconfig.json
├── api-extractor.json
├── README.md
├── DESIGN.md
└── LICENSE
```

 **Local**: Runs during `npm run dev` and in tests. Its types are the CDK Block’s public types.

 **Runtime**: Calls AWS with the SDK. Runs in deployed compute.

 **Infrastructure**: CDK Constructs and IAM grants. Runs during `cdk synth`.

 **Browser**: A stub that exports the public types and error names.

 **Shared types**: Option and input types. Types only.

 **Errors**: The CDK Block’s error names.

 **Version**: `BB_NAME` and `BB_VERSION`. The `prebuild` script generates this file.

 **Tests** for the local implementation.

 **Parity test**: Checks that every entry exports the same error names.

Each implementation class extends `Scope`. The runtime and local classes call `super(id, { parent: scope, bbName, bbVersion })`; the CDK class passes `bbName` only. Extending `Scope` gives the CDK Block its `fullId` and `buildUserAgentChain()`, which you pass to AWS SDK clients as `customUserAgent`. In the CDK class, it also gives the CDK Block a place in the construct tree and the shared execution role. CDK Blocks telemetry counts custom CDK Blocks but never sends their names.

## Configure package.json exports
<a name="custom-bb-package-json"></a>

The `package.json` uses conditional exports to route imports to the correct file:

```json
{
  "name": "@my-org/bb-notifications",
  "version": "0.1.0",
  "type": "module",
  "keywords": ["aws-blocks"],
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
  },
  "files": ["dist", "src", "README.md", "DESIGN.md", "LICENSE"],
  "dependencies": {
    "@aws-cdk-blocks/core": "^0.8.0",
    "@aws-sdk/client-sesv2": "^3.1161.0"
  },
  "peerDependencies": {
    "aws-cdk-lib": "^2.257.0",
    "constructs": "^10.6.0"
  }
}
```

Node.js uses the first condition that matches, so keep `browser`, `cdk`, and `aws-runtime` before `types` and `default`. The nested `types` under `cdk` lets TypeScript see the CDK class when it checks CDK code.

| Export condition | File | When it’s used |
| --- | --- | --- |
|  `browser`  |  `index.browser.js`  | Bundling frontend code |
|  `cdk`  |  `index.cdk.js`  | CDK synthesis (`--conditions=cdk`) |
|  `aws-runtime`  |  `index.aws.js`  | Deployed compute (AWS Lambda by default) |
|  `types`  |  `index.mock.d.ts`  | IDE IntelliSense and TypeScript compilation |
|  `default`  |  `index.mock.js`  | Local development (`npm run dev`) and tests |

## Define shared types
<a name="custom-bb-types"></a>

Start by defining the options and inputs your CDK Block accepts. Every entry imports them from `types.ts`, which has no runtime code.

```typescript
// src/types.ts
export interface NotificationsOptions {
  /** Sender address. It must be a verified identity in Amazon SES. */
  fromAddress: string;
}

export interface SendEmailInput {
  to: string;
  subject: string;
  body: string;
}
```

The class type that app code sees comes from `index.mock.ts`, because the `types` condition points to it. Keep the public methods the same in every entry.

## Define named errors
<a name="custom-bb-errors"></a>

List your CDK Block’s error names in `errors.ts`:

```typescript
// src/errors.ts
export const NotificationsErrors = {
  InvalidRecipient: 'InvalidRecipientException',
} as const;
```

Throw them with `blocksError(name, message)` from `@aws-cdk-blocks/core`. A branded error keeps its `name` and `message` when it reaches the client. Callers can then match it with `isBlocksError(e, NotificationsErrors.InvalidRecipient)` on the server or in the browser. A plain `Error`, or an error from an AWS SDK, reaches the client as a nameless error with status 500 and the message "Internal error". Don’t put raw SDK error text in a branded message.

## Implement the runtime
<a name="custom-bb-runtime"></a>

The runtime implementation uses the AWS SDK to interact with real services. It runs in deployed compute.

```typescript
// src/index.aws.ts
import { SESv2Client, SendEmailCommand } from '@aws-sdk/client-sesv2';
import { Scope, blocksError } from '@aws-cdk-blocks/core';
import type { ScopeParent } from '@aws-cdk-blocks/core';
import { NotificationsErrors } from './errors.js';
import type { NotificationsOptions, SendEmailInput } from './types.js';
import { BB_NAME, BB_VERSION } from './version.js';

export { NotificationsErrors } from './errors.js';
export type { NotificationsOptions, SendEmailInput } from './types.js';

export class Notifications extends Scope {
  private readonly client: SESv2Client;
  private readonly fromAddress: string;

  constructor(scope: ScopeParent, id: string, options: NotificationsOptions) {
    super(id, { parent: scope, bbName: BB_NAME, bbVersion: BB_VERSION });
    this.client = new SESv2Client({ customUserAgent: this.buildUserAgentChain() });
    this.fromAddress = options.fromAddress;
  }

  async sendEmail(input: SendEmailInput): Promise<{ messageId: string }> {
    if (!input.to.includes('@')) {
      throw blocksError(NotificationsErrors.InvalidRecipient, 'The recipient is not an email address.');
    }
    const result = await this.client.send(new SendEmailCommand({
      FromEmailAddress: this.fromAddress,
      Destination: { ToAddresses: [input.to] },
      Content: {
        Simple: {
          Subject: { Data: input.subject },
          Body: { Text: { Data: input.body } },
        },
      },
    }));
    return { messageId: result.MessageId ?? 'unknown' };
  }
}
```

Pass `this.buildUserAgentChain()` as `customUserAgent` so the SDK’s user agent names CDK Blocks. Only official CDK Blocks add their own name to the chain, so a custom CDK Block is not named in it.

If your CDK Block owns a named resource, such as a table, name it from `this.fullId` in the CDK layer. In the runtime and local entries, call `registerSdkIdentifiers(this.fullId, { tableName })` in the constructor. Read the name back with `getSdkIdentifiers(this)` when a method runs, not in the constructor. Both functions come from `@aws-cdk-blocks/core`. Each layer derives the same name, so the CDK layer does not need to pass it to the runtime.

## Write the local implementation
<a name="custom-bb-mock"></a>

The local implementation provides the same API but runs without AWS. Use in-memory data structures, the filesystem, or embedded databases.

```typescript
// src/index.mock.ts
import { randomUUID } from 'node:crypto';
import { writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { Scope, blocksError } from '@aws-cdk-blocks/core';
import type { ScopeParent } from '@aws-cdk-blocks/core';
import { assertNotMockInDeployedEnv, getMockDataDir } from '@aws-cdk-blocks/core/bb-utils';
import { NotificationsErrors } from './errors.js';
import type { NotificationsOptions, SendEmailInput } from './types.js';
import { BB_NAME, BB_VERSION } from './version.js';

// Fail closed if the local implementation is ever loaded in a deployed environment.
assertNotMockInDeployedEnv('@my-org/bb-notifications');

export { NotificationsErrors } from './errors.js';
export type { NotificationsOptions, SendEmailInput } from './types.js';

export class Notifications extends Scope {
  private readonly fromAddress: string;

  constructor(scope: ScopeParent, id: string, options: NotificationsOptions) {
    super(id, { parent: scope, bbName: BB_NAME, bbVersion: BB_VERSION });
    this.fromAddress = options.fromAddress;
  }

  async sendEmail(input: SendEmailInput): Promise<{ messageId: string }> {
    if (!input.to.includes('@')) {
      throw blocksError(NotificationsErrors.InvalidRecipient, 'The recipient is not an email address.');
    }
    const messageId = randomUUID();
    // .bb-data/<fullId>/ belongs to this Block instance.
    const file = join(getMockDataDir(this), `${messageId}.json`);
    writeFileSync(file, JSON.stringify({ from: this.fromAddress, ...input, messageId }));
    console.log(`[mock] Email to ${input.to}: "${input.subject}"`);
    return { messageId };
  }
}
```

During local development, emails are logged to the console and saved as JSON files instead of being sent through Amazon SES. `getMockDataDir(this)` returns `.bb-data/<fullId>/` in the project folder and creates it. Pass `this`, not the parent scope, so each instance of the CDK Block gets its own folder.

 `assertNotMockInDeployedEnv` makes the module throw if it loads in deployed compute. If the backend is ever bundled without the `aws-runtime` condition, it fails at load instead of running the local implementation.

## Implement the infrastructure
<a name="custom-bb-infra"></a>

The infrastructure export defines CDK Constructs that are synthesized during deployment. Grant permissions to `this.executionRole`, the one IAM role that all compute in the app shares.

```typescript
// src/index.cdk.ts
import * as iam from 'aws-cdk-lib/aws-iam';
import { Scope, synthGuard } from '@aws-cdk-blocks/core/cdk';
import type { ScopeParent } from '@aws-cdk-blocks/core';
import type { NotificationsOptions } from './types.js';
import { BB_NAME } from './version.js';

export { NotificationsErrors } from './errors.js';
export type { NotificationsOptions, SendEmailInput } from './types.js';

export class Notifications extends Scope {
  constructor(scope: ScopeParent, id: string, options: NotificationsOptions) {
    super(id, { parent: scope, bbName: BB_NAME });
    // All compute in the app shares one execution role. Grant to it.
    this.executionRole.addToPrincipalPolicy(new iam.PolicyStatement({
      actions: ['ses:SendEmail'],
      resources: ['*'],
      conditions: {
        StringEquals: { 'ses:FromAddress': options.fromAddress },
      },
    }));
  }

  // Runtime methods don't exist during synth. A call fails with a clear error.
  sendEmail(..._args: unknown[]): never {
    return synthGuard('Notifications', 'sendEmail');
  }
}
```

Stub every runtime method with `synthGuard`, as the CDK Blocks that ship with CDK Blocks do. If app code calls `sendEmail` at the top level of the backend module, synth stops with an error that says where to call it instead.

If the runtime needs a value that only the CDK layer knows, other than a resource name, pass it with `registerConfig(this, 'KEY', value)` from `@aws-cdk-blocks/core/cdk`. The runtime reads it as `process.env.KEY`.

## Client middleware (optional)
<a name="custom-bb-client-hook"></a>

Most CDK Blocks return plain JSON data and need no browser code. Add client middleware only if a method must give the browser a live object, such as a channel to subscribe to. This uses the Transferable pattern:

1. The server method returns an object whose `toJSON()` returns a descriptor tagged with `__blocks`.

1. The CDK Block calls `this.registerClientMiddleware()` in the constructor of its local and runtime entries. The generated frontend client imports the module it names.

1. That module calls `registerMiddleware` from `@aws-cdk-blocks/core/client`. Its `onResponse` hook turns the descriptor into the live object. An optional `onRequest` hook can change outgoing requests, for example to add a header.

```typescript
// src/index.aws.ts and src/index.mock.ts (constructor)
this.registerClientMiddleware('@my-org/bb-notifications/middleware');

// A method that returns a Transferable
async trackDelivery(messageId: string) {
  const eventsUrl = `${this.eventsBaseUrl}/${encodeURIComponent(messageId)}`;
  return {
    // The server sends this descriptor. The client middleware turns it into a live object.
    toJSON: () => ({ __blocks: 'my-org/delivery' as const, eventsUrl }),
  };
}
```

```typescript
// src/middleware.ts (package export "./middleware")
import { registerMiddleware } from '@aws-cdk-blocks/core/client';

interface DeliveryDescriptor {
  __blocks: 'my-org/delivery';
  eventsUrl: string;
}

function isDeliveryDescriptor(data: unknown): data is DeliveryDescriptor {
  return typeof data === 'object' && data !== null
    && (data as { __blocks?: unknown }).__blocks === 'my-org/delivery';
}

// Runs on import. The generated client imports this module for you.
registerMiddleware({
  onResponse(data) {
    if (!isDeliveryDescriptor(data)) return data;
    return {
      onStatus(handler: (status: string) => void) {
        const events = new EventSource(data.eventsUrl);
        events.onmessage = (event) => handler(event.data);
        return () => events.close();
      },
    };
  },
});
```

Export the middleware module from `package.json`, for example as `./middleware`. The local implementation must return a working Transferable too. The `Realtime` Block that ships with CDK Blocks uses this pattern for its channels.

## Use your Block
<a name="custom-bb-usage"></a>

After building your package, install it in your project and use it like any built-in CDK Block:

```typescript
// cdk-blocks/index.ts
import { ApiNamespace, ApiError, Scope, isBlocksError } from 'aws-cdk-blocks';
import { Notifications, NotificationsErrors } from '@my-org/bb-notifications';

const scope = new Scope('my-app');
const email = new Notifications(scope, 'email', {
  fromAddress: 'noreply@example.com',
});

export const api = new ApiNamespace(scope, 'api', () => ({
  async sendWelcomeEmail(userEmail: string) {
    try {
      return await email.sendEmail({
        to: userEmail,
        subject: 'Welcome!',
        body: 'Thanks for signing up.',
      });
    } catch (e) {
      if (isBlocksError(e, NotificationsErrors.InvalidRecipient)) {
        throw new ApiError('Enter a valid email address.', 400);
      }
      throw e;
    }
  },
}));
```

The same import resolves to the local entry during `npm run dev`, to the CDK entry during synth, and to the runtime entry in deployed compute.

## Testing your Block
<a name="custom-bb-testing"></a>

Test both the local and runtime implementations:
+  **Local implementation tests**: The scaffolded `npm test` runs the Node.js test runner on the compiled tests in `dist/`, so run `npm run build` first. Use a real `Scope` from `@aws-cdk-blocks/core` as the parent.
+  **Runtime tests**: Deploy to a sandbox and verify against real AWS services.
+  **Interface parity**: Ensure every entry accepts the same inputs and returns the same output shapes. `parity.test.ts` checks the error names.

```typescript
// src/index.test.ts
import { test } from 'node:test';
import assert from 'node:assert';
import { Scope, isBlocksError } from '@aws-cdk-blocks/core';
import { Notifications, NotificationsErrors } from './index.mock.js';

const parent = new Scope('test-app');

test('sendEmail returns a messageId', async () => {
  const email = new Notifications(parent, 'email', { fromAddress: 'noreply@example.com' });
  const result = await email.sendEmail({ to: 'user@example.com', subject: 'Test', body: 'Hello' });
  assert.ok(result.messageId);
});

test('sendEmail rejects a recipient that is not an email address', async () => {
  const email = new Notifications(parent, 'email-invalid', { fromAddress: 'noreply@example.com' });
  await assert.rejects(
    email.sendEmail({ to: 'not-an-address', subject: 'Test', body: 'Hello' }),
    (e) => isBlocksError(e, NotificationsErrors.InvalidRecipient),
  );
});
```

## Publishing
<a name="custom-bb-publishing"></a>

To share your CDK Block:
+  **Within a monorepo**: Reference it as a workspace dependency. No publishing needed.
+  **Within your organization**: Publish to a private npm registry (such as AWS CodeArtifact).
+  **Publicly**: Publish to the npm public registry. Keep the `aws-blocks` keyword that the scaffolder adds so people can find your CDK Block.

Include a `README.md` with usage examples, API documentation, and information about the AWS resources provisioned. Coding agents use this documentation to help app teams integrate your CDK Block.

## Best practices for custom CDK Blocks
<a name="custom-bb-best-practices"></a>
+  **Keep the interface identical** across entries. Consumers shouldn’t need to know which implementation is active. In the CDK entry, every runtime method is a `synthGuard` stub.
+  **Document local implementation limitations**: If the local implementation doesn’t replicate all production behavior (such as DynamoDB query limits), document the differences.
+  **Use `getMockDataDir(this)` ** for persistent local data. It follows the `.bb-data/<fullId>/` convention, where `fullId` joins the IDs of the CDK Block and its parent scopes with `-`.
+  **Throw named errors** with `blocksError()` so callers can match them by name.
+  **Minimize client middleware**: Only add it when a method returns a live object. Most CDK Blocks don’t need any.
+  **Keep every entry**: Don’t drop an entry from the export map. The browser entry can be a stub that exports types and error names.
+  **Share types in a separate file**: This ensures type consistency across all implementations.
