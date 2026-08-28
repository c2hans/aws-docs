---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-route-tcproute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::Route TcpRoute
<a name="aws-properties-appmesh-route-tcproute"></a>

An object that represents a TCP route type.

## Syntax
<a name="aws-properties-appmesh-route-tcproute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-route-tcproute-syntax.json"></a>

```
{
  "[Action](#cfn-appmesh-route-tcproute-action)" : {{TcpRouteAction}},
  "[Match](#cfn-appmesh-route-tcproute-match)" : {{TcpRouteMatch}},
  "[Timeout](#cfn-appmesh-route-tcproute-timeout)" : {{TcpTimeout}}
}
```

### YAML
<a name="aws-properties-appmesh-route-tcproute-syntax.yaml"></a>

```
  [Action](#cfn-appmesh-route-tcproute-action): {{
    TcpRouteAction}}
  [Match](#cfn-appmesh-route-tcproute-match): {{
    TcpRouteMatch}}
  [Timeout](#cfn-appmesh-route-tcproute-timeout): {{
    TcpTimeout}}
```

## Properties
<a name="aws-properties-appmesh-route-tcproute-properties"></a>

`Action`  <a name="cfn-appmesh-route-tcproute-action"></a>
The action to take if a match is determined.
*Required*: Yes
*Type*: [TcpRouteAction](aws-properties-appmesh-route-tcprouteaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Match`  <a name="cfn-appmesh-route-tcproute-match"></a>
An object that represents the criteria for determining a request match.
*Required*: No
*Type*: [TcpRouteMatch](aws-properties-appmesh-route-tcproutematch.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timeout`  <a name="cfn-appmesh-route-tcproute-timeout"></a>
An object that represents types of timeouts.
*Required*: No
*Type*: [TcpTimeout](aws-properties-appmesh-route-tcptimeout.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
