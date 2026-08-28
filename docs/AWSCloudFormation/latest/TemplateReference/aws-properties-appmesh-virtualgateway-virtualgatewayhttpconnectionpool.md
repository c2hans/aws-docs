---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualGateway VirtualGatewayHttpConnectionPool
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool"></a>

An object that represents a type of connection pool.

## Syntax
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-syntax.json"></a>

```
{
  "[MaxConnections](#cfn-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-maxconnections)" : {{Integer}},
  "[MaxPendingRequests](#cfn-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-maxpendingrequests)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-syntax.yaml"></a>

```
  [MaxConnections](#cfn-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-maxconnections): {{Integer}}
  [MaxPendingRequests](#cfn-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-maxpendingrequests): {{Integer}}
```

## Properties
<a name="aws-properties-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-properties"></a>

`MaxConnections`  <a name="cfn-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-maxconnections"></a>
Maximum number of outbound TCP connections Envoy can establish concurrently with all hosts in upstream cluster.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxPendingRequests`  <a name="cfn-appmesh-virtualgateway-virtualgatewayhttpconnectionpool-maxpendingrequests"></a>
Number of overflowing requests after `max_connections` Envoy will queue to upstream cluster.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
