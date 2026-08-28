---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewayPortMapping
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayportmapping"></a>

An object that represents a port mapping.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayportmapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayportmapping-syntax.json"></a>

```
{
  "[Port](#cfn-appmesh-virtualgateway-virtualgatewayportmapping-port)" : {{Integer}},
  "[Protocol](#cfn-appmesh-virtualgateway-virtualgatewayportmapping-protocol)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayportmapping-syntax.yaml"></a>

```
  [Port](#cfn-appmesh-virtualgateway-virtualgatewayportmapping-port): {{Integer}}
  [Protocol](#cfn-appmesh-virtualgateway-virtualgatewayportmapping-protocol): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayportmapping-properties"></a>

`Port`  <a name="cfn-appmesh-virtualgateway-virtualgatewayportmapping-port"></a>
The port used for the port mapping. Specify one protocol.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-appmesh-virtualgateway-virtualgatewayportmapping-protocol"></a>
The protocol used for the port mapping.
*Required*: Yes
*Type*: String
*Allowed values*: `http | http2 | grpc`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
