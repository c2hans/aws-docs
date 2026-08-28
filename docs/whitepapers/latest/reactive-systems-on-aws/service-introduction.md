---
source_url: https://docs.aws.amazon.com/whitepapers/latest/reactive-systems-on-aws/service-introduction.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Service introduction
<a name="service-introduction"></a>

## Amazon ECS
<a name="intro-ecs"></a>

 Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service. It is a shared state, optimistic concurrency system that provides flexible scheduling capabilities for your tasks and containers. In the reference architecture, Amazon ECS with AWS Fargate is used to run the main application which is implemented using Java. One of the objectives in the development of the application was to keep the latency as low as possible, because in this part increased latency has a negative impact on the conversion rate. For this particular use case, it’s recommended to use Amazon ECS instead of AWS Lambda. If the different components of the application were split into individual Lambda functions and these were orchestrated with AWS Step Functions, this would have a negative impact on latency, which is not a problem for many use cases, but in this particular case, keeping latency as low as possible is a very important aspect of the overall application.

## Amazon EKS
<a name="intro-eks"></a>

 [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks) (Amazon EKS) gives you the flexibility to start, run, and scale Kubernetes applications in the AWS Cloud or on-premises. Amazon EKS helps you provide highly-available and secure clusters and automates key tasks such as patching, node provisioning, and updates. Amazon EKS was not used for the implementation of the sample architecture; however, it is possible to use Amazon EKS instead of Amazon ECS.

## AWS Lambda
<a name="intro-lam"></a>

 AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers, creating workload-aware cluster scaling logic, maintaining event integrations, or managing runtimes. With Lambda, you can run code for virtually any type of application or backend service - all with zero administration. AWS Lambda's role in the example architecture is to receive messages from the Amazon Kinesis Data Stream, which is very low implementation overhead. Lambda integrates natively with Kinesis Data Streams. The polling, checkpointing, and error handling complexities are abstracted when using this integration. This allows the Lambda function code to focus on business logic processing.

## Amazon Kinesis Data Streams
<a name="intro-aks"></a>

 Amazon Kinesis Data Streams is a massively scalable and durable real-time data streaming service. In this architecture, Kinesis Data Streams is used to decouple key application components, such as processing incoming data and persisting the enriched data in Amazon DynamoDB. This split is possible because the writing of the data can be done asynchronously, while the response to the requesting client should happen as quickly as possible.

## Amazon ElastiCache
<a name="intro-elc"></a>

 Amazon ElastiCache offers a fully managed in-memory data store, compatible with Redis or Memcached that enables you to power real-time applications with sub-millisecond latency. The service can scale-out, scale-in, and scale-up to meet fluctuating application demands. Write and memory scaling is supported with sharding. In this architecture, Redis is used in two different ways: source for core data, and pub/sub implementation to actively update the L1-cache in the main application.

## Amazon DynamoDB
<a name="intro-ddb"></a>

 Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. It is a fully managed database with scalability and high availability built in. DynamoDB is used in this architecture as the central repository for the result data, since DynamoDB is fully managed, multi-region, multi-active, durable database for internet-scale applications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
