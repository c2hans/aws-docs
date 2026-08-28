---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-filter-mapfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::Filter MapFilter
<a name="aws-properties-inspectorv2-filter-mapfilter"></a>

An object that describes details of a map filter.

## Syntax
<a name="aws-properties-inspectorv2-filter-mapfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-filter-mapfilter-syntax.json"></a>

```
{
  "[Comparison](#cfn-inspectorv2-filter-mapfilter-comparison)" : {{String}},
  "[Key](#cfn-inspectorv2-filter-mapfilter-key)" : {{String}},
  "[Value](#cfn-inspectorv2-filter-mapfilter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-inspectorv2-filter-mapfilter-syntax.yaml"></a>

```
  [Comparison](#cfn-inspectorv2-filter-mapfilter-comparison): {{String}}
  [Key](#cfn-inspectorv2-filter-mapfilter-key): {{String}}
  [Value](#cfn-inspectorv2-filter-mapfilter-value): {{String}}
```

## Properties
<a name="aws-properties-inspectorv2-filter-mapfilter-properties"></a>

`Comparison`  <a name="cfn-inspectorv2-filter-mapfilter-comparison"></a>
The operator to use when comparing values in the filter.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-inspectorv2-filter-mapfilter-key"></a>
The tag key used in the filter.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-inspectorv2-filter-mapfilter-value"></a>
The tag value used in the filter.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
