---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode TlsValidationContextSdsTrust
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust"></a>

An object that represents a Transport Layer Security (TLS) Secret Discovery Service validation context trust. The proxy must be configured with a local SDS provider via a Unix Domain Socket. See App Mesh [TLS documentation](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html) for more info.

## Syntax
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust-syntax.json"></a>

```
{
  "[SecretName](#cfn-appmesh-virtualnode-tlsvalidationcontextsdstrust-secretname)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust-syntax.yaml"></a>

```
  [SecretName](#cfn-appmesh-virtualnode-tlsvalidationcontextsdstrust-secretname): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust-properties"></a>

`SecretName`  <a name="cfn-appmesh-virtualnode-tlsvalidationcontextsdstrust-secretname"></a>
A reference to an object that represents the name of the secret for a Transport Layer Security (TLS) Secret Discovery Service validation context trust.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
