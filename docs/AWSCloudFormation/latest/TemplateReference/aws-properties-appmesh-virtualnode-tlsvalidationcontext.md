---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-tlsvalidationcontext.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode TlsValidationContext
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontext"></a>

An object that represents how the proxy will validate its peer during Transport Layer Security (TLS) negotiation.

## Syntax
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontext-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontext-syntax.json"></a>

```
{
  "[SubjectAlternativeNames](#cfn-appmesh-virtualnode-tlsvalidationcontext-subjectalternativenames)" : {{SubjectAlternativeNames}},
  "[Trust](#cfn-appmesh-virtualnode-tlsvalidationcontext-trust)" : {{TlsValidationContextTrust}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontext-syntax.yaml"></a>

```
  [SubjectAlternativeNames](#cfn-appmesh-virtualnode-tlsvalidationcontext-subjectalternativenames): {{
    SubjectAlternativeNames}}
  [Trust](#cfn-appmesh-virtualnode-tlsvalidationcontext-trust): {{
    TlsValidationContextTrust}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontext-properties"></a>

`SubjectAlternativeNames`  <a name="cfn-appmesh-virtualnode-tlsvalidationcontext-subjectalternativenames"></a>
A reference to an object that represents the SANs for a Transport Layer Security (TLS) validation context. If you don't specify SANs on the *terminating* mesh endpoint, the Envoy proxy for that node doesn't verify the SAN on a peer client certificate. If you don't specify SANs on the *originating* mesh endpoint, the SAN on the certificate provided by the terminating endpoint must match the mesh endpoint service discovery configuration. Since SPIRE vended certificates have a SPIFFE ID as a name, you must set the SAN since the name doesn't match the service discovery name.
*Required*: No
*Type*: [SubjectAlternativeNames](aws-properties-appmesh-virtualnode-subjectalternativenames.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Trust`  <a name="cfn-appmesh-virtualnode-tlsvalidationcontext-trust"></a>
A reference to where to retrieve the trust chain when validating a peer’s Transport Layer Security (TLS) certificate.
*Required*: Yes
*Type*: [TlsValidationContextTrust](aws-properties-appmesh-virtualnode-tlsvalidationcontexttrust.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
