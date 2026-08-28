---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-cachepolicy-cookiesconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::CachePolicy CookiesConfig
<a name="aws-properties-cloudfront-cachepolicy-cookiesconfig"></a>

An object that determines whether any cookies in viewer requests (and if so, which cookies) are included in the cache key and in requests that CloudFront sends to the origin.

## Syntax
<a name="aws-properties-cloudfront-cachepolicy-cookiesconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-cachepolicy-cookiesconfig-syntax.json"></a>

```
{
  "[CookieBehavior](#cfn-cloudfront-cachepolicy-cookiesconfig-cookiebehavior)" : {{String}},
  "[Cookies](#cfn-cloudfront-cachepolicy-cookiesconfig-cookies)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudfront-cachepolicy-cookiesconfig-syntax.yaml"></a>

```
  [CookieBehavior](#cfn-cloudfront-cachepolicy-cookiesconfig-cookiebehavior): {{String}}
  [Cookies](#cfn-cloudfront-cachepolicy-cookiesconfig-cookies): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudfront-cachepolicy-cookiesconfig-properties"></a>

`CookieBehavior`  <a name="cfn-cloudfront-cachepolicy-cookiesconfig-cookiebehavior"></a>
Determines whether any cookies in viewer requests are included in the cache key and in requests that CloudFront sends to the origin. Valid values are:
+ `none` – No cookies in viewer requests are included in the cache key or in requests that CloudFront sends to the origin. Even when this field is set to `none`, any cookies that are listed in an `OriginRequestPolicy`*are* included in origin requests.
+ `whitelist` – Only the cookies in viewer requests that are listed in the `CookieNames` type are included in the cache key and in requests that CloudFront sends to the origin.
+ `allExcept` – All cookies in viewer requests are included in the cache key and in requests that CloudFront sends to the origin, * **except** * for those that are listed in the `CookieNames` type, which are not included.
+ `all` – All cookies in viewer requests are included in the cache key and in requests that CloudFront sends to the origin.
*Required*: Yes
*Type*: String
*Pattern*: `^(none|whitelist|allExcept|all)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Cookies`  <a name="cfn-cloudfront-cachepolicy-cookiesconfig-cookies"></a>
Contains a list of cookie names.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
