---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-gatewayroutespec.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute GatewayRouteSpec
<a name="aws-properties-appmesh-gatewayroute-gatewayroutespec"></a>

An object that represents a gateway route specification. Specify one gateway route type.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-gatewayroutespec-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-gatewayroutespec-syntax.json"></a>

```
{
  "[GrpcRoute](#cfn-appmesh-gatewayroute-gatewayroutespec-grpcroute)" : {{GrpcGatewayRoute}},
  "[Http2Route](#cfn-appmesh-gatewayroute-gatewayroutespec-http2route)" : {{HttpGatewayRoute}},
  "[HttpRoute](#cfn-appmesh-gatewayroute-gatewayroutespec-httproute)" : {{HttpGatewayRoute}},
  "[Priority](#cfn-appmesh-gatewayroute-gatewayroutespec-priority)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-gatewayroutespec-syntax.yaml"></a>

```
  [GrpcRoute](#cfn-appmesh-gatewayroute-gatewayroutespec-grpcroute): {{
    GrpcGatewayRoute}}
  [Http2Route](#cfn-appmesh-gatewayroute-gatewayroutespec-http2route): {{
    HttpGatewayRoute}}
  [HttpRoute](#cfn-appmesh-gatewayroute-gatewayroutespec-httproute): {{
    HttpGatewayRoute}}
  [Priority](#cfn-appmesh-gatewayroute-gatewayroutespec-priority): {{Integer}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-gatewayroutespec-properties"></a>

`GrpcRoute`  <a name="cfn-appmesh-gatewayroute-gatewayroutespec-grpcroute"></a>
An object that represents the specification of a gRPC gateway route.
*Required*: No
*Type*: [GrpcGatewayRoute](aws-properties-appmesh-gatewayroute-grpcgatewayroute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Http2Route`  <a name="cfn-appmesh-gatewayroute-gatewayroutespec-http2route"></a>
An object that represents the specification of an HTTP/2 gateway route.
*Required*: No
*Type*: [HttpGatewayRoute](aws-properties-appmesh-gatewayroute-httpgatewayroute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpRoute`  <a name="cfn-appmesh-gatewayroute-gatewayroutespec-httproute"></a>
An object that represents the specification of an HTTP gateway route.
*Required*: No
*Type*: [HttpGatewayRoute](aws-properties-appmesh-gatewayroute-httpgatewayroute.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Priority`  <a name="cfn-appmesh-gatewayroute-gatewayroutespec-priority"></a>
The ordering of the gateway routes spec.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
