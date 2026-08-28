---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::GlobalReplicationGroup ReshardingConfiguration
<a name="aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration"></a>

A list of `PreferredAvailabilityZones` objects that specifies the configuration of a node group in the resharded cluster.

## Syntax
<a name="aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration-syntax.json"></a>

```
{
  "[NodeGroupId](#cfn-elasticache-globalreplicationgroup-reshardingconfiguration-nodegroupid)" : {{String}},
  "[PreferredAvailabilityZones](#cfn-elasticache-globalreplicationgroup-reshardingconfiguration-preferredavailabilityzones)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration-syntax.yaml"></a>

```
  [NodeGroupId](#cfn-elasticache-globalreplicationgroup-reshardingconfiguration-nodegroupid): {{String}}
  [PreferredAvailabilityZones](#cfn-elasticache-globalreplicationgroup-reshardingconfiguration-preferredavailabilityzones): {{
    - String}}
```

## Properties
<a name="aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration-properties"></a>

`NodeGroupId`  <a name="cfn-elasticache-globalreplicationgroup-reshardingconfiguration-nodegroupid"></a>
Either the ElastiCache supplied 4-digit id or a user supplied id for the node group these configuration values apply to.
*Required*: No
*Type*: String
*Pattern*: `\d+`
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreferredAvailabilityZones`  <a name="cfn-elasticache-globalreplicationgroup-reshardingconfiguration-preferredavailabilityzones"></a>
A list of preferred availability zones for the nodes in this cluster.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
