---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-segmentsort.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition SegmentSort
<a name="aws-properties-customerprofiles-segmentdefinition-segmentsort"></a>

<a name="aws-properties-customerprofiles-segmentdefinition-segmentsort-description"></a>The `SegmentSort` property type specifies Property description not available. for an [AWS::CustomerProfiles::SegmentDefinition](aws-resource-customerprofiles-segmentdefinition.md).

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-segmentsort-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-segmentsort-syntax.json"></a>

```
{
  "[Attributes](#cfn-customerprofiles-segmentdefinition-segmentsort-attributes)" : {{[ SortAttribute, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-segmentsort-syntax.yaml"></a>

```
  [Attributes](#cfn-customerprofiles-segmentdefinition-segmentsort-attributes): {{
    - SortAttribute}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-segmentsort-properties"></a>

`Attributes`  <a name="cfn-customerprofiles-segmentdefinition-segmentsort-attributes"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [SortAttribute](aws-properties-customerprofiles-segmentdefinition-sortattribute.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
