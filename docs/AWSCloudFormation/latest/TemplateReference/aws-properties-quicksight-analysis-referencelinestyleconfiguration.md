---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-referencelinestyleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ReferenceLineStyleConfiguration
<a name="aws-properties-quicksight-analysis-referencelinestyleconfiguration"></a>

The style configuration of the reference line.

## Syntax
<a name="aws-properties-quicksight-analysis-referencelinestyleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-referencelinestyleconfiguration-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-analysis-referencelinestyleconfiguration-color)" : {{String}},
  "[Pattern](#cfn-quicksight-analysis-referencelinestyleconfiguration-pattern)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-referencelinestyleconfiguration-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-analysis-referencelinestyleconfiguration-color): {{String}}
  [Pattern](#cfn-quicksight-analysis-referencelinestyleconfiguration-pattern): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-referencelinestyleconfiguration-properties"></a>

`Color`  <a name="cfn-quicksight-analysis-referencelinestyleconfiguration-color"></a>
The hex color of the reference line.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Pattern`  <a name="cfn-quicksight-analysis-referencelinestyleconfiguration-pattern"></a>
The pattern type of the line style. Choose one of the following options:
+  `SOLID`
+  `DASHED`
+  `DOTTED`
*Required*: No
*Type*: String
*Allowed values*: `SOLID | DASHED | DOTTED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
