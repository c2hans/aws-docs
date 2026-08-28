---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-supported-dependency-types.html
---

# Supported dependency types
<a name="next-gen-supported-dependency-types"></a>

Dependency discovery identifies the following types of dependencies:
+ **AWS service endpoints** – Amazon S3, Amazon DynamoDB, SQS, and other AWS services your application calls.
+ **Internal endpoints** – Services within your VPC or organization.
+ **Third-party endpoints** – External services such as LaunchDarkly, Stripe, or Datadog.
+ **Cross-region calls** – Dependencies that resolve to endpoints in other AWS Regions.

Each discovered dependency is categorized by type:

| Type | Description | Example |
| --- | --- | --- |
| AWS service | An AWS service endpoint | Amazon S3, Amazon DynamoDB, SQS |
| Third-party | A service outside AWS and your organization | LaunchDarkly, Stripe, Datadog |
| Internal | A service within your organization | Internal microservices, shared APIs |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
