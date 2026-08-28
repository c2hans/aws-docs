---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-gatewayroute-httpqueryparametermatch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::GatewayRoute HttpQueryParameterMatch
<a name="aws-properties-appmesh-gatewayroute-httpqueryparametermatch"></a>

An object representing the query parameter to match.

## Syntax
<a name="aws-properties-appmesh-gatewayroute-httpqueryparametermatch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-gatewayroute-httpqueryparametermatch-syntax.json"></a>

```
{
  "[Exact](#cfn-appmesh-gatewayroute-httpqueryparametermatch-exact)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-gatewayroute-httpqueryparametermatch-syntax.yaml"></a>

```
  [Exact](#cfn-appmesh-gatewayroute-httpqueryparametermatch-exact): {{String}}
```

## Properties
<a name="aws-properties-appmesh-gatewayroute-httpqueryparametermatch-properties"></a>

`Exact`  <a name="cfn-appmesh-gatewayroute-httpqueryparametermatch-exact"></a>
The exact query parameter to match on.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
