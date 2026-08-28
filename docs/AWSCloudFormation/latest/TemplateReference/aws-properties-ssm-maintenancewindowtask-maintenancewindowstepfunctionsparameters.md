---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::MaintenanceWindowTask MaintenanceWindowStepFunctionsParameters
<a name="aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters"></a>

The `MaintenanceWindowStepFunctionsParameters` property type specifies the parameters for the execution of a `STEP_FUNCTIONS` task in a Systems Manager maintenance window.

`MaintenanceWindowStepFunctionsParameters` is a property of the [TaskInvocationParameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html) property type.

## Syntax
<a name="aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-syntax.json"></a>

```
{
  "[Input](#cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-input)" : {{String}},
  "[Name](#cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-syntax.yaml"></a>

```
  [Input](#cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-input): {{String}}
  [Name](#cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-name): {{String}}
```

## Properties
<a name="aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-properties"></a>

`Input`  <a name="cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-input"></a>
The inputs for the `STEP_FUNCTIONS` task.
*Required*: No
*Type*: String
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters-name"></a>
The name of the `STEP_FUNCTIONS` task.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `80`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
