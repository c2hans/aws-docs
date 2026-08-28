---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute GatewayRouteVirtualService
<a name="aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice"></a>

An object that represents the virtual service that traffic is routed to.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice-syntax.json"></a>

```
{
  "[VirtualServiceName](#cfn-appmesh-gatewayroute-gatewayroutevirtualservice-virtualservicename)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice-syntax.yaml"></a>

```
  [VirtualServiceName](#cfn-appmesh-gatewayroute-gatewayroutevirtualservice-virtualservicename): {{String}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice-properties"></a>

`VirtualServiceName`  <a name="cfn-appmesh-gatewayroute-gatewayroutevirtualservice-virtualservicename"></a>
The name of the virtual service that traffic is routed to.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
