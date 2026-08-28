---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-route-tcproutematch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::Route TcpRouteMatch
<a name="aws-properties-appmesh-route-tcproutematch"></a>

An object representing the TCP route to match.

## Syntax
<a name="aws-properties-appmesh-route-tcproutematch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-route-tcproutematch-syntax.json"></a>

```
{
  "[Port](#cfn-appmesh-route-tcproutematch-port)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-appmesh-route-tcproutematch-syntax.yaml"></a>

```
  [Port](#cfn-appmesh-route-tcproutematch-port): {{Integer}}
```

## Properties
<a name="aws-properties-appmesh-route-tcproutematch-properties"></a>

`Port`  <a name="cfn-appmesh-route-tcproutematch-port"></a>
The port number to match on.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
