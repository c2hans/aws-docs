---
source_url: https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/security-hooks.html
---

# CloudFormation Hooks
<a name="security-hooks"></a>

AWS CloudFormation Hooks is a feature that you can use to ensure that your AWS Cloud Control API resources are compliant with your organization's security, operational, and cost optimization best practices. With Hooks, you can provide code that proactively inspects the configuration of your resources before provisioning. If non-compliant resources are found, Cloud Control API either fails the operation and prevents the resources from being provisioned, or emits a warning and allows the provisioning operation to continue. You can use Hooks to evaluate your Cloud Control API resource configurations prior to create and update operations.

## Creating a Hook to validate Cloud Control API resource configurations
<a name="security-hooks-creating"></a>

You can create a Hook to validate your Cloud Control API resource configuration using either the CloudFormation console, the AWS Command Line Interface (AWS CLI), or CloudFormation. For more information, see [Creating and managing AWS CloudFormation Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/creating-and-managing-hooks.html).

## Targeting Cloud Control API for validation
<a name="security-hooks-targeting"></a>

You can configure your CloudFormation Hooks to target `CLOUD_CONTROL` operations in your Hook’s `TargetOperations` configuration.

For more information on using `TargetOperations` with Guard Hooks, see [Write Guard rules to evaluate resources for Guard Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks-write-rules.html).

For more information on using `TargetOperations` with Lambda Hooks, see [Create Lambda functions to evaluate resources for Lambda Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/lambda-hooks-create-lambda-function.html).

## Reviewing Hook invocation results
<a name="security-hooks-reviewing"></a>

You can view the results of your invocation by calling `GetResourceRequestStatus` using the `RequestToken`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Control API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudcontrolapi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
