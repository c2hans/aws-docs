---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-sheetelementconfigurationoverrides.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SheetElementConfigurationOverrides
<a name="aws-properties-quicksight-analysis-sheetelementconfigurationoverrides"></a>

The override configuration of the rendering rules of a sheet.

## Syntax
<a name="aws-properties-quicksight-analysis-sheetelementconfigurationoverrides-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-sheetelementconfigurationoverrides-syntax.json"></a>

```
{
  "[Visibility](#cfn-quicksight-analysis-sheetelementconfigurationoverrides-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-sheetelementconfigurationoverrides-syntax.yaml"></a>

```
  [Visibility](#cfn-quicksight-analysis-sheetelementconfigurationoverrides-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-sheetelementconfigurationoverrides-properties"></a>

`Visibility`  <a name="cfn-quicksight-analysis-sheetelementconfigurationoverrides-visibility"></a>
Determines whether or not the overrides are visible. Choose one of the following options:
+  `VISIBLE`
+  `HIDDEN`
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
