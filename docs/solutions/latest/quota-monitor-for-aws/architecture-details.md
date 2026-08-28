---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section describes the components and AWS services that make up this solution and the architecture details on how these components work together.

## AWS services in this solution
<a name="aws-services-in-this-solution"></a>

| AWS service | Description |
| --- | --- |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  **Core.** Monitors quota usage |
|  [Service Quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)  |  **Core.** Manages the quotas for your AWS services |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  |  **Core.** Deploys the solution templates in your account(s) |
|  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)  |  **Core.** Monitors quota usage and recommends resource deletion or quota increases |
|  [Amazon SNS](https://aws.amazon.com/sns/)  |  **Supporting.** Sends notification alerts when you reach the quota usage threshold |
|  [Amazon SQS](https://aws.amazon.com/sqs/)  |  **Supporting.** Used as a dead-letter queue for asynchronously-invoked Lambda functions |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Supporting.** Deploys the functions to manage deployments, notifications, and querying quota usages |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  **Supporting.** Deploys tables for the list of services, quotas monitored, and a summarizer |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  |  **Supporting.** Connects solution components by routing events |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  **Supporting.** Saves parameters such as notification configurations, OU IDs, or account IDs |
|  [AWS Organizations](https://aws.amazon.com/organizations/)  |  **Optional.** Supports management of resources from manager and delegated administrator accounts |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quota Monitor for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
