---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-route-tcptimeout.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::Route TcpTimeout
<a name="aws-properties-appmesh-route-tcptimeout"></a>

An object that represents types of timeouts.

## Syntax
<a name="aws-properties-appmesh-route-tcptimeout-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-route-tcptimeout-syntax.json"></a>

```
{
  "[Idle](#cfn-appmesh-route-tcptimeout-idle)" : {{Duration}}
}
```

### YAML
<a name="aws-properties-appmesh-route-tcptimeout-syntax.yaml"></a>

```
  [Idle](#cfn-appmesh-route-tcptimeout-idle): {{
    Duration}}
```

## Properties
<a name="aws-properties-appmesh-route-tcptimeout-properties"></a>

`Idle`  <a name="cfn-appmesh-route-tcptimeout-idle"></a>
An object that represents an idle timeout. An idle timeout bounds the amount of time that a connection may be idle. The default value is none.
*Required*: No
*Type*: [Duration](aws-properties-appmesh-route-duration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
