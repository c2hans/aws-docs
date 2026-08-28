---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewayAccessLog
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog"></a>

The access log configuration for a virtual gateway.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog-syntax.json"></a>

```
{
  "[File](#cfn-appmesh-virtualgateway-virtualgatewayaccesslog-file)" : {{VirtualGatewayFileAccessLog}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog-syntax.yaml"></a>

```
  [File](#cfn-appmesh-virtualgateway-virtualgatewayaccesslog-file): {{
    VirtualGatewayFileAccessLog}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog-properties"></a>

`File`  <a name="cfn-appmesh-virtualgateway-virtualgatewayaccesslog-file"></a>
The file object to send virtual gateway access logs to.
*Required*: No
*Type*: [VirtualGatewayFileAccessLog](aws-properties-appmesh-virtualgateway-virtualgatewayfileaccesslog.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
