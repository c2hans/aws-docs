---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewayListenerTlsFileCertificate
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate"></a>

An object that represents a local file certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see [Transport Layer Security (TLS)](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html#virtual-node-tls-prerequisites).

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-syntax.json"></a>

```
{
  "[CertificateChain](#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-certificatechain)" : {{String}},
  "[PrivateKey](#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-privatekey)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-syntax.yaml"></a>

```
  [CertificateChain](#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-certificatechain): {{String}}
  [PrivateKey](#cfn-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-privatekey): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-properties"></a>

`CertificateChain`  <a name="cfn-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-certificatechain"></a>
The certificate chain for the certificate.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateKey`  <a name="cfn-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate-privatekey"></a>
The private key for a certificate stored on the file system of the mesh endpoint that the proxy is running on.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
