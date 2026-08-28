---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/lambda-hooks.html
---

# Lambda Hooks
<a name="lambda-hooks"></a>

To use an AWS Lambda Hook in your account, you must first *activate* the Hook for the account and Region where you want to use it. Activating a Hook makes it usable in stack operations in the account and Region where it's activated.

When you activate a Lambda Hook, CloudFormation creates an entry in your account's registry for the activated Hook as a private Hook. This allows you to set any configuration properties the Hook includes. Configuration properties define how the Hook is configured for a given AWS account and Region.

**Topics**
+ [AWS CLI commands for working with Lambda Hooks](#commonly-used-commands-lambda-hooks)
+ [Create Lambda functions to evaluate resources for Lambda Hooks](lambda-hooks-create-lambda-function.md)
+ [Prepare to create a Lambda Hook](lambda-hooks-prepare-to-create-hook.md)
+ [Activate a Lambda Hook in your account](lambda-hooks-activate-hooks.md)
+ [View logs for the Lambda Hooks in your account](lambda-hooks-view-logs.md)
+ [Delete Lambda Hooks in your account](lambda-hooks-delete-hooks.md)

## AWS CLI commands for working with Lambda Hooks
<a name="commonly-used-commands-lambda-hooks"></a>

The AWS CLI commands for working with Lambda Hooks include:
+ [activate-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/activate-type.html) to start the activation process for a Lambda Hook.
+ [set-type-configuration](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html) to specify the configuration data for a Hook in your account.
+ [list-types](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-types.html) to list the Hooks in your account.
+ [describe-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html) to return detailed information about a specific Hook or specific Hook version, including current configuration data.
+ [deactivate-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deactivate-type.html) to remove a previously activated Hook from your account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
