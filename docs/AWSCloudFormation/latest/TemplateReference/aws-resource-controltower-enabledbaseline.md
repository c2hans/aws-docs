---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-controltower-enabledbaseline.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ControlTower::EnabledBaseline
<a name="aws-resource-controltower-enabledbaseline"></a>

The resource represents an enabled baseline. It specifies an asynchronous operation that applies a baseline to the specified target. For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html).

## Syntax
<a name="aws-resource-controltower-enabledbaseline-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-controltower-enabledbaseline-syntax.json"></a>

```
{
  "Type" : "AWS::ControlTower::EnabledBaseline",
  "Properties" : {
      "[BaselineIdentifier](#cfn-controltower-enabledbaseline-baselineidentifier)" : {{String}},
      "[BaselineVersion](#cfn-controltower-enabledbaseline-baselineversion)" : {{String}},
      "[Parameters](#cfn-controltower-enabledbaseline-parameters)" : {{[ Parameter, ... ]}},
      "[Tags](#cfn-controltower-enabledbaseline-tags)" : {{[ Tag, ... ]}},
      "[TargetIdentifier](#cfn-controltower-enabledbaseline-targetidentifier)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-controltower-enabledbaseline-syntax.yaml"></a>

```
Type: AWS::ControlTower::EnabledBaseline
Properties:
  [BaselineIdentifier](#cfn-controltower-enabledbaseline-baselineidentifier): {{String}}
  [BaselineVersion](#cfn-controltower-enabledbaseline-baselineversion): {{String}}
  [Parameters](#cfn-controltower-enabledbaseline-parameters): {{
    - Parameter}}
  [Tags](#cfn-controltower-enabledbaseline-tags): {{
    - Tag}}
  [TargetIdentifier](#cfn-controltower-enabledbaseline-targetidentifier): {{String}}
```

## Properties
<a name="aws-resource-controltower-enabledbaseline-properties"></a>

`BaselineIdentifier`  <a name="cfn-controltower-enabledbaseline-baselineidentifier"></a>
The specific `Baseline` enabled as part of the `EnabledBaseline` resource.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[0-9a-zA-Z_\-:\/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BaselineVersion`  <a name="cfn-controltower-enabledbaseline-baselineversion"></a>
The enabled version of the `Baseline`.
*Required*: Yes
*Type*: String
*Pattern*: `^\d+(?:\.\d+){0,2}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-controltower-enabledbaseline-parameters"></a>
Shows the parameters that are applied when enabling this `Baseline`.
*Required*: No
*Type*: Array of [Parameter](aws-properties-controltower-enabledbaseline-parameter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-controltower-enabledbaseline-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-controltower-enabledbaseline-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetIdentifier`  <a name="cfn-controltower-enabledbaseline-targetidentifier"></a>
The target on which to enable the `Baseline`.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[0-9a-zA-Z_\-:\/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-controltower-enabledbaseline-return-values"></a>

### Ref
<a name="aws-resource-controltower-enabledbaseline-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the enabled baseline identifier. For example:

 `arn:aws:controltower:us-west-2:123456789012:enabledbaseline/AB12CD34EF56GH789`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-controltower-enabledbaseline-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type.

####
<a name="aws-resource-controltower-enabledbaseline-return-values-fn--getatt-fn--getatt"></a>

`EnabledBaselineIdentifier`  <a name="EnabledBaselineIdentifier-fn::getatt"></a>
The unique identifier of the enabled baseline.
