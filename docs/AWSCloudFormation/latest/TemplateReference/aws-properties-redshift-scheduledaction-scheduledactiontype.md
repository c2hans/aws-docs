---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-scheduledaction-scheduledactiontype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::ScheduledAction ScheduledActionType
<a name="aws-properties-redshift-scheduledaction-scheduledactiontype"></a>

The action type that specifies an Amazon Redshift API operation that is supported by the Amazon Redshift scheduler.

## Syntax
<a name="aws-properties-redshift-scheduledaction-scheduledactiontype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-scheduledaction-scheduledactiontype-syntax.json"></a>

```
{
  "[PauseCluster](#cfn-redshift-scheduledaction-scheduledactiontype-pausecluster)" : {{PauseClusterMessage}},
  "[ResizeCluster](#cfn-redshift-scheduledaction-scheduledactiontype-resizecluster)" : {{ResizeClusterMessage}},
  "[ResumeCluster](#cfn-redshift-scheduledaction-scheduledactiontype-resumecluster)" : {{ResumeClusterMessage}}
}
```

### YAML
<a name="aws-properties-redshift-scheduledaction-scheduledactiontype-syntax.yaml"></a>

```
  [PauseCluster](#cfn-redshift-scheduledaction-scheduledactiontype-pausecluster): {{
    PauseClusterMessage}}
  [ResizeCluster](#cfn-redshift-scheduledaction-scheduledactiontype-resizecluster): {{
    ResizeClusterMessage}}
  [ResumeCluster](#cfn-redshift-scheduledaction-scheduledactiontype-resumecluster): {{
    ResumeClusterMessage}}
```

## Properties
<a name="aws-properties-redshift-scheduledaction-scheduledactiontype-properties"></a>

`PauseCluster`  <a name="cfn-redshift-scheduledaction-scheduledactiontype-pausecluster"></a>
An action that runs a `PauseCluster` API operation.
*Required*: No
*Type*: [PauseClusterMessage](aws-properties-redshift-scheduledaction-pauseclustermessage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResizeCluster`  <a name="cfn-redshift-scheduledaction-scheduledactiontype-resizecluster"></a>
An action that runs a `ResizeCluster` API operation.
*Required*: No
*Type*: [ResizeClusterMessage](aws-properties-redshift-scheduledaction-resizeclustermessage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResumeCluster`  <a name="cfn-redshift-scheduledaction-scheduledactiontype-resumecluster"></a>
An action that runs a `ResumeCluster` API operation.
*Required*: No
*Type*: [ResumeClusterMessage](aws-properties-redshift-scheduledaction-resumeclustermessage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
