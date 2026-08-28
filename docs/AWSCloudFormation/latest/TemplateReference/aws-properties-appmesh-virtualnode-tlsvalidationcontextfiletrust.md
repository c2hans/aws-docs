---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode TlsValidationContextFileTrust
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust"></a>

An object that represents a Transport Layer Security (TLS) validation context trust for a local file.

## Syntax
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust-syntax.json"></a>

```
{
  "[CertificateChain](#cfn-appmesh-virtualnode-tlsvalidationcontextfiletrust-certificatechain)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust-syntax.yaml"></a>

```
  [CertificateChain](#cfn-appmesh-virtualnode-tlsvalidationcontextfiletrust-certificatechain): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust-properties"></a>

`CertificateChain`  <a name="cfn-appmesh-virtualnode-tlsvalidationcontextfiletrust-certificatechain"></a>
The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
