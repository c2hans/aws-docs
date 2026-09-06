---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewayTlsValidationContextSdsTrust
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust"></a>

An object that represents a virtual gateway's listener's Transport Layer Security (TLS) Secret Discovery Service validation context trust. The proxy must be configured with a local SDS provider via a Unix Domain Socket. See App Mesh [TLS documentation](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html) for more info.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust-syntax.json"></a>

```
{
  "[SecretName](#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust-secretname)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust-syntax.yaml"></a>

```
  [SecretName](#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust-secretname): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust-properties"></a>

`SecretName`  <a name="cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontextsdstrust-secretname"></a>
A reference to an object that represents the name of the secret for a virtual gateway's Transport Layer Security (TLS) Secret Discovery Service validation context trust.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
