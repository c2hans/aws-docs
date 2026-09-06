---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-anchordateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template AnchorDateConfiguration
<a name="aws-properties-quicksight-template-anchordateconfiguration"></a>

The date configuration of the filter.

## Syntax
<a name="aws-properties-quicksight-template-anchordateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-anchordateconfiguration-syntax.json"></a>

```
{
  "[AnchorOption](#cfn-quicksight-template-anchordateconfiguration-anchoroption)" : {{String}},
  "[ParameterName](#cfn-quicksight-template-anchordateconfiguration-parametername)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-anchordateconfiguration-syntax.yaml"></a>

```
  [AnchorOption](#cfn-quicksight-template-anchordateconfiguration-anchoroption): {{String}}
  [ParameterName](#cfn-quicksight-template-anchordateconfiguration-parametername): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-anchordateconfiguration-properties"></a>

`AnchorOption`  <a name="cfn-quicksight-template-anchordateconfiguration-anchoroption"></a>
The options for the date configuration. Choose one of the options below:
+  `NOW`
*Required*: No
*Type*: String
*Allowed values*: `NOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterName`  <a name="cfn-quicksight-template-anchordateconfiguration-parametername"></a>
The name of the parameter that is used for the anchor date configuration.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
