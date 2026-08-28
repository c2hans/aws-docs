---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-referenceline.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ReferenceLine
<a name="aws-properties-quicksight-dashboard-referenceline"></a>

The reference line visual display options.

## Syntax
<a name="aws-properties-quicksight-dashboard-referenceline-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-referenceline-syntax.json"></a>

```
{
  "[DataConfiguration](#cfn-quicksight-dashboard-referenceline-dataconfiguration)" : {{ReferenceLineDataConfiguration}},
  "[LabelConfiguration](#cfn-quicksight-dashboard-referenceline-labelconfiguration)" : {{ReferenceLineLabelConfiguration}},
  "[Status](#cfn-quicksight-dashboard-referenceline-status)" : {{String}},
  "[StyleConfiguration](#cfn-quicksight-dashboard-referenceline-styleconfiguration)" : {{ReferenceLineStyleConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-referenceline-syntax.yaml"></a>

```
  [DataConfiguration](#cfn-quicksight-dashboard-referenceline-dataconfiguration): {{
    ReferenceLineDataConfiguration}}
  [LabelConfiguration](#cfn-quicksight-dashboard-referenceline-labelconfiguration): {{
    ReferenceLineLabelConfiguration}}
  [Status](#cfn-quicksight-dashboard-referenceline-status): {{String}}
  [StyleConfiguration](#cfn-quicksight-dashboard-referenceline-styleconfiguration): {{
    ReferenceLineStyleConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-referenceline-properties"></a>

`DataConfiguration`  <a name="cfn-quicksight-dashboard-referenceline-dataconfiguration"></a>
The data configuration of the reference line.
*Required*: Yes
*Type*: [ReferenceLineDataConfiguration](aws-properties-quicksight-dashboard-referencelinedataconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LabelConfiguration`  <a name="cfn-quicksight-dashboard-referenceline-labelconfiguration"></a>
The label configuration of the reference line.
*Required*: No
*Type*: [ReferenceLineLabelConfiguration](aws-properties-quicksight-dashboard-referencelinelabelconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-quicksight-dashboard-referenceline-status"></a>
The status of the reference line. Choose one of the following options:
+  `ENABLE`
+  `DISABLE`
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StyleConfiguration`  <a name="cfn-quicksight-dashboard-referenceline-styleconfiguration"></a>
The style configuration of the reference line.
*Required*: No
*Type*: [ReferenceLineStyleConfiguration](aws-properties-quicksight-dashboard-referencelinestyleconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
