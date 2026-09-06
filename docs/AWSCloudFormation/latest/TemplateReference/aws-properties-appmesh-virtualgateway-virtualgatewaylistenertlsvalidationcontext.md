---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewayListenerTlsValidationContext
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext"></a>

An object that represents a virtual gateway's listener's Transport Layer Security (TLS) validation context.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-syntax.json"></a>

```
{
  "[SubjectAlternativeNames](#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-subjectalternativenames)" : {{SubjectAlternativeNames}},
  "[Trust](#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-trust)" : {{VirtualGatewayListenerTlsValidationContextTrust}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-syntax.yaml"></a>

```
  [SubjectAlternativeNames](#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-subjectalternativenames): {{
    SubjectAlternativeNames}}
  [Trust](#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-trust): {{
    VirtualGatewayListenerTlsValidationContextTrust}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-properties"></a>

`SubjectAlternativeNames`  <a name="cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-subjectalternativenames"></a>
A reference to an object that represents the SANs for a virtual gateway listener's Transport Layer Security (TLS) validation context.
*Required*: No
*Type*: [SubjectAlternativeNames](aws-properties-appmesh-virtualgateway-subjectalternativenames.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Trust`  <a name="cfn-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontext-trust"></a>
A reference to where to retrieve the trust chain when validating a peer’s Transport Layer Security (TLS) certificate.
*Required*: Yes
*Type*: [VirtualGatewayListenerTlsValidationContextTrust](aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsvalidationcontexttrust.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
