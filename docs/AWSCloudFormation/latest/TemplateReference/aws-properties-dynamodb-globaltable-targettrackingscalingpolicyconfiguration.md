---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable TargetTrackingScalingPolicyConfiguration
<a name="aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration"></a>

Defines a target tracking scaling policy.

## Syntax
<a name="aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-syntax.json"></a>

```
{
  "[DisableScaleIn](#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-disablescalein)" : {{Boolean}},
  "[ScaleInCooldown](#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-scaleincooldown)" : {{Integer}},
  "[ScaleOutCooldown](#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-scaleoutcooldown)" : {{Integer}},
  "[TargetValue](#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-targetvalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-syntax.yaml"></a>

```
  [DisableScaleIn](#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-disablescalein): {{Boolean}}
  [ScaleInCooldown](#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-scaleincooldown): {{Integer}}
  [ScaleOutCooldown](#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-scaleoutcooldown): {{Integer}}
  [TargetValue](#cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-targetvalue): {{Number}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-properties"></a>

`DisableScaleIn`  <a name="cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-disablescalein"></a>
Indicates whether scale in by the target tracking scaling policy is disabled. The default value is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScaleInCooldown`  <a name="cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-scaleincooldown"></a>
The amount of time, in seconds, after a scale-in activity completes before another scale-in activity can start.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScaleOutCooldown`  <a name="cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-scaleoutcooldown"></a>
The amount of time, in seconds, after a scale-out activity completes before another scale-out activity can start.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetValue`  <a name="cfn-dynamodb-globaltable-targettrackingscalingpolicyconfiguration-targetvalue"></a>
Defines a target value for the scaling policy.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
