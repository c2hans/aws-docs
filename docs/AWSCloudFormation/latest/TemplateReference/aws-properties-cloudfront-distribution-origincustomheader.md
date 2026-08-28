---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-origincustomheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution OriginCustomHeader
<a name="aws-properties-cloudfront-distribution-origincustomheader"></a>

A complex type that contains `HeaderName` and `HeaderValue` elements, if any, for this distribution.

## Syntax
<a name="aws-properties-cloudfront-distribution-origincustomheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-origincustomheader-syntax.json"></a>

```
{
  "[HeaderName](#cfn-cloudfront-distribution-origincustomheader-headername)" : {{String}},
  "[HeaderValue](#cfn-cloudfront-distribution-origincustomheader-headervalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-origincustomheader-syntax.yaml"></a>

```
  [HeaderName](#cfn-cloudfront-distribution-origincustomheader-headername): {{String}}
  [HeaderValue](#cfn-cloudfront-distribution-origincustomheader-headervalue): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-origincustomheader-properties"></a>

`HeaderName`  <a name="cfn-cloudfront-distribution-origincustomheader-headername"></a>
The name of a header that you want CloudFront to send to your origin. For more information, see [Adding Custom Headers to Origin Requests](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html) in the * Amazon CloudFront Developer Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HeaderValue`  <a name="cfn-cloudfront-distribution-origincustomheader-headervalue"></a>
The value for the header that you specified in the `HeaderName` field.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-cloudfront-distribution-origincustomheader--seealso"></a>
+ [OriginCustomHeader](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_OriginCustomHeader.html) in the *Amazon CloudFront API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
