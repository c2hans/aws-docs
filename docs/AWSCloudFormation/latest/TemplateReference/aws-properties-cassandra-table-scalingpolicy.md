---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cassandra-table-scalingpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Table ScalingPolicy
<a name="aws-properties-cassandra-table-scalingpolicy"></a>

Amazon Keyspaces supports the `target tracking` auto scaling policy. With this policy, Amazon Keyspaces auto scaling ensures that the table's ratio of consumed to provisioned capacity stays at or near the target value that you specify. You define the target value as a percentage between 20 and 90.

## Syntax
<a name="aws-properties-cassandra-table-scalingpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cassandra-table-scalingpolicy-syntax.json"></a>

```
{
  "[TargetTrackingScalingPolicyConfiguration](#cfn-cassandra-table-scalingpolicy-targettrackingscalingpolicyconfiguration)" : {{TargetTrackingScalingPolicyConfiguration}}
}
```

### YAML
<a name="aws-properties-cassandra-table-scalingpolicy-syntax.yaml"></a>

```
  [TargetTrackingScalingPolicyConfiguration](#cfn-cassandra-table-scalingpolicy-targettrackingscalingpolicyconfiguration): {{
    TargetTrackingScalingPolicyConfiguration}}
```

## Properties
<a name="aws-properties-cassandra-table-scalingpolicy-properties"></a>

`TargetTrackingScalingPolicyConfiguration`  <a name="cfn-cassandra-table-scalingpolicy-targettrackingscalingpolicyconfiguration"></a>
The auto scaling policy that scales a table based on the ratio of consumed to provisioned capacity.
*Required*: No
*Type*: [TargetTrackingScalingPolicyConfiguration](aws-properties-cassandra-table-targettrackingscalingpolicyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
