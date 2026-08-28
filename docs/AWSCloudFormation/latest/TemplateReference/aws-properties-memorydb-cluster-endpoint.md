---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-memorydb-cluster-endpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MemoryDB::Cluster Endpoint
<a name="aws-properties-memorydb-cluster-endpoint"></a>

Represents the information required for client programs to connect to the cluster and its nodes.

## Syntax
<a name="aws-properties-memorydb-cluster-endpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-memorydb-cluster-endpoint-syntax.json"></a>

```
{
  "[Address](#cfn-memorydb-cluster-endpoint-address)" : {{String}},
  "[Port](#cfn-memorydb-cluster-endpoint-port)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-memorydb-cluster-endpoint-syntax.yaml"></a>

```
  [Address](#cfn-memorydb-cluster-endpoint-address): {{String}}
  [Port](#cfn-memorydb-cluster-endpoint-port): {{Integer}}
```

## Properties
<a name="aws-properties-memorydb-cluster-endpoint-properties"></a>

`Address`  <a name="cfn-memorydb-cluster-endpoint-address"></a>
The DNS hostname of the node.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-memorydb-cluster-endpoint-port"></a>
The port number that the engine is listening on.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
