---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-listenertlsacmcertificate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode ListenerTlsAcmCertificate
<a name="aws-properties-appmesh-virtualnode-listenertlsacmcertificate"></a>

An object that represents an AWS Certificate Manager certificate.

## Syntax
<a name="aws-properties-appmesh-virtualnode-listenertlsacmcertificate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-listenertlsacmcertificate-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-appmesh-virtualnode-listenertlsacmcertificate-certificatearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-listenertlsacmcertificate-syntax.yaml"></a>

```
  [CertificateArn](#cfn-appmesh-virtualnode-listenertlsacmcertificate-certificatearn): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-listenertlsacmcertificate-properties"></a>

`CertificateArn`  <a name="cfn-appmesh-virtualnode-listenertlsacmcertificate-certificatearn"></a>
The Amazon Resource Name (ARN) for the certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see [Transport Layer Security (TLS)](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html#virtual-node-tls-prerequisites).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
