---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-filter-numberfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::Filter NumberFilter
<a name="aws-properties-inspectorv2-filter-numberfilter"></a>

An object that describes the details of a number filter.

## Syntax
<a name="aws-properties-inspectorv2-filter-numberfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-filter-numberfilter-syntax.json"></a>

```
{
  "[LowerInclusive](#cfn-inspectorv2-filter-numberfilter-lowerinclusive)" : {{Number}},
  "[UpperInclusive](#cfn-inspectorv2-filter-numberfilter-upperinclusive)" : {{Number}}
}
```

### YAML
<a name="aws-properties-inspectorv2-filter-numberfilter-syntax.yaml"></a>

```
  [LowerInclusive](#cfn-inspectorv2-filter-numberfilter-lowerinclusive): {{Number}}
  [UpperInclusive](#cfn-inspectorv2-filter-numberfilter-upperinclusive): {{Number}}
```

## Properties
<a name="aws-properties-inspectorv2-filter-numberfilter-properties"></a>

`LowerInclusive`  <a name="cfn-inspectorv2-filter-numberfilter-lowerinclusive"></a>
The lowest number to be included in the filter.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpperInclusive`  <a name="cfn-inspectorv2-filter-numberfilter-upperinclusive"></a>
The highest number to be included in the filter.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
