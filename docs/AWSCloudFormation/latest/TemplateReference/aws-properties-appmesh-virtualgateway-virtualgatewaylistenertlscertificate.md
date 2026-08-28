---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewayListenerTlsCertificate
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate"></a>

An object that represents a listener's Transport Layer Security (TLS) certificate.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-syntax.json"></a>

```
{
  "[ACM](#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-acm)" : {{VirtualGatewayListenerTlsAcmCertificate}},
  "[File](#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-file)" : {{VirtualGatewayListenerTlsFileCertificate}},
  "[SDS](#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-sds)" : {{VirtualGatewayListenerTlsSdsCertificate}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-syntax.yaml"></a>

```
  [ACM](#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-acm): {{
    VirtualGatewayListenerTlsAcmCertificate}}
  [File](#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-file): {{
    VirtualGatewayListenerTlsFileCertificate}}
  [SDS](#cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-sds): {{
    VirtualGatewayListenerTlsSdsCertificate}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-properties"></a>

`ACM`  <a name="cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-acm"></a>
A reference to an object that represents an AWS Certificate Manager certificate.
*Required*: No
*Type*: [VirtualGatewayListenerTlsAcmCertificate](aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsacmcertificate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`File`  <a name="cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-file"></a>
A reference to an object that represents a local file certificate.
*Required*: No
*Type*: [VirtualGatewayListenerTlsFileCertificate](aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SDS`  <a name="cfn-appmesh-virtualgateway-virtualgatewaylistenertlscertificate-sds"></a>
A reference to an object that represents a virtual gateway's listener's Secret Discovery Service certificate.
*Required*: No
*Type*: [VirtualGatewayListenerTlsSdsCertificate](aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
