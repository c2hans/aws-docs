---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-clienttlscertificate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode ClientTlsCertificate
<a name="aws-properties-appmesh-virtualnode-clienttlscertificate"></a>

An object that represents the client's certificate.

## Syntax
<a name="aws-properties-appmesh-virtualnode-clienttlscertificate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-clienttlscertificate-syntax.json"></a>

```
{
  "[File](#cfn-appmesh-virtualnode-clienttlscertificate-file)" : {{ListenerTlsFileCertificate}},
  "[SDS](#cfn-appmesh-virtualnode-clienttlscertificate-sds)" : {{ListenerTlsSdsCertificate}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-clienttlscertificate-syntax.yaml"></a>

```
  [File](#cfn-appmesh-virtualnode-clienttlscertificate-file): {{
    ListenerTlsFileCertificate}}
  [SDS](#cfn-appmesh-virtualnode-clienttlscertificate-sds): {{
    ListenerTlsSdsCertificate}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-clienttlscertificate-properties"></a>

`File`  <a name="cfn-appmesh-virtualnode-clienttlscertificate-file"></a>
An object that represents a local file certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see [Transport Layer Security (TLS)](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html).
*Required*: No
*Type*: [ListenerTlsFileCertificate](aws-properties-appmesh-virtualnode-listenertlsfilecertificate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SDS`  <a name="cfn-appmesh-virtualnode-clienttlscertificate-sds"></a>
A reference to an object that represents a client's TLS Secret Discovery Service certificate.
*Required*: No
*Type*: [ListenerTlsSdsCertificate](aws-properties-appmesh-virtualnode-listenertlssdscertificate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
