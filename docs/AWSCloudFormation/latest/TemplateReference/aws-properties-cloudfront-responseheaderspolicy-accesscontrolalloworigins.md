---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-responseheaderspolicy-accesscontrolalloworigins.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ResponseHeadersPolicy AccessControlAllowOrigins
<a name="aws-properties-cloudfront-responseheaderspolicy-accesscontrolalloworigins"></a>

A list of origins (domain names) that CloudFront can use as the value for the `Access-Control-Allow-Origin` HTTP response header.

For more information about the `Access-Control-Allow-Origin` HTTP response header, see [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) in the MDN Web Docs.

## Syntax
<a name="aws-properties-cloudfront-responseheaderspolicy-accesscontrolalloworigins-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-responseheaderspolicy-accesscontrolalloworigins-syntax.json"></a>

```
{
  "[Items](#cfn-cloudfront-responseheaderspolicy-accesscontrolalloworigins-items)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudfront-responseheaderspolicy-accesscontrolalloworigins-syntax.yaml"></a>

```
  [Items](#cfn-cloudfront-responseheaderspolicy-accesscontrolalloworigins-items): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudfront-responseheaderspolicy-accesscontrolalloworigins-properties"></a>

`Items`  <a name="cfn-cloudfront-responseheaderspolicy-accesscontrolalloworigins-items"></a>
The list of origins (domain names). You can specify `*` to allow all origins.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
