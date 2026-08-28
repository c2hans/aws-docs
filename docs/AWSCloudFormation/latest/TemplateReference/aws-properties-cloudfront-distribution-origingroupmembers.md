---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-origingroupmembers.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution OriginGroupMembers
<a name="aws-properties-cloudfront-distribution-origingroupmembers"></a>

A complex data type for the origins included in an origin group.

## Syntax
<a name="aws-properties-cloudfront-distribution-origingroupmembers-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-origingroupmembers-syntax.json"></a>

```
{
  "[Items](#cfn-cloudfront-distribution-origingroupmembers-items)" : {{[ OriginGroupMember, ... ]}},
  "[Quantity](#cfn-cloudfront-distribution-origingroupmembers-quantity)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-origingroupmembers-syntax.yaml"></a>

```
  [Items](#cfn-cloudfront-distribution-origingroupmembers-items): {{
    - OriginGroupMember}}
  [Quantity](#cfn-cloudfront-distribution-origingroupmembers-quantity): {{Integer}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-origingroupmembers-properties"></a>

`Items`  <a name="cfn-cloudfront-distribution-origingroupmembers-items"></a>
Items (origins) in an origin group.
*Required*: Yes
*Type*: Array of [OriginGroupMember](aws-properties-cloudfront-distribution-origingroupmember.md)
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Quantity`  <a name="cfn-cloudfront-distribution-origingroupmembers-quantity"></a>
The number of origins in an origin group.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
