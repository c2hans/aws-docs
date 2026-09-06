---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-statuscodes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution StatusCodes
<a name="aws-properties-cloudfront-distribution-statuscodes"></a>

A complex data type for the status codes that you specify that, when returned by a primary origin, trigger CloudFront to failover to a second origin.

## Syntax
<a name="aws-properties-cloudfront-distribution-statuscodes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-statuscodes-syntax.json"></a>

```
{
  "[Items](#cfn-cloudfront-distribution-statuscodes-items)" : {{[ Integer, ... ]}},
  "[Quantity](#cfn-cloudfront-distribution-statuscodes-quantity)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-statuscodes-syntax.yaml"></a>

```
  [Items](#cfn-cloudfront-distribution-statuscodes-items): {{
    - Integer}}
  [Quantity](#cfn-cloudfront-distribution-statuscodes-quantity): {{Integer}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-statuscodes-properties"></a>

`Items`  <a name="cfn-cloudfront-distribution-statuscodes-items"></a>
The items (status codes) for an origin group.
*Required*: Yes
*Type*: Array of Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Quantity`  <a name="cfn-cloudfront-distribution-statuscodes-quantity"></a>
The number of status codes.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
