---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGatewayV2::DomainName DomainNameConfiguration
<a name="aws-properties-apigatewayv2-domainname-domainnameconfiguration"></a>

The `DomainNameConfiguration` property type specifies the configuration for an API's domain name.

`DomainNameConfiguration` is a property of the [AWS::ApiGatewayV2::DomainName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html) resource.

## Syntax
<a name="aws-properties-apigatewayv2-domainname-domainnameconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigatewayv2-domainname-domainnameconfiguration-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatearn)" : {{String}},
  "[CertificateName](#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatename)" : {{String}},
  "[EndpointType](#cfn-apigatewayv2-domainname-domainnameconfiguration-endpointtype)" : {{String}},
  "[IpAddressType](#cfn-apigatewayv2-domainname-domainnameconfiguration-ipaddresstype)" : {{String}},
  "[OwnershipVerificationCertificateArn](#cfn-apigatewayv2-domainname-domainnameconfiguration-ownershipverificationcertificatearn)" : {{String}},
  "[SecurityPolicy](#cfn-apigatewayv2-domainname-domainnameconfiguration-securitypolicy)" : {{String}}
}
```

### YAML
<a name="aws-properties-apigatewayv2-domainname-domainnameconfiguration-syntax.yaml"></a>

```
  [CertificateArn](#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatearn): {{String}}
  [CertificateName](#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatename): {{String}}
  [EndpointType](#cfn-apigatewayv2-domainname-domainnameconfiguration-endpointtype): {{String}}
  [IpAddressType](#cfn-apigatewayv2-domainname-domainnameconfiguration-ipaddresstype): {{String}}
  [OwnershipVerificationCertificateArn](#cfn-apigatewayv2-domainname-domainnameconfiguration-ownershipverificationcertificatearn): {{String}}
  [SecurityPolicy](#cfn-apigatewayv2-domainname-domainnameconfiguration-securitypolicy): {{String}}
```

## Properties
<a name="aws-properties-apigatewayv2-domainname-domainnameconfiguration-properties"></a>

`CertificateArn`  <a name="cfn-apigatewayv2-domainname-domainnameconfiguration-certificatearn"></a>
An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CertificateName`  <a name="cfn-apigatewayv2-domainname-domainnameconfiguration-certificatename"></a>
The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointType`  <a name="cfn-apigatewayv2-domainname-domainnameconfiguration-endpointtype"></a>
The endpoint type.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressType`  <a name="cfn-apigatewayv2-domainname-domainnameconfiguration-ipaddresstype"></a>
The IP address types that can invoke the domain name. Use `ipv4` to allow only IPv4 addresses to invoke your domain name, or use `dualstack` to allow both IPv4 and IPv6 addresses to invoke your domain name.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OwnershipVerificationCertificateArn`  <a name="cfn-apigatewayv2-domainname-domainnameconfiguration-ownershipverificationcertificatearn"></a>
The Amazon resource name (ARN) for the public certificate issued by AWS Certificate Manager. This ARN is used to validate custom domain ownership. It's required only if you configure mutual TLS and use either an ACM-imported or a private CA certificate ARN as the regionalCertificateArn.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityPolicy`  <a name="cfn-apigatewayv2-domainname-domainnameconfiguration-securitypolicy"></a>
The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are `TLS_1_0` and `TLS_1_2`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-apigatewayv2-domainname-domainnameconfiguration--seealso"></a>
+ [DomainNameConfiguration](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames-domainname.html#domainnames-domainname-model-domainnameconfiguration) in the *Amazon API Gateway Version 2 API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
