---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-vpcoriginconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution VpcOriginConfig
<a name="aws-properties-cloudfront-distribution-vpcoriginconfig"></a>

An Amazon CloudFront VPC origin configuration.

## Syntax
<a name="aws-properties-cloudfront-distribution-vpcoriginconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-vpcoriginconfig-syntax.json"></a>

```
{
  "[OriginKeepaliveTimeout](#cfn-cloudfront-distribution-vpcoriginconfig-originkeepalivetimeout)" : {{Integer}},
  "[OriginReadTimeout](#cfn-cloudfront-distribution-vpcoriginconfig-originreadtimeout)" : {{Integer}},
  "[OwnerAccountId](#cfn-cloudfront-distribution-vpcoriginconfig-owneraccountid)" : {{String}},
  "[VpcOriginId](#cfn-cloudfront-distribution-vpcoriginconfig-vpcoriginid)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-vpcoriginconfig-syntax.yaml"></a>

```
  [OriginKeepaliveTimeout](#cfn-cloudfront-distribution-vpcoriginconfig-originkeepalivetimeout): {{Integer}}
  [OriginReadTimeout](#cfn-cloudfront-distribution-vpcoriginconfig-originreadtimeout): {{Integer}}
  [OwnerAccountId](#cfn-cloudfront-distribution-vpcoriginconfig-owneraccountid): {{String}}
  [VpcOriginId](#cfn-cloudfront-distribution-vpcoriginconfig-vpcoriginid): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-vpcoriginconfig-properties"></a>

`OriginKeepaliveTimeout`  <a name="cfn-cloudfront-distribution-vpcoriginconfig-originkeepalivetimeout"></a>
Specifies how long, in seconds, CloudFront persists its connection to the origin. The minimum timeout is 1 second, the maximum is 300 seconds, and the default (if you don't specify otherwise) is 5 seconds.
For more information, see [Keep-alive timeout (custom origins only)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginKeepaliveTimeout) in the *Amazon CloudFront Developer Guide*.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginReadTimeout`  <a name="cfn-cloudfront-distribution-vpcoriginconfig-originreadtimeout"></a>
Specifies how long, in seconds, CloudFront waits for a response from the origin. This is also known as the *origin response timeout*. The minimum timeout is 1 second, the maximum is 120 seconds, and the default (if you don't specify otherwise) is 30 seconds.
For more information, see [Response timeout](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginResponseTimeout) in the *Amazon CloudFront Developer Guide*.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OwnerAccountId`  <a name="cfn-cloudfront-distribution-vpcoriginconfig-owneraccountid"></a>
The account ID of the AWS account that owns the VPC origin.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcOriginId`  <a name="cfn-cloudfront-distribution-vpcoriginconfig-vpcoriginid"></a>
The VPC origin ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
