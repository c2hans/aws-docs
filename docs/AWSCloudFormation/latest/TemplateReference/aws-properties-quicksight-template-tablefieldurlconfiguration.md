---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-tablefieldurlconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TableFieldURLConfiguration
<a name="aws-properties-quicksight-template-tablefieldurlconfiguration"></a>

The URL configuration for a table field.

## Syntax
<a name="aws-properties-quicksight-template-tablefieldurlconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-tablefieldurlconfiguration-syntax.json"></a>

```
{
  "[ImageConfiguration](#cfn-quicksight-template-tablefieldurlconfiguration-imageconfiguration)" : {{TableFieldImageConfiguration}},
  "[LinkConfiguration](#cfn-quicksight-template-tablefieldurlconfiguration-linkconfiguration)" : {{TableFieldLinkConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-tablefieldurlconfiguration-syntax.yaml"></a>

```
  [ImageConfiguration](#cfn-quicksight-template-tablefieldurlconfiguration-imageconfiguration): {{
    TableFieldImageConfiguration}}
  [LinkConfiguration](#cfn-quicksight-template-tablefieldurlconfiguration-linkconfiguration): {{
    TableFieldLinkConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-tablefieldurlconfiguration-properties"></a>

`ImageConfiguration`  <a name="cfn-quicksight-template-tablefieldurlconfiguration-imageconfiguration"></a>
The image configuration of a table field URL.
*Required*: No
*Type*: [TableFieldImageConfiguration](aws-properties-quicksight-template-tablefieldimageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinkConfiguration`  <a name="cfn-quicksight-template-tablefieldurlconfiguration-linkconfiguration"></a>
The link configuration of a table field URL.
*Required*: No
*Type*: [TableFieldLinkConfiguration](aws-properties-quicksight-template-tablefieldlinkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
