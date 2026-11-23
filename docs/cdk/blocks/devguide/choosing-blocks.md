---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/choosing-blocks.html
---

# Choosing AWS CDK Blocks

Use this page, or point your coding agent at it, to decide whether to build with AWS CDK Blocks. It explains how CDK Blocks builds on the AWS CDK, compares it with other ways to build on AWS, and lists what it requires. To choose a specific CDK Block, see the pages linked at the end.

## Should I use CDK Blocks?
<a name="choosing-blocks-answer"></a>

CDK Blocks builds on the AWS CDK. A CDK Construct defines AWS infrastructure, such as a queue or a database. A CDK Block adds two things to a construct. It includes the code your application calls to use that infrastructure, and it includes a local implementation, so you can run and test without an AWS account.

The code in each CDK Block follows AWS best practices. For example, it retries failed work, sends messages that keep failing to a dead-letter queue, and grants only the AWS Identity and Access Management (IAM) permissions it needs. You don’t write that code yourself.

Use CDK Blocks to build TypeScript applications on AWS. These include APIs for frontends, other services, and command line tools, as well as background jobs, scheduled jobs, realtime capabilities, and AI agents. Every CDK Block contains a CDK Construct, so you can add any other CDK Construct to the same stack.

## How does CDK Blocks compare with other approaches?
<a name="choosing-blocks-compare"></a>

The following table compares CDK Blocks with CDK Constructs on their own, and with three other ways to build on AWS.

| Question | CDK Blocks |  AWS CDK Constructs |  AWS SDK from your own server | A managed backend platform | Containers you run yourself |
| --- | --- | --- | --- | --- | --- |
| What do you write? | You create CDK Blocks and write the methods your callers use, all in one `cdk-blocks/` directory. Each CDK Block provides its infrastructure, the code that calls its AWS service, and a local implementation. | You define every resource. You also write the code that calls each service, connect your API, and write the IAM policies. | You write a server that calls AWS services through the AWS SDK. You create the resources some other way. | You write app code against the platform’s APIs. The platform defines and runs the backend. | You write the application, build the container images, and configure orchestration, networking, and scaling. |
| Who writes retries, dead-letter queues, and batch failure handling? | The CDK Blocks do. For example, `AsyncJob` creates a dead-letter queue, reports which jobs in a batch failed, and sets the queue timeout to match the worker’s timeout. | You do. Constructs create the infrastructure, but your application code handles failures. | You do. | It depends on the platform. | You do. |
| Where does it run? | In your own AWS account, as a CDK stack. | In your AWS account, on compute you define. | Wherever you host the server. | On the platform’s infrastructure. | On the cluster or container service you operate. |
| Can you run the whole application locally without an AWS account? | Yes. `npm run dev` runs every CDK Block locally and stores data in `.bb-data/`. Three capabilities need a deployed stack: the `Dashboard` route, `Auth` providers that sign in through Amazon Cognito, and `KnowledgeBase` sources in Amazon S3. | No. You test against AWS, or against emulators you set up. | The server runs locally, but its AWS SDK calls go to AWS unless you stub them. | It depends on the platform. | The containers run locally, but the AWS services they call still need AWS or emulators. |
| Who writes IAM permissions? | The CDK Blocks do. Each CDK Block grants only the access it needs to one shared execution role. | You do, with grant methods or policy statements. | You do, for the server’s role or credentials. | The platform does. | You do, for task or pod roles. |
| How do callers get a typed client? | TypeScript callers import types directly from the backend, so there is no schema to maintain. Dart, Swift, and Kotlin clients are generated from a spec file. | You define the API and the client, or generate the client from a schema. | You define the API and the client. | Usually through the platform’s own client SDK. | You define the API and the client. |
| Where does your code run? | Your API methods run on AWS Lambda by default, or on a container with the `Compute` Block. Each call has about 29 seconds to respond. Work that takes longer goes in an `AsyncJob`, which runs in the background: on Lambda for up to 15 minutes, or on a container for longer jobs. | On any compute you define. | In your server process. | On whatever the platform provides. | In processes you size and run, in any language. |
| What if you need something the CDK Blocks don’t provide? | Add any CDK Construct to the same stack, point a CDK Block at a resource you already have with `fromExisting`, or copy a CDK Block’s source into your project with vendorize. | You already control every resource. | You control the server code. The infrastructure is managed elsewhere. | You are limited to the platform’s extension points. | You control everything you run. |

## When should I choose CDK Blocks?
<a name="choosing-blocks-when"></a>

 **Choose CDK Blocks when:**
+ You build a TypeScript app on AWS, such as an API, a background worker, a scheduled job, a realtime capability, or an AI agent.
+ You want the code that calls AWS services to follow AWS best practices, without writing it yourself.
+ You want to build and test locally without an AWS account, and then deploy the same code.
+ You want IAM permissions and resource settings to come from the CDK Blocks you use.
+ You already have a CDK app. You can add CDK Blocks to one of its stacks with the `BlocksBackend` construct. For more information, see [Pattern 1: CDK in CDK Blocks](existing-infrastructure.md#existing-cdk-in-blocks).
+ You are a platform developer. You can package your organization’s approved patterns, such as encryption or sign-in rules, as custom CDK Blocks that your app teams install from npm. For more information, see [Creating custom CDK Blocks](custom-building-blocks.md).

## What does CDK Blocks require?
<a name="choosing-blocks-when-not"></a>

 **CDK Blocks fits when your application meets these requirements:**
+  **TypeScript on Node.js.** CDK Blocks are TypeScript packages. Your code runs on Node.js 24 on AWS, and local development needs Node.js 22 or later.
+  **API calls that respond within about 29 seconds.** Put longer work in an `AsyncJob`. It runs in the background, and on a container it can run for longer than 15 minutes.
+  **HTTP and WebSocket.** CDK Blocks serve requests over HTTP and WebSocket.
+  ** AWS as the deployment target.** CDK Blocks deploys as a CDK stack in your own AWS account.
+  **One shared execution role.** All CDK Blocks code runs with one shared IAM role. You can limit that role with a permissions boundary, but you can’t give each function its own role.

If part of your application doesn’t meet these requirements, such as a service in another language, build that part with CDK Constructs or containers in the same stack. Use CDK Blocks for the rest.

## When is another approach a better fit?
<a name="choosing-blocks-alternatives"></a>

 **Choose AWS CDK Constructs without CDK Blocks when** you need full control of every resource setting, and you’re ready to write the service calls, IAM policies, and local testing setup yourself.

 **Choose the AWS SDK from your own server when** you already run a server and only need to call a few AWS services from it.

 **Choose a managed backend platform when** you accept the platform’s limits so you don’t have to run infrastructure, and you don’t need the resources in your own AWS account.

 **Choose containers you run yourself when** your API needs a server process that keeps running between requests, a language other than TypeScript, or a protocol other than HTTP and WebSocket.

## Decision table
<a name="choosing-blocks-rules"></a>

Start at the top row and stop at the first row that matches your application.

| If | Then |
| --- | --- |
| Your application isn’t written in TypeScript for Node.js. | Use another approach, such as containers you run yourself. |
| Your application must run outside AWS. | Use another approach. |
| An API call needs more than about 29 seconds, or your API needs a server process that keeps running, or a protocol other than HTTP and WebSocket. | Build that API with containers. Long background work still fits CDK Blocks. Put it in an `AsyncJob`, and run it on a container if it takes more than 15 minutes. |
| You already have a CDK app. | Add CDK Blocks to one of its stacks with `BlocksBackend`. For more information, see [Pattern 1: CDK in CDK Blocks](existing-infrastructure.md#existing-cdk-in-blocks). |
| CDK Blocks cover most of your application, but one resource has no CDK Block. | Use CDK Blocks, and add a CDK Construct for that resource to the same stack. For more information, see [Existing infrastructure](existing-infrastructure.md#existing-patterns-overview). |
| Your organization needs its own approved version of a capability. | Build a custom CDK Block. For more information, see [Creating custom CDK Blocks](custom-building-blocks.md). |
| Your application is TypeScript, runs on AWS, and there are CDK Blocks for what it needs. | Use CDK Blocks. |

## Next steps
<a name="choosing-blocks-next"></a>
+ To choose a CDK Block, see [Data storage](bb-data-storage.md), [Authentication](bb-authentication.md), and the full list in [CDK Blocks reference](building-blocks-reference.md).
+ To learn when to go beyond a CDK Block, see [Existing infrastructure](existing-infrastructure.md#existing-patterns-overview).
