---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-replicationgroup-endpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::ReplicationGroup Endpoint
<a name="aws-properties-elasticache-replicationgroup-endpoint"></a>

Represents the information required for client programs to connect to a cache node. This value is read-only.

## Syntax
<a name="aws-properties-elasticache-replicationgroup-endpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-replicationgroup-endpoint-syntax.json"></a>

```
{
  "[Address](#cfn-elasticache-replicationgroup-endpoint-address)" : {{String}},
  "[Port](#cfn-elasticache-replicationgroup-endpoint-port)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticache-replicationgroup-endpoint-syntax.yaml"></a>

```
  [Address](#cfn-elasticache-replicationgroup-endpoint-address): {{String}}
  [Port](#cfn-elasticache-replicationgroup-endpoint-port): {{String}}
```

## Properties
<a name="aws-properties-elasticache-replicationgroup-endpoint-properties"></a>

`Address`  <a name="cfn-elasticache-replicationgroup-endpoint-address"></a>
The DNS hostname of the cache node.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-elasticache-replicationgroup-endpoint-port"></a>
The port number that the cache engine is listening on.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
