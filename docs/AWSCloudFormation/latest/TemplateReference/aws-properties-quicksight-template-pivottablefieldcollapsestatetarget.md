---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-pivottablefieldcollapsestatetarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template PivotTableFieldCollapseStateTarget
<a name="aws-properties-quicksight-template-pivottablefieldcollapsestatetarget"></a>

The target of a pivot table field collapse state.

## Syntax
<a name="aws-properties-quicksight-template-pivottablefieldcollapsestatetarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-pivottablefieldcollapsestatetarget-syntax.json"></a>

```
{
  "[FieldDataPathValues](#cfn-quicksight-template-pivottablefieldcollapsestatetarget-fielddatapathvalues)" : {{[ DataPathValue, ... ]}},
  "[FieldId](#cfn-quicksight-template-pivottablefieldcollapsestatetarget-fieldid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-pivottablefieldcollapsestatetarget-syntax.yaml"></a>

```
  [FieldDataPathValues](#cfn-quicksight-template-pivottablefieldcollapsestatetarget-fielddatapathvalues): {{
    - DataPathValue}}
  [FieldId](#cfn-quicksight-template-pivottablefieldcollapsestatetarget-fieldid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-pivottablefieldcollapsestatetarget-properties"></a>

`FieldDataPathValues`  <a name="cfn-quicksight-template-pivottablefieldcollapsestatetarget-fielddatapathvalues"></a>
The data path of the pivot table's header. Used to set the collapse state.
*Required*: No
*Type*: Array of [DataPathValue](aws-properties-quicksight-template-datapathvalue.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldId`  <a name="cfn-quicksight-template-pivottablefieldcollapsestatetarget-fieldid"></a>
The field ID of the pivot table that the collapse state needs to be set to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
