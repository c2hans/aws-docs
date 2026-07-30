---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewayTlsValidationContextTrust
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust"></a>

An object that represents a Transport Layer Security (TLS) validation context trust.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-syntax.json"></a>

```
{
  "[ACM](#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-acm)" : {{VirtualGatewayTlsValidationContextAcmTrust}},
  "[File](#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-file)" : {{VirtualGatewayTlsValidationContextFileTrust}},
  "[SDS](#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-sds)" : {{VirtualGatewayTlsValidationContextSdsTrust}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-syntax.yaml"></a>

```
  [ACM](#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-acm): {{
    VirtualGatewayTlsValidationContextAcmTrust}}
  [File](#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-file): {{
    VirtualGatewayTlsValidationContextFileTrust}}
  [SDS](#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-sds): {{
    VirtualGatewayTlsValidationContextSdsTrust}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-properties"></a>

`ACM`  <a name="cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-acm"></a>
A reference to an object that represents a Transport Layer Security (TLS) validation context trust for an AWS Certificate Manager certificate.
*Required*: No
*Type*: [VirtualGatewayTlsValidationContextAcmTrust](aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextacmtrust.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`File`  <a name="cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-file"></a>
An object that represents a Transport Layer Security (TLS) validation context trust for a local file.
*Required*: No
*Type*: [VirtualGatewayTlsValidationContextFileTrust](aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextfiletrust.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SDS`  <a name="cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust-sds"></a>
A reference to an object that represents a virtual gateway's Transport Layer Security (TLS) Secret Discovery Service validation context trust.
*Required*: No
*Type*: [VirtualGatewayTlsValidationContextSdsTrust](aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
