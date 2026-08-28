---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-gatewayroutetarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute GatewayRouteTarget
<a name="aws-properties-appmesh-gatewayroute-gatewayroutetarget"></a>

An object that represents a gateway route target.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-gatewayroutetarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-gatewayroutetarget-syntax.json"></a>

```
{
  "[Port](#cfn-appmesh-gatewayroute-gatewayroutetarget-port)" : {{Integer}},
  "[VirtualService](#cfn-appmesh-gatewayroute-gatewayroutetarget-virtualservice)" : {{GatewayRouteVirtualService}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-gatewayroutetarget-syntax.yaml"></a>

```
  [Port](#cfn-appmesh-gatewayroute-gatewayroutetarget-port): {{Integer}}
  [VirtualService](#cfn-appmesh-gatewayroute-gatewayroutetarget-virtualservice): {{
    GatewayRouteVirtualService}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-gatewayroutetarget-properties"></a>

`Port`  <a name="cfn-appmesh-gatewayroute-gatewayroutetarget-port"></a>
The port number of the gateway route target.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VirtualService`  <a name="cfn-appmesh-gatewayroute-gatewayroutetarget-virtualservice"></a>
An object that represents a virtual service gateway route target.
*Required*: Yes
*Type*: [GatewayRouteVirtualService](aws-properties-appmesh-gatewayroute-gatewayroutevirtualservice.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
