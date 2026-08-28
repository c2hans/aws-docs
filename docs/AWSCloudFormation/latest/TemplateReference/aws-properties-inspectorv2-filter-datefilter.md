---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-filter-datefilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::Filter DateFilter
<a name="aws-properties-inspectorv2-filter-datefilter"></a>

Contains details on the time range used to filter findings.

## Syntax
<a name="aws-properties-inspectorv2-filter-datefilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-filter-datefilter-syntax.json"></a>

```
{
  "[EndInclusive](#cfn-inspectorv2-filter-datefilter-endinclusive)" : {{Integer}},
  "[StartInclusive](#cfn-inspectorv2-filter-datefilter-startinclusive)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-inspectorv2-filter-datefilter-syntax.yaml"></a>

```
  [EndInclusive](#cfn-inspectorv2-filter-datefilter-endinclusive): {{Integer}}
  [StartInclusive](#cfn-inspectorv2-filter-datefilter-startinclusive): {{Integer}}
```

## Properties
<a name="aws-properties-inspectorv2-filter-datefilter-properties"></a>

`EndInclusive`  <a name="cfn-inspectorv2-filter-datefilter-endinclusive"></a>
A timestamp representing the end of the time period filtered on.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartInclusive`  <a name="cfn-inspectorv2-filter-datefilter-startinclusive"></a>
A timestamp representing the start of the time period filtered on.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
