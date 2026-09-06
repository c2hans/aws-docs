---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewayTlsValidationContextAcmTrust
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust"></a>

An object that represents a Transport Layer Security (TLS) validation context trust for an AWS Certificate Manager certificate.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust-syntax.json"></a>

```
{
  "[CertificateAuthorityArns](#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust-certificateauthorityarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust-syntax.yaml"></a>

```
  [CertificateAuthorityArns](#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust-certificateauthorityarns): {{
    - String}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust-properties"></a>

`CertificateAuthorityArns`  <a name="cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust-certificateauthorityarns"></a>
One or more ACM Amazon Resource Name (ARN)s.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
