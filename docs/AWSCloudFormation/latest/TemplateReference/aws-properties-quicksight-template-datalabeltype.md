---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-datalabeltype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DataLabelType
<a name="aws-properties-quicksight-template-datalabeltype"></a>

The option that determines the data label type.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-template-datalabeltype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-datalabeltype-syntax.json"></a>

```
{
  "[DataPathLabelType](#cfn-quicksight-template-datalabeltype-datapathlabeltype)" : {{DataPathLabelType}},
  "[FieldLabelType](#cfn-quicksight-template-datalabeltype-fieldlabeltype)" : {{FieldLabelType}},
  "[MaximumLabelType](#cfn-quicksight-template-datalabeltype-maximumlabeltype)" : {{MaximumLabelType}},
  "[MinimumLabelType](#cfn-quicksight-template-datalabeltype-minimumlabeltype)" : {{MinimumLabelType}},
  "[RangeEndsLabelType](#cfn-quicksight-template-datalabeltype-rangeendslabeltype)" : {{RangeEndsLabelType}}
}
```

### YAML
<a name="aws-properties-quicksight-template-datalabeltype-syntax.yaml"></a>

```
  [DataPathLabelType](#cfn-quicksight-template-datalabeltype-datapathlabeltype): {{
    DataPathLabelType}}
  [FieldLabelType](#cfn-quicksight-template-datalabeltype-fieldlabeltype): {{
    FieldLabelType}}
  [MaximumLabelType](#cfn-quicksight-template-datalabeltype-maximumlabeltype): {{
    MaximumLabelType}}
  [MinimumLabelType](#cfn-quicksight-template-datalabeltype-minimumlabeltype): {{
    MinimumLabelType}}
  [RangeEndsLabelType](#cfn-quicksight-template-datalabeltype-rangeendslabeltype): {{
    RangeEndsLabelType}}
```

## Properties
<a name="aws-properties-quicksight-template-datalabeltype-properties"></a>

`DataPathLabelType`  <a name="cfn-quicksight-template-datalabeltype-datapathlabeltype"></a>
The option that specifies individual data values for labels.
*Required*: No
*Type*: [DataPathLabelType](aws-properties-quicksight-template-datapathlabeltype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldLabelType`  <a name="cfn-quicksight-template-datalabeltype-fieldlabeltype"></a>
Determines the label configuration for the entire field.
*Required*: No
*Type*: [FieldLabelType](aws-properties-quicksight-template-fieldlabeltype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumLabelType`  <a name="cfn-quicksight-template-datalabeltype-maximumlabeltype"></a>
Determines the label configuration for the maximum value in a visual.
*Required*: No
*Type*: [MaximumLabelType](aws-properties-quicksight-template-maximumlabeltype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLabelType`  <a name="cfn-quicksight-template-datalabeltype-minimumlabeltype"></a>
Determines the label configuration for the minimum value in a visual.
*Required*: No
*Type*: [MinimumLabelType](aws-properties-quicksight-template-minimumlabeltype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RangeEndsLabelType`  <a name="cfn-quicksight-template-datalabeltype-rangeendslabeltype"></a>
Determines the label configuration for range end value in a visual.
*Required*: No
*Type*: [RangeEndsLabelType](aws-properties-quicksight-template-rangeendslabeltype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
