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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
