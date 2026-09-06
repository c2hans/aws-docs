---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-tablefieldurlconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TableFieldURLConfiguration
<a name="aws-properties-quicksight-analysis-tablefieldurlconfiguration"></a>

The URL configuration for a table field.

## Syntax
<a name="aws-properties-quicksight-analysis-tablefieldurlconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-tablefieldurlconfiguration-syntax.json"></a>

```
{
  "[ImageConfiguration](#cfn-quicksight-analysis-tablefieldurlconfiguration-imageconfiguration)" : {{TableFieldImageConfiguration}},
  "[LinkConfiguration](#cfn-quicksight-analysis-tablefieldurlconfiguration-linkconfiguration)" : {{TableFieldLinkConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-tablefieldurlconfiguration-syntax.yaml"></a>

```
  [ImageConfiguration](#cfn-quicksight-analysis-tablefieldurlconfiguration-imageconfiguration): {{
    TableFieldImageConfiguration}}
  [LinkConfiguration](#cfn-quicksight-analysis-tablefieldurlconfiguration-linkconfiguration): {{
    TableFieldLinkConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-tablefieldurlconfiguration-properties"></a>

`ImageConfiguration`  <a name="cfn-quicksight-analysis-tablefieldurlconfiguration-imageconfiguration"></a>
The image configuration of a table field URL.
*Required*: No
*Type*: [TableFieldImageConfiguration](aws-properties-quicksight-analysis-tablefieldimageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinkConfiguration`  <a name="cfn-quicksight-analysis-tablefieldurlconfiguration-linkconfiguration"></a>
The link configuration of a table field URL.
*Required*: No
*Type*: [TableFieldLinkConfiguration](aws-properties-quicksight-analysis-tablefieldlinkconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
