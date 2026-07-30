---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cassandra-table-targettrackingscalingpolicyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Table TargetTrackingScalingPolicyConfiguration
<a name="aws-properties-cassandra-table-targettrackingscalingpolicyconfiguration"></a>

Amazon Keyspaces supports the `target tracking` auto scaling policy for a provisioned table. This policy scales a table based on the ratio of consumed to provisioned capacity. The auto scaling target is a percentage of the provisioned capacity of the table.
+ `targetTrackingScalingPolicyConfiguration`: To define the target tracking policy, you must define the target value.
  + `targetValue`: The target utilization rate of the table. Amazon Keyspaces auto scaling ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `targetValue` as a percentage. A `double` between 20 and 90. (Required)
  + `disableScaleIn`: A `boolean` that specifies if `scale-in` is disabled or enabled for the table. This parameter is disabled by default. To turn on `scale-in`, set the `boolean` value to `FALSE`. This means that capacity for a table can be automatically scaled down on your behalf. (Optional)
  + `scaleInCooldown`: A cooldown period in seconds between scaling activities that lets the table stabilize before another scale in activity starts. If no value is provided, the default is 0. (Optional)
  + `scaleOutCooldown`: A cooldown period in seconds between scaling activities that lets the table stabilize before another scale out activity starts. If no value is provided, the default is 0. (Optional)

## Syntax
<a name="aws-properties-cassandra-table-targettrackingscalingpolicyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cassandra-table-targettrackingscalingpolicyconfiguration-syntax.json"></a>

```
{
  "[DisableScaleIn](#cfn-cassandra-table-targettrackingscalingpolicyconfiguration-disablescalein)" : {{Boolean}},
  "[ScaleInCooldown](#cfn-cassandra-table-targettrackingscalingpolicyconfiguration-scaleincooldown)" : {{Integer}},
  "[ScaleOutCooldown](#cfn-cassandra-table-targettrackingscalingpolicyconfiguration-scaleoutcooldown)" : {{Integer}},
  "[TargetValue](#cfn-cassandra-table-targettrackingscalingpolicyconfiguration-targetvalue)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cassandra-table-targettrackingscalingpolicyconfiguration-syntax.yaml"></a>

```
  [DisableScaleIn](#cfn-cassandra-table-targettrackingscalingpolicyconfiguration-disablescalein): {{Boolean}}
  [ScaleInCooldown](#cfn-cassandra-table-targettrackingscalingpolicyconfiguration-scaleincooldown): {{Integer}}
  [ScaleOutCooldown](#cfn-cassandra-table-targettrackingscalingpolicyconfiguration-scaleoutcooldown): {{Integer}}
  [TargetValue](#cfn-cassandra-table-targettrackingscalingpolicyconfiguration-targetvalue): {{Integer}}
```

## Properties
<a name="aws-properties-cassandra-table-targettrackingscalingpolicyconfiguration-properties"></a>

`DisableScaleIn`  <a name="cfn-cassandra-table-targettrackingscalingpolicyconfiguration-disablescalein"></a>
Specifies if `scale-in` is enabled.
When auto scaling automatically decreases capacity for a table, the table *scales in*. When scaling policies are set, they can't scale in the table lower than its minimum capacity.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScaleInCooldown`  <a name="cfn-cassandra-table-targettrackingscalingpolicyconfiguration-scaleincooldown"></a>
Specifies a `scale-in` cool down period.
A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScaleOutCooldown`  <a name="cfn-cassandra-table-targettrackingscalingpolicyconfiguration-scaleoutcooldown"></a>
Specifies a scale out cool down period.
A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetValue`  <a name="cfn-cassandra-table-targettrackingscalingpolicyconfiguration-targetvalue"></a>
Specifies the target value for the target tracking auto scaling policy.
Amazon Keyspaces auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. This ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `targetValue` as a percentage. An `integer` between 20 and 90.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
