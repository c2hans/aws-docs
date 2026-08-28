---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::MaintenanceWindowTask CloudWatchOutputConfig
<a name="aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig"></a>

Configuration options for sending command output to Amazon CloudWatch Logs.

## Syntax
<a name="aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig-syntax.json"></a>

```
{
  "[CloudWatchLogGroupName](#cfn-ssm-maintenancewindowtask-cloudwatchoutputconfig-cloudwatchloggroupname)" : {{String}},
  "[CloudWatchOutputEnabled](#cfn-ssm-maintenancewindowtask-cloudwatchoutputconfig-cloudwatchoutputenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig-syntax.yaml"></a>

```
  [CloudWatchLogGroupName](#cfn-ssm-maintenancewindowtask-cloudwatchoutputconfig-cloudwatchloggroupname): {{String}}
  [CloudWatchOutputEnabled](#cfn-ssm-maintenancewindowtask-cloudwatchoutputconfig-cloudwatchoutputenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig-properties"></a>

`CloudWatchLogGroupName`  <a name="cfn-ssm-maintenancewindowtask-cloudwatchoutputconfig-cloudwatchloggroupname"></a>
The name of the CloudWatch Logs log group where you want to send command output. If you don't specify a group name, AWS Systems Manager automatically creates a log group for you. The log group uses the following naming format:
 `aws/ssm/SystemsManagerDocumentName`
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CloudWatchOutputEnabled`  <a name="cfn-ssm-maintenancewindowtask-cloudwatchoutputconfig-cloudwatchoutputenabled"></a>
Enables Systems Manager to send command output to CloudWatch Logs.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
