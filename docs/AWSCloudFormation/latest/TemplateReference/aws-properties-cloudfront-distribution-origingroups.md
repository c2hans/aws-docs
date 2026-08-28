---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-origingroups.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution OriginGroups
<a name="aws-properties-cloudfront-distribution-origingroups"></a>

A complex data type for the origin groups specified for a distribution.

## Syntax
<a name="aws-properties-cloudfront-distribution-origingroups-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-origingroups-syntax.json"></a>

```
{
  "[Items](#cfn-cloudfront-distribution-origingroups-items)" : {{[ OriginGroup, ... ]}},
  "[Quantity](#cfn-cloudfront-distribution-origingroups-quantity)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-origingroups-syntax.yaml"></a>

```
  [Items](#cfn-cloudfront-distribution-origingroups-items): {{
    - OriginGroup}}
  [Quantity](#cfn-cloudfront-distribution-origingroups-quantity): {{Integer}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-origingroups-properties"></a>

`Items`  <a name="cfn-cloudfront-distribution-origingroups-items"></a>
The items (origin groups) in a distribution.
*Required*: No
*Type*: Array of [OriginGroup](aws-properties-cloudfront-distribution-origingroup.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Quantity`  <a name="cfn-cloudfront-distribution-origingroups-quantity"></a>
The number of origin groups.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
