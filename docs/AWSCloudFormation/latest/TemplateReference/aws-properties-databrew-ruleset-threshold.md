---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-ruleset-threshold.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Ruleset Threshold
<a name="aws-properties-databrew-ruleset-threshold"></a>

The threshold used with a non-aggregate check expression. The non-aggregate check expression will be applied to each row in a specific column. Then the threshold will be used to determine whether the validation succeeds.

## Syntax
<a name="aws-properties-databrew-ruleset-threshold-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-ruleset-threshold-syntax.json"></a>

```
{
  "[Type](#cfn-databrew-ruleset-threshold-type)" : {{String}},
  "[Unit](#cfn-databrew-ruleset-threshold-unit)" : {{String}},
  "[Value](#cfn-databrew-ruleset-threshold-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-databrew-ruleset-threshold-syntax.yaml"></a>

```
  [Type](#cfn-databrew-ruleset-threshold-type): {{String}}
  [Unit](#cfn-databrew-ruleset-threshold-unit): {{String}}
  [Value](#cfn-databrew-ruleset-threshold-value): {{Number}}
```

## Properties
<a name="aws-properties-databrew-ruleset-threshold-properties"></a>

`Type`  <a name="cfn-databrew-ruleset-threshold-type"></a>
The type of a threshold. Used for comparison of an actual count of rows that satisfy the rule to the threshold value.
*Required*: No
*Type*: String
*Allowed values*: `GREATER_THAN_OR_EQUAL | LESS_THAN_OR_EQUAL | GREATER_THAN | LESS_THAN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-databrew-ruleset-threshold-unit"></a>
Unit of threshold value. Can be either a COUNT or PERCENTAGE of the full sample size used for validation.
*Required*: No
*Type*: String
*Allowed values*: `COUNT | PERCENTAGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-databrew-ruleset-threshold-value"></a>
The value of a threshold.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
