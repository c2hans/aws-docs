---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/security.html
---

# Security in AWS CDK Blocks

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](http://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security *of* the cloud and security *in* the cloud:
+  **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](http://aws.amazon.com/compliance/programs/). AWS CDK Blocks is a framework that you install from npm. It runs in your build and in your AWS account, so compliance coverage comes from the AWS services that it provisions for your app. To learn which compliance programs apply to those services, see [AWS Services in Scope by Compliance Program](http://aws.amazon.com/compliance/services-in-scope/).
+  **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations.

This documentation helps you understand how to apply the shared responsibility model when using CDK Blocks.

## How CDK Blocks manages permissions
<a name="security-permissions"></a>

CDK Blocks configures IAM permissions for the resources your application uses. When you create a CDK Block, it grants access to its own resource on one IAM role, the execution role.

All compute in a `BlocksStack` or `BlocksBackend` runs as this one role. That includes the default API function, every `Compute` you create, and the handlers for queues, schedules, and WebSocket connections. A `Compute` that runs one `ApiNamespace` or a whole `Scope` gets its own function, memory, and scaling, but it still runs as the shared role. If you move code to its own `Compute`, that code can still reach the same resources.

Because the role is shared, every API method in the stack can reach the resources of every CDK Block in the stack, not only the CDK Blocks it uses. To keep two workloads from reaching each other’s data, deploy them as separate stacks, or in separate AWS accounts.

Most grants are scoped to the CDK Block’s own resource, but they allow more actions than the CDK Block calls. `EmailClient`, secret `AppSetting`, and existing database `Database` grants are wider, as the table shows. The following table lists the grants for common CDK Blocks.

| Block | Actions granted to the execution role | Resource |
| --- | --- | --- |
|  `KVStore`  |  `dynamodb:GetItem`, `BatchGetItem`, `Query`, `Scan`, `ConditionCheckItem`, `PutItem`, `UpdateItem`, `DeleteItem`, `BatchWriteItem`, `DescribeTable`, `GetRecords`, `GetShardIterator`. With a customer managed key, also the KMS actions to use that key. | The table, and `dynamodb:Query` on its indexes |
|  `FileBucket`  |  `s3:GetObject*`, `s3:PutObject`, `s3:PutObjectTagging`, `s3:PutObjectVersionTagging`, `s3:PutObjectRetention`, `s3:PutObjectLegalHold`, `s3:DeleteObject*`, `s3:List*`, `s3:GetBucket*`, `s3:Abort*`. With a KMS key, also the KMS actions to use that key. | The bucket and its objects |
|  `Database`  |  `dsql:DbConnect` on a `dsql` cluster, or `rds-db:connect` on an `aurora` cluster. The role connects as a database role that can only read and write data. On an existing database with `DatabaseCluster.fromExisting({ name })`, `ssm:GetParameter` instead, plus `kms:Decrypt` on any key for calls through SSM. | The cluster, the app’s database role on an `aurora` cluster, or the parameter that holds the connection string |
|  `Secret`  |  `secretsmanager:GetSecretValue`, `DescribeSecret`, `ListSecretVersionIds`. With `allowRuntimeWrite: true`, also `PutSecretValue`, `UpdateSecret`, and `UpdateSecretVersionStage`. | The secret |
|  `AppSetting`  |  `ssm:GetParameter` and `ssm:PutParameter`. With `secret: true`, also `kms:Decrypt` and `kms:Encrypt`. | The parameter. KMS access is limited to calls made through Parameter Store, or to your key if you set `kmsKeyArn`. |
|  `EmailClient`  |  `ses:SendEmail`, `ses:SendBulkEmail`  | All Amazon Simple Email Service (Amazon SES) identities and configuration sets in the account |
|  `AsyncJob`  |  `sqs:SendMessage`, `ReceiveMessage`, `DeleteMessage`, `ChangeMessageVisibility`, `GetQueueAttributes`, `GetQueueUrl`  | The job’s queue |

The role also has the `AWSLambdaBasicExecutionRole` managed policy and read access to the app’s configuration file in Amazon S3. Authentication, `Realtime`, `Agent`, `KnowledgeBase`, and other CDK Blocks add their grants to the same role. `CronJob` invokes your compute through its own scheduler role.

 **See the full policy**
Every `cdk synth` writes a report of the execution role to `cdk.out/<stackName>.blocks-iam.json`, or `cdk.out/<stackName>.<backendId>.blocks-iam.json` for a `BlocksBackend` inside your own stack. The report lists every statement on the role, the CDK Blocks that own the resources each statement references (empty when it names only literal ARNs or `*`), the managed policies, the permissions boundary, and every IAM role that CDK Blocks created. It is not deployed. The file is sorted, so a CI step can compare it with the previous build and fail when permissions grow.

```bash
npx cdk synth --quiet
jq '.executionRole.statements[] | {actions, blocks}' cdk.out/my-app.blocks-iam.json
```

 **Grant access to your own resources**
You don’t need to write IAM policies for CDK Block resources. If you add your own CDK resources in the CDK layer, you grant their permissions yourself. Grant them to `stack.executionRole`, where `stack` is the stack that `BlocksStack.create(…​)` returns (`blocksStack` in the project templates). Pass the resource’s name or ARN to your code with `registerConfig`. Every compute reads it from `process.env` at startup.

```typescript
// cdk-blocks/index.cdk.ts
import * as sns from 'aws-cdk-lib/aws-sns';
import { registerConfig } from 'aws-cdk-blocks/cdk';

const topic = new sns.Topic(blocksStack, 'Alerts');
topic.grantPublish(blocksStack.executionRole);
registerConfig(blocksStack, 'ALERTS_TOPIC_ARN', topic.topicArn);
```
In your backend code, read the ARN with `process.env.ALERTS_TOPIC_ARN`.

 **Cap every role with a permissions boundary**
Set `defaults.permissionsBoundary` to attach an IAM permissions boundary to every role that CDK Blocks creates. This covers the execution role, the helper roles that CDK Blocks create, the CDK custom resource roles, and the roles that `Hosting` creates. A boundary is a ceiling, not a grant. The role’s effective permissions are what both its policies and the boundary allow. Pass a policy name, a full policy ARN (needed when the policy has a path), or an `iam.IManagedPolicy`.
The examples on this page keep the template’s preset choice, `sandboxMode ? BlocksPresets.sandbox : BlocksPresets.production`, and add settings to it. If you spread `BlocksPresets.production` alone, sandboxes also get production settings, such as no `localhost` CORS origins and retained resources.

```typescript
// cdk-blocks/index.cdk.ts
export const blocksStack = await BlocksStack.create(app, stackName, {
  backendHandlerPath: join(__dirname, 'index.handler.ts'),
  backendCDKPath: join(__dirname, 'index.ts'),
  defaults: { ...(sandboxMode ? BlocksPresets.sandbox : BlocksPresets.production), permissionsBoundary: 'my-app-boundary' },
});
```
A boundary limits the shared role, but it does not split it. Every handler still runs as the same role.

## Authentication
<a name="security-authentication"></a>

CDK Blocks provides the `Auth` Block to handle user identity. Sessions are kept server side and sent as HTTP-only cookies. Signing out deletes the session, and a password reset ends every session the user had.

 **Default store**
Uses an Amazon Cognito user pool. Supports email and password sign-in, multi-factor authentication (MFA) with SMS, TOTP, or email codes, passkeys, user groups, and account recovery flows. Email codes need an Amazon Simple Email Service (Amazon SES) sender, set with the `email` option. Social, SAML, and OIDC providers sign in through Cognito, and each user becomes a user pool user.

 ** `store: 'builtin'` **
Creates no user pool. Your backend verifies each OIDC or OAuth 2.0 sign-in itself and keeps only the session.

For more information, see [Authentication](bb-authentication.md).

 **Best practices:**
+ Define namespaces that hold signed-in methods with `auth.protect`, so a forgotten or unawaited guard can’t leave a method open.
+ Every `ApiNamespace` method is a public endpoint until it calls `requireAuth`. The local implementation applies no authentication, so a method that you forget to protect passes every local check. Call `auth.requireAuth(context)` server-side in every API method that accesses user data. Never trust client-side authentication alone.
+ Scope data access by `user.userSub` to prevent unauthorized cross-user access. It stays the same for the user’s lifetime.
+ Mark attributes that you use for authorization, such as a role or tenant ID, with `userWritable: false`, so end users can’t write them.
+ Set `removalPolicy: 'retain'` on any `Auth` Block whose user pool holds real users.

## Data protection
<a name="security-data-protection"></a>

CDK Blocks uses the following data protection mechanisms:

 **Encryption at rest**
CDK Blocks encrypt stored data at rest as follows:
+  `KVStore`: DynamoDB encryption with the AWS managed key `aws/dynamodb`. Set `encryption: 'customer-managed'` to create a customer managed key for the table, or set `encryption: KVStore.fromKmsKey(keyArn)` to use a key that you already own.
+  `FileBucket`: S3 server-side encryption with Amazon S3 managed keys (SSE-S3). The same `encryption` option selects a KMS key instead. `FileBucket` also blocks all public access and rejects requests that do not use TLS. For records that must not change, set `objectLock: { mode, retentionDays }`. To log requests to a bucket, set `accessLogging: true` on the bucket, or `defaults.storageAccessLogging: true` for every bucket in the stack.
+  `Database`: Aurora DSQL encryption with an AWS owned key on a `dsql` cluster. An `aurora` cluster also encrypts its storage with an AWS owned key, because the express configuration accepts no customer managed KMS key. An existing database keeps the encryption that you configured for it.
+  `Secret`: AWS Secrets Manager encryption with the `aws/secretsmanager` key. `AppSetting` with `secret: true`: Parameter Store SecureString with the `aws/ssm` key, or your key if you set `kmsKeyArn`.

 **Encryption in transit**
All communication between your application and AWS services uses TLS. API Gateway endpoints use HTTPS exclusively.

 **Local development**
During local development, data is stored unencrypted in the `.bb-data/` directory on your machine. This includes the values of `Secret` and secret `AppSetting` Blocks. This directory should be added to `.gitignore` (which CDK Blocks does by default) and should not contain production data.

## Network security
<a name="security-network"></a>

By default, CDK Blocks deploys your API behind Amazon API Gateway, which provides:
+ HTTPS-only endpoints (HTTP is not supported)
+ DDoS protection via AWS Shield Standard
+ Request throttling, which CDK Blocks turns on for the backend API stage and the `Realtime` WebSocket stage. For more information, see [API protection](#security-api-protection).
 **Front door**
The `apiFrontDoor` option on `BlocksStack.create` or `BlocksBackend.create` sets how clients reach the API. With `'apigateway'` (the default), clients call the API Gateway endpoint directly. With `'cloudfront'`, CDK Blocks puts an Amazon CloudFront distribution in front of the API. Either way, clients should call `publicApiUrl`, which is also the `ApiUrl` stack output. When you pass the backend to `Hosting`, the browser reaches the API on the same origin through the hosting front door, except with `frontDoor: 'none'`, where it calls the API cross-origin. Neither option makes CloudFront the only way in: the API Gateway `execute-api` URL stays reachable. Changing the option later changes the API’s domain and signs out every user, so choose it before you have real users.
 **Web application firewall**
 AWS WAF is off by default. Set `apiWaf: { enabled: true }` to create a web ACL with the AWS managed Common and Known Bad Inputs rule groups and a rate limit for each IP address (`rateLimit`, default 1000 requests in 5 minutes). Or pass `apiWaf: { webAclArn }` to attach a web ACL that you already have. Under `apiFrontDoor: 'cloudfront'`, the web ACL must be in `us-east-1`, so outside that Region pass `webAclArn`. `apiWaf` does not cover the `Realtime` WebSocket API. Browser traffic that arrives through `Hosting` is not rate limited by `apiWaf`; turn on the WAF of the hosting front door for that. When `Hosting’s CloudFront distribution serves the API under `apiFrontDoor: 'cloudfront'`, `apiWaf` creates no web ACL at all, and `cdk synth` warns about it.
 **Access logs**
API Gateway access logging is off in both presets, and `cdk synth` warns about this for the production preset. Turn it on with `defaults.accessLogging: true`. It sets the API Gateway logging role, which the whole account shares in each Region, so turn it on for only one CDK Blocks stack per Region. The same setting also turns on Amazon S3 server access logs for every `FileBucket`, each with its own log bucket. To keep those off, also set `defaults.storageAccessLogging: false`. The following example turns on access logs and the WAF.

  ```typescript
  // cdk-blocks/index.cdk.ts
  export const blocksStack = await BlocksStack.create(app, stackName, {
    backendHandlerPath: join(__dirname, 'index.handler.ts'),
    backendCDKPath: join(__dirname, 'index.ts'),
    defaults: { ...(sandboxMode ? BlocksPresets.sandbox : BlocksPresets.production), accessLogging: true },
    apiWaf: { enabled: true, rateLimit: 2000 },
  });
  ```
 **VPC**
For additional network isolation, place your compute in a virtual private cloud (VPC) with `defaults.vpc`. CDK Blocks puts your compute functions in the VPC’s private subnets, creates the VPC endpoints that your CDK Blocks need, and wires the security groups. A VPC adds cost, such as network address translation (NAT) gateways and interface endpoints, so use one only when you need it.

  ```typescript
  // cdk-blocks/index.cdk.ts (the template already imports cdk)
  import * as ec2 from 'aws-cdk-lib/aws-ec2';

  // A VPC must live in a stack. Create it in a small network stack.
  const network = new cdk.Stack(app, `${stackName}-network`);
  const vpc = new ec2.Vpc(network, 'AppVpc', { maxAzs: 2, natGateways: 1 });

  export const blocksStack = await BlocksStack.create(app, stackName, {
    backendHandlerPath: join(__dirname, 'index.handler.ts'),
    backendCDKPath: join(__dirname, 'index.ts'),
    defaults: { ...(sandboxMode ? BlocksPresets.sandbox : BlocksPresets.production), vpc: { network: vpc } },
  });
  ```

## API protection
<a name="security-api-protection"></a>

 **Input validation**
Always validate inputs in your API methods. CDK Blocks does not perform automatic input validation. Your API methods receive whatever the client sends. To reject bad input, throw `ApiError(message, 400)`. A plain `Error` thrown in an API method reaches the client as a nameless error with status 500 and the message "Internal error", so your message is lost. To let the frontend check for a specific error, pass a name, as in `new ApiError(message, 404, { name: 'NotFoundError' })`, and check it with `isBlocksError` from `aws-cdk-blocks/client`.

```typescript
// cdk-blocks/index.ts
import { ApiNamespace, ApiError } from 'aws-cdk-blocks';

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async createItem(title: string) {
    if (!title || title.length > 200) {
      throw new ApiError('Title must be 1-200 characters', 400);
    }
    // ...
    return { title };
  },
}));
```

 **Rate limiting**
CDK Blocks sets throttling on the backend API stage and the `Realtime` WebSocket stage from `defaults.throttling`. The API Gateway front doors that `Hosting` creates do not get these limits. The production preset allows 1,000 requests per second with a burst of 2,000. The sandbox preset allows 200 with a burst of 400. To change the limits, override `throttling`, as shown in the following example. For a limit on each client, use the rate rule in `apiWaf`.

 **CORS**
Your API accepts cross-origin requests only from the origins in `defaults.allowedOrigins`, plus the hosting front door’s origin when you use `Hosting`. Each entry in `allowedOrigins` is a regular expression, so escape the dots. The production preset lists no origins. The sandbox preset allows `localhost` and `127.0.0.1`, so a local frontend can call a deployed sandbox. With `Hosting`, browser calls through the hosting front door use the same origin, so you don’t need to configure CORS. If you host your frontend somewhere else, add its origin.

```typescript
// cdk-blocks/index.cdk.ts
export const blocksStack = await BlocksStack.create(app, stackName, {
  backendHandlerPath: join(__dirname, 'index.handler.ts'),
  backendCDKPath: join(__dirname, 'index.ts'),
  defaults: {
    ...(sandboxMode ? BlocksPresets.sandbox : BlocksPresets.production),
    throttling: { rateLimit: 2000, burstLimit: 4000 },
    allowedOrigins: ['https://app\\.example\\.com'],
  },
});
```

## Managing secrets
<a name="security-secrets"></a>

Don’t hardcode secrets (API keys, database passwords, third-party tokens) in your source code. Don’t put them in Lambda environment variables or in `registerConfig` either. Anyone who can read the function’s configuration, or the app’s configuration file, can read those values. Store production secrets in the `Secret` Block. Each `Secret` is one AWS Secrets Manager secret, and your code reads it when it needs the value.

```typescript
// cdk-blocks/index.ts
import { ApiNamespace, ApiError, Scope, Secret } from 'aws-cdk-blocks';

const scope = new Scope('my-app');
const paymentKey = new Secret(scope, 'payment-api-key');

export const api = new ApiNamespace(scope, 'api', (context) => ({
  async charge(amount: number) {
    const key = await paymentKey.get();
    if (key === null) {
      throw new ApiError('Payments are not configured', 503);
    }
    // Call the payment provider with key ...
    return { charged: amount };
  },
}));
```

A `Secret` is read-only at runtime by default. The object has no `put()` method, and the execution role can only read the secret. `get()` returns `null` until a value is set. Set the value outside your app: from your stack’s settings resource group in the AWS Resource Groups console, which the app’s `/aws-blocks/settings` route opens, or with `aws secretsmanager put-secret-value`. The default name comes from the stack and CDK Block IDs, so the CLI works without a `name`. Set `name` if you want one that does not depend on them. Your app reads a new value within 5 minutes, or the time you set with `cacheTtlSeconds`.

If your app sets or rotates the value itself, pass `allowRuntimeWrite: true`. Then `put()` is available and the role can write the secret:

```typescript
const token = new Secret(scope, 'service-token', { allowRuntimeWrite: true });
await token.put('new-value');
```

For a random value that only your app uses, such as a signing key, pass `generate: true`.

 `AppSetting` with `secret: true` stores the value as a Parameter Store SecureString. It is a free fallback for a secret of little value in a prototype. For any secret that protects a production app, use `Secret`.

## Least privilege for deployment
<a name="security-least-privilege"></a>

The IAM user or role that deploys your CDK Blocks application needs permissions to create and manage the underlying resources (Lambda, DynamoDB, API Gateway, CloudFormation, etc.). We recommend:
+ Use a dedicated deployment role with scoped permissions.
+ Don’t deploy with your personal administrator credentials in production.
+ Use CI/CD pipelines with OIDC-based authentication (no long-lived access keys).
+ If your deployment role requires a permissions boundary on every role it creates, set `defaults.permissionsBoundary`. For more information, see [How CDK Blocks manages permissions](#security-permissions).
