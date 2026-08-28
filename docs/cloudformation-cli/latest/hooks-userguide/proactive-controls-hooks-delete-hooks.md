---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/proactive-controls-hooks-delete-hooks.html
---

# Delete proactive control-based Hooks in your account
<a name="proactive-controls-hooks-delete-hooks"></a>

When you no longer need an activated proactive control-based Hook, use the following procedures to delete it in your account.

To temporarily disable a Hook instead of deleting it, see [Disable and enable CloudFormation Hooks](hooks-disable-enable.md).

**Topics**
+ [Delete a proactive control-based Hook in your account (console)](#proactive-controls-hooks-delete-hook-console)
+ [Delete a proactive control-based Hook in your account (AWS CLI)](#proactive-controls-hooks-delete-hook-cli)

## Delete a proactive control-based Hook in your account (console)
<a name="proactive-controls-hooks-delete-hook-console"></a>

**To delete a proactive control-based Hook in your account**

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. On the navigation bar at the top of the screen, choose the AWS Region where the Hook is located.

1. From the navigation pane, choose **Hooks**.

1. On the **Hooks** page, find the proactive control-based Hook you want to delete.

1. Select the check box next to your Hook and choose **Delete**.

1. When prompted for confirmation, type out the Hook name to confirm deleting the specified Hook and then choose **Delete**.

## Delete a proactive control-based Hook in your account (AWS CLI)
<a name="proactive-controls-hooks-delete-hook-cli"></a>

**Note**
Before you can delete the Hook, you must first disable it. For more information, see [Disable and enable a Hook in your account (AWS CLI)](hooks-disable-enable.md#hooks-disable-enable-cli).

Use the following [deactivate-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deactivate-type.html) command to deactivate a Hook, which removes it from your account. Replace placeholders with your specific values.

```
aws cloudformation deactivate-type \
  --type-arn {{"arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyOrg-Security-ComplianceHook"}} \
  --region {{us-west-2}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
