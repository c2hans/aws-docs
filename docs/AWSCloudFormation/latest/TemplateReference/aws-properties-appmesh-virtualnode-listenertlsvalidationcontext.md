---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-listenertlsvalidationcontext.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode ListenerTlsValidationContext
<a name="aws-properties-appmesh-virtualnode-listenertlsvalidationcontext"></a>

An object that represents a listener's Transport Layer Security (TLS) validation context.

## Syntax
<a name="aws-properties-appmesh-virtualnode-listenertlsvalidationcontext-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-listenertlsvalidationcontext-syntax.json"></a>

```
{
  "[SubjectAlternativeNames](#cfn-appmesh-virtualnode-listenertlsvalidationcontext-subjectalternativenames)" : {{SubjectAlternativeNames}},
  "[Trust](#cfn-appmesh-virtualnode-listenertlsvalidationcontext-trust)" : {{ListenerTlsValidationContextTrust}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-listenertlsvalidationcontext-syntax.yaml"></a>

```
  [SubjectAlternativeNames](#cfn-appmesh-virtualnode-listenertlsvalidationcontext-subjectalternativenames): {{
    SubjectAlternativeNames}}
  [Trust](#cfn-appmesh-virtualnode-listenertlsvalidationcontext-trust): {{
    ListenerTlsValidationContextTrust}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-listenertlsvalidationcontext-properties"></a>

`SubjectAlternativeNames`  <a name="cfn-appmesh-virtualnode-listenertlsvalidationcontext-subjectalternativenames"></a>
A reference to an object that represents the SANs for a listener's Transport Layer Security (TLS) validation context.
*Required*: No
*Type*: [SubjectAlternativeNames](aws-properties-appmesh-virtualnode-subjectalternativenames.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Trust`  <a name="cfn-appmesh-virtualnode-listenertlsvalidationcontext-trust"></a>
A reference to where to retrieve the trust chain when validating a peer’s Transport Layer Security (TLS) certificate.
*Required*: Yes
*Type*: [ListenerTlsValidationContextTrust](aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
