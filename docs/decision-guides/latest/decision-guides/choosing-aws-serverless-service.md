---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/choosing-aws-serverless-service.html
---

# Choosing an AWS serverless service
<a name="choosing-aws-serverless-service"></a>

|  |  |
| --- |--- |
| **Purpose** | Help determine which AWS serverless services are the best fit for your workload. |
| **Last updated** | September 4, 2026 |
| **Audience** | Developers and architects evaluating AWS serverless services for new or existing workloads. |
| **Covered services** |  + [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) (Event Functions, MicroVMs, Durable Functions)<br />+ [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)<br />+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)<br />+ [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html)<br />+ [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)<br />+ [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)<br />+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)<br />+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)<br />+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)<br />+ [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)<br />+ [Amazon Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html)<br />+ [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)<br />+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html)<br />+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)<br />+ [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)  |

## Introduction
<a name="serverless-intro"></a>

With AWS serverless services, you can build and run applications without provisioning or managing servers. You pay only for the resources you consume, and services scale automatically in response to demand.

AWS offers serverless options across compute, API management, application integration, orchestration, and data storage, that you can use to assemble complete applications from managed services. You can build applications ranging from microservices that handle discrete business logic as a part of your application backend, to event-driven workflows that perform data transformations or processing.

![Core serverless services grouped by category: compute, API layer, application integration, data storage, deployment, and observability.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/core-services-serverless.png)

 Traditional application frameworks bundle routing, data access, and integrations into a single codebase that you scale and maintain as one unit. This approach works well for getting started quickly, and frameworks like Express, Django, and Spring Boot provide familiar tools that boost initial productivity. However, as applications grow and rely on more external systems, complexity increases. The monolithic model makes scaling individual features difficult and slows down both development and troubleshooting. Serverless development addresses these challenges by composing independent services that each handle a specific function. Instead of building common distributed patterns from scratch, you use purpose-built AWS services for queues, event buses, publish/subscribe, orchestration, and APIs.

 There are well-established patterns in distributed architectures, including queues, event buses, publish/subscribe, orchestration, APIs, and event streams, that you can implement using purpose-built AWS services rather than building from scratch. When your application needs one of these patterns, use the corresponding AWS service:

| Pattern | AWS service |
| --- | --- |
| Queue | Amazon SQS |
| Event bus | Amazon EventBridge |
| Publish/subscribe (fan-out) | Amazon SNS |
| Orchestration | Step Functions |
| API | Amazon API Gateway |
| Event streams | Amazon Kinesis |

This guide helps you select the AWS serverless services and tools that are the best fit for your workload patterns and organizational requirements.

## Understand
<a name="serverless-understand"></a>

These services communicate through events, which are messages that represent a change in state. For example, when a customer uploads a photo to Amazon S3, Amazon S3 publishes an event that triggers a Lambda function to generate a thumbnail, without the upload service needing to know about the thumbnail service. You can also handle long-running tasks asynchronously. For example, you can implement a queue using Amazon SQS to manage order submissions. Then use Step Functions to manage a workflow that updates user information and inventory counts after every order is processed. Along the way, you use Amazon CloudWatch to log actions, monitor application activity, and AWS X-Ray to trace data flows for debugging. Event producers don't need to know which downstream services will respond. This decoupling allows each component to scale, deploy, and evolve independently. For information about advantages of a decoupled architecture, see [What is EDA (Event-Driven Architecture)?](https://aws.amazon.com/what-is/eda/).

![Serverless event-driven architecture with Lambda at the center, connected through events to the full ecosystem of serverless services.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/serverless-conceptual.png)

The following sections describe the services available in each category of a serverless architecture, and what they are optimized for.

------
#### [ Serverless compute ]
+ **Lambda Event Functions**: Run code in response to events without provisioning servers. Event functions scale automatically from zero to thousands of concurrent executions and charge per request and execution duration. Optimized for event-driven, short-lived workloads with a maximum duration of 15 minutes per invocation. Lambda also supports response streaming for progressive delivery of results, which is useful for generative AI and large payload responses. For workflows that need to run longer, Lambda durable functions automatically persist state across multiple invocations, enabling long-running executions while staying within the per-invocation time limit.
+ **Lambda MicroVMs**: A different compute form factor under the Lambda service, distinct from Event Functions in timeout, programming model, concurrency model, and billing. MicroVMs run isolated, stateful execution environments for user or AI-generated code. Each MicroVM provides VM-level isolation powered by Firecracker with full operating system capabilities (installing packages, mounting filesystems), snapshot-based rapid startup, and up to 8-hour lifetimes. MicroVMs support suspend and resume to reduce idle costs while preserving memory and disk state, port-listening protocols (HTTP/2, gRPC, WebSocket), and flexible resource allocation with baseline capacity that can burst to 4x during peak activity. Unlike Event Functions, MicroVMs use a Dockerfile-based programming model and allocate one environment per session rather than scaling per request. Suited for AI coding sandboxes, interactive development environments, data analytics notebooks, multi-tenant CI executors, security scanning, reinforcement learning environments, and game servers. Each MicroVM gets a dedicated HTTPS endpoint without requiring load balancers or ingress infrastructure, and supports configurable egress networking for VPC access and public internet connectivity.
+ **AWS Fargate**: Run containers without managing servers or clusters. Fargate handles provisioning and scaling of compute for containerized workloads. Suited for long-running services, batch processing, or workloads that need custom runtimes and fine-grained resource control.

**Tip**
For a deeper comparison of serverless compute options, see [AWS Fargate or AWS Lambda?](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/fargate-or-lambda.html)

------
#### [ API layer ]
+ **Amazon API Gateway HTTP API**: Lightweight, lower-cost API routing optimized for Lambda and HTTP backends with automatic deployments.
+ **Amazon API Gateway REST API**: Full-featured API management with request validation, response streaming, caching, AWS WAF integration, usage plans, API keys, and private endpoints.
+ **AWS AppSync**: Managed GraphQL service with real-time subscriptions, offline sync, and automatic data source integration (DynamoDB, Lambda, HTTP). Best for mobile and web apps with complex data requirements. AWS AppSync Events provides serverless WebSocket APIs for real-time publish/subscribe messaging, allowing applications to both publish and subscribe to events over a single WebSocket connection with data source integrations for processing published events.
+ **Lambda function URLs**: Dedicated HTTPS endpoints for individual Lambda functions without API Gateway. Suited for single-function microservices or webhooks where API management features aren't needed.
+ **Amazon API Gateway WebSocket APIs**: Persistent, bidirectional connections between clients and backend services. Use for chat applications, real-time dashboards, multiplayer games, or financial trading platforms where the server needs to push data to clients without polling.

------
#### [ Application integration ]
+ **Amazon Simple Queue Service**: Fully managed message queue for decoupling services. Supports standard (at-least-once, best-effort ordering) and FIFO (exactly-once, strict ordering) queues. Use for buffering, load leveling, and asynchronous processing.
+ **Amazon Simple Notification Service**: Publish/subscribe messaging for fan-out to multiple subscribers (Lambda, Amazon SQS, HTTP, email, SMS). Use when one event needs to trigger multiple downstream actions. Supports message filtering with subscription filter policies including wildcard and prefix matching, allowing subscribers to receive only relevant messages without custom filtering logic.
+ **Amazon EventBridge**: Serverless event bus for routing events from AWS services, SaaS apps, and custom sources using content-based filtering rules. Use for event-driven architectures with complex routing or third-party integrations.

**Tip**
For a deeper comparison, see [Amazon SQS, Amazon SNS, or Amazon EventBridge?](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/sns-or-sqs-or-eventbridge.html)

------
#### [ Orchestration ]
+ **AWS Step Functions Standard Workflows**: Coordinate multi-step processes with exactly-once execution, full execution history, and up to one year duration. Use for order processing, human approvals, and ETL pipelines.
+ **AWS Step Functions Express Workflows**: High-volume, short-duration orchestration (up to 5 minutes) with at-least-once execution. Use for IoT data ingestion, streaming transforms, and high-rate event processing.

Step Functions supports variables for assigning data in one state and using it in subsequent states, and JSONata transformations for advanced data manipulation including date formatting and mathematical operations. These features simplify data sharing across states and reduce the need for intermediate processing steps. For large-scale batch processing, Distributed Map runs the same process across millions of items from Amazon S3, Athena, or JSON datasets in parallel without provisioning compute infrastructure.

------
#### [ Data storage ]
+ **Amazon DynamoDB**: Serverless NoSQL key-value and document database with single-digit millisecond response times at any scale. No connection pooling needed. Use for high-throughput, low-latency data access with flexible schemas.
+ **Amazon Simple Storage Service**: Object storage with unlimited capacity. Use for file storage, data lakes, static assets, and event-driven processing (Amazon S3 triggers Lambda on upload).
+ **Amazon Aurora Serverless**: On-demand, auto-scaling relational database compatible with MySQL and PostgreSQL. Use when you need SQL semantics, complex joins, or ACID transactions with serverless scaling.

**Tip**
For a deeper comparison, see [Choosing an AWS database service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/databases-on-aws-how-to-choose.html).

------
#### [ Deployment and infrastructure as code ]
+ **AWS Serverless Application Model**: CloudFormation extension with shorthand syntax for Lambda, API Gateway, DynamoDB, and Step Functions. Includes local testing through the SAM CLI. Best for serverless-first applications.
+ **AWS Cloud Development Kit (AWS CDK)**: Define infrastructure using programming languages (TypeScript, Python, Java, C\#, Go). Best for complex applications that benefit from loops, conditionals, and reusable constructs.
+ **Terraform**: Multi-cloud IaC using HashiCorp Configuration Language (HCL). Best for platform teams managing infrastructure across providers.

------
#### [ Observability ]
+ **Amazon CloudWatch**: Metrics, logs, alarms, and dashboards for monitoring Lambda functions, API Gateway, and other services.
+ **AWS X-Ray**: Distributed tracing for understanding request flow across Lambda functions and integrated services. Essential for debugging event-driven architectures.

**Tip**
For a deeper comparison, see [Choosing an AWS monitoring and observability service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/monitoring-on-aws-how-to-choose.html).

------

## Consider
<a name="serverless-consider"></a>

Here are some key factors to consider when choosing AWS serverless services. Choosing the right combination involves balancing these factors to match your workload patterns, technical requirements, and organizational goals. This helps you optimize for performance, cost, and operational simplicity.

------
#### [ Workload pattern ]

Understanding the operational pattern of your application is the most important factor in selecting serverless services. Different workload patterns demand different service combinations. Serverless data processing largely falls within the following patterns:
+ **Asynchronous processing**: File processing, image manipulation, batch transformations, and webhooks. These workloads process events that don't require an immediate response and benefit from queues for buffering and fan-out for parallel processing.
+ **Synchronous request/response**: Web APIs, mobile backends, and microservices. These workloads need low-latency compute that responds to individual HTTP requests and scales with concurrent traffic.
+ **Streaming**: IoT telemetry, click-stream analysis, real-time analytics, and transaction processing. These workloads ingest high-velocity, continuous data that must be processed in near-real time.
+ **Orchestration**: Multi-step approval flows, ETL pipelines, and saga patterns. These workloads coordinate tasks with branching logic, error handling, and state management.

Each pattern uses a different combination of serverless services. For detailed examples and recommended service combinations for each pattern, see the Choose section.

------
#### [ Execution duration and concurrency ]

Serverless compute services differ significantly in how long they allow a single execution to run and how they handle concurrency. Unlike traditional servers, Lambda event functions do not run constantly. When a function is triggered by an event, this is called an invocation. Lambda event functions are limited to 15 minutes in duration, but on average, across all AWS customers, most invocations last for less than a second.

**Short-lived, event-driven invocations** are best served by Lambda, which supports execution durations up to 15 minutes and scales automatically per-request to thousands of concurrent invocations. The Lambda service runs instances of your function only when needed and scales automatically from zero requests per day to thousands per second. You pay only for the compute time that is actually used, so there is no charge when your code is not running. The per-millisecond billing of Lambda can reduce cost for short-duration workloads.

There are many types of invocation events that can trigger short-lived functions. Some examples include an HTTP request from API Gateway, a schedule managed by an EventBridge rule, a message from an IoT device, or a notification that a file was uploaded to an Amazon S3 bucket.

**Stateful, interactive sessions**, such as AI coding sandboxes, interactive notebooks, and multi-tenant CI environments, need isolated environments that retain state across user interactions. Lambda MicroVMs are a different compute form factor from Event Functions: they use a Dockerfile-based programming model, allocate one environment per session (not per request), and bill on a baseline plus burst model rather than per-millisecond. MicroVMs provide VM-level isolation with full OS capabilities, snapshot-based rapid startup, up to 8-hour lifetimes, and suspend/resume to reduce idle costs.

**Long-running or steady-state processes**, such as batch jobs, persistent WebSocket connections, or services that require more than 15 minutes of continuous processing, are better served by Fargate, which can run indefinitely. For details on how Fargate and Lambda scale differently, see the Scaling model and latency tab. Fargate provides consistent resource allocation for workloads that exceed the timeout or compute limits of Lambda. Additionally, Lambda durable functions enable multi-step, long-running executions that persist state across multiple invocations. Each individual invocation still respects the 15-minute limit. Durable functions automatically checkpoint progress and resume where they left off, so total workflow durations can far exceed 15 minutes without requiring Fargate or external orchestration.

Consider both the average and maximum execution time of your workloads. A Lambda function that occasionally exceeds 15 minutes fails unpredictably and requires architectural redesign. Your application architecture and needs determine how to invoke a function. For example, batch-processing patterns have different requirements than on-demand data processing. Fargate suits a microservice that primarily handles batch data processing. Lambda is simpler to deploy and maintain for on-demand processing.

------
#### [ Cost model and predictability ]

One of the key advantages of serverless development is that you pay only for the resources you consume. Serverless technologies are pay-as-you-go, which means you can scale up and down as your application needs change without paying for idle capacity. However, different AWS serverless services use different pricing models that favor different usage patterns.

**Pay-per-use pricing** (Lambda, Step Functions Express, EventBridge) charges based on actual invocations and duration, with no cost when idle. For Lambda, you are charged based on the number of requests for your functions and the duration it takes for your code to run. There is no charge when your code is not running. This model suits unpredictable or spiky workloads where traffic can drop to zero, and for early-stage applications where demand is uncertain.

**Capacity-based pricing** (Fargate, Amazon Aurora Serverless, DynamoDB provisioned mode) charges for reserved compute or throughput capacity. While this might incur costs during low-traffic periods, it becomes more cost-effective at sustained, predictable scale where per-request pricing would exceed the equivalent reserved capacity. For example, DynamoDB provisioned mode lets you adjust your tables' throughput capacity as needed, which can be more economical for workloads with consistent traffic patterns.

**Hybrid pricing** (DynamoDB on-demand, API Gateway) offers per-request pricing that scales linearly without upfront commitment. This provides cost predictability without the need to forecast capacity, but can become expensive at very high throughput compared to provisioned alternatives.

**Baseline plus burst pricing** (Lambda MicroVMs) charges for configured baseline resources while the MicroVM is running, with the ability to burst to 4x baseline during peak activity. Suspended MicroVMs reduce cost while preserving state. This model suits interactive workloads with variable activity and idle periods.

Model your expected traffic patterns across daily, weekly, and seasonal cycles. Workloads with high peak-to-average ratios favor per-use pricing. Steady-state workloads might benefit from capacity-based pricing. You can also use a combination: for example, Lambda with pay-per-use for variable compute alongside DynamoDB provisioned mode for predictable data access patterns.

------
#### [ Operational complexity ]

Traditional web application frameworks bundle routing, data access, connection pools, and integrations into a single codebase that you deploy and maintain as one unit. Setting up, configuring, and maintaining the frameworks, runtime environments, and infrastructure slows down your delivery of features and bug fixes. As applications grow and rely on more external systems, this complexity increases ramp-up time for new developers, makes tracking down the source of bugs more challenging, and delays the delivery of new features.

Serverless services exist on a spectrum of operational responsibility that reduces or eliminates this overhead. Instead of managing everything in one package, you compose loosely connected services where each one does one thing well with as few dependencies as possible.

**Minimal management**: Lambda, API Gateway, DynamoDB, Amazon SQS, Amazon SNS, EventBridge, and Step Functions require no server provisioning, patching, or capacity planning. You don't need to set up connection pools, configure runtime environments, or manage scaling infrastructure. You can focus entirely on writing or generating code that solves business problems.

**Container management**: Fargate requires building and maintaining container images, configuring task definitions, and managing deployment pipelines. You don't manage the underlying infrastructure, but you own the container lifecycle. This model suits teams that need custom runtimes or have existing containerized workloads they want to run without managing clusters.

**Infrastructure as code complexity**: AWS Serverless Application Model minimizes IaC complexity for serverless-only architectures with shorthand syntax and local testing. AWS Cloud Development Kit (AWS CDK) and Terraform provide more power for complex applications at the cost of steeper learning curves and more code to maintain.

Consider your team's existing skills, the number of services to manage, and your organization's operational standards. If your teams are spending more time maintaining infrastructure than building features, moving toward the minimal management end of the spectrum can free up resources for higher-value work.

------
#### [ Scaling model and latency ]

How a service scales directly impacts your application's responsiveness under load. In serverless architectures, scaling happens automatically, but different services use different mechanisms that affect latency and throughput.

**Per-request scaling** (Lambda) creates a new execution environment for each concurrent request. Lambda invokes your function in an execution environment, which provides a secure and isolated runtime environment that manages the processes and resources required to run the function. This provides near-instant response to traffic spikes, scaling from zero to thousands of concurrent executions in seconds.

However, per-request scaling introduces cold starts, which are initialization delays that occur when Lambda creates a new execution environment. The largest contributor to cold start time is the time that Lambda spends initializing the function, which includes loading the function's code, starting the runtime, and initializing the function code. For Java, Python, and .NET workloads, Lambda SnapStart can improve startup performance by up to 10x at no extra cost by taking a snapshot of the initialized execution environment and caching it for low-latency access. For other runtimes, you can mitigate cold starts with Provisioned Concurrency at additional cost.

**Task-level scaling** (Fargate) adds or removes container instances based on metrics such as CPU utilization, memory usage, or request count. Scaling adds new tasks in seconds to minutes and avoids cold starts for requests handled by existing tasks. Once a task is running, it stays warm for its entire lifetime, providing consistent latency for all requests it handles.

**Throughput-based scaling** (DynamoDB, Kinesis) adjusts read/write capacity or shard count based on demand. DynamoDB on-demand mode scales instantly to accommodate your workload's traffic patterns. Provisioned mode requires auto-scaling configuration but provides predictable throughput at lower per-request costs. With serverless architecture and DynamoDB, connection pools are not necessary to rapidly connect and scale the database. Instead, you adjust your tables' throughput capacity as needed.

For strict latency requirements (sub-100ms P99), evaluate cold-start behavior carefully. Lambda with Provisioned Concurrency or SnapStart, or Fargate with pre-warmed tasks, provides predictable latency for API workloads. For data processing workloads where latency is less critical, standard Lambda scaling is typically sufficient.

------
#### [ Integration and composability ]

Serverless architectures are composed from multiple services that communicate through events. An event represents a change in state, or an update. For example, an item placed in a shopping cart, a file uploaded to a storage system, or an order becoming ready to ship. The depth of native integration between services affects how quickly you can build and how much custom code you need to write.

**Deep native integration**: Lambda integrates with over 200 AWS services as event sources. Some services can trigger Lambda functions directly. For example, when an image is added to an Amazon S3 bucket, Lambda can be triggered to resize it. Some services cannot invoke Lambda directly, but you can use an event source mapping, which is a polling mechanism that reads from an event source and invokes a Lambda function. You can use event source mappings to process items from a stream or queue in: DynamoDB Streams, Amazon Kinesis, Amazon MQ, Amazon MSK, self-managed Apache Kafka, and Amazon SQS.

**Event routing flexibility**: EventBridge provides content-based routing with filtering rules, allowing a single event bus to route events to different targets based on event content. Amazon SNS provides topic-based fan-out to deliver messages to multiple subscribers simultaneously. Amazon SQS provides point-to-point buffering where consumers actively poll messages from the queue. Common combinations include routing EventBridge or Amazon SNS events to an Amazon SQS queue as a buffer for downstream consumers, pulling events from a stream or queue with EventBridge Pipes, and routing events to Kinesis for analytics.

**API integration patterns**: API Gateway offers two integration approaches. Proxy integrations directly pass all request information to a Lambda function for processing, which is simpler to configure. Non-proxy (custom) integrations can transform data before it reaches your function and before output returns to clients, which is useful for legacy code migration or keeping function code focused on business logic. REST API provides the broadest feature set including caching, request validation, and WAF. HTTP API provides the lowest latency and cost. AWS AppSync provides real-time subscriptions and GraphQL. Lambda function URLs provide the simplest single-function HTTPS endpoint without requiring API Gateway. For bidirectional communication where the server needs to push data to clients, API Gateway WebSocket APIs provide persistent connections suited for chat, real-time dashboards, and multiplayer games.

Due to the loose coupling between components of an event-driven system, your compute functions are not aware of other activities in the architecture. You can scale components independently, one service can fail without impacting other services, and events can be flexibly routed, buffered, and provide a log for audit.

------
#### [ Portability and standards ]

Your choice of serverless services affects how portable your architecture is across environments. Serverless applications usually comprise several AWS services, integrated with custom code run in Lambda functions. While Lambda can be integrated with most AWS services, you should consider the trade-off between deep platform integration and the ability to run workloads in other environments.

**AWS native services** (Lambda, Step Functions, EventBridge, DynamoDB) provide the deepest integration and lowest operational overhead. You can use any of these services through the AWS SDK without needing to install applications or configure servers. Becoming proficient with using these services through code in your Lambda functions is an important step to producing well-designed serverless applications. However, these services create coupling to AWS-specific APIs and event formats, meaning migrating to another cloud requires significant refactoring.

**Standards-based services** (Fargate with Docker containers, Amazon MQ with AMQP, Amazon MSK with Apache Kafka) run on open protocols or open-source technologies. If you need a custom runtime that is not provided by AWS, you can create and deploy a custom container image on Fargate. Amazon MSK provides Apache Kafka compatibility for teams with existing Kafka expertise. These options make workload portability more feasible at the cost of higher operational complexity and less tight integration with other AWS services.

**Deployment frameworks**: AWS Serverless Application Model and AWS Cloud Development Kit (AWS CDK) generate CloudFormation templates and are AWS-only. AWS Serverless Application Model extends CloudFormation with shorthand syntax focused on speeding up serverless development, offering optimized definitions for API Gateway, Lambda, and Step Functions resources, plus local Lambda testing through the SAM CLI. Terraform provides multi-cloud infrastructure definition using a single workflow across providers but with less serverless-specific tooling and limited local Lambda testing capabilities.

Containers and standards-based messaging can improve portability for multi-cloud requirements. Native serverless services offer close integration with other AWS services, which can simplify development when your workload runs primarily on AWS.

------

## Choose
<a name="serverless-choose"></a>

The following information can help you evaluate which AWS serverless services fit your workload requirements.

The following table highlights which services are optimized for which circumstances.

| Serverless category | What is it optimized for? | Serverless services |
| --- | --- | --- |
| Compute | Running code in response to events with minimal operational overhead, scaling per-request with no idle cost. Running isolated, stateful execution environments for user or AI-generated code. | [Lambda Event Functions](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)<br />[Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html)<br />[AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) |
| API layer | Routing HTTP and WebSocket requests to backend services, managing authentication, throttling, and caching. | [Amazon API Gateway HTTP API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html)<br />[Amazon API Gateway REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-rest-api.html)<br />[AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html)<br />[Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html)<br />[Amazon API Gateway WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html) |
| Application integration | Decoupling services through messaging, publish/subscribe, and event routing for asynchronous, loosely-coupled architectures. | [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)<br />[Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)<br />[Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) |
| Orchestration | Coordinating multi-step workflows with branching, error handling, retries, and state management. | [AWS Step Functions Standard Workflows](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)<br />[AWS Step Functions Express Workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html) |
| Data storage | Storing and retrieving data with automatic scaling, no server management, and pay-per-use pricing. | [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)<br />[Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)<br />[Amazon Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) |
| Deployment and IaC | Defining, deploying, and managing serverless infrastructure and application code as code. | [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)<br />[AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html)<br />[Terraform getting-started tutorial](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) on the HashiCorp website |
| Observability | Monitoring performance, tracing requests across services, and diagnosing issues in event-driven architectures. | [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)<br />[AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) |

The following tabs provide detailed guidance based on your specific workload needs. Choose the tab that best describes what you need to build, and review the recommended services and examples for that use case.

------
#### [ Synchronous API backend ]

You need to handle HTTP requests from web or mobile clients, process them, and return responses with low latency.

For web APIs and mobile backends, API Gateway routes HTTP requests to Lambda functions. DynamoDB handles low-latency data access. HTTP API provides simple routing at lower cost, while REST API adds caching, request validation, and WAF integration. You can handle authentication with Amazon Cognito, and AWS Serverless Application Model can define these resources with shorthand syntax.

To implement synchronous processing, use AWS Lambda for compute and Amazon API Gateway Gateway for routing requests. Use AWS Step Functions to orchestrate microservice workflows. Store data and files with DynamoDB and Amazon S3, and authenticate users with Amazon Amazon Cognito.

For example, suppose you want to build a microservices application that looks up weather data by zip code. The client resolves the hostname through Amazon Route 53. The HTTP GET request routes to API Gateway, which verifies an access token through Amazon Cognito, then sends the request to a Lambda function. The function queries DynamoDB, customizes the data, sends an event to Amazon SQS for analytics, and another to Amazon SNS for alerts. After traffic slows, Lambda tears down the execution environment. You pay only for actual function usage.

![Weather microservice architecture: a mobile client's request flows through Route 53, API Gateway, Cognito, Lambda, DynamoDB, SQS, and SNS, with CloudWatch monitoring throughout.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/weather-microservice-serverless.png)

**Tip**
For deeper guidance on compute selection, see [AWS Fargate or AWS Lambda?](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/fargate-or-lambda.html)

------
#### [ Asynchronous event processing ]

You need to handle events that don't require an immediate response, with reliable delivery and the ability to absorb traffic spikes.

For workloads that process events without an immediate response, Amazon SQS handles buffering and load leveling. Amazon SNS can fan out a single event to multiple subscribers in parallel. EventBridge filters events by content and integrates with SaaS applications. Step Functions coordinates multi-step processing, with DynamoDB or Amazon S3 for storing results.

To implement asynchronous processing, use AWS Lambda for compute and AWS Step Functions for orchestration. Route messages with Amazon Simple Notification Service for fan-out and Amazon Simple Queue Service for durable queuing. Store results in DynamoDB and Amazon S3.

For example, when a user uploads a photo to Amazon S3, Amazon S3 publishes an event that invokes a Lambda function to generate a thumbnail. If you also need to categorize the image and notify the user, use Amazon SNS to fan out that single upload event to multiple Lambda functions processing in parallel.

**Tip**
For deeper guidance on integration services, see [Amazon SQS, Amazon SNS, or Amazon EventBridge?](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/sns-or-sqs-or-eventbridge.html)

------
#### [ Multi-step workflow orchestration ]

You need to coordinate a sequence of tasks with branching logic, error handling, retries, and human approval steps.

Standard Workflows handle processes that run up to 1 year with exactly-once execution and full audit history. For high-volume, short-duration processing (up to 5 minutes), Express Workflows operate at lower cost per execution.

Step Functions is useful when you have workflows with more than one state, need to branch, or run tasks in parallel. The Step Functions service acts as the state model for your application. Standard Workflows provide exactly-once execution with a full, auditable execution history, making them well-suited for order processing, human approval workflows, and ETL pipelines. Express Workflows provide at-least-once execution at higher volume and lower cost, making them well-suited for IoT data ingestion, streaming transforms, and high-rate event processing.

**Tip**
For deeper guidance, see [Choosing an AWS application integration service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/application-integration-on-aws-how-to-choose.html).

------
#### [ Real-time streaming data ]

You need to ingest, process, and analyze high-velocity continuous data in near-real time. Lambda and Amazon Kinesis can process real-time streaming data. Use cases include activity tracking, click-stream analysis, log filtering, IoT telemetry, and metering.

For native AWS integration, Kinesis Data Streams handles stream ingestion. Amazon MSK can ingest streams with Apache Kafka compatibility. Either Lambda or Fargate processes the stream data, with DynamoDB or Amazon S3 for storing results.

To implement serverless streaming, use AWS Lambda for compute and Amazon Kinesis for collecting and analyzing real-time data. Store results with DynamoDB and Amazon S3.

For example, when items are written to a DynamoDB table, DynamoDB Streams publishes events that invoke a Lambda function to generate real-time analytics. For higher-volume ingestion like IoT telemetry from millions of devices, use Kinesis Data Streams to collect and buffer the data before processing.

------
#### [ Long-running or batch processing ]

You need processing that exceeds the 15-minute limit of Lambda, requires persistent connections, or benefits from custom container runtimes.

For workflows that exceed 15 minutes but consist of discrete steps, Lambda durable functions checkpoint progress and resume across invocations. Step Functions Distributed Map can process millions of items from Amazon S3, Athena, or JSON in parallel without provisioning compute. Fargate supports continuous processing, persistent connections, and fine-grained CPU/memory control.

For example, a nightly data pipeline that processes 10 million Amazon S3 objects uses Step Functions Distributed Map to parallelize the work. A video transcoding service that processes files for 30\+ minutes uses Fargate. A multi-step loan approval workflow that spans days uses Lambda durable functions to persist state between human review steps.

**Tip**
For deeper guidance on compute selection, see [AWS Fargate or AWS Lambda?](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/fargate-or-lambda.html)

------
#### [ Isolated execution environments ]

You need to run user-supplied or AI-generated code in isolated environments with strong tenant separation and state preservation.

Lambda MicroVMs provide VM-level isolation powered by Firecracker, with full operating system capabilities, snapshot-based rapid startup, and up to 8-hour lifetimes. Each MicroVM gets a dedicated HTTPS URL supporting HTTP/2, gRPC, and WebSocket protocols. MicroVMs can be suspended when idle to reduce costs while preserving memory and disk state. Unlike Event Functions, MicroVMs use a Dockerfile-based programming model, allocate one environment per session, and bill on a baseline plus burst model (up to 4x baseline during peak activity). Each MicroVM supports configurable egress networking for VPC access and public internet connectivity, without requiring load balancers or ingress infrastructure.

For example, an AI coding assistant gives each user session its own MicroVM to safely execute generated code. An interactive notebook platform runs each student's code in an isolated MicroVM that persists state between interactions.

------

## Use
<a name="serverless-use"></a>

You should now have a clear understanding of each AWS serverless service and which one might be the best fit for your organization and use case. To explore how to use and learn more about each available service, the following section provides links to in-depth documentation, hands-on tutorials, and resources to get you started.

------
#### [ Serverless compute ]

**AWS Lambda**
+ **Get started with AWS Lambda** Learn how to create your first Lambda function using the console. [Lambda getting-started tutorial](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
+ **Using AWS Lambda with other services** Explore common use cases and learn how Lambda integrates with other AWS services. [Lambda service integrations](https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html)
+ **Serverless Patterns Workshop** Build a serverless microservice with Lambda, API Gateway, and DynamoDB in a hands-on workshop. [Serverless Patterns Workshop](https://catalog.workshops.aws/serverless-patterns) on the AWS Workshops website.
+ **AWS Lambda Pricing** Understand the per-request and per-duration pricing model. [Lambda pricing page](https://aws.amazon.com/lambda/pricing/)

**AWS Fargate**
+ **Getting started with Fargate on Amazon ECS** Learn how to run containers on Fargate without managing servers. [Fargate getting-started guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-fargate.html)
+ **Creating a cluster with a Fargate Linux task using the AWS CLI** Set up a cluster, register a task definition, and run a task. [Fargate CLI tutorial](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html)

**Lambda MicroVMs**
+ **Create your first MicroVM** Build an isolated execution environment with VM-level isolation. [MicroVMs getting-started guide](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html)

------
#### [ API layer ]

**Amazon API Gateway REST API**
+ **Build a REST API with Lambda integration** Create a REST API that integrates with a Lambda function. [REST API with Lambda tutorial](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-as-simple-proxy-for-lambda.html)
+ **Controlling and managing access to a REST API** Learn about authentication and authorization options. [REST API access control guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html)

**Amazon API Gateway HTTP API**
+ **Build an HTTP API with Lambda and DynamoDB** Create a low-latency, low-cost HTTP API with a Lambda backend. [HTTP API with DynamoDB tutorial](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html)
+ **Choosing between REST APIs and HTTP APIs** Understand the feature and pricing differences between the two API types. [REST vs HTTP API comparison](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html)

**AWS AppSync**
+ **Getting started with AWS AppSync** Build a GraphQL API with real-time data synchronization. [AppSync quickstart guide](https://docs.aws.amazon.com/appsync/latest/devguide/quickstart.html)

**Lambda function URLs**
+ **Creating and managing Lambda function URLs** Add a dedicated HTTPS endpoint to a Lambda function without API Gateway. [Lambda function URLs guide](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html)

------
#### [ Application integration ]

**Amazon Simple Queue Service**
+ **Getting started with Amazon SQS** Create a queue, send messages, and receive messages using the console. [SQS getting-started guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html)
+ **Orchestrate Queue-based Microservices** Design a serverless workflow that orchestrates a message queue-based microservice. [Queue-based microservices tutorial](https://aws.amazon.com/getting-started/hands-on/orchestrate-microservices-with-message-queues-on-step-functions/) on the AWS website

**Amazon Simple Notification Service**
+ **Getting started with Amazon SNS** Create a topic, subscribe endpoints, and publish messages. [SNS getting-started guide](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html)
+ **Send Fanout Event Notifications** Implement a fanout messaging scenario using Amazon SNS and Amazon SQS. [Fanout notifications tutorial](https://aws.amazon.com/getting-started/hands-on/send-fanout-event-notifications/) on the AWS website

**Amazon EventBridge**
+ **Getting started with Amazon EventBridge** Create a basic rule that routes events to a target. [EventBridge getting-started guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html)
+ **Building event-driven architectures workshop** Learn event-driven design with EventBridge and other serverless services. [Event-Driven Architecture Workshop](https://event-driven-architecture.workshop.aws/) on the AWS Workshops website.

------
#### [ Orchestration ]

**AWS Step Functions**
+ **Getting started with AWS Step Functions** Create a basic workflow for processing credit card applications. [Step Functions tutorial](https://docs.aws.amazon.com/step-functions/latest/dg/getting-started-with-sfn.html)
+ **AWS Step Functions Workshop** Explore the primary features of Step Functions through interactive modules. [Step Functions Workshop](https://catalog.workshops.aws/stepfunctions/en-US) on the AWS Workshops website.
+ **Standard vs. Express Workflows** Understand differences between Standard and Express workflow types. [Standard vs Express guide](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html)
+ **Design Patterns for AWS Step Functions** Learn how to implement design patterns in your state machines. [Design Patterns for Step Functions](https://explore.skillbuilder.aws/learn/course/external/view/elearning/10471/design-patterns-for-aws-step-functions) on AWS Skill Builder.

------
#### [ Data storage ]

**Amazon DynamoDB**
+ **Getting started with DynamoDB** Create a table, write, read, update, and query data using the AWS CLI. [DynamoDB getting-started tutorial](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html)
+ **Choosing an AWS database service** Use our database decision guide for deeper guidance on database selection. [Database decision guide](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/databases-on-aws-how-to-choose.html)

**Amazon Simple Storage Service**
+ **Getting started with Amazon S3** Create a bucket, upload objects, and configure access. [S3 getting-started tutorial](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)
+ **Using an Amazon S3 trigger to invoke a Lambda function** Process files automatically when they're uploaded to a bucket. [S3 trigger with Lambda tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html)

**Amazon Aurora Serverless**
+ **Using Amazon Aurora Serverless v2** Learn how Amazon Aurora Serverless automatically adjusts capacity based on demand. [Aurora Serverless v2 guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html)

------
#### [ Deployment and IaC ]

**AWS Serverless Application Model**
+ **Getting started with AWS Serverless Application Model** Initialize, build, and deploy a serverless application with the SAM CLI. [SAM getting-started tutorial](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started.html)
+ **Testing locally with SAM CLI** Invoke Lambda functions locally and run API Gateway locally for development. [SAM CLI local testing guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-local.html)

**AWS Cloud Development Kit (AWS CDK)**
+ **Getting started with the AWS Cloud Development Kit (AWS CDK)** Create your first CDK app and deploy infrastructure using your preferred programming language. [CDK getting-started tutorial](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

**Terraform**
+ **Getting started with Terraform on AWS** Learn how to provision AWS infrastructure with Terraform. [Terraform getting-started tutorial](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) on the HashiCorp website.

------
#### [ Observability ]

**Amazon CloudWatch**
+ **Getting started with CloudWatch** Set up dashboards, alarms, and log groups for your serverless application. [CloudWatch getting-started guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingStarted.html)

**AWS X-Ray**
+ **Getting started with AWS X-Ray** Trace requests across Lambda, API Gateway, and downstream services. [X-Ray getting-started guide](https://docs.aws.amazon.com/xray/latest/devguide/xray-gettingstarted.html)
+ **Choosing an AWS monitoring and observability service** Use our monitoring decision guide for deeper guidance on observability tooling. [Monitoring decision guide](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/monitoring-on-aws-how-to-choose.html)

------

## Explore
<a name="serverless-explore"></a>

Once you have determined which approach best fits your workload, review these resources to help you begin implementing. You can find service-specific resources in the previous section, and general serverless architecture resources in the following section.
+ **Architecture diagrams** Explore reference architecture diagrams for serverless on AWS. [ Explore architecture diagrams](https://docs.aws.amazon.com/reference-architecture-diagrams/)
+ **Serverless Patterns Workshop** Build serverless microservices with hands-on exercises covering unit and integration testing, infrastructure as code, and common architectural patterns. [Serverless Patterns Workshop](https://catalog.workshops.aws/serverless-patterns) on the AWS Workshops website.
+ **Serverless Land** Explore serverless patterns, blogs, videos, and learning resources from the AWS serverless community. [Serverless Land patterns and resources](https://serverlessland.com/)
+ **Whitepapers** Explore whitepapers for serverless best practices, architecture guidance, and cost optimization. [ Explore whitepapers](https://aws.amazon.com/whitepapers/?whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc&awsf.whitepapers-content-type=*all&awsf.whitepapers-global-methodology=*all&awsf.whitepapers-tech-category=tech-category%23serverless&awsf.whitepapers-industries=*all&awsf.whitepapers-business-category=*all)
+ **AWS Solutions** Explore vetted solutions and architectural guidance for common serverless use cases. [Explore solutions](https://aws.amazon.com/solutions/serverless/)
