---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-truststore-cacertificatesbundles3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::TrustStore CaCertificatesBundleS3Location
<a name="aws-properties-cloudfront-truststore-cacertificatesbundles3location"></a>

The CA certificates bundle location in Amazon S3.

## Syntax
<a name="aws-properties-cloudfront-truststore-cacertificatesbundles3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-truststore-cacertificatesbundles3location-syntax.json"></a>

```
{
  "[Bucket](#cfn-cloudfront-truststore-cacertificatesbundles3location-bucket)" : {{String}},
  "[Key](#cfn-cloudfront-truststore-cacertificatesbundles3location-key)" : {{String}},
  "[Region](#cfn-cloudfront-truststore-cacertificatesbundles3location-region)" : {{String}},
  "[Version](#cfn-cloudfront-truststore-cacertificatesbundles3location-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-truststore-cacertificatesbundles3location-syntax.yaml"></a>

```
  [Bucket](#cfn-cloudfront-truststore-cacertificatesbundles3location-bucket): {{String}}
  [Key](#cfn-cloudfront-truststore-cacertificatesbundles3location-key): {{String}}
  [Region](#cfn-cloudfront-truststore-cacertificatesbundles3location-region): {{String}}
  [Version](#cfn-cloudfront-truststore-cacertificatesbundles3location-version): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-truststore-cacertificatesbundles3location-properties"></a>

`Bucket`  <a name="cfn-cloudfront-truststore-cacertificatesbundles3location-bucket"></a>
The S3 bucket.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-cloudfront-truststore-cacertificatesbundles3location-key"></a>
The location's key.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-cloudfront-truststore-cacertificatesbundles3location-region"></a>
The location's Region.
*Required*: Yes
*Type*: String
*Pattern*: `[a-z]{2}-[a-z]+-\d`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-cloudfront-truststore-cacertificatesbundles3location-version"></a>
The location's version.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
