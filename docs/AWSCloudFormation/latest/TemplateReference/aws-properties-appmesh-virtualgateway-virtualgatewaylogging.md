---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewaylogging.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewayLogging
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylogging"></a>

An object that represents logging information.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylogging-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylogging-syntax.json"></a>

```
{
  "[AccessLog](#cfn-appmesh-virtualgateway-virtualgatewaylogging-accesslog)" : {{VirtualGatewayAccessLog}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylogging-syntax.yaml"></a>

```
  [AccessLog](#cfn-appmesh-virtualgateway-virtualgatewaylogging-accesslog): {{
    VirtualGatewayAccessLog}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylogging-properties"></a>

`AccessLog`  <a name="cfn-appmesh-virtualgateway-virtualgatewaylogging-accesslog"></a>
The access log configuration.
*Required*: No
*Type*: [VirtualGatewayAccessLog](aws-properties-appmesh-virtualgateway-virtualgatewayaccesslog.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
