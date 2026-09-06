---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-cachetagconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution CacheTagConfig
<a name="aws-properties-cloudfront-distribution-cachetagconfig"></a>

A complex type that specifies the HTTP header name from which CloudFront extracts cache tags from origin responses. When you add `CacheTagConfig` to a distribution, CloudFront reads the specified header from origin responses, parses the comma-separated tag values, and stores them with the cached object. You can then invalidate cached objects by tag using the `CreateInvalidation` API.

## Syntax
<a name="aws-properties-cloudfront-distribution-cachetagconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-cachetagconfig-syntax.json"></a>

```
{
  "[HeaderName](#cfn-cloudfront-distribution-cachetagconfig-headername)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-cachetagconfig-syntax.yaml"></a>

```
  [HeaderName](#cfn-cloudfront-distribution-cachetagconfig-headername): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-cachetagconfig-properties"></a>

`HeaderName`  <a name="cfn-cloudfront-distribution-cachetagconfig-headername"></a>
The name of the HTTP header that your origin includes in responses. CloudFront uses this header to extract cache tags. The header value must contain comma-separated tag values (for example, `product:electronics, category:tv, brand:example`).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
