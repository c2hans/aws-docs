---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-legacycustomorigin.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution LegacyCustomOrigin
<a name="aws-properties-cloudfront-distribution-legacycustomorigin"></a>

A custom origin. A custom origin is any origin that is *not* an Amazon S3 bucket, with one exception. An Amazon S3 bucket that is [configured with static website hosting](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html)*is* a custom origin.

**Note**
This property is legacy. We recommend that you use [Origin](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html) instead.

## Syntax
<a name="aws-properties-cloudfront-distribution-legacycustomorigin-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-legacycustomorigin-syntax.json"></a>

```
{
  "[DNSName](#cfn-cloudfront-distribution-legacycustomorigin-dnsname)" : {{String}},
  "[HTTPPort](#cfn-cloudfront-distribution-legacycustomorigin-httpport)" : {{Integer}},
  "[HTTPSPort](#cfn-cloudfront-distribution-legacycustomorigin-httpsport)" : {{Integer}},
  "[OriginProtocolPolicy](#cfn-cloudfront-distribution-legacycustomorigin-originprotocolpolicy)" : {{String}},
  "[OriginSSLProtocols](#cfn-cloudfront-distribution-legacycustomorigin-originsslprotocols)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-legacycustomorigin-syntax.yaml"></a>

```
  [DNSName](#cfn-cloudfront-distribution-legacycustomorigin-dnsname): {{String}}
  [HTTPPort](#cfn-cloudfront-distribution-legacycustomorigin-httpport): {{Integer}}
  [HTTPSPort](#cfn-cloudfront-distribution-legacycustomorigin-httpsport): {{Integer}}
  [OriginProtocolPolicy](#cfn-cloudfront-distribution-legacycustomorigin-originprotocolpolicy): {{String}}
  [OriginSSLProtocols](#cfn-cloudfront-distribution-legacycustomorigin-originsslprotocols): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-legacycustomorigin-properties"></a>

`DNSName`  <a name="cfn-cloudfront-distribution-legacycustomorigin-dnsname"></a>
The domain name assigned to your CloudFront distribution.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HTTPPort`  <a name="cfn-cloudfront-distribution-legacycustomorigin-httpport"></a>
The HTTP port that CloudFront uses to connect to the origin. Specify the HTTP port that the origin listens on.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HTTPSPort`  <a name="cfn-cloudfront-distribution-legacycustomorigin-httpsport"></a>
The HTTPS port that CloudFront uses to connect to the origin. Specify the HTTPS port that the origin listens on.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginProtocolPolicy`  <a name="cfn-cloudfront-distribution-legacycustomorigin-originprotocolpolicy"></a>
Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginSSLProtocols`  <a name="cfn-cloudfront-distribution-legacycustomorigin-originsslprotocols"></a>
The minimum SSL/TLS protocol version that CloudFront uses when communicating with your origin server over HTTPs.
For more information, see [Minimum Origin SSL Protocol](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginSSLProtocols) in the *Amazon CloudFront Developer Guide*.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
