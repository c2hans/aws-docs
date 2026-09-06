---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-tablefieldoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TableFieldOptions
<a name="aws-properties-quicksight-dashboard-tablefieldoptions"></a>

The field options of a table visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-tablefieldoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-tablefieldoptions-syntax.json"></a>

```
{
  "[Order](#cfn-quicksight-dashboard-tablefieldoptions-order)" : {{[ String, ... ]}},
  "[PinnedFieldOptions](#cfn-quicksight-dashboard-tablefieldoptions-pinnedfieldoptions)" : {{TablePinnedFieldOptions}},
  "[SelectedFieldOptions](#cfn-quicksight-dashboard-tablefieldoptions-selectedfieldoptions)" : {{[ TableFieldOption, ... ]}},
  "[TransposedTableOptions](#cfn-quicksight-dashboard-tablefieldoptions-transposedtableoptions)" : {{[ TransposedTableOption, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-tablefieldoptions-syntax.yaml"></a>

```
  [Order](#cfn-quicksight-dashboard-tablefieldoptions-order): {{
    - String}}
  [PinnedFieldOptions](#cfn-quicksight-dashboard-tablefieldoptions-pinnedfieldoptions): {{
    TablePinnedFieldOptions}}
  [SelectedFieldOptions](#cfn-quicksight-dashboard-tablefieldoptions-selectedfieldoptions): {{
    - TableFieldOption}}
  [TransposedTableOptions](#cfn-quicksight-dashboard-tablefieldoptions-transposedtableoptions): {{
    - TransposedTableOption}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-tablefieldoptions-properties"></a>

`Order`  <a name="cfn-quicksight-dashboard-tablefieldoptions-order"></a>
The order of the field IDs that are configured as field options for a table visual.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `512 | 200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PinnedFieldOptions`  <a name="cfn-quicksight-dashboard-tablefieldoptions-pinnedfieldoptions"></a>
The settings for the pinned columns of a table visual.
*Required*: No
*Type*: [TablePinnedFieldOptions](aws-properties-quicksight-dashboard-tablepinnedfieldoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectedFieldOptions`  <a name="cfn-quicksight-dashboard-tablefieldoptions-selectedfieldoptions"></a>
The field options to be configured to a table.
*Required*: No
*Type*: Array of [TableFieldOption](aws-properties-quicksight-dashboard-tablefieldoption.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransposedTableOptions`  <a name="cfn-quicksight-dashboard-tablefieldoptions-transposedtableoptions"></a>
The `TableOptions` of a transposed table.
*Required*: No
*Type*: Array of [TransposedTableOption](aws-properties-quicksight-dashboard-transposedtableoption.md)
*Minimum*: `0`
*Maximum*: `10001`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
