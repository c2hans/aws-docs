---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-originrequestpolicy-headersconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::OriginRequestPolicy HeadersConfig
<a name="aws-properties-cloudfront-originrequestpolicy-headersconfig"></a>

An object that determines whether any HTTP headers (and if so, which headers) are included in requests that CloudFront sends to the origin.

## Syntax
<a name="aws-properties-cloudfront-originrequestpolicy-headersconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-originrequestpolicy-headersconfig-syntax.json"></a>

```
{
  "[HeaderBehavior](#cfn-cloudfront-originrequestpolicy-headersconfig-headerbehavior)" : {{String}},
  "[Headers](#cfn-cloudfront-originrequestpolicy-headersconfig-headers)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudfront-originrequestpolicy-headersconfig-syntax.yaml"></a>

```
  [HeaderBehavior](#cfn-cloudfront-originrequestpolicy-headersconfig-headerbehavior): {{String}}
  [Headers](#cfn-cloudfront-originrequestpolicy-headersconfig-headers): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudfront-originrequestpolicy-headersconfig-properties"></a>

`HeaderBehavior`  <a name="cfn-cloudfront-originrequestpolicy-headersconfig-headerbehavior"></a>
Determines whether any HTTP headers are included in requests that CloudFront sends to the origin. Valid values are:
+ `none` – No HTTP headers in viewer requests are included in requests that CloudFront sends to the origin. Even when this field is set to `none`, any headers that are listed in a `CachePolicy`*are* included in origin requests.
+ `whitelist` – Only the HTTP headers that are listed in the `Headers` type are included in requests that CloudFront sends to the origin.
+ `allViewer` – All HTTP headers in viewer requests are included in requests that CloudFront sends to the origin.
+ `allViewerAndWhitelistCloudFront` – All HTTP headers in viewer requests and the additional CloudFront headers that are listed in the `Headers` type are included in requests that CloudFront sends to the origin. The additional headers are added by CloudFront.
+ `allExcept` – All HTTP headers in viewer requests are included in requests that CloudFront sends to the origin, * **except** * for those listed in the `Headers` type, which are not included.
*Required*: Yes
*Type*: String
*Pattern*: `^(none|whitelist|allViewer|allViewerAndWhitelistCloudFront|allExcept)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Headers`  <a name="cfn-cloudfront-originrequestpolicy-headersconfig-headers"></a>
Contains a list of HTTP header names.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
