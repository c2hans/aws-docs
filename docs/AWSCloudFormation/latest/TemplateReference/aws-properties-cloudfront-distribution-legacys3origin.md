---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-legacys3origin.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution LegacyS3Origin
<a name="aws-properties-cloudfront-distribution-legacys3origin"></a>

The origin as an Amazon S3 bucket.

**Note**
This property is legacy. We recommend that you use [Origin](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html) instead.

## Syntax
<a name="aws-properties-cloudfront-distribution-legacys3origin-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-legacys3origin-syntax.json"></a>

```
{
  "[DNSName](#cfn-cloudfront-distribution-legacys3origin-dnsname)" : {{String}},
  "[OriginAccessIdentity](#cfn-cloudfront-distribution-legacys3origin-originaccessidentity)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-legacys3origin-syntax.yaml"></a>

```
  [DNSName](#cfn-cloudfront-distribution-legacys3origin-dnsname): {{String}}
  [OriginAccessIdentity](#cfn-cloudfront-distribution-legacys3origin-originaccessidentity): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-legacys3origin-properties"></a>

`DNSName`  <a name="cfn-cloudfront-distribution-legacys3origin-dnsname"></a>
The domain name assigned to your CloudFront distribution.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginAccessIdentity`  <a name="cfn-cloudfront-distribution-legacys3origin-originaccessidentity"></a>
The CloudFront origin access identity to associate with the distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 through CloudFront.
This property is legacy. We recommend that you use [OriginAccessControl](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-originaccesscontrol.html) instead.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
