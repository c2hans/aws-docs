---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-nullvalueformatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard NullValueFormatConfiguration
<a name="aws-properties-quicksight-dashboard-nullvalueformatconfiguration"></a>

The options that determine the null value format configuration.

## Syntax
<a name="aws-properties-quicksight-dashboard-nullvalueformatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-nullvalueformatconfiguration-syntax.json"></a>

```
{
  "[NullString](#cfn-quicksight-dashboard-nullvalueformatconfiguration-nullstring)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-nullvalueformatconfiguration-syntax.yaml"></a>

```
  [NullString](#cfn-quicksight-dashboard-nullvalueformatconfiguration-nullstring): {{
    String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-nullvalueformatconfiguration-properties"></a>

`NullString`  <a name="cfn-quicksight-dashboard-nullvalueformatconfiguration-nullstring"></a>
Determines the null string of null values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
