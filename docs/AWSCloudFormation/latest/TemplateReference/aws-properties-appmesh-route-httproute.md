---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-route-httproute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::Route HttpRoute
<a name="aws-properties-appmesh-route-httproute"></a>

An object that represents an HTTP or HTTP/2 route type.

## Syntax
<a name="aws-properties-appmesh-route-httproute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-route-httproute-syntax.json"></a>

```
{
  "[Action](#cfn-appmesh-route-httproute-action)" : {{HttpRouteAction}},
  "[Match](#cfn-appmesh-route-httproute-match)" : {{HttpRouteMatch}},
  "[RetryPolicy](#cfn-appmesh-route-httproute-retrypolicy)" : {{HttpRetryPolicy}},
  "[Timeout](#cfn-appmesh-route-httproute-timeout)" : {{HttpTimeout}}
}
```

### YAML
<a name="aws-properties-appmesh-route-httproute-syntax.yaml"></a>

```
  [Action](#cfn-appmesh-route-httproute-action): {{
    HttpRouteAction}}
  [Match](#cfn-appmesh-route-httproute-match): {{
    HttpRouteMatch}}
  [RetryPolicy](#cfn-appmesh-route-httproute-retrypolicy): {{
    HttpRetryPolicy}}
  [Timeout](#cfn-appmesh-route-httproute-timeout): {{
    HttpTimeout}}
```

## Properties
<a name="aws-properties-appmesh-route-httproute-properties"></a>

`Action`  <a name="cfn-appmesh-route-httproute-action"></a>
An object that represents the action to take if a match is determined.
*Required*: Yes
*Type*: [HttpRouteAction](aws-properties-appmesh-route-httprouteaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Match`  <a name="cfn-appmesh-route-httproute-match"></a>
An object that represents the criteria for determining a request match.
*Required*: Yes
*Type*: [HttpRouteMatch](aws-properties-appmesh-route-httproutematch.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetryPolicy`  <a name="cfn-appmesh-route-httproute-retrypolicy"></a>
An object that represents a retry policy.
*Required*: No
*Type*: [HttpRetryPolicy](aws-properties-appmesh-route-httpretrypolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timeout`  <a name="cfn-appmesh-route-httproute-timeout"></a>
An object that represents types of timeouts.
*Required*: No
*Type*: [HttpTimeout](aws-properties-appmesh-route-httptimeout.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
