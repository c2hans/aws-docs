---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/pattern-serverless-ml-inference.html
---

# Pattern 1: Serverless ML inference pipeline
<a name="pattern-serverless-ml-inference"></a>

In many enterprise environments, teams need to infuse AI into operational workflows, for example, to classify user feedback, detect anomalies in incoming telemetry, or score risk in real time. These machine learning (ML)-powered features are often embedded within customer-facing applications, mobile apps, or internal automation systems.

However, traditional ML inference workloads typically require the following:
+ Pre-provisioned compute such as Amazon Elastic Compute Cloud (Amazon EC2) instances and containers
+ Manual scaling policies
+ Persistent infrastructure even when idle
+ Complex deployment and monitoring pipelines

These requirements result in the following:
+ Underutilized resources for sporadic inference
+ Operational complexity for model versioning, failover, and auto-scaling
+ Increased cost, particularly for low-frequency or bursty workloads

Moreover, engineering teams often lack the specialized ML infrastructure skills to maintain this complexity, and AI adoption stalls at the prototype phase.

## The serverless ML inference pattern: Lightweight, event-driven, scalable
<a name="the-serverless-ml-inference-pattern--lightweight--event-driven--scalable.7453c825-a6a6-5917-90d7-b9b1532770ff"></a>

The serverless ML inference pipeline pattern uses fully managed, event-driven AWS services to eliminate the infrastructure burden. This approach enables inference workflows that trigger and run only when needed and scale automatically with demand.

This pattern is ideal to do the following tasks:
+ Run lightweight ML models that are trained in Amazon SageMaker or locally.
+ Perform classification, scoring, or transformation in near real-time.
+ Embed ML logic in microservices, APIs, or data ingestion pipelines.

The reference architecture implements each layer as follows:
+ **Event trigger** – Uses [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) for user requests, [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) for business events, and [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) for data uploads.
+ **Processing layer** – Implements [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) to normalize input, validate schema, and enrich metadata.
+ **Inference layer** – Deploys [SageMaker Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) endpoint to perform classification, regression, or scoring.
+ **Post-processing** – Uses Lambda to format the response, store logs, and emit new events.
+ **Output** – Implements API Gateway to return results to users or publishes events to EventBridge for downstream processing.

**Note**
This entire pipeline can deploy as infrastructure as code (IaC) by using AWS Cloud Development Kit (AWS CDK) or AWS Serverless Application Model (AWS SAM), versioned, and observable.

## Use case: Sentiment classification for customer feedback
<a name="use-case--sentiment-classification-for-customer-feedback.c622447f-bc08-528e-b87f-2d697fc8919a"></a>

A global ecommerce company wants to classify the customer feedback left on product reviews or support tickets to identify detractors early and prioritize follow-up. The classification system must address the following requirements:
+ Traffic is highly variable with spikes during campaign periods.
+ Inference must occur in real time to integrate with the support triage system.
+ The model is lightweight (100ms inference latency) and trained in SageMaker.

For this use case, the serverless inference pipeline solution consists of the following steps:

1. User feedback is submitted to API Gateway which then sends it to EventBridge.

1. Lambda preprocesses and formats the text payload.

1. The SageMaker Serverless Inference endpoint runs a sentiment classification model.

1. Lambda routes "negative" results to the support escalation queue.

1. Results are logged in Amazon DynamoDB for analytics and retraining.

## Business value of the serverless ML inference pipeline
<a name="business-value-of-the-serverless-ml-inference-pipeline.c63eac9d-40d9-595b-aa68-0b83a70bf02a"></a>

The serverless ML inference pipeline delivers value in the following areas:
+ **Scalability** – Automatically scales to thousands of inferences per minute with no manual tuning
+ **Cost efficiency** – Pays only for execution time with zero cost during idle periods
+ **Developer velocity** – Enables teams to deploy end-to-end AI inference workflows without managing infrastructure
+ **Resilience** – Provides built-in retries, logging, and stateless execution to ensure robustness
+ **Observability** – Monitors model usage, input and output volumes, and latency by using Amazon CloudWatch and AWS X-Ray

The serverless ML inference pipeline is the entry point for many organizations looking to adopt AI incrementally and pragmatically. It's the ideal pattern to achieve the following objectives:
+ Real-time, low-latency AI
+ Cost-efficient deployment of traditional ML models
+ Seamless integration with modern serverless and event-driven systems

By abstracting away the infrastructure, teams can focus on the business logic, model accuracy, and delivering real value, without sacrificing operational control or scalability.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
