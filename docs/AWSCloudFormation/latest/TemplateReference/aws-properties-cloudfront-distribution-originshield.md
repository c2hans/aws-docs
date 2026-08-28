---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-originshield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution OriginShield
<a name="aws-properties-cloudfront-distribution-originshield"></a>

CloudFront Origin Shield.

Using Origin Shield can help reduce the load on your origin. For more information, see [Using Origin Shield](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html) in the *Amazon CloudFront Developer Guide*.

## Syntax
<a name="aws-properties-cloudfront-distribution-originshield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-originshield-syntax.json"></a>

```
{
  "[Enabled](#cfn-cloudfront-distribution-originshield-enabled)" : {{Boolean}},
  "[OriginShieldRegion](#cfn-cloudfront-distribution-originshield-originshieldregion)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-originshield-syntax.yaml"></a>

```
  [Enabled](#cfn-cloudfront-distribution-originshield-enabled): {{Boolean}}
  [OriginShieldRegion](#cfn-cloudfront-distribution-originshield-originshieldregion): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-originshield-properties"></a>

`Enabled`  <a name="cfn-cloudfront-distribution-originshield-enabled"></a>
A flag that specifies whether Origin Shield is enabled.
When it's enabled, CloudFront routes all requests through Origin Shield, which can help protect your origin. When it's disabled, CloudFront might send requests directly to your origin from multiple edge locations or regional edge caches.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginShieldRegion`  <a name="cfn-cloudfront-distribution-originshield-originshieldregion"></a>
The AWS Region for Origin Shield.
Specify the AWS Region that has the lowest latency to your origin. To specify a region, use the region code, not the region name. For example, specify the US East (Ohio) region as `us-east-2`.
When you enable CloudFront Origin Shield, you must specify the AWS Region for Origin Shield. For the list of AWS Regions that you can specify, and for help choosing the best Region for your origin, see [Choosing the AWS Region for Origin Shield](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html#choose-origin-shield-region) in the *Amazon CloudFront Developer Guide*.
*Required*: No
*Type*: String
*Pattern*: `[a-z]{2}-[a-z]+-\d`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
