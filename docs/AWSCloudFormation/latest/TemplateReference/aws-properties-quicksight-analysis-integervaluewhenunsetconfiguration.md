---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-integervaluewhenunsetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis IntegerValueWhenUnsetConfiguration
<a name="aws-properties-quicksight-analysis-integervaluewhenunsetconfiguration"></a>

A parameter declaration for the `Integer` data type.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-analysis-integervaluewhenunsetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-integervaluewhenunsetconfiguration-syntax.json"></a>

```
{
  "[CustomValue](#cfn-quicksight-analysis-integervaluewhenunsetconfiguration-customvalue)" : {{Number}},
  "[ValueWhenUnsetOption](#cfn-quicksight-analysis-integervaluewhenunsetconfiguration-valuewhenunsetoption)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-integervaluewhenunsetconfiguration-syntax.yaml"></a>

```
  [CustomValue](#cfn-quicksight-analysis-integervaluewhenunsetconfiguration-customvalue): {{Number}}
  [ValueWhenUnsetOption](#cfn-quicksight-analysis-integervaluewhenunsetconfiguration-valuewhenunsetoption): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-integervaluewhenunsetconfiguration-properties"></a>

`CustomValue`  <a name="cfn-quicksight-analysis-integervaluewhenunsetconfiguration-customvalue"></a>
A custom value that's used when the value of a parameter isn't set.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueWhenUnsetOption`  <a name="cfn-quicksight-analysis-integervaluewhenunsetconfiguration-valuewhenunsetoption"></a>
The built-in options for default values. The value can be one of the following:
+ `RECOMMENDED`: The recommended value.
+ `NULL`: The `NULL` value.
*Required*: No
*Type*: String
*Allowed values*: `RECOMMENDED_VALUE | NULL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
