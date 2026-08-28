---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-referencelinevaluelabelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ReferenceLineValueLabelConfiguration
<a name="aws-properties-quicksight-analysis-referencelinevaluelabelconfiguration"></a>

The value label configuration of the label in a reference line.

## Syntax
<a name="aws-properties-quicksight-analysis-referencelinevaluelabelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-referencelinevaluelabelconfiguration-syntax.json"></a>

```
{
  "[FormatConfiguration](#cfn-quicksight-analysis-referencelinevaluelabelconfiguration-formatconfiguration)" : {{NumericFormatConfiguration}},
  "[RelativePosition](#cfn-quicksight-analysis-referencelinevaluelabelconfiguration-relativeposition)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-referencelinevaluelabelconfiguration-syntax.yaml"></a>

```
  [FormatConfiguration](#cfn-quicksight-analysis-referencelinevaluelabelconfiguration-formatconfiguration): {{
    NumericFormatConfiguration}}
  [RelativePosition](#cfn-quicksight-analysis-referencelinevaluelabelconfiguration-relativeposition): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-referencelinevaluelabelconfiguration-properties"></a>

`FormatConfiguration`  <a name="cfn-quicksight-analysis-referencelinevaluelabelconfiguration-formatconfiguration"></a>
The format configuration of the value label.
*Required*: No
*Type*: [NumericFormatConfiguration](aws-properties-quicksight-analysis-numericformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RelativePosition`  <a name="cfn-quicksight-analysis-referencelinevaluelabelconfiguration-relativeposition"></a>
The relative position of the value label. Choose one of the following options:
+  `BEFORE_CUSTOM_LABEL`
+  `AFTER_CUSTOM_LABEL`
*Required*: No
*Type*: String
*Allowed values*: `BEFORE_CUSTOM_LABEL | AFTER_CUSTOM_LABEL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
