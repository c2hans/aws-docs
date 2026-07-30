---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode ListenerTlsValidationContextTrust
<a name="aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust"></a>

An object that represents a listener's Transport Layer Security (TLS) validation context trust.

## Syntax
<a name="aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust-syntax.json"></a>

```
{
  "[File](#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-file)" : {{TlsValidationContextFileTrust}},
  "[SDS](#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-sds)" : {{TlsValidationContextSdsTrust}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust-syntax.yaml"></a>

```
  [File](#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-file): {{
    TlsValidationContextFileTrust}}
  [SDS](#cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-sds): {{
    TlsValidationContextSdsTrust}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-listenertlsvalidationcontexttrust-properties"></a>

`File`  <a name="cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-file"></a>
An object that represents a Transport Layer Security (TLS) validation context trust for a local file.
*Required*: No
*Type*: [TlsValidationContextFileTrust](aws-properties-appmesh-virtualnode-tlsvalidationcontextfiletrust.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SDS`  <a name="cfn-appmesh-virtualnode-listenertlsvalidationcontexttrust-sds"></a>
A reference to an object that represents a listener's Transport Layer Security (TLS) Secret Discovery Service validation context trust.
*Required*: No
*Type*: [TlsValidationContextSdsTrust](aws-properties-appmesh-virtualnode-tlsvalidationcontextsdstrust.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
