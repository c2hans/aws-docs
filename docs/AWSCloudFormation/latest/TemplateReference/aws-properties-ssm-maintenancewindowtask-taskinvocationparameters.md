---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::MaintenanceWindowTask TaskInvocationParameters
<a name="aws-properties-ssm-maintenancewindowtask-taskinvocationparameters"></a>

The `TaskInvocationParameters` property type specifies the task execution parameters for a maintenance window task in AWS Systems Manager.

`TaskInvocationParameters` is a property of the [AWS::SSM::MaintenanceWindowTask](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html) property type.

## Syntax
<a name="aws-properties-ssm-maintenancewindowtask-taskinvocationparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-maintenancewindowtask-taskinvocationparameters-syntax.json"></a>

```
{
  "[MaintenanceWindowAutomationParameters](#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowautomationparameters)" : {{MaintenanceWindowAutomationParameters}},
  "[MaintenanceWindowLambdaParameters](#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowlambdaparameters)" : {{MaintenanceWindowLambdaParameters}},
  "[MaintenanceWindowRunCommandParameters](#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowruncommandparameters)" : {{MaintenanceWindowRunCommandParameters}},
  "[MaintenanceWindowStepFunctionsParameters](#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowstepfunctionsparameters)" : {{MaintenanceWindowStepFunctionsParameters}}
}
```

### YAML
<a name="aws-properties-ssm-maintenancewindowtask-taskinvocationparameters-syntax.yaml"></a>

```
  [MaintenanceWindowAutomationParameters](#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowautomationparameters): {{
    MaintenanceWindowAutomationParameters}}
  [MaintenanceWindowLambdaParameters](#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowlambdaparameters): {{
    MaintenanceWindowLambdaParameters}}
  [MaintenanceWindowRunCommandParameters](#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowruncommandparameters): {{
    MaintenanceWindowRunCommandParameters}}
  [MaintenanceWindowStepFunctionsParameters](#cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowstepfunctionsparameters): {{
    MaintenanceWindowStepFunctionsParameters}}
```

## Properties
<a name="aws-properties-ssm-maintenancewindowtask-taskinvocationparameters-properties"></a>

`MaintenanceWindowAutomationParameters`  <a name="cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowautomationparameters"></a>
The parameters for an `AUTOMATION` task type.
*Required*: No
*Type*: [MaintenanceWindowAutomationParameters](aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaintenanceWindowLambdaParameters`  <a name="cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowlambdaparameters"></a>
The parameters for a `LAMBDA` task type.
*Required*: No
*Type*: [MaintenanceWindowLambdaParameters](aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaintenanceWindowRunCommandParameters`  <a name="cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowruncommandparameters"></a>
The parameters for a `RUN_COMMAND` task type.
*Required*: No
*Type*: [MaintenanceWindowRunCommandParameters](aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaintenanceWindowStepFunctionsParameters`  <a name="cfn-ssm-maintenancewindowtask-taskinvocationparameters-maintenancewindowstepfunctionsparameters"></a>
The parameters for a `STEP_FUNCTIONS` task type.
*Required*: No
*Type*: [MaintenanceWindowStepFunctionsParameters](aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
