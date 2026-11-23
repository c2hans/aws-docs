---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/existing-apps.html
---

# CDK Blocks for existing apps

You can add CDK Blocks to an application that already exists. Each CDK Block packages a capability’s infrastructure as a CDK Construct, the code your app uses to call it, and a local implementation. Your existing app keeps its frontend, its hosting, and the resources it already has, and the CDK Blocks you add deploy to your own AWS account next to them.

This page covers two kinds of existing apps:
+  [AWS Amplify Gen 2 apps](#existing-apps-amplify-gen2)
+  [Existing AWS CDK apps](#existing-apps-cdk)

For pre-deployed resources and other infrastructure patterns, see [Integrating with existing infrastructure](existing-infrastructure.md).

## AWS Amplify Gen 2 apps
<a name="existing-apps-amplify-gen2"></a>

To add CDK Blocks to an Amplify Gen 2 app, run the project creation command from the root of the app:

```bash
npm create @aws-cdk-blocks/blocks-app@latest
```

The command looks for `amplify/backend.ts`. When it finds that file, it treats the directory as an Amplify Gen 2 project and selects the `amplify` template. You can’t choose this template for a new app. The command lists the changes it will make and asks you to confirm. It doesn’t commit anything, so you can review the diff first.

### What the command adds
<a name="existing-apps-amplify-gen2-changes"></a>

| File | Change |
| --- | --- |
|  `cdk-blocks/`  | A new workspace for your CDK Blocks backend. `index.ts` defines a sample API, `index.cdk.ts` creates the CDK Blocks backend, `client.js` is the frontend client, and `cognito-verifier.ts` checks the sign-in tokens of your Amplify users. |
|  `amplify/blocks.ts`  | A new file that adds the CDK Blocks backend to your Amplify backend. |
|  `amplify/backend.ts`  | Exports `backend` and calls `initBlocks(backend)` at the end of the file. If the command can’t change the file, it writes the lines to `amplify/blocks-manual-patch.txt` for you to add. |
|  `package.json`  | Adds `cdk-blocks` to `workspaces`, adds dependencies, and adds the scripts in the next section. Existing scripts with the same name are kept. |
|  `.gitignore`  | Adds the local data directory `.bb-data/` and other CDK Blocks entries. |
|  `amplify.yml`  | Adds `export NODE_OPTIONS="--conditions=cdk"` before `npx ampx pipeline-deploy`. If the file doesn’t exist, the command creates one. Check its `frontend` settings, such as `baseDirectory`, against your build. |

The two lines added to `amplify/backend.ts` are:

```typescript
import { initBlocks } from './blocks.js';
await initBlocks(backend);
```

 `initBlocks` does the following:

1. Creates a stack for CDK Blocks with `backend.createStack('blocks')`.

1. Creates a `BlocksBackend` in that stack. It uses `BlocksPresets.sandbox` when `AMPLIFY_SANDBOX` is `true` and `BlocksPresets.production` otherwise.

1. If the app has Amplify auth, passes the user pool ID, the app client ID, and the Region to the CDK Blocks runtime as `COGNITO_USER_POOL_ID`, `COGNITO_CLIENT_ID`, and `COGNITO_REGION`.

1. Adds the CDK Blocks API URL to `amplify_outputs.json` as `custom.blocks_api_url`.

### Calling the API with Amplify sign-in
<a name="existing-apps-amplify-gen2-auth"></a>

The generated `client.js` reads the API URL from `amplify_outputs.json`. Before each call, it gets the signed-in user’s ID token from Amplify Auth and sends it as a bearer token. On the backend, `CognitoVerifier` checks that token. Methods that don’t call it stay public.

```typescript
// cdk-blocks/index.ts
const auth = new CognitoVerifier({
  userPoolId: process.env.COGNITO_USER_POOL_ID!,
  clientId: process.env.COGNITO_CLIENT_ID!,
  tokenUse: 'id',
});

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async putNote(key: string, value: string) {
    const user = await auth.requireAuth(context);
    await store.put(`${user.sub}:${key}`, value);
    return { success: true };
  },
}));
```

 `requireAuth` returns the user, or responds with a 401 `NotAuthenticatedException` error when the token is missing or not valid. `requireRole(context, group)` also responds with a 403 `NotAuthorizedException` error when the token’s groups don’t include the group. These are the error names that the `Auth` Block uses. In your frontend, import the API from the workspace:

```typescript
import { api } from 'cdk-blocks';
const result = await api.greet('World');
```

When you add a namespace or a method, run `npm run blocks:generate-client` to update `client.js`.

### Running and deploying
<a name="existing-apps-amplify-gen2-run"></a>

| Command | What it does |
| --- | --- |
|  `npm run blocks:dev`  | Serves the CDK Blocks API on `http://localhost:3001` with each CDK Block’s local implementation. |
|  `npm run blocks:stop`  | Stops the local server. |
|  `npm run sandbox`  | Runs `ampx sandbox`, which deploys your Amplify backend and the CDK Blocks stack to a sandbox. |
|  `npm run sandbox:delete`  | Deletes the sandbox. |

CDK Blocks doesn’t add an `npm run dev` script to an Amplify project. Amplify Hosting deploys production through `amplify.yml`, which runs `npx ampx pipeline-deploy` with the `cdk` condition set. Without that condition, CDK Block imports resolve to their local implementations and create no infrastructure.

To add more CDK Blocks, declare them in `cdk-blocks/index.ts`. For the list of CDK Blocks, see [CDK Blocks reference](building-blocks-reference.md).

## Existing AWS CDK apps
<a name="existing-apps-cdk"></a>

A CDK Block is a CDK Construct, so you can add CDK Blocks to an existing CDK app. Use the `BlocksBackend` construct to put CDK Blocks inside a stack you already have, next to your other resources. To keep CDK Blocks in its own stack, use `BlocksStack`.

```typescript
const blocks = await BlocksBackend.create(stack, 'BlocksApi', {
  backendHandlerPath: './cdk-blocks/index.handler.ts',
  backendCDKPath: './cdk-blocks/index.ts',
  defaults: BlocksPresets.production,
});

topic.grantPublish(blocks.executionRole);
registerConfig(blocks, 'ALERTS_TOPIC_ARN', topic.topicArn);
```

 `BlocksBackend.create()` is asynchronous, so call it from a static factory method on your stack. Grant your existing resources to `blocks.executionRole`, the IAM role that all CDK Blocks compute in the app shares. Pass values such as ARNs to your code with `registerConfig`. Run synth with the `cdk` condition, for example `NODE_OPTIONS="--conditions=cdk" npx cdk synth`. For the full example, see [Pattern 1: CDK in CDK Blocks](existing-infrastructure.md#existing-cdk-in-blocks).

To create the `cdk-blocks/` workspace, you can run `npm create @aws-cdk-blocks/blocks-app@latest` in the root of the CDK app. In a project that has a `package.json` and no `amplify/backend.ts`, the command adds the workspace, dependencies, and scripts. If `cdk.json` already exists, the command leaves it unchanged.

To use a CDK Block with a resource your CDK app already deploys, such as an existing table or bucket, see [Pattern 2: fromExisting](existing-infrastructure.md#existing-from-existing). To compare CDK Blocks with plain CDK Constructs, see [Choosing AWS CDK Blocks](choosing-blocks.md).

## Related resources
<a name="existing-apps-related"></a>
+  [Integrating with existing infrastructure](existing-infrastructure.md)
+  [Choosing AWS CDK Blocks](choosing-blocks.md)
+  [Local development](local-development.md)
+  [Deploy your application to AWS](deploy-to-aws.md)
+  [CLI reference](cli-reference.md)
