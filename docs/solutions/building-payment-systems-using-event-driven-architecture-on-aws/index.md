---
source_url: https://docs.aws.amazon.com/solutions/building-payment-systems-using-event-driven-architecture-on-aws/index.html
---

---
title: 'Guidance for Building Payment Systems Using Event-Driven Architecture on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-payment-systems-using-event-driven-architecture-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Building Payment Systems Using Event-Driven Architecture on AWS

## Overview

This Guidance demonstrates near real-time processing of account posting events for payment systems. Payment systems must persistently store and idempotently process all customer transactions and activities to maintain data integrity, requiring relational databases with transactional capabilities. These applications often use synchronous requests and must commit transactions to databases one by one rather than concurrently. This Guidance aims to create asynchronous, event-driven architectural patterns in a system that you can automatically deploy in your environment through infrastructure as code (IaC).

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-payment-systems-using-event-driven-architecture-on-aws.pdf)

![Architecture diagram](/images/solutions/building-payment-systems-using-event-driven-architecture-on-aws/images/building-payment-systems-using-event-driven-architecture-on-aws-1.png)

1. **Step 1**: Your user initiates a payment, which the authorization application approves and persists to an Amazon DynamoDB table.
1. **Step 2**: An Amazon EventBridge pipe reads the approved authorization records from the DynamoDB table stream and publishes events to an EventBridge custom event bus.
1. **Step 3**: You can add duplicate checking logic to the EventBridge pipe through an AWS Lambda deduplication function.
1. **Step 4**: An EventBridge rule invokes an enrichment Lambda function for matching events to add context like account type and bank details.
1. **Step 5**: The Lambda function queries the metadata and publishes a new event containing the extra info to the EventBridge custom event bus.
1. **Step 6**: An EventBridge rule watching for enriched events invokes an AWS Step Functions workflow to apply business rules to the event as part of a rules engine.
1. **Step 7**: When an event passes all business rules, the Step Functions workflow publishes a new event back to the EventBridge custom event bus.
1. **Step 8**: An EventBridge rule adds a message to an Amazon Simple Queue Service (Amazon SQS) queue as a buffer to avoid overrunning the downstream posting subsystem.
1. **Step 9**: A Lambda function reads from the Amazon SQS queue and invokes the downstream posting subsystem to post the transaction.
1. **Step 10**: The Lambda function publishes the final event back to the EventBridge custom event bus.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/compute/building-payment-systems-using-event-driven-architecture-on-aws.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-building-event-driven-payment-systems-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS CloudFormation helps you automate your infrastructure building and deployment through IaC templates, helping you limit human error and make small, repeatable, incremental, and reversible changes. AWS X-Ray traces functions and events, generating an application topology map that you can use to improve performance and identify bottlenecks during troubleshooting. Amazon CloudWatch acts as the central telemetry storage and provides log collection, dashboards, alarms, and analysis capabilities from Lambda and Step Functions. AWS CloudTrail monitors and records all API activities across your AWS accounts, giving you the ability to audit activity or API calls made to EventBridge, Lambda, and Step Functions. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) establishes a strong identity and authorization foundation, and you can set up identity-based policies following the least-privilege principle to limit the access Lambda, Step Functions, and EventBridge have to downstream AWS services. You can also use resource-based policies to limit access further. Additionally, this Guidance lets you encrypt sensitive data from start to finish. AWS Key Management Service (AWS KMS) provides the ability to securely decrypt and encrypt data at rest. Step Functions and EventBridge encrypt data at rest and in transit, and Lambda encrypts data in transit. You can securely store Lambda code secrets using AWS Secrets Manager. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance enables you to use EventBridge, Lambda, and Step Functions in combination to create an event-driven, fault-tolerant architecture. These three services are regional and are deployed across multiple Availability Zones (AZs). EventBridge uses buses and rules to enable a publish-subscribe model with downstream targets, and this model enables loose coupling, enabling components to scale independently. Powertools for AWS Lambda (Python) lets you write and implement idempotent functions so that each request is completed exactly once. Lambda functions are stateless by design and can scale independently, and Lambda sends failed requests to an Amazon SQS dead letter queue for fault isolation and further troubleshooting. Step Functions provides built-in error handling, time-outs, and parallel processing to handle your distributed application reliably. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda manages its own scaling mechanism when invoked asynchronously by EventBridge, and the serverless architecture removes the need for you to run and maintain physical servers for compute activities. Step Functions orchestrates business processes, and in the event of a time-out, you can gracefully terminate long-running or stuck calls or implement an alternative task. Additionally, DynamoDB is inherently designed to process large volumes of data with high performance. Its on-demand mode enables it to serve a large number of requests without any capacity planning. By carefully designing the DynamoDB primary key, you can build tables with a large number of distinct values and avoid throttling while reading or writing. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses serverless services with a pay-for-value billing model, so you can lower your total application cost because you don't pay for overprovisioning, and resource utilization is optimized on your behalf. This also lowers your operational costs, because you don’t have to manage the infrastructure or create patches. Additionally, EventBridge pipes provide a consistent and cost-effective way to create point-to-point integration between event producers and consumers. The DynamoDB on-demand capacity mode scales based on traffic and helps you avoid overprovisioning or underprovisioning database resources. Additionally, you can use Arm-based Lambda architecture powered by AWS Graviton2 processors to gain up to 20 percent cost efficiency. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The architecture uses AWS serverless services, which are elastic by design and only provision the resources necessary to complete the required tasks. The use of AWS Graviton2 processors in Lambda can deliver up to 19 percent better performance at 20 percent lower cost, reducing your energy consumption. By using direct service integration with Step Functions, you can further reduce the carbon footprint of your workload and avoid running unnecessary components. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
