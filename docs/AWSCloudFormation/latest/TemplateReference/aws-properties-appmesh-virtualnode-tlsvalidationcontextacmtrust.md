---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode TlsValidationContextAcmTrust
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust"></a>

An object that represents a Transport Layer Security (TLS) validation context trust for an AWS Certificate Manager certificate.

## Syntax
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust-syntax.json"></a>

```
{
  "[CertificateAuthorityArns](#cfn-appmesh-virtualnode-tlsvalidationcontextacmtrust-certificateauthorityarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust-syntax.yaml"></a>

```
  [CertificateAuthorityArns](#cfn-appmesh-virtualnode-tlsvalidationcontextacmtrust-certificateauthorityarns): {{
    - String}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextacmtrust-properties"></a>

`CertificateAuthorityArns`  <a name="cfn-appmesh-virtualnode-tlsvalidationcontextacmtrust-certificateauthorityarns"></a>
One or more ACM Amazon Resource Name (ARN)s.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
