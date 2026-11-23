---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/deploy-to-aws.html
---

# Deploy your application to AWS

After developing and testing your application locally, you can deploy it to AWS. This page covers the one-time AWS account setup and the deployment commands.

## Setting up AWS credentials
<a name="deploy-aws-account"></a>

If you already have AWS credentials configured, skip to [Bootstrap the AWS CDK](#deploy-aws-cdk-bootstrap).

### Sign up for an AWS account
<a name="deploy-aws-sign-up"></a>

If you don’t already have an AWS account, complete the following steps to create one.

1. Open https://portal.aws.amazon.com/billing/signup.

1. Follow the online instructions.

   Part of the sign-up procedure involves receiving a phone call and entering a verification code on the phone keypad.

   When you sign up for an AWS account, an * AWS account root user* is created. The root user has access to all AWS services and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](https://docs.aws.amazon.com/accounts/latest/reference/root-user-tasks.html).

### Create a user with administrative access
<a name="deploy-aws-iam"></a>

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam/) as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

1. Enable IAM Identity Center.

   For more information about enabling IAM Identity Center, see [Enabling AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html) in the * AWS IAM Identity Center User Guide*.

1. In IAM Identity Center, grant administrative access to a user.

   For more information about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/quick-start-default-idc.html) in the * AWS IAM Identity Center User Guide*.
**Note**
Administrative access is recommended for getting started. For production environments, use a least-privilege IAM policy scoped to only the resources that AWS CDK Blocks creates.

### Install and configure the AWS CLI
<a name="deploy-aws-cli"></a>

1. Install the AWS CLI version 2. For more information about installing the AWS CLI, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

1. Configure the AWS CLI with your credentials. For more information about configuring the AWS CLI, see [Configuring the AWS CLI to use IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html).

1. Verify your configuration by running the following command:

   ```bash
   aws sts get-caller-identity
   ```

   This command should return your account ID, user ID, and ARN.

 `npm run sandbox` and `npm run deploy` deploy with the same credentials that the CDK uses. Before they deploy, they print the deployment target: the credentials (an AWS profile or access keys from the environment) and the Region. The Region comes from `cdk.json` (or `~/.cdk.json`), the `AWS_REGION` or `AWS_DEFAULT_REGION` environment variable, or your profile. Check this line before each deploy.

### Bootstrap the AWS CDK
<a name="deploy-aws-cdk-bootstrap"></a>

CDK Blocks uses the AWS CDK to deploy infrastructure. You must bootstrap your AWS account before your first deployment.

From your project directory, run the following command, replacing `ACCOUNT_ID` and `REGION` with your values:

```bash
npx cdk bootstrap aws://ACCOUNT_ID/REGION --app=
```

For example:

```bash
npx cdk bootstrap aws://123456789012/us-east-1 --app=
```

The empty `--app=` option stops the CDK from synthesizing your app to find environments, because the command already names the account and Region.

You need to bootstrap only one time per account and Region combination. `npm run sandbox` and `npm run deploy` check this before they synthesize. If the account and Region are not bootstrapped, they stop and print the command to run.

Some apps also deploy a support stack in `us-east-1`, so bootstrap `us-east-1` in the same account too. This happens when the stack that holds `Hosting` uses the CloudFront front door with monitoring on (the default) and sets an explicit account and an explicit Region other than `us-east-1`, or when the app has a Lambda@Edge function (for example a Next.js route with `runtime = 'edge'`). The check that runs before a deploy covers only your app’s Region.

## Deploy to a sandbox
<a name="deploy-sandbox"></a>

A sandbox is your own temporary copy of the backend, for testing against real AWS services. To deploy your application to a sandbox, run the following command:

```bash
npm run sandbox
```

The sandbox:
+ Deploys the backend with a full CloudFormation deployment. The first deploy can take several minutes.
+ Then runs `cdk watch`. When you save a code change, it is hotswapped into the AWS Lambda function.
+ Starts the local dev server at `http://localhost:3000`. It serves your frontend locally and sends API calls to the deployed backend. Templates without a frontend (`backend`, `api-only`, and `sql`) start the server on port 3001 instead.
+ Uses real AWS services (DynamoDB, API Gateway, Lambda)
+ Gives each developer an isolated environment. The stack is named `<stackId>-<sandboxId>`. AWS CDK Blocks keeps the sandbox ID in `.cdk-blocks-sandbox/sandbox-id.txt`, which you don’t commit, so each machine gets its own stack.

 `cdk watch` hotswaps only code. It skips an infrastructure change, such as a new CDK Block or a changed CDK Block option, and prints a warning about changes that can’t be hotswapped. To deploy that change, stop the sandbox and run `npm run sandbox` again. Pressing  Ctrl C  stops only the local processes. Your AWS resources keep running until you destroy them.

The same code that ran locally now runs on AWS. CDK Blocks automatically resolve to their AWS implementations. `KVStore` becomes a DynamoDB table, `Auth` provisions an Amazon Cognito user pool, and `ApiNamespace` creates an API Gateway endpoint backed by a Lambda function.

Other sandbox commands:
+  `npm run sandbox:deploy` deploys the sandbox once and exits, with no `cdk watch` and no local dev server. Use it in scripts and CI.
+  `npm run sandbox:preview` deploys the sandbox with your frontend hosted in preview shape: served through an API Gateway HTTP API, with no CloudFront distribution. It prints the preview URL and exits. Running it again hotswaps a change that touches only backend code. A plain `npm run sandbox` or `npm run sandbox:deploy` removes the hosted preview (it prints a warning first), and the next preview gets a new URL. Templates without a frontend do not have this script.
+  `npm run sandbox:console` opens the CloudFormation console’s stack list, filtered to the stack from your last deploy. It uses the Region from `AWS_REGION`, `AWS_DEFAULT_REGION`, or your AWS CLI configuration, and `us-east-1` if none is set.

### Removing a sandbox
<a name="deploy-sandbox-destroy"></a>

To remove sandbox resources, run the following command:

```bash
npm run sandbox:destroy
```

This deletes every stack the sandbox deployed, including any support stack in `us-east-1`. A support stack that holds a Lambda@Edge function cannot be deleted for a few hours after its CloudFront distribution is gone. In that case the command says so; run `npm run sandbox:destroy` again later.

### Recover from a failed sandbox deploy
<a name="deploy-sandbox-recovery"></a>

The sandbox usually deploys with CloudFormation Express Mode, which turns off automatic rollback. (When an existing sandbox stack has a Lambda Web Function endpoint, the sandbox prints `Express Mode off for this deploy` and deploys with rollback instead.) A failed deploy leaves the stack in a failed state, and the next `npm run sandbox` cannot update it. To recover, destroy the sandbox and deploy again:

```bash
npm run sandbox:destroy
npm run sandbox
```

If `sandbox:destroy` reports that the stack is in `UPDATE_ROLLBACK_FAILED`, run the following command first, using your sandbox stack name:

```bash
aws cloudformation continue-update-rollback --stack-name <your-sandbox-stack>
```

## Full deployment
<a name="deploy-production"></a>

For a complete deployment including hosting, run the following command:

```bash
npm run deploy
```

This runs `cdk deploy --all`, a full CloudFormation deployment of every stack in your app. Most apps have one stack. The `us-east-1` support stack, if your app has one, deploys too. The deploy runs with `--require-approval never`, so the CDK does not stop to ask you to approve IAM or security group changes.

The production stack is named `<stackId>-prod`. The `stackId` comes from `.blocks/config.json`, which `npm create @aws-cdk-blocks/blocks-app` writes when it creates your project, for example `{ "stackId": "my-app-a1b2c3" }`. Commit this file. The command has no option for a stage or a stack name, so every `npm run deploy` to the same account and Region updates the same stack, whoever runs it. To deploy separate stages such as beta and prod, use a pipeline. For more information, see [Staged deployments with a pipeline](#deploy-pipeline).

When the deploy finishes, the command prints the API URL and the frontend URL. CloudFront can serve the previous frontend build for a short time after that. To wait until the new build is live, add `--wait-live`:

```bash
npm run deploy -- --wait-live
```

The command then waits up to 180 seconds for the new build. To change the limit, add `--wait-live-timeout=<seconds>` (1 to 3600). If the new build is not confirmed in time, the deploy has still succeeded, but the command exits with a nonzero code. `--wait-live` has no effect for an app without `Hosting`.

### Deleting the production stack
<a name="deploy-production-destroy"></a>

To delete the production stack, run the following command:

```bash
npm run destroy
```

The production preset keeps stateful resources such as tables and buckets (`RETAIN`), so they stay in your account after the stack is deleted. Retained buckets can still lose their objects: if a delete attempt fails, the command empties every bucket in every stack of the app before it retries. An `Auth` user pool follows the preset too, unless you set `removalPolicy` on the CDK Block. Set `removalPolicy: 'retain'` on any user pool that holds real users, so a stack that uses another preset keeps it as well.

**Warning**
 `npm run destroy` runs `cdk destroy` without `--all`. As a result, on an app with more than one top-level stack, such as an app with a `us-east-1` support stack for `Hosting`, the first attempt always fails. The command then empties the buckets in every stack before it retries, so you lose the objects in buckets the preset would keep. Even after the retries, the stacks are not deleted. For those apps, don’t run `npm run destroy`. Run `cdk destroy` with the stack names yourself.

### Running the CDK CLI yourself
<a name="deploy-cdk-condition"></a>

The npm scripts run your CDK app with the `cdk` export condition. `cdk.json` runs `npx tsx -C cdk cdk-blocks/index.cdk.ts`, and the scripts set `NODE_OPTIONS=--conditions=cdk`. If you run `cdk synth` or `cdk deploy` another way, or load your backend from an existing CDK app, set the condition yourself:

```bash
NODE_OPTIONS="--conditions=cdk" npx cdk synth
```

Without it, Node.js resolves each CDK Block to its local implementation instead of its CDK Construct, and `BlocksStack.create()` stops with a `Missing --conditions=cdk` error.

## Staged deployments with a pipeline
<a name="deploy-pipeline"></a>

To deploy to more than one stage, define a pipeline with the `Pipeline` construct from `aws-cdk-blocks/cdk`. It is built on `@aws-cdk-blocks/pipeline`, which you can also use on its own without the CDK Blocks secret and configuration defaults.

 `Pipeline` creates one self-mutating AWS CodePipeline for each branch. Each pipeline pulls your code from your source repository through an AWS CodeConnections connection and runs `cdk synth`. It updates itself when its own definition changes, then deploys each stage in order. A stage can target its own account and Region (`env`), wait for a manual approval (`requireApproval`), and wait for a bake time after it deploys (`bakeTime`). To deploy a stage to a different account than the pipeline, also set `crossAccountKeys: true`.

Create `cdk-blocks/pipeline.cdk.ts`:

```typescript
import * as cdk from 'aws-cdk-lib';
import { Pipeline } from 'aws-cdk-blocks/cdk';

const app = new cdk.App();

await Pipeline.create(app, 'MyAppPipeline', {
  appFile: './index.cdk.ts',
  source: {
    repo: 'my-org/my-app',
    connectionArn: 'arn:aws:codeconnections:us-east-1:111122223333:connection/EXAMPLE',
  },
  synth: {
    commands: ['npm ci', 'npx cdk synth --app "npx tsx -C cdk cdk-blocks/pipeline.cdk.ts"'],
  },
  branches: [
    {
      branch: 'main',
      stages: [
        { name: 'beta' },
        { name: 'prod', requireApproval: true },
      ],
    },
  ],
});
```

 `appFile` points at your app’s `index.cdk.ts`, relative to the pipeline file. The pipeline imports it once for each stage, and `BlocksStack.create()` adds the app’s stack to that stage. Each stage gets its own stack, named after the pipeline, branch, and stage, for example `MyAppPipeline-main-Stage-beta-<stackId>-prod`. The `synth` commands point `cdk synth` at the pipeline file, because `cdk.json` still points at `index.cdk.ts` for `npm run deploy`.

Before the first run:

1. Create a connection to your source repository provider in the AWS CodeConnections console and finish authorizing it. A new connection stays in `PENDING` status until you do.

1. Commit and push the pipeline file, `package-lock.json`, and `.blocks/config.json`.

1. Deploy the pipeline one time from your machine:

   ```bash
   npx cdk deploy --app "npx tsx -C cdk cdk-blocks/pipeline.cdk.ts"
   ```

After that, each push to `main` runs the pipeline. For more options, such as steps that run after a deploy and build secrets, see [pipeline package source](https://github.com/aws/cdk-blocks/tree/main/packages/pipeline).

## Next steps
<a name="deploy-next-steps"></a>
+ To configure custom domains, VPC settings, or other environment-specific infrastructure, see [The CDK layer](concepts.md#concepts-cdk-layer) in the Concepts topic.
+ To integrate CDK Blocks into an existing CDK application, see [Integrating with existing infrastructure](existing-infrastructure.md).
