---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/ce-api.html
---

# Using the AWS Cost Explorer API
<a name="ce-api"></a>

The Cost Explorer API allows you to programmatically query your cost and usage data. You can query for aggregated data such as total monthly costs or total daily usage. You can also query for granular data, such as the number of daily write operations for DynamoDB database tables in your production environment.

If you use a programming language that AWS provides an SDK for, we recommend that you use the SDK. All the AWS SDKs greatly simplify the process of signing requests and save you a significant amount of time when compared with using the AWS Cost Explorer API. In addition, the SDKs integrate easily with your development environment and provide easy access to related commands.

For more information about available SDKs, see [Tools for Amazon Web Services](https://aws.amazon.com/tools). For more information about the AWS Cost Explorer API, see the [AWS Billing and Cost Management API Reference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/).

## Service endpoint
<a name="ce-endpoint"></a>

The Cost Explorer API provides the following endpoint:

https://ce.us-east-1.amazonaws.com

## Granting IAM permissions to use the AWS Cost Explorer API
<a name="ce-iam"></a>

A user must be granted explicit permission to query the AWS Cost Explorer API. For the policy that grants the necessary permissions to a user, see [View costs and usage](billing-example-policies.md#example-policy-ce-api).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
