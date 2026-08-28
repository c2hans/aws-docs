---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-httpgatewayroute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute HttpGatewayRoute
<a name="aws-properties-appmesh-gatewayroute-httpgatewayroute"></a>

An object that represents an HTTP gateway route.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-httpgatewayroute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-httpgatewayroute-syntax.json"></a>

```
{
  "[Action](#cfn-appmesh-gatewayroute-httpgatewayroute-action)" : {{HttpGatewayRouteAction}},
  "[Match](#cfn-appmesh-gatewayroute-httpgatewayroute-match)" : {{HttpGatewayRouteMatch}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-httpgatewayroute-syntax.yaml"></a>

```
  [Action](#cfn-appmesh-gatewayroute-httpgatewayroute-action): {{
    HttpGatewayRouteAction}}
  [Match](#cfn-appmesh-gatewayroute-httpgatewayroute-match): {{
    HttpGatewayRouteMatch}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-httpgatewayroute-properties"></a>

`Action`  <a name="cfn-appmesh-gatewayroute-httpgatewayroute-action"></a>
An object that represents the action to take if a match is determined.
*Required*: Yes
*Type*: [HttpGatewayRouteAction](aws-properties-appmesh-gatewayroute-httpgatewayrouteaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Match`  <a name="cfn-appmesh-gatewayroute-httpgatewayroute-match"></a>
An object that represents the criteria for determining a request match.
*Required*: Yes
*Type*: [HttpGatewayRouteMatch](aws-properties-appmesh-gatewayroute-httpgatewayroutematch.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
