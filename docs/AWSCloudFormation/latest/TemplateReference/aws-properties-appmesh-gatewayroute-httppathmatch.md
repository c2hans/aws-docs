---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-httppathmatch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute HttpPathMatch
<a name="aws-properties-appmesh-gatewayroute-httppathmatch"></a>

An object representing the path to match in the request.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-httppathmatch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-httppathmatch-syntax.json"></a>

```
{
  "[Exact](#cfn-appmesh-gatewayroute-httppathmatch-exact)" : {{String}},
  "[Regex](#cfn-appmesh-gatewayroute-httppathmatch-regex)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-httppathmatch-syntax.yaml"></a>

```
  [Exact](#cfn-appmesh-gatewayroute-httppathmatch-exact): {{String}}
  [Regex](#cfn-appmesh-gatewayroute-httppathmatch-regex): {{String}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-httppathmatch-properties"></a>

`Exact`  <a name="cfn-appmesh-gatewayroute-httppathmatch-exact"></a>
The exact path to match on.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Regex`  <a name="cfn-appmesh-gatewayroute-httppathmatch-regex"></a>
The regex used to match the path.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
