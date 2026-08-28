---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-pivottabledatapathoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template PivotTableDataPathOption
<a name="aws-properties-quicksight-template-pivottabledatapathoption"></a>

The data path options for the pivot table field options.

## Syntax
<a name="aws-properties-quicksight-template-pivottabledatapathoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-pivottabledatapathoption-syntax.json"></a>

```
{
  "[DataPathList](#cfn-quicksight-template-pivottabledatapathoption-datapathlist)" : {{[ DataPathValue, ... ]}},
  "[Width](#cfn-quicksight-template-pivottabledatapathoption-width)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-pivottabledatapathoption-syntax.yaml"></a>

```
  [DataPathList](#cfn-quicksight-template-pivottabledatapathoption-datapathlist): {{
    - DataPathValue}}
  [Width](#cfn-quicksight-template-pivottabledatapathoption-width): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-pivottabledatapathoption-properties"></a>

`DataPathList`  <a name="cfn-quicksight-template-pivottabledatapathoption-datapathlist"></a>
The list of data path values for the data path options.
*Required*: Yes
*Type*: Array of [DataPathValue](aws-properties-quicksight-template-datapathvalue.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Width`  <a name="cfn-quicksight-template-pivottabledatapathoption-width"></a>
The width of the data path option.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
