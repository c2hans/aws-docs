---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-tablefieldoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TableFieldOptions
<a name="aws-properties-quicksight-template-tablefieldoptions"></a>

The field options of a table visual.

## Syntax
<a name="aws-properties-quicksight-template-tablefieldoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-tablefieldoptions-syntax.json"></a>

```
{
  "[Order](#cfn-quicksight-template-tablefieldoptions-order)" : {{[ String, ... ]}},
  "[PinnedFieldOptions](#cfn-quicksight-template-tablefieldoptions-pinnedfieldoptions)" : {{TablePinnedFieldOptions}},
  "[SelectedFieldOptions](#cfn-quicksight-template-tablefieldoptions-selectedfieldoptions)" : {{[ TableFieldOption, ... ]}},
  "[TransposedTableOptions](#cfn-quicksight-template-tablefieldoptions-transposedtableoptions)" : {{[ TransposedTableOption, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-tablefieldoptions-syntax.yaml"></a>

```
  [Order](#cfn-quicksight-template-tablefieldoptions-order): {{
    - String}}
  [PinnedFieldOptions](#cfn-quicksight-template-tablefieldoptions-pinnedfieldoptions): {{
    TablePinnedFieldOptions}}
  [SelectedFieldOptions](#cfn-quicksight-template-tablefieldoptions-selectedfieldoptions): {{
    - TableFieldOption}}
  [TransposedTableOptions](#cfn-quicksight-template-tablefieldoptions-transposedtableoptions): {{
    - TransposedTableOption}}
```

## Properties
<a name="aws-properties-quicksight-template-tablefieldoptions-properties"></a>

`Order`  <a name="cfn-quicksight-template-tablefieldoptions-order"></a>
The order of the field IDs that are configured as field options for a table visual.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `512 | 200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PinnedFieldOptions`  <a name="cfn-quicksight-template-tablefieldoptions-pinnedfieldoptions"></a>
The settings for the pinned columns of a table visual.
*Required*: No
*Type*: [TablePinnedFieldOptions](aws-properties-quicksight-template-tablepinnedfieldoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectedFieldOptions`  <a name="cfn-quicksight-template-tablefieldoptions-selectedfieldoptions"></a>
The field options to be configured to a table.
*Required*: No
*Type*: Array of [TableFieldOption](aws-properties-quicksight-template-tablefieldoption.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransposedTableOptions`  <a name="cfn-quicksight-template-tablefieldoptions-transposedtableoptions"></a>
The `TableOptions` of a transposed table.
*Required*: No
*Type*: Array of [TransposedTableOption](aws-properties-quicksight-template-transposedtableoption.md)
*Minimum*: `0`
*Maximum*: `10001`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
