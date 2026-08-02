---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-customfilterlistconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template CustomFilterListConfiguration
<a name="aws-properties-quicksight-template-customfilterlistconfiguration"></a>

A list of custom filter values.

## Syntax
<a name="aws-properties-quicksight-template-customfilterlistconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-customfilterlistconfiguration-syntax.json"></a>

```
{
  "[CategoryValues](#cfn-quicksight-template-customfilterlistconfiguration-categoryvalues)" : {{[ String, ... ]}},
  "[MatchOperator](#cfn-quicksight-template-customfilterlistconfiguration-matchoperator)" : {{String}},
  "[NullOption](#cfn-quicksight-template-customfilterlistconfiguration-nulloption)" : {{String}},
  "[SelectAllOptions](#cfn-quicksight-template-customfilterlistconfiguration-selectalloptions)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-customfilterlistconfiguration-syntax.yaml"></a>

```
  [CategoryValues](#cfn-quicksight-template-customfilterlistconfiguration-categoryvalues): {{
    - String}}
  [MatchOperator](#cfn-quicksight-template-customfilterlistconfiguration-matchoperator): {{String}}
  [NullOption](#cfn-quicksight-template-customfilterlistconfiguration-nulloption): {{String}}
  [SelectAllOptions](#cfn-quicksight-template-customfilterlistconfiguration-selectalloptions): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-customfilterlistconfiguration-properties"></a>

`CategoryValues`  <a name="cfn-quicksight-template-customfilterlistconfiguration-categoryvalues"></a>
The list of category values for the filter.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `512 | 100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchOperator`  <a name="cfn-quicksight-template-customfilterlistconfiguration-matchoperator"></a>
The match operator that is used to determine if a filter should be applied.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | DOES_NOT_EQUAL | CONTAINS | DOES_NOT_CONTAIN | STARTS_WITH | ENDS_WITH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullOption`  <a name="cfn-quicksight-template-customfilterlistconfiguration-nulloption"></a>
This option determines how null values should be treated when filtering data.
+ `ALL_VALUES`: Include null values in filtered results.
+ `NULLS_ONLY`: Only include null values in filtered results.
+ `NON_NULLS_ONLY`: Exclude null values from filtered results.
*Required*: Yes
*Type*: String
*Allowed values*: `ALL_VALUES | NULLS_ONLY | NON_NULLS_ONLY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectAllOptions`  <a name="cfn-quicksight-template-customfilterlistconfiguration-selectalloptions"></a>
Select all of the values. Null is not the assigned value of select all.
+  `FILTER_ALL_VALUES`
*Required*: No
*Type*: String
*Allowed values*: `FILTER_ALL_VALUES`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
