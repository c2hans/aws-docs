---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-cloudwatchlogs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster CloudWatchLogs
<a name="aws-properties-msk-cluster-cloudwatchlogs"></a>

Details of the CloudWatch Logs destination for broker logs.

## Syntax
<a name="aws-properties-msk-cluster-cloudwatchlogs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-cloudwatchlogs-syntax.json"></a>

```
{
  "[Enabled](#cfn-msk-cluster-cloudwatchlogs-enabled)" : {{Boolean}},
  "[LogGroup](#cfn-msk-cluster-cloudwatchlogs-loggroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-cluster-cloudwatchlogs-syntax.yaml"></a>

```
  [Enabled](#cfn-msk-cluster-cloudwatchlogs-enabled): {{Boolean}}
  [LogGroup](#cfn-msk-cluster-cloudwatchlogs-loggroup): {{String}}
```

## Properties
<a name="aws-properties-msk-cluster-cloudwatchlogs-properties"></a>

`Enabled`  <a name="cfn-msk-cluster-cloudwatchlogs-enabled"></a>
Specifies whether broker logs get sent to the specified CloudWatch Logs destination.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroup`  <a name="cfn-msk-cluster-cloudwatchlogs-loggroup"></a>
The CloudWatch log group that is the destination for broker logs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
