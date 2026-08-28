---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute GatewayRouteHostnameMatch
<a name="aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch"></a>

An object representing the gateway route host name to match.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch-syntax.json"></a>

```
{
  "[Exact](#cfn-appmesh-gatewayroute-gatewayroutehostnamematch-exact)" : {{String}},
  "[Suffix](#cfn-appmesh-gatewayroute-gatewayroutehostnamematch-suffix)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch-syntax.yaml"></a>

```
  [Exact](#cfn-appmesh-gatewayroute-gatewayroutehostnamematch-exact): {{String}}
  [Suffix](#cfn-appmesh-gatewayroute-gatewayroutehostnamematch-suffix): {{String}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-gatewayroutehostnamematch-properties"></a>

`Exact`  <a name="cfn-appmesh-gatewayroute-gatewayroutehostnamematch-exact"></a>
The exact host name to match on.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `253`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Suffix`  <a name="cfn-appmesh-gatewayroute-gatewayroutehostnamematch-suffix"></a>
The specified ending characters of the host name to match on.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `253`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
