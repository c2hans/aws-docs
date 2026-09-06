---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-stringdefaultvalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis StringDefaultValues
<a name="aws-properties-quicksight-analysis-stringdefaultvalues"></a>

The default values of the `StringParameterDeclaration`.

## Syntax
<a name="aws-properties-quicksight-analysis-stringdefaultvalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-stringdefaultvalues-syntax.json"></a>

```
{
  "[DynamicValue](#cfn-quicksight-analysis-stringdefaultvalues-dynamicvalue)" : {{DynamicDefaultValue}},
  "[StaticValues](#cfn-quicksight-analysis-stringdefaultvalues-staticvalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-stringdefaultvalues-syntax.yaml"></a>

```
  [DynamicValue](#cfn-quicksight-analysis-stringdefaultvalues-dynamicvalue): {{
    DynamicDefaultValue}}
  [StaticValues](#cfn-quicksight-analysis-stringdefaultvalues-staticvalues): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-stringdefaultvalues-properties"></a>

`DynamicValue`  <a name="cfn-quicksight-analysis-stringdefaultvalues-dynamicvalue"></a>
The dynamic value of the `StringDefaultValues`. Different defaults displayed according to users, groups, and values mapping.
*Required*: No
*Type*: [DynamicDefaultValue](aws-properties-quicksight-analysis-dynamicdefaultvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticValues`  <a name="cfn-quicksight-analysis-stringdefaultvalues-staticvalues"></a>
The static values of the `DecimalDefaultValues`.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `50000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
