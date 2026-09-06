---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpooldomain-customdomainconfigtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolDomain CustomDomainConfigType
<a name="aws-properties-cognito-userpooldomain-customdomainconfigtype"></a>

The configuration for a hosted UI custom domain.

## Syntax
<a name="aws-properties-cognito-userpooldomain-customdomainconfigtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpooldomain-customdomainconfigtype-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-cognito-userpooldomain-customdomainconfigtype-certificatearn)" : {{String}},
  "[SecurityPolicy](#cfn-cognito-userpooldomain-customdomainconfigtype-securitypolicy)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpooldomain-customdomainconfigtype-syntax.yaml"></a>

```
  [CertificateArn](#cfn-cognito-userpooldomain-customdomainconfigtype-certificatearn): {{String}}
  [SecurityPolicy](#cfn-cognito-userpooldomain-customdomainconfigtype-securitypolicy): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpooldomain-customdomainconfigtype-properties"></a>

`CertificateArn`  <a name="cfn-cognito-userpooldomain-customdomainconfigtype-certificatearn"></a>
The Amazon Resource Name (ARN) of an AWS Certificate Manager SSL certificate. You use this certificate for the subdomain of your custom domain.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityPolicy`  <a name="cfn-cognito-userpooldomain-customdomainconfigtype-securitypolicy"></a>
The security policy for the custom domain. Defines the minimum TLS version and cipher suites that Amazon CloudFront supports when communicating with clients. For specific guidance, see [Supported protocols and ciphers between viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html). Valid values are as follows:
+ `TLS_V1_3_2025` (strictest): A post-quantum-ready policy requiring TLS 1.3. It provides the strongest security posture and is ideal for workloads where all clients and browsers are updated to the latest versions. [Supported protocols and ciphers for TLSv1.3\_2025](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html).
+ `TLS_V1_2_2021` (recommended): A post-quantum-ready policy which prefers TLS 1.3 but allows fallback to TLS 1.2 to accommodate older clients. It is the recommended minimum for typical commercial-grade consumer applications. [Supported protocols and ciphers for TLSv1.2\_2021](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html).
+ `TLS_V1` (strongly discouraged): Permits fallback to TLS 1.0. It offers the broadest compatibility, including support for legacy clients that are more than a decade old. This compatibility comes at the expense of allowing TLS versions and cryptographic algorithms that are no longer considered safe for commercial use. [Supported protocols and ciphers for TLSv1](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html).
*Required*: No
*Type*: String
*Allowed values*: `TLS_V1 | TLS_V1_2_2021 | TLS_V1_3_2025`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
