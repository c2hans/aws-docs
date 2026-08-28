---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-managedscalingpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster ManagedScalingPolicy
<a name="aws-properties-emr-cluster-managedscalingpolicy"></a>

 Managed scaling policy for an Amazon EMR cluster. The policy specifies the limits for resources that can be added or terminated from a cluster. The policy only applies to the core and task nodes. The master node cannot be scaled after initial configuration.

## Syntax
<a name="aws-properties-emr-cluster-managedscalingpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-managedscalingpolicy-syntax.json"></a>

```
{
  "[ComputeLimits](#cfn-emr-cluster-managedscalingpolicy-computelimits)" : {{ComputeLimits}},
  "[ScalingStrategy](#cfn-emr-cluster-managedscalingpolicy-scalingstrategy)" : {{String}},
  "[UtilizationPerformanceIndex](#cfn-emr-cluster-managedscalingpolicy-utilizationperformanceindex)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emr-cluster-managedscalingpolicy-syntax.yaml"></a>

```
  [ComputeLimits](#cfn-emr-cluster-managedscalingpolicy-computelimits): {{
    ComputeLimits}}
  [ScalingStrategy](#cfn-emr-cluster-managedscalingpolicy-scalingstrategy): {{String}}
  [UtilizationPerformanceIndex](#cfn-emr-cluster-managedscalingpolicy-utilizationperformanceindex): {{Integer}}
```

## Properties
<a name="aws-properties-emr-cluster-managedscalingpolicy-properties"></a>

`ComputeLimits`  <a name="cfn-emr-cluster-managedscalingpolicy-computelimits"></a>
The Amazon EC2 unit limits for a managed scaling policy. The managed scaling activity of a cluster is not allowed to go above or below these limits. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.
*Required*: No
*Type*: [ComputeLimits](aws-properties-emr-cluster-computelimits.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingStrategy`  <a name="cfn-emr-cluster-managedscalingpolicy-scalingstrategy"></a>
Determines whether a custom scaling utilization performance index can be set. Possible values include *ADVANCED* or *DEFAULT*.
*Required*: No
*Type*: String
*Allowed values*: `DEFAULT | ADVANCED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UtilizationPerformanceIndex`  <a name="cfn-emr-cluster-managedscalingpolicy-utilizationperformanceindex"></a>
An integer value that represents an advanced scaling strategy. Setting a higher value optimizes for performance. Setting a lower value optimizes for resource conservation. Setting the value to 50 balances performance and resource conservation. Possible values are 1, 25, 50, 75, and 100.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
