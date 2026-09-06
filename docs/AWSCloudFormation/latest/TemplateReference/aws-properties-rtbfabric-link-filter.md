---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-link-filter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::Link Filter
<a name="aws-properties-rtbfabric-link-filter"></a>

Describes the configuration of a filter.

## Syntax
<a name="aws-properties-rtbfabric-link-filter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-link-filter-syntax.json"></a>

```
{
  "[Criteria](#cfn-rtbfabric-link-filter-criteria)" : {{[ FilterCriterion, ... ]}}
}
```

### YAML
<a name="aws-properties-rtbfabric-link-filter-syntax.yaml"></a>

```
  [Criteria](#cfn-rtbfabric-link-filter-criteria): {{
    - FilterCriterion}}
```

## Properties
<a name="aws-properties-rtbfabric-link-filter-properties"></a>

`Criteria`  <a name="cfn-rtbfabric-link-filter-criteria"></a>
Describes the criteria for a filter.
*Required*: Yes
*Type*: Array of [FilterCriterion](aws-properties-rtbfabric-link-filtercriterion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
