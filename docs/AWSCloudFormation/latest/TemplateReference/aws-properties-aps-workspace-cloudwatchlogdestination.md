---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-workspace-cloudwatchlogdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::Workspace CloudWatchLogDestination
<a name="aws-properties-aps-workspace-cloudwatchlogdestination"></a>

Configuration details for logging to CloudWatch Logs.

## Syntax
<a name="aws-properties-aps-workspace-cloudwatchlogdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-workspace-cloudwatchlogdestination-syntax.json"></a>

```
{
  "[LogGroupArn](#cfn-aps-workspace-cloudwatchlogdestination-loggrouparn)" : {{String}}
}
```

### YAML
<a name="aws-properties-aps-workspace-cloudwatchlogdestination-syntax.yaml"></a>

```
  [LogGroupArn](#cfn-aps-workspace-cloudwatchlogdestination-loggrouparn): {{String}}
```

## Properties
<a name="aws-properties-aps-workspace-cloudwatchlogdestination-properties"></a>

`LogGroupArn`  <a name="cfn-aps-workspace-cloudwatchlogdestination-loggrouparn"></a>
The ARN of the CloudWatch log group.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
