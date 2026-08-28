---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute HttpGatewayRouteRewrite
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite"></a>

An object representing the gateway route to rewrite.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite-syntax.json"></a>

```
{
  "[Hostname](#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-hostname)" : {{GatewayRouteHostnameRewrite}},
  "[Path](#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-path)" : {{HttpGatewayRoutePathRewrite}},
  "[Prefix](#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-prefix)" : {{HttpGatewayRoutePrefixRewrite}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite-syntax.yaml"></a>

```
  [Hostname](#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-hostname): {{
    GatewayRouteHostnameRewrite}}
  [Path](#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-path): {{
    HttpGatewayRoutePathRewrite}}
  [Prefix](#cfn-appmesh-gatewayroute-httpgatewayrouterewrite-prefix): {{
    HttpGatewayRoutePrefixRewrite}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouterewrite-properties"></a>

`Hostname`  <a name="cfn-appmesh-gatewayroute-httpgatewayrouterewrite-hostname"></a>
The host name to rewrite.
*Required*: No
*Type*: [GatewayRouteHostnameRewrite](aws-properties-appmesh-gatewayroute-gatewayroutehostnamerewrite.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-appmesh-gatewayroute-httpgatewayrouterewrite-path"></a>
The path to rewrite.
*Required*: No
*Type*: [HttpGatewayRoutePathRewrite](aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-appmesh-gatewayroute-httpgatewayrouterewrite-prefix"></a>
The specified beginning characters to rewrite.
*Required*: No
*Type*: [HttpGatewayRoutePrefixRewrite](aws-properties-appmesh-gatewayroute-httpgatewayrouteprefixrewrite.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
