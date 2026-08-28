---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-innerfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard InnerFilter
<a name="aws-properties-quicksight-dashboard-innerfilter"></a>

The `InnerFilter` defines the subset of data to be used with the `NestedFilter`.

## Syntax
<a name="aws-properties-quicksight-dashboard-innerfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-innerfilter-syntax.json"></a>

```
{
  "[CategoryInnerFilter](#cfn-quicksight-dashboard-innerfilter-categoryinnerfilter)" : {{CategoryInnerFilter}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-innerfilter-syntax.yaml"></a>

```
  [CategoryInnerFilter](#cfn-quicksight-dashboard-innerfilter-categoryinnerfilter): {{
    CategoryInnerFilter}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-innerfilter-properties"></a>

`CategoryInnerFilter`  <a name="cfn-quicksight-dashboard-innerfilter-categoryinnerfilter"></a>
A `CategoryInnerFilter` filters text values for the `NestedFilter`.
*Required*: No
*Type*: [CategoryInnerFilter](aws-properties-quicksight-dashboard-categoryinnerfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
