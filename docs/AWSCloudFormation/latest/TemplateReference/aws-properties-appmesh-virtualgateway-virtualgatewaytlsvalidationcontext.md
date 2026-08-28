---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewayTlsValidationContext
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext"></a>

An object that represents a Transport Layer Security (TLS) validation context.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-syntax.json"></a>

```
{
  "[SubjectAlternativeNames](#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-subjectalternativenames)" : {{SubjectAlternativeNames}},
  "[Trust](#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-trust)" : {{VirtualGatewayTlsValidationContextTrust}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-syntax.yaml"></a>

```
  [SubjectAlternativeNames](#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-subjectalternativenames): {{
    SubjectAlternativeNames}}
  [Trust](#cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-trust): {{
    VirtualGatewayTlsValidationContextTrust}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-properties"></a>

`SubjectAlternativeNames`  <a name="cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-subjectalternativenames"></a>
A reference to an object that represents the SANs for a virtual gateway's listener's Transport Layer Security (TLS) validation context.
*Required*: No
*Type*: [SubjectAlternativeNames](aws-properties-appmesh-virtualgateway-subjectalternativenames.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Trust`  <a name="cfn-appmesh-virtualgateway-virtualgatewaytlsvalidationcontext-trust"></a>
A reference to where to retrieve the trust chain when validating a peer’s Transport Layer Security (TLS) certificate.
*Required*: Yes
*Type*: [VirtualGatewayTlsValidationContextTrust](aws-properties-appmesh-virtualgateway-virtualgatewaytlsvalidationcontexttrust.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
