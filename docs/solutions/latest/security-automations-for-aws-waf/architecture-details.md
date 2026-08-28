---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section describes the components and AWS services that make up this solution and the architecture details on how these components work together.

## AWS services in this solution
<a name="aws-services-in-this-solution"></a>

| AWS service | Description |
| --- | --- |
|  [AWS WAF](https://aws.amazon.com/waf/)  |  **Core**. Deploys an AWS WAF web ACL, AWS Managed Rules rule groups, custom rules, and IP sets. Makes AWS WAF API calls to block common attacks and secure web applications. |
|  [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/)  |  **Core**. Delivers AWS WAF logs to Amazon S3 buckets. |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  **Core**. Stores AWS WAF, CloudFront, and ALB logs. |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Core**. Deploys multiple Lambda functions to support custom rules. |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  |  **Core**. Creates events rules to invoke Lambda. |
|  [Amazon Athena](https://aws.amazon.com/athena/)  |  **Supporting**. Creates Athena queries and work groups to support the Athena log parser. |
|  [AWS Glue](https://aws.amazon.com/glue/)  |  **Supporting**. Creates databases and tables to support the Athena log parser. |
|  [Amazon SNS](https://aws.amazon.com/sns/)  |  **Supporting**. Sends Amazon Simple Notification Service (Amazon SNS) email notifications to support IP retention on allowed and denied lists. |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  **Supporting**. Provides application-level resource monitoring and visualization of resource operations and cost data. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Automations for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
