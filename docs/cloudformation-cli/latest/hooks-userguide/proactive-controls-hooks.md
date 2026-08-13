---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/proactive-controls-hooks.html
---

# AWS Control Tower proactive controls as Hooks
<a name="proactive-controls-hooks"></a>

The AWS Control Tower Control Catalog provides pre-built compliance rules (proactive controls) that you can implement as Hooks. This approach saves setup time and helps you validate resource configurations against AWS best practices across your organization without writing code.

Proactive controls evaluate AWS resources before deployment, preventing non-compliant resources from being created rather than detecting issues later. They check configurations against established security, operational, and governance standards.

To get started, simply activate proactive control-based Hooks in your desired account and Region. These Hooks will then evaluate specific target types to ensure compliance with your selected controls.

For more information about available proactive controls, see the [AWS Control Tower Control Catalog](https://docs.aws.amazon.com/controltower/latest/controlreference/controls-reference.html).

**Topics**
+ [AWS CLI commands for working with Hooks](#commonly-used-commands-proactive-controls-hooks)
+ [Activate a proactive control-based Hook in your account](proactive-controls-hooks-activate-hooks.md)
+ [Delete proactive control-based Hooks in your account](proactive-controls-hooks-delete-hooks.md)

## AWS CLI commands for working with Hooks
<a name="commonly-used-commands-proactive-controls-hooks"></a>

The AWS CLI commands for working with proactive control-based Hooks include:
+ [activate-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/activate-type.html) to start the activation process for a proactive control-based Hook.
+ [set-type-configuration](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html) to specify the controls to apply to a proactive control-based Hook in your account.
+ [list-types](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-types.html) to list the Hooks in your account.
+ [describe-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html) to return detailed information about a specific Hook or specific Hook version, including current configuration data.
+ [deactivate-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deactivate-type.html) to remove a previously activated Hook from your account.
