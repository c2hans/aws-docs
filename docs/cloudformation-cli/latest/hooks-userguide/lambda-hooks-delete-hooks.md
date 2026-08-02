---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/lambda-hooks-delete-hooks.html
---

# Delete Lambda Hooks in your account
<a name="lambda-hooks-delete-hooks"></a>

When you no longer need an activated Lambda Hook, use the following procedures to delete it in your account.

To temporarily disable a Hook instead of deleting it, see [Disable and enable CloudFormation Hooks](hooks-disable-enable.md).

**Topics**
+ [Delete a Lambda Hook in your account (console)](#lambda-hooks-delete-hook-console)
+ [Delete a Lambda Hook in your account (AWS CLI)](#lambda-hooks-delete-hook-cli)

## Delete a Lambda Hook in your account (console)
<a name="lambda-hooks-delete-hook-console"></a>

**To delete a Lambda Hook in your account**

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. On the navigation bar at the top of the screen, choose the AWS Region where the Hook is located.

1. From the navigation pane, choose **Hooks**.

1. On the **Hooks** page, find the Lambda Hook you want to delete.

1. Select the check box next to your Hook and choose **Delete**.

1. When prompted for confirmation, type out the Hook name to confirm deleting the specified Hook and then choose **Delete**.

## Delete a Lambda Hook in your account (AWS CLI)
<a name="lambda-hooks-delete-hook-cli"></a>

**Note**
Before you can delete the Hook, you must first disable it. For more information, see [Disable and enable a Hook in your account (AWS CLI)](hooks-disable-enable.md#hooks-disable-enable-cli).

Use the following [https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deactivate-type.html](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deactivate-type.html) command to deactivate a Hook, which removes it from your account. Replace placeholders with your specific values.

```
aws cloudformation deactivate-type \
  --type-arn {{"arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyTestHook"}} \
  --region {{us-west-2}}
```
