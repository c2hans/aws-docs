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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
