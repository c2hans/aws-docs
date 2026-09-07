---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/fargate-or-lambda.html
---

# AWS Fargate or AWS Lambda?
<a name="fargate-or-lambda"></a>

**Understand the differences and pick the one that's right for you**

|  |  |
| --- |--- |
| **Purpose** | To explore whether AWS Fargate or AWS Lambda meet your needs for a serverless compute service. |
| **Last updated** | August 21, 2026 |
| **Covered services** |  +  [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)  <br />+  [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)   |

## Introduction
<a name="fl-introduction"></a>

You might have already considered the broader range of AWS compute services. These are covered in the [Choosing an AWS compute service decision guide](https://docs.aws.amazon.com/decision-guides/latest/compute-on-aws-how-to-choose/choosing-aws-compute-service.html). If you narrowed your choice to AWS Lambda and AWS Fargate, you are likely looking for a serverless compute service. Both services share the following benefits:

**Note**
This guide covers Lambda functions and Lambda Managed Instances. Lambda MicroVMs, which provide session-based isolated sandboxes for running untrusted code, are a distinct compute primitive not covered in this guide. For information about Lambda MicroVMs, see [Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html) in the Lambda Developer Guide.

**Note**
AWS also offers related compute options not covered in this guide, including Amazon ECS Express Mode for simplified container deployment and Amazon ECS Managed Instances for running containers on specific EC2 instance types with managed infrastructure. For a complete view of container compute options, see [the Amazon ECS Developer Guide](https://docs.aws.amazon.com/ecs/latest/developerguide/AWS_Fargate.html).
+  **Reduced operational overhead:** Both Lambda and Fargate abstract away server management. This reduces the need for patching, maintenance, and capacity planning.
+  **Pay-per-use pricing:** You only pay for the compute resources you actually use. This can lower costs for variable workloads.
+  **Faster deployment:** These services typically offer quicker deployment times. This is compared to provisioning and configuring EC2 instances.
+  **Built-in high availability:** Both services handle infrastructure redundancy automatically.
+  **Simplified compliance:** A reduced attack surface and built-in security features can ease compliance efforts.
+  **Focus on code:** Developers can concentrate on writing application code rather than managing infrastructure.

 While Lambda and Fargate are both serverless options, there are significant differences between them.

**AWS Fargate**
AWS Fargate is a serverless compute engine for containers. It is primarily used with Amazon ECS. With Fargate, you can focus on deploying and scaling containerized applications without managing the underlying infrastructure. Fargate is ideal for long-running applications, microservices, or batch processing. It gives you fine-grained control over resource allocation (CPU, memory) without managing underlying servers.

**AWS Lambda**
AWS Lambda is a serverless computing service that runs your code as functions in response to events. It manages the underlying compute resources for you. Lambda functions are best suited for event-driven applications. Examples include processing files uploaded to Amazon S3, responding to HTTP requests, running scheduled tasks, or processing data streams. Data stream sources include Amazon Kinesis and Amazon DynamoDB. Lambda functions have a maximum execution time of 15 minutes per invocation. Lambda also offers durable functions, a programming model for workflows that can run for up to 1 year using checkpoint-and-replay execution. With Lambda Managed Instances, you can run functions on a wide range of EC2 instance types. You retain the operational simplicity of Lambda.

Use the following guidelines to help you choose between the two services:
+ If your project involves event-driven tasks, unpredictable workloads, or wait-heavy orchestration workflows, consider Lambda functions.
+ If your workloads are steady-state or predictable and benefit from EC2 pricing and specialized compute, Lambda Managed Instances might be well suited.
+ If you need to run containerized applications with specific resource needs or persistent processes, Fargate is worth considering.

You can also combine both services in a hybrid architecture. For patterns that combine Lambda and Fargate, see [Run event-driven and scheduled workloads at scale with Fargate](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-event-driven-and-scheduled-workloads-at-scale-with-aws-fargate.html) in AWS Prescriptive Guidance.

The following table provides a side-by-side comparison of key differences between these services.

|  |  |  |
| --- |--- |--- |
|  Feature  |  AWS Fargate  |  AWS Lambda  |
|  Execution model  |  Container-based, serverless compute  |  Event-driven, serverless functions (with optional durable orchestration)  |
|  Supported languages  |  Any language that can run in a container  |  Node.js, Python, Java, C\#, Go, Ruby, and PowerShell. You can also [build a custom runtime](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html) for other languages. |
|  Use case  |  Long-running, containerized applications  |  Short-duration, event-driven tasks (or workflows up to 1 year with durable functions)  |
|  Execution pattern  |  Continuous compute (long-running processes, persistent connections)  |  Event-driven with optional wait-heavy orchestration (durable functions)  |
|  Scaling  |  Automatic scaling based on desired task count, with predictive scaling support  |  Automatic scaling per request  |
|  Cold start  |  Varies by image size and configuration  |  Varies by runtime and package size  |
|  Execution time limit  |  No hard limit  |  15 minutes per invocation (durable functions orchestrate workflows up to 1 year)  |
|  Memory allocation  |  Up to 244 GiB  |  Up to 10 GiB  |
|  CPU allocation  |  Up to 32 vCPU  |  Proportional to memory, up to 6 vCPU  |
|  Networking  |  Runs in VPC with ENIs; supports Amazon VPC Lattice and IPv6-only configurations  |  Can run in AWS managed VPC or attached to a customer-managed VPC using AWS Hyperplane |
|  State management  |  Containers can maintain in-memory state across requests while running. External storage is recommended for critical data.  |  Stateless by design (state must be managed externally, for example, Amazon S3, Amazon DynamoDB, Amazon EFS). Durable functions can persist workflow state for up to 1 year.  |
|  Container support  |  Full container support  |  Limited container support (via container image deployments)  |
|  Orchestration  |  Integrated with Amazon ECS |  No orchestration required  |
|  Deployment strategies  |  Native blue/green, canary, and linear deployments  |  Weighted aliases for gradual deployments  |
|  Pricing model  |  Per second billing for vCPU and memory used; Fargate Spot available for x86 and ARM  |  Per invocation and duration (GB-seconds); Lambda Managed Instances offer EC2-based pricing  |
|  Concurrency limits  |  Based on cluster capacity  |  1000 concurrent executions by default (can be increased)  |
|  Event-driven invocation  |  Requires additional setup  |  Native support for various AWS event sources  |
|  Cold start mitigation  |  Lazy loading images with Seekable OCI (SOCI) can speed up starting Fargate tasks  |  Provisioned concurrency, SnapStart (for Java, Python, and .NET), and Lambda Managed Instances available  |
|  Package size limit  |  No specific limit (container size limited by configured ephemeral storage, 200 GiB maximum)  |  250 MB unzipped, including layers, 10 GB for container image deployments  |

## Differences between Fargate and Lambda
<a name="fl-differences"></a>

 Explore the differences between Fargate and Lambda in a number of key areas.

------
#### [ Languages supported ]

 **Fargate**: AWS Fargate is a serverless compute engine for containers, used with Amazon ECS for orchestration. It supports any programming language or runtime environment that can be packaged into a Docker container. This flexibility means you can use virtually any language, framework, or library that suits your application needs. You can use Python, Java, Node.js, Go, .NET, Ruby, PHP, or even custom languages and environments. Fargate can run them as long as they are encapsulated in a container. This broad language support makes Fargate ideal for running diverse applications. These include legacy systems, multi-language microservices, and modern cloud-native applications.

 **Lambda**: AWS Lambda offers native support for a more limited set of languages compared to Fargate. Lambda functions are purpose-built for event-driven workloads. Lambda officially supports the following languages and runtimes:
+  Node.js
+  Python
+  Java
+  Go
+  Ruby
+  C\#
+  PowerShell

 Lambda also supports custom runtimes. With custom runtimes, you can bring your own language or runtime environment. However, this requires more setup and management compared to using natively supported options. If you deploy your Lambda function from a container image, you can write your function in Rust. Use an AWS OS-only base image and include the Rust runtime client in your image. If you use a language without an AWS-provided runtime interface client, you must create your own.

------
#### [ Event-driven invocation ]

 **Lambda** is inherently designed for event-driven computing. Lambda functions are triggered in response to changes in data, user actions, or scheduled tasks. It integrates natively with many AWS services. These include Amazon S3 (for example, invoking a function when a file is uploaded), DynamoDB (for example, triggering on data updates), and API Gateway (for example, handling HTTP requests). The Lambda event-driven architecture is ideal for applications that need to respond immediately to events. These applications do not require persistent compute resources.

 **Fargate** is not natively event-driven. However, with some additional boilerplate logic, it can integrate with event sources such as Amazon SQS and Kinesis. Lambda handles the bulk of this integration logic for you. With Fargate, you must implement this integration yourself using the APIs for these services.

------
#### [ Runtime/use cases ]

 **Fargate** is designed to run containerized applications. It provides a flexible runtime environment where you can define the CPU, memory, and networking settings for your containers. Fargate operates on a container-based model. It supports long-running processes, persistent services, and applications with specific runtime requirements. The containers in Fargate can run indefinitely because there is no hard limit on execution time. This makes it ideal for applications that need to run continuously. With container restart policies in Fargate, individual containers within a task can restart automatically without restarting the entire task. This improves resilience for multi-container workloads. Fargate integrates with CloudWatch Container Insights with enhanced observability. With this feature, you get detailed per-container metrics and traces for monitoring application performance.

 **Lambda** functions are optimized for short-lived, event-driven tasks. Lambda functions have a maximum execution time of 15 minutes per invocation. This makes Lambda functions well-suited for scenarios such as file processing, real-time data streaming, and HTTP request handling. These tasks are brief and do not require long-running processes.

 With durable functions in Lambda, you can build long-running workflows that can persist state across multiple invocations for up to 1 year. Durable functions provide built-in error handling, automatic retries, and recovery after failures. A durable functions SDK is available for JavaScript, TypeScript, Python, Java, and C\# (.NET). During wait periods, your function suspends without incurring compute charges. With durable functions, you can address use cases that previously required persistent compute environments.

 When choosing between durable functions and Fargate for long-running workloads, consider the execution pattern. Durable functions are cost-effective for workflows that spend most of their time waiting, such as human approvals, scheduled delays, or external API callbacks. You do not incur compute charges during wait periods. Fargate is more appropriate for workloads that require continuous compute, such as data processing, persistent network connections, or services that must remain active without interruption.

 In Lambda, the runtime environment is more abstracted. You have less control over the underlying infrastructure. For standard functions, each invocation is independent and stateless. Any state or data that needs to persist between invocations must be managed externally. Examples include databases or storage services.

------
#### [ Scaling ]

 **Fargate** scales by adjusting the number of running tasks. This is based on the desired state defined in your container orchestration service (Amazon ECS). Scaling can be done manually or automatically through Amazon EC2 Auto Scaling. For more information, see [Under the hood: Amazon ECS and Fargate increase task launch rates](https://aws.amazon.com/blogs/containers/under-the-hood-amazon-elastic-container-service-and-aws-fargate-increase-task-launch-rates/) on the AWS Containers blog.

 In Fargate, each task runs in its isolated environment. Scaling involves launching additional tasks or stopping them based on the load. The Amazon ECS service scheduler can launch up to 500 tasks in less than a minute per service. This applies to web and other long-running services. Amazon ECS also supports predictive scaling. It uses historical patterns to proactively increase tasks before demand spikes occur. Target tracking policies for CPU and memory utilization support 20-second metric resolution. This enables faster scaling signal detection. Amazon ECS can also automatically rebalance service tasks across Availability Zones. This maintains high availability. Fargate integrates with AWS Fault Injection Service (FIS). With FIS, you can run controlled fault injection experiments to test application resilience.

![Diagram showing task launch differences between Fargate and Lambda.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/task-launches.png)

 For **Lambda**, *concurrency* is the number of in-flight requests that your AWS Lambda function is handling at the same time. This differs from concurrency in Fargate. Each Fargate task can handle concurrent requests as long as there are available compute and network resources. For each concurrent request, Lambda provisions a separate instance of your execution environment. As your functions receive more requests, Lambda automatically scales the number of execution environments. This continues until you reach your account concurrency limit. By default, Lambda provides your account with a total concurrency limit of 1,000 concurrent executions. This limit applies across all functions in an AWS Region. You can request a quota increase if needed.

 With Lambda Managed Instances, scaling works differently. Instead of provisioning a new execution environment for each concurrent request, Managed Instances scale asynchronously based on CPU resource utilization. Each execution environment can handle multiple concurrent invocations. This approach maximizes resource utilization. It is well-suited for steady-state or predictable workloads.

 For each Lambda function using the default compute type, the concurrency scaling rate is 1,000 execution instances every 10 seconds. This continues up to the maximum account concurrency. For more information, see [Lambda functions now scale 12 times faster when handling high-volume requests](https://aws.amazon.com/blogs/aws/aws-lambda-functions-now-scale-12-times-faster-when-handling-high-volume-requests/) on the AWS Compute blog. If the number of requests in a 10 second period exceeds 1,000, the additional requests are throttled. The following graph demonstrates how Lambda scaling works assuming an account concurrency of 7000.

![Bar graph showing how instances are throttled when number exceeds 1000.](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/instance-throttling.png)

------
#### [ Cold start and cold-start mitigation ]

 **Lambda** functions can experience cold starts. These occur when a function is invoked after being idle for some time. During a cold start, the Lambda service initializes a new execution environment. This includes loading the runtime, dependencies, and the function code. Cold start duration varies from under 100 milliseconds to over 1 second, depending on runtime, package size, and initialization logic. For runtimes with longer initialization times such as Java or C\#, cold starts can be longer without optimization. Cold starts can impact performance of applications that require low-latency responses.

 To mitigate cold starts in Lambda, consider the following strategies:
+  **Minimize function size**: Reduce the size of your function package and its dependencies. This can decrease the time needed for initialization.
+  **Increase memory allocation**: Higher memory allocations increase CPU capacity. This can reduce initialization time.
+  **Keep functions warm**: Periodically invoke your Lambda functions (for example, using CloudWatch Events). This keeps them active and reduces the likelihood of cold starts.
+  **Lambda SnapStart**: Use [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) for Java, Python, and .NET functions to reduce startup time. SnapStart takes a snapshot of the initialized execution environment. Subsequent invocations resume from the snapshot rather than performing a full cold start.
+  **Provisioned concurrency**: This feature keeps a specified number of function instances warm and ready to serve requests. This reduces cold start latency. However, it increases costs. You pay for the provisioned instances even if they are not actively handling requests.
+  **Lambda Managed Instances**: Run functions on a wide range of EC2 instance types. These include processors such as Graviton4 and high-bandwidth networking options. Pre-provisioned execution environments eliminate cold starts. Lambda handles instance lifecycle, OS and runtime patching, routing, load balancing, and automatic scaling. Lambda Managed Instances also support multi-concurrent invocations per execution environment. They offer EC2 pricing advantages such as Compute Savings Plans and Reserved Instances.

 **Fargate** is not generally impacted by cold starts in the same way as Lambda. The time to start a Fargate task correlates directly to the time it takes to [pull the container images](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-pull-behavior.html) defined in the task from the image registry. Fargate also supports lazy loading of container images that have been indexed with [Seekable OCI (SOCI)](https://aws.amazon.com/blogs/aws/aws-fargate-enables-faster-container-startup-using-seekable-oci/). Lazy loading container images with SOCI reduces the time to launch Amazon ECS tasks on Fargate. Fargate uses SOCI index manifest v2. This provides improved performance for lazy loading. After a task starts on Fargate, it is a long-running process. It is always ready to handle requests. If you need to start new tasks in response to scaling events, there might be some delay during initialization. This is typically less significant compared to Lambda cold starts.

------
#### [ Memory and CPU options ]

 **Fargate** provides granular control over both memory and CPU resources for your containerized applications. When you launch a task in Fargate, you can specify the exact CPU and memory requirements for your application. The CPU and memory allocations are independent. You can choose combinations that best suit your workload. You can select CPU values ranging from 0.25 vCPUs to 32 vCPUs. Memory ranges from 0.5 GB to 244 GB per task, depending on your configuration.

 This flexibility is ideal for applications with specific performance characteristics. Examples include memory-intensive databases or CPU-bound computation tasks. Fargate allows you to optimize your resource allocation. You can balance cost and performance effectively.

 In **Lambda**, memory and CPU are linked. The CPU is automatically allocated in proportion to the amount of memory you select. You can choose memory allocations between 128 MB and 10 GB, in 1 MB increments. The CPU scales with the memory, up to 6 vCPU. Higher memory settings result in more CPU power. However, you do not have direct control over the CPU allocation itself.

 This model is designed for simplicity. You can quickly adjust memory settings without managing CPU configurations. However, it might be less flexible for workloads that require a specific balance between CPU and memory resources. The Lambda model is suitable for tasks where you want straightforward scaling based on memory needs. It might not be optimal for applications with complex or highly specific resource demands.

------
#### [ Networking ]

 When you deploy tasks in **Fargate**, they run in an Amazon VPC (Amazon Virtual Private Cloud). This gives you full control over the networking environment. You can configure security groups, network access control lists (ACLs), and routing tables. Each Fargate task gets its own network interface with a dedicated private IP address. You can assign a public IP address if needed.

 Fargate supports advanced networking features such as load balancing (using AWS Elastic Load Balancing), VPC peering, and direct access to other AWS services within the VPC. You can also use AWS PrivateLink for secure, private connectivity to supported AWS services. This avoids traversing the internet. Fargate tasks also support Amazon VPC Lattice. This provides standardized service-to-service connectivity, security, and observability. Fargate tasks can run in IPv6-only configurations. This allows tasks to communicate exclusively over IPv6.

 By default, **Lambda** functions run in a managed network environment. You do not have direct control over network interfaces or IP addresses. However, Lambda can be attached to a customer-managed VPC using AWS Hyperplane. This enables you to control access to resources inside your VPC.

 When Lambda functions are attached to a customer-managed VPC, they inherit the VPC security groups and subnet configurations. This allows them to interact securely with other AWS services (such as RDS databases) within the same VPC. Because Lambda scales by creating many concurrent execution environments, each maintains its own database connection. High concurrency can exhaust database connection limits. For relational database access, use [Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) to pool and manage connections. This avoids connection exhaustion during high concurrency.

 The Lambda service uses a Network Function Virtualization platform to provide NAT capabilities. This connects the Lambda VPC to customer VPCs. It configures the required elastic network interfaces (ENIs) when Lambda functions are created or updated. It also enables ENIs from your account to be shared across multiple execution environments. This allows Lambda to make more efficient use of network resources when functions scale.

ENIs are an exhaustible resource with a soft limit of 250 per Region. Monitor elastic network interface usage if you configure Lambda functions for VPC access. Lambda functions in the same AZ and same security group can share ENIs. If you increase concurrency limits in Lambda, evaluate if you need an elastic network interface increase. If the limit is reached, invocations of VPC-enabled Lambda functions are throttled.

------
#### [ Pricing model ]

 **Fargate** pricing is based on the resources allocated to your containers. Specifically, this means the vCPU and memory you select for each task. You are billed per second, with a one-minute minimum charge. Costs are directly tied to the resources your application consumes. You pay for what you provision, regardless of whether the application is actively processing requests. Fargate is well-suited for predictable workloads where you need specific resource configurations. You can optimize costs by adjusting the allocated resources. Fargate Spot is available for both x86 and ARM-based Linux workloads. This provides significant cost savings for fault-tolerant applications. There might be additional charges for related services. These include data transfer, storage, and networking (for example, VPC, Elastic Load Balancing).

 **Lambda** has a different pricing structure that is event-driven and pay-per-execution. You are charged based on the number of requests and execution duration. Duration is measured in milliseconds. Lambda also factors in the amount of memory you allocate to your function. Costs scale based on the memory used and the execution time. The pricing model includes a free tier. It offers 1 million free requests and 400,000 GB-seconds of compute time per month. This makes Lambda particularly cost-effective for low-volume, sporadic workloads.

 The Lambda pricing model is ideal for applications with unpredictable or bursty traffic patterns. You only pay for actual function invocations and execution time. You do not need to provision or pay for idle capacity.

 With Lambda Managed Instances, Lambda offers instance-based pricing that uses EC2 pricing models. These include On-Demand, Reserved Instances, and Compute Savings Plans. This can drive cost efficiency for steady-state or predictable workloads.

 Both Fargate and Lambda are eligible for [Compute Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html). These can reduce costs by up to 66% in exchange for a commitment to a consistent amount of compute usage. This is measured in dollars per hour for a 1- or 3-year term.

 When you compare costs between the two services, you typically pay less with Lambda at lower traffic volumes. However, the per-second resource billing of Fargate tends to be more economical for sustained, high-throughput workloads. As request volume grows, Lambda costs scale linearly. In contrast, Fargate costs remain relatively stable regardless of requests handled within the provisioned resources.

------

## Use
<a name="fl-use"></a>

Now that you've read about the criteria for choosing between AWS Fargate and AWS Lambda, you can select the service that meets your needs, and use the following information to help you get started using each of them.

------
#### [ AWS Fargate ]
+  **Learn how to create an Amazon ECS Linux task for the Fargate launch type**

  Get started with Amazon ECS on AWS Fargate by using the Fargate launch type for your Linux tasks.

   [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-fargate.html)
+  **Learn how to create an Amazon ECS Windows task for the Fargate launch type**

   Get started with Amazon ECS on AWS Fargate by using the Fargate launch type for your Windows tasks.

   [Explore the guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Windows_fargate-getting_started.html)
+  **Getting started with Fargate and Amazon EKS**

   This guide describes how to get started running your pods on AWS Fargate with your Amazon EKS cluster.

   [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/fargate-getting-started.html)
+  **AWS Fargate pricing**

   Use this guide to understand how vCPU, memory, storage, and operating system configurations impact AWS Fargate pricing.

   [Explore the guide](https://aws.amazon.com/fargate/pricing/)
+  **AWS Fargate frequently asked questions**

   Get answers to common questions about AWS Fargate capabilities, and best practices for implementation.

   [Explore the guide](https://aws.amazon.com/fargate/faqs/)

------
#### [ AWS Lambda ]
+  **Create a serverless file-processing app**

   A step-by-step walkthrough of setting up and using Amazon SNS. It covers topics such as creating a topic, subscribing endpoints to a topic, publishing messages, and configuring access permissions.

   [Explore the guide](https://docs.aws.amazon.com/lambda/latest/dg/file-processing-app.html)
+  **Serverless Developer Guide**

   This guide helps you develop a better conceptual understanding of serverless application development, and how various AWS services fit into together to create *application patterns* that form the core of your cloud applications.

   [Explore the guide](https://docs.aws.amazon.com/serverless/latest/devguide/welcome.html)
+  **Serverless Land**

   This site brings together the latest information, blogs, videos, code, and learning resources for AWS Serverless. Learn to use and build apps that scale automatically on low-cost, fully managed serverless architecture.

   [Explore the site](https://serverlessland.com/lambda)
+  **AWS Lambda pricing**

   Use this guide to estimate expenses and optimize costs based on function usage and configuration. It includes a pricing calculator to calculate your AWS Lambda and architecture cost in a single estimate.

   [Explore the guide](https://aws.amazon.com/lambda/pricing/)
+  **AWS Lambda frequently asked questions**

   Get answers to common questions about AWS Lambda capabilities, and best practices for implementation.

   [Explore the guide](https://aws.amazon.com/lambda/faqs/)

------
