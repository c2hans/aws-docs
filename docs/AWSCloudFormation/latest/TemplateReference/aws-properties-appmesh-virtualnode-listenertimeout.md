---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-listenertimeout.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode ListenerTimeout
<a name="aws-properties-appmesh-virtualnode-listenertimeout"></a>

An object that represents timeouts for different protocols.

## Syntax
<a name="aws-properties-appmesh-virtualnode-listenertimeout-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-listenertimeout-syntax.json"></a>

```
{
  "[GRPC](#cfn-appmesh-virtualnode-listenertimeout-grpc)" : {{GrpcTimeout}},
  "[HTTP](#cfn-appmesh-virtualnode-listenertimeout-http)" : {{HttpTimeout}},
  "[HTTP2](#cfn-appmesh-virtualnode-listenertimeout-http2)" : {{HttpTimeout}},
  "[TCP](#cfn-appmesh-virtualnode-listenertimeout-tcp)" : {{TcpTimeout}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-listenertimeout-syntax.yaml"></a>

```
  [GRPC](#cfn-appmesh-virtualnode-listenertimeout-grpc): {{
    GrpcTimeout}}
  [HTTP](#cfn-appmesh-virtualnode-listenertimeout-http): {{
    HttpTimeout}}
  [HTTP2](#cfn-appmesh-virtualnode-listenertimeout-http2): {{
    HttpTimeout}}
  [TCP](#cfn-appmesh-virtualnode-listenertimeout-tcp): {{
    TcpTimeout}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-listenertimeout-properties"></a>

`GRPC`  <a name="cfn-appmesh-virtualnode-listenertimeout-grpc"></a>
An object that represents types of timeouts.
*Required*: No
*Type*: [GrpcTimeout](aws-properties-appmesh-virtualnode-grpctimeout.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HTTP`  <a name="cfn-appmesh-virtualnode-listenertimeout-http"></a>
An object that represents types of timeouts.
*Required*: No
*Type*: [HttpTimeout](aws-properties-appmesh-virtualnode-httptimeout.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HTTP2`  <a name="cfn-appmesh-virtualnode-listenertimeout-http2"></a>
An object that represents types of timeouts.
*Required*: No
*Type*: [HttpTimeout](aws-properties-appmesh-virtualnode-httptimeout.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TCP`  <a name="cfn-appmesh-virtualnode-listenertimeout-tcp"></a>
An object that represents types of timeouts.
*Required*: No
*Type*: [TcpTimeout](aws-properties-appmesh-virtualnode-tcptimeout.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
