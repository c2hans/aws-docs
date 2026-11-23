---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/what-is-blocks.html
---

# What is AWS CDK Blocks?

 AWS CDK Blocks is an expansion of the AWS Cloud Development Kit (CDK). Each CDK Block packages a CDK construct along with the connecting code applications need to use that infrastructure, incorporating AWS service-specific best practices and a local testing setup. AWS is releasing more than 17 CDK Blocks for common uses of AWS, including data storage and processing, background jobs, and building AI agents. Developers can build and test their applications locally and deploy the same code unchanged to their own AWS account.
+  [CDK Blocks reference](building-blocks-reference.md)
+  [Getting started with AWS CDK Blocks](getting-started.md)
+  [CLI reference](cli-reference.md)

Your entire application runs locally without an AWS account. When you’re ready, deploy the same code to AWS without changing anything.

## Why CDK Blocks
<a name="why-blocks"></a>

 **Your account, your infrastructure, and your standards**
Every app deploys as a standard CDK stack to your own AWS account. Set a CDK Block’s options, point it at an existing resource with `fromExisting`, change its infrastructure in the CDK layer, or copy its source into your project with `vendorize`. Add any CDK Construct next to the CDK Blocks.

 **Your standards as custom CDK Blocks**
Platform developers package their own standards as custom CDK Blocks and share them through npm, so app teams start from the same approved pattern.

 **Your whole app on your machine, and the same code on AWS **
Run one command to get a working application on your machine. You don’t need an AWS account until you’re ready to deploy.

 **End-to-end type safety**
Define your backend once. Your frontend types update on their own. TypeScript carries types from your database to your UI, and a TypeScript frontend calls the backend with no code generation step. For Swift, Kotlin, and Dart, you generate a client from a spec file.

 **Guidance for coding agents**
New projects include an `AGENTS.md` file with instructions for coding agents. Each CDK Block’s documentation ships in the npm package, under `node_modules/aws-cdk-blocks/docs/`. No plugins needed.

## CDK Blocks
<a name="building-blocks-overview"></a>

A CDK Block packages an app capability: a CDK Construct for its infrastructure, its runtime code, and a local implementation. Each CDK Block is an npm package. You import it and use it in your backend code.

The following table lists all available CDK Blocks.

### Data and storage
<a name="data-and-storage"></a>

| Block | Description |  AWS service |
| --- | --- | --- |
|  `KVStore`  | Key-value and structured data with conditional writes, indexes, and queries | Amazon DynamoDB |
|  `Database`  | SQL on PostgreSQL with migrations and transactions | Amazon Aurora DSQL, or Amazon Aurora PostgreSQL Serverless v2 |
|  `FileBucket`  | File storage with presigned URLs | Amazon S3 |

### Authentication
<a name="authentication"></a>

| Block | Description |  AWS service |
| --- | --- | --- |
|  `Auth`  | Email and password sign-in with MFA, groups, and passkeys, plus social, OIDC, and SAML sign-in | Amazon Cognito, or no user pool with `store: 'builtin'`  |

### Compute and background
<a name="compute-and-background"></a>

| Block | Description |  AWS service |
| --- | --- | --- |
|  `AsyncJob`  | Background work with retries, and optional status tracking | Amazon SQS \+ AWS Lambda or AWS Fargate |
|  `CronJob`  | Scheduled task execution | Amazon EventBridge Scheduler \+ AWS Lambda |
|  `Compute`  | Choose where a workload runs: serverless or container |  AWS Lambda or AWS Fargate |

### AI
<a name="ai"></a>

| Block | Description |  AWS service |
| --- | --- | --- |
|  `Agent`  | AI agent with tools, HITL approval, conversation persistence | Amazon Bedrock AgentCore Runtime \+ Amazon Bedrock models |
|  `KnowledgeBase`  | Semantic document retrieval and RAG | Amazon Bedrock Knowledge Bases |

### Communication
<a name="communication"></a>

| Block | Description |  AWS service |
| --- | --- | --- |
|  `Realtime`  | WebSocket pub/sub channels | Amazon API Gateway WebSocket |
|  `EmailClient`  | Transactional email | Amazon SES |

### Configuration
<a name="configuration"></a>

| Block | Description |  AWS service |
| --- | --- | --- |
|  `AppSetting`  | Configuration values that are not sensitive, such as feature flags and settings for the whole app |  AWS Systems Manager Parameter Store |
|  `Secret`  | Production secrets, such as API keys and connection strings |  AWS Secrets Manager |

### Observability
<a name="observability"></a>

| Block | Description |  AWS service |
| --- | --- | --- |
|  `Logger`  | Structured JSON logging with levels and context | Amazon CloudWatch Logs |
|  `Metrics`  | Custom application metrics | Amazon CloudWatch |
|  `Tracer`  | Distributed request tracing |  AWS X-Ray |
|  `Dashboard`  | Dashboard with health and logs for each compute, plus the metrics you choose | Amazon CloudWatch |

### Hosting and deployment
<a name="hosting-and-deployment"></a>

| Component | Description |  AWS service |
| --- | --- | --- |
|  `Hosting`  | Frontend deployment with SSR support (CDK layer, import from `aws-cdk-blocks/cdk`) | Amazon CloudFront \+ Amazon S3 |

For detailed API references for each CDK Block, see [CDK Blocks reference](building-blocks-reference.md).

## How CDK Blocks works
<a name="how-it-works"></a>

CDK Blocks uses Node.js conditional exports to load different code for each context:
+  **Local development**: CDK Blocks use in-memory and filesystem storage. Your app runs on your machine.
+  **CDK synthesis**: CDK Blocks produce CDK Constructs. CDK Blocks creates a CloudFormation template.
+  ** AWS Lambda runtime**: CDK Blocks call AWS services through the SDK.

The same `new KVStore(scope, 'todos')` line becomes a local store in development, a DynamoDB table at deploy time, and SDK calls in production. You don’t change any code.

## Supported platforms
<a name="supported-platforms-overview"></a>

CDK Blocks supports web frameworks (Next.js, Nuxt, Astro, React, Vue, Svelte, Angular), native mobile (Swift, Kotlin, Dart/Flutter), and desktop apps. Type safety extends from your backend all the way to your client, regardless of platform.

For the full list of supported frameworks and versions, see [Supported platforms](supported-platforms.md).

## Related services and tools
<a name="related-services"></a>

The following are some of the AWS services and tools that CDK Blocks works with. This is not an exhaustive list.

 ** AWS Amplify**
 AWS Amplify is a set of tools and services for building and hosting apps. You can add CDK Blocks to an existing Amplify Gen 2 app. For more information, see [CDK Blocks for existing apps](existing-apps.md).

 ** AWS Lambda**
CDK Blocks runs your backend on AWS Lambda by default. With the `Compute` Block, you can run a workload as a container on AWS Fargate instead. For more information, see the [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).

 **Amazon Elastic Container Service (Amazon ECS)**
With the `Compute` Block set to `container`, CDK Blocks runs your backend as a long-lived process on AWS Fargate, the serverless compute engine for Amazon ECS. For more information, see the [Amazon ECS Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html).

 **Amazon API Gateway**
CDK Blocks uses API Gateway to expose your backend APIs and WebSocket channels. For more information, see the [API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html).

 **Amazon DynamoDB**
Several CDK Blocks use DynamoDB for data persistence. For more information, see the [Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html).

 **Amazon Aurora**
The Database Block uses Aurora DSQL by default, and Aurora PostgreSQL Serverless v2 for an `aurora` cluster. For more information, see the [Amazon Aurora DSQL User Guide](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/what-is-aurora-dsql.html) and the [Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html).

 **Amazon Bedrock**
The Agent Block uses Amazon Bedrock models and runs its agent loop on Amazon Bedrock AgentCore Runtime. The KnowledgeBase Block uses Amazon Bedrock Knowledge Bases. For more information, see the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html).

 **Amazon Cognito**
The `Auth` Block uses a Cognito user pool by default. For more information, see the [Amazon Cognito Developer Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html).

 **Amazon S3**
 `FileBucket` stores files in Amazon S3, and `Hosting` serves static assets from it. For more information, see the [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

 **Amazon SQS**
 `AsyncJob` queues work in Amazon SQS. For more information, see the [Amazon SQS Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html).

 **Amazon EventBridge**
 `CronJob` runs on an Amazon EventBridge Scheduler schedule. For more information, see the [Amazon EventBridge Scheduler User Guide](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html).

 **Amazon SES**
 `EmailClient` sends email through Amazon SES. For more information, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html).

 ** AWS Secrets Manager**
The `Secret` Block stores a secret in Secrets Manager. For more information, see the [AWS Secrets Manager User Guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html).

 ** AWS Systems Manager Parameter Store**
 `AppSetting` stores configuration values in Parameter Store. For more information, see the [AWS Systems Manager User Guide](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html).

 **Amazon CloudWatch**
 `Logger`, `Metrics`, and `Dashboard` send data to CloudWatch. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

 ** AWS X-Ray**
 `Tracer` sends traces to X-Ray. For more information, see the [AWS X-Ray Developer Guide](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html).

 **Amazon CloudFront**
 `Hosting` serves your frontend through CloudFront. For more information, see the [Amazon CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html).

## Next steps
<a name="next-steps"></a>
+  [Getting started with AWS CDK Blocks](getting-started.md): Set up your environment and build your first application.
+  [AWS CDK Blocks concepts](concepts.md): Learn about CDK Blocks, scopes, and the app definition.
+  [CDK Blocks reference](building-blocks-reference.md): Browse all available CDK Blocks and their APIs.
