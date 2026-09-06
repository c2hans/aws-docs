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
