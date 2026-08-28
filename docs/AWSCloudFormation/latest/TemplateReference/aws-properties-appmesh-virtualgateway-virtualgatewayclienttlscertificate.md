---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewayClientTlsCertificate
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate"></a>

An object that represents the virtual gateway's client's Transport Layer Security (TLS) certificate.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate-syntax.json"></a>

```
{
  "[File](#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-file)" : {{VirtualGatewayListenerTlsFileCertificate}},
  "[SDS](#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-sds)" : {{VirtualGatewayListenerTlsSdsCertificate}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate-syntax.yaml"></a>

```
  [File](#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-file): {{
    VirtualGatewayListenerTlsFileCertificate}}
  [SDS](#cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-sds): {{
    VirtualGatewayListenerTlsSdsCertificate}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayclienttlscertificate-properties"></a>

`File`  <a name="cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-file"></a>
An object that represents a local file certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see [ Transport Layer Security (TLS) ](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html).
*Required*: No
*Type*: [VirtualGatewayListenerTlsFileCertificate](aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlsfilecertificate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SDS`  <a name="cfn-appmesh-virtualgateway-virtualgatewayclienttlscertificate-sds"></a>
A reference to an object that represents a virtual gateway's client's Secret Discovery Service certificate.
*Required*: No
*Type*: [VirtualGatewayListenerTlsSdsCertificate](aws-properties-appmesh-virtualgateway-virtualgatewaylistenertlssdscertificate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
