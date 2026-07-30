---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-responseheaderspolicy-customheadersconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ResponseHeadersPolicy CustomHeadersConfig
<a name="aws-properties-cloudfront-responseheaderspolicy-customheadersconfig"></a>

A list of HTTP response header names and their values. CloudFront includes these headers in HTTP responses that it sends for requests that match a cache behavior that's associated with this response headers policy.

## Syntax
<a name="aws-properties-cloudfront-responseheaderspolicy-customheadersconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-responseheaderspolicy-customheadersconfig-syntax.json"></a>

```
{
  "[Items](#cfn-cloudfront-responseheaderspolicy-customheadersconfig-items)" : {{[ CustomHeader, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudfront-responseheaderspolicy-customheadersconfig-syntax.yaml"></a>

```
  [Items](#cfn-cloudfront-responseheaderspolicy-customheadersconfig-items): {{
    - CustomHeader}}
```

## Properties
<a name="aws-properties-cloudfront-responseheaderspolicy-customheadersconfig-properties"></a>

`Items`  <a name="cfn-cloudfront-responseheaderspolicy-customheadersconfig-items"></a>
The list of HTTP response headers and their values.
*Required*: Yes
*Type*: Array of [CustomHeader](aws-properties-cloudfront-responseheaderspolicy-customheader.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
