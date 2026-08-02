---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-stringvaluewhenunsetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis StringValueWhenUnsetConfiguration
<a name="aws-properties-quicksight-analysis-stringvaluewhenunsetconfiguration"></a>

The configuration that defines the default value of a `String` parameter when a value has not been set.

## Syntax
<a name="aws-properties-quicksight-analysis-stringvaluewhenunsetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-stringvaluewhenunsetconfiguration-syntax.json"></a>

```
{
  "[CustomValue](#cfn-quicksight-analysis-stringvaluewhenunsetconfiguration-customvalue)" : {{String}},
  "[ValueWhenUnsetOption](#cfn-quicksight-analysis-stringvaluewhenunsetconfiguration-valuewhenunsetoption)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-stringvaluewhenunsetconfiguration-syntax.yaml"></a>

```
  [CustomValue](#cfn-quicksight-analysis-stringvaluewhenunsetconfiguration-customvalue): {{String}}
  [ValueWhenUnsetOption](#cfn-quicksight-analysis-stringvaluewhenunsetconfiguration-valuewhenunsetoption): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-stringvaluewhenunsetconfiguration-properties"></a>

`CustomValue`  <a name="cfn-quicksight-analysis-stringvaluewhenunsetconfiguration-customvalue"></a>
A custom value that's used when the value of a parameter isn't set.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueWhenUnsetOption`  <a name="cfn-quicksight-analysis-stringvaluewhenunsetconfiguration-valuewhenunsetoption"></a>
The built-in options for default values. The value can be one of the following:
+ `RECOMMENDED`: The recommended value.
+ `NULL`: The `NULL` value.
*Required*: No
*Type*: String
*Allowed values*: `RECOMMENDED_VALUE | NULL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
