---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-httpgatewayrouteheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute HttpGatewayRouteHeader
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouteheader"></a>

An object that represents the HTTP header in the gateway route.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouteheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouteheader-syntax.json"></a>

```
{
  "[Invert](#cfn-appmesh-gatewayroute-httpgatewayrouteheader-invert)" : {{Boolean}},
  "[Match](#cfn-appmesh-gatewayroute-httpgatewayrouteheader-match)" : {{HttpGatewayRouteHeaderMatch}},
  "[Name](#cfn-appmesh-gatewayroute-httpgatewayrouteheader-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouteheader-syntax.yaml"></a>

```
  [Invert](#cfn-appmesh-gatewayroute-httpgatewayrouteheader-invert): {{Boolean}}
  [Match](#cfn-appmesh-gatewayroute-httpgatewayrouteheader-match): {{
    HttpGatewayRouteHeaderMatch}}
  [Name](#cfn-appmesh-gatewayroute-httpgatewayrouteheader-name): {{String}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-httpgatewayrouteheader-properties"></a>

`Invert`  <a name="cfn-appmesh-gatewayroute-httpgatewayrouteheader-invert"></a>
Specify `True` to match anything except the match criteria. The default value is `False`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Match`  <a name="cfn-appmesh-gatewayroute-httpgatewayrouteheader-match"></a>
An object that represents the method and value to match with the header value sent in a request. Specify one match method.
*Required*: No
*Type*: [HttpGatewayRouteHeaderMatch](aws-properties-appmesh-gatewayroute-httpgatewayrouteheadermatch.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appmesh-gatewayroute-httpgatewayrouteheader-name"></a>
A name for the HTTP header in the gateway route that will be matched on.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
