---
source_url: https://docs.aws.amazon.com/solutions/incremental-data-exports-from-amazon-dynamodb-to-amazon-s3/index.html
---

---
title: 'Guidance for Incremental Data Exports from Amazon DynamoDB to Amazon S3'
canonical_url: https://docs.aws.amazon.com/solutions/incremental-data-exports-from-amazon-dynamodb-to-amazon-s3/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Incremental Data Exports from Amazon DynamoDB to Amazon S3

## Overview

This Guidance shows how the Amazon DynamoDB continuous incremental exports feature can help capture and transfer ongoing data changes between DynamoDB tables. By starting with a full export to set up a new table and then applying incremental updates, users can keep their tables synchronized across different AWS accounts and AWS Regions. This approach offers an alternative to traditional disaster recovery (DR) solutions, especially for situations where data recovery needs to happen within 30 minutes or longer. Unlike global tables, which require constant updates to a secondary table, the export method allows for creating and loading the secondary table only when needed for recovery. This flexibility makes it easier to manage data and maintain multiple copies effectively.

## How it works

This architecture diagram demonstrates a serverless workflow to achieve continuous data exports from Amazon DynamoDB to Amazon Simple Storage Service (Amazon S3) using the DynamoDB incremental exports feature.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/incremental-data-exports-from-amazon-dynamodb-to-amazon-s3.pdf?target=_blank)

![Architecture diagram](/images/solutions/incremental-data-exports-from-amazon-dynamodb-to-amazon-s3/images/incremental-data-exports-from-amazon-dynamodb-to-amazon-s3-1.png)

1. **Step 1**: The Amazon EventBridge Scheduler is configured to execute at a frequency exceeding the required export window with the capability to catch up on any missed exports if necessary.
1. **Step 2**: The AWS Step Functions workflow is initialized by retrieving the current state information from the AWS Systems Manager Parameter Store. This allows for the execution of state-specific actions, such as handling a paused workflow scenario.
1. **Step 3**: Perform any necessary sanity checks, such as verifying the existence of the table and confirming that point-in-time recovery (PITR) is enabled.
1. **Step 4**: The state information is evaluated to determine if a full export is required for the capture of the complete dataset from the table as the initial step.
1. **Step 5**: To initiate the export of the table, the workflow invokes the Amazon DynamoDB API.
1. **Step 6**: The export operation starts writing the data, along with the associated manifest and summary, to the specified Amazon Simple Storage Service (Amazon S3) bucket and prefix.
1. **Step 7**: The workflow pauses execution and waits for the full export operation to complete before proceeding to the next step. Additional validation checks can be performed at this stage to confirm whether the full export was successfully executed.
1. **Step 8**: State information is written to the Parameter Store to record the outcome.
1. **Step 9**: A notification is sent to the end user through an Amazon Simple Notification Service (Amazon SNS) topic.
1. **Step 10**: The workflow execution concludes, terminating in either a successful or failed state.
1. **Step 11**: The incremental export operation first verifies that PITR has remained continuously enabled since the completion of the full export. If PITR is disabled at any point, the PITR history is wiped, resulting in a gap in the data.
1. **Step 12**: The incremental export operation requires two time values. The start time value is passed as input to an AWS Lambda function, along with the desired export window. The Lambda function then returns the end time value, as well as any other necessary information.
1. **Step 13**: The workflow invokes the DynamoDB API to export the table with extra parameters as required by the incremental export API. This is then followed by a similar flow as before: the exported data is written to the Amazon S3 bucket.
1. **Step 14**: The workflow waits for the incremental export to finish before moving to the next step. More checks can be executed here to check whether the incremental export completed successfully or not.
1. **Step 15**: State information is written to the Parameter Store to record the outcome of the operation.
1. **Step 16**: A notification is sent to the end user through an Amazon SNS topic.
1. **Step 17**: The workflow execution concludes, terminating in either a successful or failed state.
1. **Step 18**: AWS Key Management Service (AWS KMS), AWS X-Ray, and Amazon CloudWatch Logs are used to provide encryption keys, traceability, and logging capabilities, respectively.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-incremental-data-exports-from-amazon-dynamodb-to-amazon-s3)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The services used in this Guidance provide capabilities for infrastructure as code, workflow orchestration, serverless computing, and observability. Specifically, the AWS Cloud Development Kit (AWS CDK) allows the Guidance to be deployed using infrastructure as code, making it easy to manage and update. Step Functions provides a visual workflow with capabilities for orchestration, debugging, retries, and monitoring. Lambda enables complex functionality, such as time manipulation. All logs are centralized in CloudWatch, and X-Ray provides end-to-end traceability. Together, these services make this Guidance easy to deploy, manage, and troubleshoot. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance includes services with capabilities for access control, encryption, and configuration management. For example, AWS Identity and Access Management (IAM) allows granular control over AWS services to help ensure least privilege access, and the IAM roles used by Step Functions are scoped to only the necessary resources and services. The Amazon S3 bucket and Amazon SNS topic enforce SSL connectivity. In addition, encryption at rest is enabled using AWS KMS, while TLS helps ensure encrypted communication between services. This Guidance also uses the Systems Manager Parameter Store to store state information, further reducing the need for human interaction. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Step Functions incorporates built-in mechanisms to handle exceptions and automatically retry when necessary while Systems Manager manages the required state information. These services allow the Guidance to automatically recover from known failure modes through the retry capabilities inherent to Step Functions, as well as the state information stored in the Systems Manager Parameter Store. Furthermore, as the workflow is entirely serverless, there is no need to manually manage capacity. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses advanced serverless technologies so that the most suitable service is used for each specific task. For example, it uses the Systems Manager Parameter Store for managing state information and Lambda for handling complex time-related operations. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The various services used within this Guidance, including Step Functions, can be fine-tuned through the adjustment of multiple parameters. This flexibility enables users to control the frequency at which the incremental exports are executed. For instance, implementing longer export windows would result in fewer runs, albeit potentially larger export files. Additionally, users can use the lifecycle management features of Amazon S3 to transition older data objects to more cost-effective storage classes, further optimizing the overall expenditure. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

In a traditional, server-based infrastructure, organizations often need to provision computing resources to handle peak workloads, leading to significant over-provisioning and underutilization of hardware during off-peak periods. This inefficient use of resources can have a detrimental impact on the environment. By adopting a serverless approach, this Guidance helps ensure that computing resources are only used when actively required, automatically scaling the underlying infrastructure based on real-time demands. This dynamic scaling optimizes resource utilization and reduces the overall carbon footprint and energy consumption associated with the infrastructure. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
