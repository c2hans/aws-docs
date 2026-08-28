---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-s3originconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution S3OriginConfig
<a name="aws-properties-cloudfront-distribution-s3originconfig"></a>

A complex type that contains information about the Amazon S3 origin. If the origin is a custom origin or an S3 bucket that is configured as a website endpoint, use the `CustomOriginConfig` element instead.

## Syntax
<a name="aws-properties-cloudfront-distribution-s3originconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-s3originconfig-syntax.json"></a>

```
{
  "[OriginAccessIdentity](#cfn-cloudfront-distribution-s3originconfig-originaccessidentity)" : {{String}},
  "[OriginReadTimeout](#cfn-cloudfront-distribution-s3originconfig-originreadtimeout)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-s3originconfig-syntax.yaml"></a>

```
  [OriginAccessIdentity](#cfn-cloudfront-distribution-s3originconfig-originaccessidentity): {{String}}
  [OriginReadTimeout](#cfn-cloudfront-distribution-s3originconfig-originreadtimeout): {{Integer}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-s3originconfig-properties"></a>

`OriginAccessIdentity`  <a name="cfn-cloudfront-distribution-s3originconfig-originaccessidentity"></a>
If you're using origin access control (OAC) instead of origin access identity, specify an empty `OriginAccessIdentity` element. For more information, see [Restricting access to an AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.html) in the *Amazon CloudFront Developer Guide*.
The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can *only* access objects in an Amazon S3 bucket through CloudFront. The format of the value is:
 `origin-access-identity/cloudfront/ID-of-origin-access-identity`
The ` ID-of-origin-access-identity ` is the value that CloudFront returned in the `ID` element when you created the origin access identity.
If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty `OriginAccessIdentity` element.
To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty `OriginAccessIdentity` element.
To replace the origin access identity, update the distribution configuration and specify the new origin access identity.
For more information about the origin access identity, see [Serving Private Content through CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginReadTimeout`  <a name="cfn-cloudfront-distribution-s3originconfig-originreadtimeout"></a>
Specifies how long, in seconds, CloudFront waits for a response from the origin. This is also known as the *origin response timeout*. The minimum timeout is 1 second, the maximum is 120 seconds, and the default (if you don't specify otherwise) is 30 seconds.
For more information, see [Response timeout](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginResponseTimeout) in the *Amazon CloudFront Developer Guide*.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-cloudfront-distribution-s3originconfig--seealso"></a>
+ [S3OriginConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_S3OriginConfig.html) in the *Amazon CloudFront API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
