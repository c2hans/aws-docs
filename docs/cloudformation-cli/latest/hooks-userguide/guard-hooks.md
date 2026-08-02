---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/guard-hooks.html
---

# Guard Hooks
<a name="guard-hooks"></a>

To use an AWS CloudFormation Guard Hook in your account, you must *activate* the Hook for the account and Region where you want to use it. Activating a Hook makes it usable in stack operations in the account and Region where it's activated.

When you activate a Guard Hook, CloudFormation creates an entry in your account's registry for the activated Hook as a private Hook. This allows you to set any configuration properties the Hook includes. Configuration properties define how the Hook is configured for a given AWS account and Region.

**Topics**
+ [AWS CLI commands for working with Guard Hooks](#commonly-used-commands-guard-hooks)
+ [Write Guard rules to evaluate resources for Guard Hooks](guard-hooks-write-rules.md)
+ [Prepare to create a Guard Hook](guard-hooks-prepare-to-create-hook.md)
+ [Activate a Guard Hook in your account](guard-hooks-activate-hooks.md)
+ [View logs for the Guard Hooks in your account](guard-hooks-view-logs.md)
+ [Delete Guard Hooks in your account](guard-hooks-delete-hooks.md)

## AWS CLI commands for working with Guard Hooks
<a name="commonly-used-commands-guard-hooks"></a>

The AWS CLI commands for working with Guard Hooks include:
+ [https://docs.aws.amazon.com/cli/latest/reference/cloudformation/activate-type.html](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/activate-type.html) to start the activation process for a Guard Hook.
+ [https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html) to specify the configuration data for a Hook in your account.
+ [https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-types.html](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-types.html) to list the Hooks in your account.
+ [https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html) to return detailed information about a specific Hook or specific Hook version, including current configuration data.
+ [https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deactivate-type.html](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deactivate-type.html) to remove a previously activated Hook from your account.
