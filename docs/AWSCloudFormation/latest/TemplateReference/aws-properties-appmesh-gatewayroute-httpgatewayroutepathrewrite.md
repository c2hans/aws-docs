---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute HttpGatewayRoutePathRewrite
<a name="aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite"></a>

An object that represents the path to rewrite.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite-syntax.json"></a>

```
{
  "[Exact](#cfn-appmesh-gatewayroute-httpgatewayroutepathrewrite-exact)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite-syntax.yaml"></a>

```
  [Exact](#cfn-appmesh-gatewayroute-httpgatewayroutepathrewrite-exact): {{String}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-httpgatewayroutepathrewrite-properties"></a>

`Exact`  <a name="cfn-appmesh-gatewayroute-httpgatewayroutepathrewrite-exact"></a>
The exact path to rewrite.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
