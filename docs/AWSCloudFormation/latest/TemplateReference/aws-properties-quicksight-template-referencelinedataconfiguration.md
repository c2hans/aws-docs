---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-referencelinedataconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ReferenceLineDataConfiguration
<a name="aws-properties-quicksight-template-referencelinedataconfiguration"></a>

The data configuration of the reference line.

## Syntax
<a name="aws-properties-quicksight-template-referencelinedataconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-referencelinedataconfiguration-syntax.json"></a>

```
{
  "[AxisBinding](#cfn-quicksight-template-referencelinedataconfiguration-axisbinding)" : {{String}},
  "[DynamicConfiguration](#cfn-quicksight-template-referencelinedataconfiguration-dynamicconfiguration)" : {{ReferenceLineDynamicDataConfiguration}},
  "[SeriesType](#cfn-quicksight-template-referencelinedataconfiguration-seriestype)" : {{String}},
  "[StaticConfiguration](#cfn-quicksight-template-referencelinedataconfiguration-staticconfiguration)" : {{ReferenceLineStaticDataConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-referencelinedataconfiguration-syntax.yaml"></a>

```
  [AxisBinding](#cfn-quicksight-template-referencelinedataconfiguration-axisbinding): {{String}}
  [DynamicConfiguration](#cfn-quicksight-template-referencelinedataconfiguration-dynamicconfiguration): {{
    ReferenceLineDynamicDataConfiguration}}
  [SeriesType](#cfn-quicksight-template-referencelinedataconfiguration-seriestype): {{String}}
  [StaticConfiguration](#cfn-quicksight-template-referencelinedataconfiguration-staticconfiguration): {{
    ReferenceLineStaticDataConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-referencelinedataconfiguration-properties"></a>

`AxisBinding`  <a name="cfn-quicksight-template-referencelinedataconfiguration-axisbinding"></a>
The axis binding type of the reference line. Choose one of the following options:
+  `PrimaryY`
+  `SecondaryY`
*Required*: No
*Type*: String
*Allowed values*: `PRIMARY_YAXIS | SECONDARY_YAXIS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DynamicConfiguration`  <a name="cfn-quicksight-template-referencelinedataconfiguration-dynamicconfiguration"></a>
The dynamic configuration of the reference line data configuration.
*Required*: No
*Type*: [ReferenceLineDynamicDataConfiguration](aws-properties-quicksight-template-referencelinedynamicdataconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SeriesType`  <a name="cfn-quicksight-template-referencelinedataconfiguration-seriestype"></a>
The series type of the reference line data configuration. Choose one of the following options:
+  `BAR`
+  `LINE`
*Required*: No
*Type*: String
*Allowed values*: `BAR | LINE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticConfiguration`  <a name="cfn-quicksight-template-referencelinedataconfiguration-staticconfiguration"></a>
The static data configuration of the reference line data configuration.
*Required*: No
*Type*: [ReferenceLineStaticDataConfiguration](aws-properties-quicksight-template-referencelinestaticdataconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
