---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-integerdefaultvalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis IntegerDefaultValues
<a name="aws-properties-quicksight-analysis-integerdefaultvalues"></a>

The default values of the `IntegerParameterDeclaration`.

## Syntax
<a name="aws-properties-quicksight-analysis-integerdefaultvalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-integerdefaultvalues-syntax.json"></a>

```
{
  "[DynamicValue](#cfn-quicksight-analysis-integerdefaultvalues-dynamicvalue)" : {{DynamicDefaultValue}},
  "[StaticValues](#cfn-quicksight-analysis-integerdefaultvalues-staticvalues)" : {{[ Number, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-integerdefaultvalues-syntax.yaml"></a>

```
  [DynamicValue](#cfn-quicksight-analysis-integerdefaultvalues-dynamicvalue): {{
    DynamicDefaultValue}}
  [StaticValues](#cfn-quicksight-analysis-integerdefaultvalues-staticvalues): {{
    - Number}}
```

## Properties
<a name="aws-properties-quicksight-analysis-integerdefaultvalues-properties"></a>

`DynamicValue`  <a name="cfn-quicksight-analysis-integerdefaultvalues-dynamicvalue"></a>
The dynamic value of the `IntegerDefaultValues`. Different defaults are displayed according to users, groups, and values mapping.
*Required*: No
*Type*: [DynamicDefaultValue](aws-properties-quicksight-analysis-dynamicdefaultvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticValues`  <a name="cfn-quicksight-analysis-integerdefaultvalues-staticvalues"></a>
The static values of the `IntegerDefaultValues`.
*Required*: No
*Type*: Array of Number
*Minimum*: `0`
*Maximum*: `50000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
