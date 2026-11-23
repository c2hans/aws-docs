---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-connectiongroup-viewerfallback.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ConnectionGroup ViewerFallback

The distribution whose certificate CloudFront uses for viewer requests that arrive on the connection group's Anycast static IPs without Server Name Indication (SNI). You can specify one distribution per Anycast static IP list.

## Syntax
<a name="aws-properties-cloudfront-connectiongroup-viewerfallback-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-connectiongroup-viewerfallback-syntax.json"></a>

```json
{
  "[DistributionId](#cfn-cloudfront-connectiongroup-viewerfallback-distributionid)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-connectiongroup-viewerfallback-syntax.yaml"></a>

```yaml
  [DistributionId](#cfn-cloudfront-connectiongroup-viewerfallback-distributionid): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-connectiongroup-viewerfallback-properties"></a>

`DistributionId`  <a name="cfn-cloudfront-connectiongroup-viewerfallback-distributionid"></a>
The ID of the distribution whose certificate CloudFront uses to establish TLS connections for viewer requests that don't include SNI.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
