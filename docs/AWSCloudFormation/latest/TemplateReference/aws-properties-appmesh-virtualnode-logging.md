---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-logging.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode Logging
<a name="aws-properties-appmesh-virtualnode-logging"></a>

An object that represents the logging information for a virtual node.

## Syntax
<a name="aws-properties-appmesh-virtualnode-logging-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-logging-syntax.json"></a>

```
{
  "[AccessLog](#cfn-appmesh-virtualnode-logging-accesslog)" : {{AccessLog}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-logging-syntax.yaml"></a>

```
  [AccessLog](#cfn-appmesh-virtualnode-logging-accesslog): {{
    AccessLog}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-logging-properties"></a>

`AccessLog`  <a name="cfn-appmesh-virtualnode-logging-accesslog"></a>
The access log configuration for a virtual node.
*Required*: No
*Type*: [AccessLog](aws-properties-appmesh-virtualnode-accesslog.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
