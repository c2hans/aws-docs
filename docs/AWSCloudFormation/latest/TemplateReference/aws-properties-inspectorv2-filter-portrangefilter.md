---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-filter-portrangefilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::Filter PortRangeFilter
<a name="aws-properties-inspectorv2-filter-portrangefilter"></a>

An object that describes the details of a port range filter.

## Syntax
<a name="aws-properties-inspectorv2-filter-portrangefilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-filter-portrangefilter-syntax.json"></a>

```
{
  "[BeginInclusive](#cfn-inspectorv2-filter-portrangefilter-begininclusive)" : {{Integer}},
  "[EndInclusive](#cfn-inspectorv2-filter-portrangefilter-endinclusive)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-inspectorv2-filter-portrangefilter-syntax.yaml"></a>

```
  [BeginInclusive](#cfn-inspectorv2-filter-portrangefilter-begininclusive): {{Integer}}
  [EndInclusive](#cfn-inspectorv2-filter-portrangefilter-endinclusive): {{Integer}}
```

## Properties
<a name="aws-properties-inspectorv2-filter-portrangefilter-properties"></a>

`BeginInclusive`  <a name="cfn-inspectorv2-filter-portrangefilter-begininclusive"></a>
The port number the port range begins at.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndInclusive`  <a name="cfn-inspectorv2-filter-portrangefilter-endinclusive"></a>
The port number the port range ends at.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
