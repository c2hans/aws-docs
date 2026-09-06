---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-decimalvaluewhenunsetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DecimalValueWhenUnsetConfiguration
<a name="aws-properties-quicksight-dashboard-decimalvaluewhenunsetconfiguration"></a>

The configuration that defines the default value of a `Decimal` parameter when a value has not been set.

## Syntax
<a name="aws-properties-quicksight-dashboard-decimalvaluewhenunsetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-decimalvaluewhenunsetconfiguration-syntax.json"></a>

```
{
  "[CustomValue](#cfn-quicksight-dashboard-decimalvaluewhenunsetconfiguration-customvalue)" : {{Number}},
  "[ValueWhenUnsetOption](#cfn-quicksight-dashboard-decimalvaluewhenunsetconfiguration-valuewhenunsetoption)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-decimalvaluewhenunsetconfiguration-syntax.yaml"></a>

```
  [CustomValue](#cfn-quicksight-dashboard-decimalvaluewhenunsetconfiguration-customvalue): {{Number}}
  [ValueWhenUnsetOption](#cfn-quicksight-dashboard-decimalvaluewhenunsetconfiguration-valuewhenunsetoption): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-decimalvaluewhenunsetconfiguration-properties"></a>

`CustomValue`  <a name="cfn-quicksight-dashboard-decimalvaluewhenunsetconfiguration-customvalue"></a>
A custom value that's used when the value of a parameter isn't set.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueWhenUnsetOption`  <a name="cfn-quicksight-dashboard-decimalvaluewhenunsetconfiguration-valuewhenunsetoption"></a>
The built-in options for default values. The value can be one of the following:
+ `RECOMMENDED`: The recommended value.
+ `NULL`: The `NULL` value.
*Required*: No
*Type*: String
*Allowed values*: `RECOMMENDED_VALUE | NULL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
