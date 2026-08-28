---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-customoriginconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution CustomOriginConfig
<a name="aws-properties-cloudfront-distribution-customoriginconfig"></a>

A custom origin. A custom origin is any origin that is *not* an Amazon S3 bucket, with one exception. An Amazon S3 bucket that is [configured with static website hosting](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html)*is* a custom origin.

## Syntax
<a name="aws-properties-cloudfront-distribution-customoriginconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-customoriginconfig-syntax.json"></a>

```
{
  "[HTTPPort](#cfn-cloudfront-distribution-customoriginconfig-httpport)" : {{Integer}},
  "[HTTPSPort](#cfn-cloudfront-distribution-customoriginconfig-httpsport)" : {{Integer}},
  "[IpAddressType](#cfn-cloudfront-distribution-customoriginconfig-ipaddresstype)" : {{String}},
  "[OriginKeepaliveTimeout](#cfn-cloudfront-distribution-customoriginconfig-originkeepalivetimeout)" : {{Integer}},
  "[OriginMtlsConfig](#cfn-cloudfront-distribution-customoriginconfig-originmtlsconfig)" : {{OriginMtlsConfig}},
  "[OriginProtocolPolicy](#cfn-cloudfront-distribution-customoriginconfig-originprotocolpolicy)" : {{String}},
  "[OriginReadTimeout](#cfn-cloudfront-distribution-customoriginconfig-originreadtimeout)" : {{Integer}},
  "[OriginSSLProtocols](#cfn-cloudfront-distribution-customoriginconfig-originsslprotocols)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-customoriginconfig-syntax.yaml"></a>

```
  [HTTPPort](#cfn-cloudfront-distribution-customoriginconfig-httpport): {{Integer}}
  [HTTPSPort](#cfn-cloudfront-distribution-customoriginconfig-httpsport): {{Integer}}
  [IpAddressType](#cfn-cloudfront-distribution-customoriginconfig-ipaddresstype): {{String}}
  [OriginKeepaliveTimeout](#cfn-cloudfront-distribution-customoriginconfig-originkeepalivetimeout): {{Integer}}
  [OriginMtlsConfig](#cfn-cloudfront-distribution-customoriginconfig-originmtlsconfig): {{
    OriginMtlsConfig}}
  [OriginProtocolPolicy](#cfn-cloudfront-distribution-customoriginconfig-originprotocolpolicy): {{String}}
  [OriginReadTimeout](#cfn-cloudfront-distribution-customoriginconfig-originreadtimeout): {{Integer}}
  [OriginSSLProtocols](#cfn-cloudfront-distribution-customoriginconfig-originsslprotocols): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-customoriginconfig-properties"></a>

`HTTPPort`  <a name="cfn-cloudfront-distribution-customoriginconfig-httpport"></a>
The HTTP port that CloudFront uses to connect to the origin. Specify the HTTP port that the origin listens on.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HTTPSPort`  <a name="cfn-cloudfront-distribution-customoriginconfig-httpsport"></a>
The HTTPS port that CloudFront uses to connect to the origin. Specify the HTTPS port that the origin listens on.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressType`  <a name="cfn-cloudfront-distribution-customoriginconfig-ipaddresstype"></a>
Specifies which IP protocol CloudFront uses when connecting to your origin. If your origin uses both IPv4 and IPv6 protocols, you can choose `dualstack` to help optimize reliability.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | ipv6 | dualstack`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginKeepaliveTimeout`  <a name="cfn-cloudfront-distribution-customoriginconfig-originkeepalivetimeout"></a>
Specifies how long, in seconds, CloudFront persists its connection to the origin. The minimum timeout is 1 second, the maximum is 300 seconds, and the default (if you don't specify otherwise) is 5 seconds.
For more information, see [Keep-alive timeout (custom origins only)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginKeepaliveTimeout) in the *Amazon CloudFront Developer Guide*.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginMtlsConfig`  <a name="cfn-cloudfront-distribution-customoriginconfig-originmtlsconfig"></a>
Configures mutual TLS authentication between CloudFront and your origin server.
*Required*: No
*Type*: [OriginMtlsConfig](aws-properties-cloudfront-distribution-originmtlsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginProtocolPolicy`  <a name="cfn-cloudfront-distribution-customoriginconfig-originprotocolpolicy"></a>
Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Valid values are:
+ `http-only` – CloudFront always uses HTTP to connect to the origin.
+ `match-viewer` – CloudFront connects to the origin using the same protocol that the viewer used to connect to CloudFront.
+ `https-only` – CloudFront always uses HTTPS to connect to the origin.
*Required*: Yes
*Type*: String
*Allowed values*: `http-only | match-viewer | https-only`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginReadTimeout`  <a name="cfn-cloudfront-distribution-customoriginconfig-originreadtimeout"></a>
Specifies how long, in seconds, CloudFront waits for a response from the origin. This is also known as the *origin response timeout*. The minimum timeout is 1 second, the maximum is 120 seconds, and the default (if you don't specify otherwise) is 30 seconds.
For more information, see [Response timeout](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginResponseTimeout) in the *Amazon CloudFront Developer Guide*.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginSSLProtocols`  <a name="cfn-cloudfront-distribution-customoriginconfig-originsslprotocols"></a>
Specifies the minimum SSL/TLS protocol that CloudFront uses when connecting to your origin over HTTPS. Valid values include `SSLv3`, `TLSv1`, `TLSv1.1`, and `TLSv1.2`.
For more information, see [Minimum Origin SSL Protocol](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginSSLProtocols) in the *Amazon CloudFront Developer Guide*.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-cloudfront-distribution-customoriginconfig--seealso"></a>
+ [CustomOriginConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CustomOriginConfig.html) in the *Amazon CloudFront API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
