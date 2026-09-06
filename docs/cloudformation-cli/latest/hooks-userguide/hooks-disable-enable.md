---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-disable-enable.html
---

# Disable and enable CloudFormation Hooks
<a name="hooks-disable-enable"></a>

This topic describes how to disable and then re-enable a Hook to temporarily prevent it from being active in your account. Disabling Hooks can be useful when you need to investigate an issue without interference from Hooks.

## Disable and enable a Hook in your account (console)
<a name="hooks-disable-enable-console"></a>

**To disable a Hook in your account**

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. On the navigation bar at the top of the screen, choose the AWS Region where the Hook is located.

1. From the navigation pane, choose **Hooks**.

1. Choose the name of the Hook you want to disable.

1. On the Hook details page, to the right of the Hook's name, choose the **Disable** button.

1. When prompted for confirmation, choose **Disable Hook**.

**To re-enable a previously disabled Hook**

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. On the navigation bar at the top of the screen, choose the AWS Region where the Hook is located.

1. From the navigation pane, choose **Hooks**.

1. Choose the name of the Hook you want to enable.

1. On the Hook details page, to the right of the Hook's name, choose the **Enable** button.

1. When prompted for confirmation, choose **Enable Hook**.

## Disable and enable a Hook in your account (AWS CLI)
<a name="hooks-disable-enable-cli"></a>

**Important**
The AWS CLI commands for disabling and enabling Hooks replace the entire Hook configuration with the values specified in the `--configuration` option. To avoid unintended changes, you must include all existing settings you wish to keep when running these commands. To view the current configuration data, use the [describe-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-type.html) command.

**To disable a Hook**
Use the following [set-type-configuration](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html) command and specify `HookInvocationStatus` as `DISABLED` to disable the Hook. Replace the placeholders with your specific values.

```
aws cloudformation set-type-configuration \
  --configuration "{"CloudFormationConfiguration":{"HookConfiguration":{"HookInvocationStatus": "DISABLED", "FailureMode": {{"FAIL"}}, "TargetOperations": {{["STACK","RESOURCE","CHANGE_SET"]}}, "Properties":{{{}}}}}}" \
  --type-arn {{"arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyTestHook"}} \
  --region {{us-west-2}}
```

**To re-enable a previously disabled Hook**
Use the following [set-type-configuration](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-configuration.html) command and specify `HookInvocationStatus` as `ENABLED` to re-enable the Hook. Replace the placeholders with your specific values.

```
aws cloudformation set-type-configuration \
  --configuration "{"CloudFormationConfiguration":{"HookConfiguration":{"HookInvocationStatus": "ENABLED", "FailureMode": {{"FAIL"}}, "TargetOperations": {{["STACK","RESOURCE","CHANGE_SET"]}}, "Properties":{{{}}}}}}" \
  --type-arn {{"arn:aws:cloudformation:us-west-2:123456789012:type/hook/MyTestHook"}} \
  --region {{us-west-2}}
```

For more information, see [Hook configuration schema syntax reference](hook-configuration-schema.md).
