---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-filterlistconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FilterListConfiguration
<a name="aws-properties-quicksight-template-filterlistconfiguration"></a>

A list of filter configurations.

## Syntax
<a name="aws-properties-quicksight-template-filterlistconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-filterlistconfiguration-syntax.json"></a>

```
{
  "[CategoryValues](#cfn-quicksight-template-filterlistconfiguration-categoryvalues)" : {{[ String, ... ]}},
  "[MatchOperator](#cfn-quicksight-template-filterlistconfiguration-matchoperator)" : {{String}},
  "[NullOption](#cfn-quicksight-template-filterlistconfiguration-nulloption)" : {{String}},
  "[SelectAllOptions](#cfn-quicksight-template-filterlistconfiguration-selectalloptions)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-filterlistconfiguration-syntax.yaml"></a>

```
  [CategoryValues](#cfn-quicksight-template-filterlistconfiguration-categoryvalues): {{
    - String}}
  [MatchOperator](#cfn-quicksight-template-filterlistconfiguration-matchoperator): {{String}}
  [NullOption](#cfn-quicksight-template-filterlistconfiguration-nulloption): {{String}}
  [SelectAllOptions](#cfn-quicksight-template-filterlistconfiguration-selectalloptions): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-filterlistconfiguration-properties"></a>

`CategoryValues`  <a name="cfn-quicksight-template-filterlistconfiguration-categoryvalues"></a>
The list of category values for the filter.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `512 | 100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchOperator`  <a name="cfn-quicksight-template-filterlistconfiguration-matchoperator"></a>
The match operator that is used to determine if a filter should be applied.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | DOES_NOT_EQUAL | CONTAINS | DOES_NOT_CONTAIN | STARTS_WITH | ENDS_WITH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullOption`  <a name="cfn-quicksight-template-filterlistconfiguration-nulloption"></a>
This option determines how null values should be treated when filtering data.
+ `ALL_VALUES`: Include null values in filtered results.
+ `NULLS_ONLY`: Only include null values in filtered results.
+ `NON_NULLS_ONLY`: Exclude null values from filtered results.
*Required*: No
*Type*: String
*Allowed values*: `ALL_VALUES | NULLS_ONLY | NON_NULLS_ONLY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectAllOptions`  <a name="cfn-quicksight-template-filterlistconfiguration-selectalloptions"></a>
Select all of the values. Null is not the assigned value of select all.
+  `FILTER_ALL_VALUES`
*Required*: No
*Type*: String
*Allowed values*: `FILTER_ALL_VALUES`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
