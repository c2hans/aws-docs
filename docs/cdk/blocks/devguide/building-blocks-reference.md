---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/building-blocks-reference.html
---

# CDK Blocks reference

 AWS CDK Blocks ships with built-in CDK Blocks covering authentication, data storage, realtime messaging, AI, observability, and more. Each CDK Block provides a typed API, automatic resource provisioning, and a local implementation for offline development.

Import CDK Blocks from `aws-cdk-blocks`. Each entry below also names the package that contains the CDK Block, which has its own README.

For more information about source code and advanced configuration, see [CDK Blocks on GitHub](https://github.com/aws/cdk-blocks).

## Authentication
<a name="authentication"></a>

A CDK Block for user identity and session management.
+  **Auth** (`@aws-cdk-blocks/bb-auth`): Email and password sign-in backed by an Amazon Cognito user pool, with multi-factor authentication (MFA), groups, and passkeys. Social, SAML, and OIDC providers go in one `providers` record. With `store: 'builtin'`, your backend verifies OIDC and OAuth 2.0 sign-ins without a user pool, and `stubIdp()` gives you an offline identity provider for development. `Auth` replaces `AuthBasic`, `AuthCognito`, and `AuthOIDC`.

For more information, see [Authentication](bb-authentication.md).

## Data storage
<a name="data-storage"></a>

CDK Blocks for persisting and retrieving data.
+  **KVStore** (`@aws-cdk-blocks/bb-kv-store`): Key-value and document storage backed by DynamoDB, with schema validation, composite keys, and secondary indexes. Use for caches, session stores, and app records that you list or query. For feature flags, use AppSetting.
+  **Database** (`@aws-cdk-blocks/bb-database`): SQL on PostgreSQL with migrations, transactions, and a Kysely dialect. It runs on Amazon Aurora DSQL by default, or on Aurora PostgreSQL Serverless v2 for Row Level Security and the rest of PostgreSQL. Use for relational data.
+  **FileBucket** (`@aws-cdk-blocks/bb-file-bucket`): File storage for uploads and downloads with presigned URLs. Use for user-generated content.

For more information, see [Data storage](bb-data-storage.md).

## Realtime and async
<a name="realtime-and-async"></a>

CDK Blocks for realtime communication and background processing.
+  **Realtime** (`@aws-cdk-blocks/bb-realtime`): Typed WebSocket pub/sub channels. Use for live updates, chat, and notifications.
+  **AsyncJob** (`@aws-cdk-blocks/bb-async-job`): Background work via Amazon SQS, with retries and a dead-letter queue. Jobs are fire-and-forget by default. Set `trackStatus: true` to read each job’s status with `getStatus()` or `waitUntilComplete()`. Use for tasks that don’t need immediate results.
+  **CronJob** (`@aws-cdk-blocks/bb-cron-job`): Scheduled task execution via an Amazon EventBridge Scheduler schedule. Use for periodic maintenance and batch processing.
+  **Compute** (`@aws-cdk-blocks/bb-compute`): Choose where a workload runs. A `serverless` compute runs on AWS Lambda, and a `container` compute runs on AWS Fargate. Pass it as the `compute` option of an `ApiNamespace`, `AsyncJob`, `CronJob`, or `Scope`, each of which runs on either compute type. `Realtime` and `RawRoute` always stay on the app’s default compute, including inside a container `Scope`. Workloads without one use the app’s default serverless compute.

For more information, see [Realtime and async](bb-realtime-async.md).

## AI
<a name="ai"></a>

CDK Blocks for AI capabilities.
+  **Agent** (`@aws-cdk-blocks/bb-agent`): AI agent with streaming, tool calling, human-in-the-loop (HITL) approval, and conversation persistence. Locally, uses a canned keyword-based provider (no real model needed). On AWS, the agent loop runs on an Amazon Bedrock AgentCore Runtime, which is billed for vCPU and memory while a session runs. It streams to clients over a `Realtime` WebSocket. The default model is `BedrockModels.BALANCED`, called through a global inference profile.
+  **KnowledgeBase** (`@aws-cdk-blocks/bb-knowledge-base`): Semantic document retrieval via Amazon Bedrock Knowledge Bases. Use for RAG and contextual search.

For more information, see [AI](bb-ai.md).

## Communication
<a name="communication"></a>

CDK Blocks for sending messages to users.
+  **EmailClient** (`@aws-cdk-blocks/bb-email-client`): Transactional email sending via Amazon SES. Locally, captures emails for testing.

For more information, see [Communication](bb-communication.md).

## Configuration
<a name="configuration"></a>

CDK Blocks for application settings and secrets.
+  **AppSetting** (`@aws-cdk-blocks/bb-app-setting`): A single configuration value that is not sensitive, backed by SSM Parameter Store. Use for feature flags and runtime config for the whole app. Don’t use it for API keys or other production secrets.
+  **Secret** (`@aws-cdk-blocks/bb-secret`): A single application secret backed by AWS Secrets Manager, such as an API key or a connection string. It keeps the previous version and can wrap an existing secret with `Secret.fromExisting(arn)`. A `Secret` is read-only at runtime by default; set `allowRuntimeWrite: true` to add `put()`.

For more information, see [Configuration](bb-configuration.md).

## Observability
<a name="observability"></a>

CDK Blocks for monitoring, logging, and tracing.
+  **Metrics** (`@aws-cdk-blocks/bb-metrics`): Custom application metrics via CloudWatch Embedded Metric Format.
+  **Logger** (`@aws-cdk-blocks/bb-logger`): Structured JSON logging with levels and contextual metadata.
+  **Tracer** (`@aws-cdk-blocks/bb-tracer`): Distributed tracing via AWS X-Ray.
+  **Dashboard** (`@aws-cdk-blocks/bb-dashboard`): A CloudWatch dashboard organized by compute. Each compute gets health and logs sections, plus traces when the app has a Tracer. Metric widgets appear for the metrics you list in `metricConfigs`. It works without Metrics or Logger.

For more information, see [Observability](bb-observability.md).

## Hosting
<a name="hosting"></a>

Frontend deployment (CDK layer only, import from `aws-cdk-blocks/cdk`).
+  **Hosting** (`aws-cdk-blocks/cdk`, built on `@aws-cdk-blocks/hosting`): Frontend deployment with SSR support. Auto-detects framework (Next.js, Nuxt, Astro, SPA).

For more information, see [Hosting](bb-hosting.md).
