---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-cachepolicy-headersconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::CachePolicy HeadersConfig
<a name="aws-properties-cloudfront-cachepolicy-headersconfig"></a>

An object that determines whether any HTTP headers (and if so, which headers) are included in the cache key and in requests that CloudFront sends to the origin.

## Syntax
<a name="aws-properties-cloudfront-cachepolicy-headersconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-cachepolicy-headersconfig-syntax.json"></a>

```
{
  "[HeaderBehavior](#cfn-cloudfront-cachepolicy-headersconfig-headerbehavior)" : {{String}},
  "[Headers](#cfn-cloudfront-cachepolicy-headersconfig-headers)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudfront-cachepolicy-headersconfig-syntax.yaml"></a>

```
  [HeaderBehavior](#cfn-cloudfront-cachepolicy-headersconfig-headerbehavior): {{String}}
  [Headers](#cfn-cloudfront-cachepolicy-headersconfig-headers): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudfront-cachepolicy-headersconfig-properties"></a>

`HeaderBehavior`  <a name="cfn-cloudfront-cachepolicy-headersconfig-headerbehavior"></a>
Determines whether any HTTP headers are included in the cache key and in requests that CloudFront sends to the origin. Valid values are:
+ `none` – No HTTP headers are included in the cache key or in requests that CloudFront sends to the origin. Even when this field is set to `none`, any headers that are listed in an `OriginRequestPolicy`*are* included in origin requests.
+ `whitelist` – Only the HTTP headers that are listed in the `Headers` type are included in the cache key and in requests that CloudFront sends to the origin.
*Required*: Yes
*Type*: String
*Pattern*: `^(none|whitelist)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Headers`  <a name="cfn-cloudfront-cachepolicy-headersconfig-headers"></a>
Contains a list of HTTP header names.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
