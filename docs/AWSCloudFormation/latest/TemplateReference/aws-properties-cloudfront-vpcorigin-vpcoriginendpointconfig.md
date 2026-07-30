---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-vpcorigin-vpcoriginendpointconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::VpcOrigin VpcOriginEndpointConfig
<a name="aws-properties-cloudfront-vpcorigin-vpcoriginendpointconfig"></a>

An Amazon CloudFront VPC origin endpoint configuration.

## Syntax
<a name="aws-properties-cloudfront-vpcorigin-vpcoriginendpointconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-vpcorigin-vpcoriginendpointconfig-syntax.json"></a>

```
{
  "[Arn](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-arn)" : {{String}},
  "[HTTPPort](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-httpport)" : {{Integer}},
  "[HTTPSPort](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-httpsport)" : {{Integer}},
  "[IpAddressType](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-ipaddresstype)" : {{String}},
  "[Name](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-name)" : {{String}},
  "[OriginProtocolPolicy](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-originprotocolpolicy)" : {{String}},
  "[OriginSSLProtocols](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-originsslprotocols)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudfront-vpcorigin-vpcoriginendpointconfig-syntax.yaml"></a>

```
  [Arn](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-arn): {{String}}
  [HTTPPort](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-httpport): {{Integer}}
  [HTTPSPort](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-httpsport): {{Integer}}
  [IpAddressType](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-ipaddresstype): {{String}}
  [Name](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-name): {{String}}
  [OriginProtocolPolicy](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-originprotocolpolicy): {{String}}
  [OriginSSLProtocols](#cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-originsslprotocols): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudfront-vpcorigin-vpcoriginendpointconfig-properties"></a>

`Arn`  <a name="cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-arn"></a>
The ARN of the CloudFront VPC origin endpoint configuration.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HTTPPort`  <a name="cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-httpport"></a>
The HTTP port for the CloudFront VPC origin endpoint configuration. The default value is `80`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HTTPSPort`  <a name="cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-httpsport"></a>
The HTTPS port of the CloudFront VPC origin endpoint configuration. The default value is `443`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressType`  <a name="cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-ipaddresstype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | dualstack`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-name"></a>
The name of the CloudFront VPC origin endpoint configuration.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginProtocolPolicy`  <a name="cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-originprotocolpolicy"></a>
The origin protocol policy for the CloudFront VPC origin endpoint configuration.
*Required*: No
*Type*: String
*Allowed values*: `http-only | match-viewer | https-only`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginSSLProtocols`  <a name="cfn-cloudfront-vpcorigin-vpcoriginendpointconfig-originsslprotocols"></a>
Specifies the minimum SSL/TLS protocol that CloudFront uses when connecting to your origin over HTTPS. Valid values include `SSLv3`, `TLSv1`, `TLSv1.1`, and `TLSv1.2`.
For more information, see [Minimum Origin SSL Protocol](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html#DownloadDistValuesOriginSSLProtocols) in the *Amazon CloudFront Developer Guide*.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
