---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewaylistener.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewayListener
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistener"></a>

An object that represents a listener for a virtual gateway.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistener-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistener-syntax.json"></a>

```
{
  "[ConnectionPool](#cfn-appmesh-virtualgateway-virtualgatewaylistener-connectionpool)" : {{VirtualGatewayConnectionPool}},
  "[HealthCheck](#cfn-appmesh-virtualgateway-virtualgatewaylistener-healthcheck)" : {{VirtualGatewayHealthCheckPolicy}},
  "[PortMapping](#cfn-appmesh-virtualgateway-virtualgatewaylistener-portmapping)" : {{VirtualGatewayPortMapping}},
  "[TLS](#cfn-appmesh-virtualgateway-virtualgatewaylistener-tls)" : {{VirtualGatewayListenerTls}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistener-syntax.yaml"></a>

```
  [ConnectionPool](#cfn-appmesh-virtualgateway-virtualgatewaylistener-connectionpool): {{
    VirtualGatewayConnectionPool}}
  [HealthCheck](#cfn-appmesh-virtualgateway-virtualgatewaylistener-healthcheck): {{
    VirtualGatewayHealthCheckPolicy}}
  [PortMapping](#cfn-appmesh-virtualgateway-virtualgatewaylistener-portmapping): {{
    VirtualGatewayPortMapping}}
  [TLS](#cfn-appmesh-virtualgateway-virtualgatewaylistener-tls): {{
    VirtualGatewayListenerTls}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewaylistener-properties"></a>

`ConnectionPool`  <a name="cfn-appmesh-virtualgateway-virtualgatewaylistener-connectionpool"></a>
The connection pool information for the listener.
*Required*: No
*Type*: [VirtualGatewayConnectionPool](aws-properties-appmesh-virtualgateway-virtualgatewayconnectionpool.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheck`  <a name="cfn-appmesh-virtualgateway-virtualgatewaylistener-healthcheck"></a>
The health check information for the listener.
*Required*: No
*Type*: [VirtualGatewayHealthCheckPolicy](aws-properties-appmesh-virtualgateway-virtualgatewayhealthcheckpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortMapping`  <a name="cfn-appmesh-virtualgateway-virtualgatewaylistener-portmapping"></a>
The port mapping information for the listener.
*Required*: Yes
*Type*: [VirtualGatewayPortMapping](aws-properties-appmesh-virtualgateway-virtualgatewayportmapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TLS`  <a name="cfn-appmesh-virtualgateway-virtualgatewaylistener-tls"></a>
A reference to an object that represents the Transport Layer Security (TLS) properties for the listener.
*Required*: No
*Type*: [VirtualGatewayListenerTls](aws-properties-appmesh-virtualgateway-virtualgatewaylistenertls.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
