---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-nullvalueformatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template NullValueFormatConfiguration
<a name="aws-properties-quicksight-template-nullvalueformatconfiguration"></a>

The options that determine the null value format configuration.

## Syntax
<a name="aws-properties-quicksight-template-nullvalueformatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-nullvalueformatconfiguration-syntax.json"></a>

```
{
  "[NullString](#cfn-quicksight-template-nullvalueformatconfiguration-nullstring)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-nullvalueformatconfiguration-syntax.yaml"></a>

```
  [NullString](#cfn-quicksight-template-nullvalueformatconfiguration-nullstring): {{
    String}}
```

## Properties
<a name="aws-properties-quicksight-template-nullvalueformatconfiguration-properties"></a>

`NullString`  <a name="cfn-quicksight-template-nullvalueformatconfiguration-nullstring"></a>
Determines the null string of null values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
