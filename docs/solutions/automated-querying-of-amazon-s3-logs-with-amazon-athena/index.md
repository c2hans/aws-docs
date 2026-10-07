---
source_url: https://docs.aws.amazon.com/solutions/automated-querying-of-amazon-s3-logs-with-amazon-athena/index.html
---

---
title: 'Guidance for Automated Querying of Amazon S3 Logs with Amazon Athena'
canonical_url: https://docs.aws.amazon.com/solutions/automated-querying-of-amazon-s3-logs-with-amazon-athena/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Automated Querying of Amazon S3 Logs with Amazon Athena

## Overview

The Guidance demonstrates an automated workflow for users to easily query and identify requests from various Amazon Simple Storage Service (Amazon S3) related logs. By deploying the provided AWS CloudFormation stack, users can set up the necessary infrastructure to automatically copy and process their Amazon S3 logs. The workflow uses Amazon Athena, a serverless query service, to enable users to run SQL queries against the log data and identify potential security or operational issues.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automated-querying-of-amazon-s3-logs-with-amazon-athena.pdf)

![Architecture diagram](/images/solutions/automated-querying-of-amazon-s3-logs-with-amazon-athena/images/automated-querying-of-amazon-s3-logs-with-amazon-athena-1.png)

1. **Step 1**: Deploy the Guidance as a stack by uploading the template into the AWS CloudFormation console.
1. **Step 2**: CloudFormation deploys the necessary resources, including AWS Lambda custom resources.
1. **Step 3**: The Lambda custom resource function submits an Amazon Simple Storage Service (Amazon S3) batch operations job to copy logs based on the prefix and date parameters defined in the stack.
1. **Step 4**: The Amazon S3 batch operations job automatically generates a manifest file and copies the logs to a prefix in the Amazon S3 solution bucket.
1. **Step 5**: When the copy job is complete, an Amazon S3 event invokes the Lambda job tracker function.
1. **Step 6**: The Lambda job tracker function verifies the copy job is complete. A Lambda query function is then invoked for Amazon Athena.
1. **Step 7**: The Lambda function responsible for Athena queries submits a query based on the user's specifications, such as "Anonymous Access."
1. **Step 8**: Athena saves the query results to the Amazon S3 solution bucket.
1. **Step 9**: The Lambda query tracker function publishes a message to Amazon Simple Notification Service (Amazon SNS) indicating that the Athena query has completed, along with the location of the query results in a CSV format.
1. **Step 10**: The Amazon SNS topic sends the message from the Lambda query tracker through email to the user.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-automated-querying-of-amazon-s3-logs-with-amazon-athena)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses CloudFormation for comprehensive resource deployment tracking and visibility. In addition, Lambda records operational events in Amazon CloudWatch logs, while Amazon SNS delivers near real-time workflow status notifications. Moreover, Amazon S3 batch operations execute copy operations at scale, providing detailed completion reports at both task and aggregate levels. This combination enables rapid issue identification and root cause analysis through detailed logging and monitoring capabilities. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Security best practices are implemented with AWS Identity and Access Management (IAM), employing the principle of least privilege. Each component, particularly the Lambda functions, operates with permissions scoped to only those required for their specific tasks. This granular access control minimizes the potential attack surface area. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This architecture supports highly available workloads through multiple AWS services. First, Lambda is serverless and is designed to automatically scale as the number of concurrent request increases; this service also runs each function across multiple Availability Zones (AZs) to help ensure high availability. Second, Amazon SNS stores each message it receives across multiple AZs, and it delivers each message at least once. Third, Amazon S3 provides a reliable and durable storage across multiple AZs for the Amazon S3 logs that needs to be queried. Fourth, Amazon S3 batch operations provides a purpose built feature to perform reliable large-scale object copy with error retries and scaling. Lastly, the AWS Software Development Kit (AWS SDK) is optimized to perform retries and backoff to handle transient errors. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda enables parallel API request processing, while Athena provides SQL-based querying capabilities that scale automatically with data volume. In addition, Amazon S3 batch operations handles billions of objects efficiently, and Amazon S3 delivers consistent low-latency access to log data. This serverless approach eliminates infrastructure management overhead while maintaining high performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance minimizes costs through serverless computing and efficient storage management. Specifically, Amazon S3 lifecycle rules automatically expire unnecessary data, while Lambda charges only for actual compute time used. And, the pay-per-query model of Athena eliminates the need for persistent query infrastructure. Lastly, Amazon S3 batch operations provides cost-effective bulk operations without requiring dedicated compute resources. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance promotes sustainability through efficient resource utilization. Event-driven Lambda functions only consume resources when needed, while Amazon S3 lifecycle policies automatically remove unnecessary data. The serverless architecture eliminates idle resource waste, and the solution's automated scaling helps ensure resources match actual demand. Finally, integration with Amazon SNS enables efficient message delivery without the users having to maintain dedicated infrastructures. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
