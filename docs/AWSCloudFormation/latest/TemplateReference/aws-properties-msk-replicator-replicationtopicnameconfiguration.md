---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-replicationtopicnameconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator ReplicationTopicNameConfiguration
<a name="aws-properties-msk-replicator-replicationtopicnameconfiguration"></a>

Configuration for specifying replicated topic names will be the same as their corresponding upstream topics or prefixed with source cluster alias.

## Syntax
<a name="aws-properties-msk-replicator-replicationtopicnameconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-replicationtopicnameconfiguration-syntax.json"></a>

```
{
  "[Type](#cfn-msk-replicator-replicationtopicnameconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-replicator-replicationtopicnameconfiguration-syntax.yaml"></a>

```
  [Type](#cfn-msk-replicator-replicationtopicnameconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-msk-replicator-replicationtopicnameconfiguration-properties"></a>

`Type`  <a name="cfn-msk-replicator-replicationtopicnameconfiguration-type"></a>
The type of replication topic name configuration, identical to upstream topic name or prefixed with source cluster alias.
*Required*: No
*Type*: String
*Allowed values*: `PREFIXED_WITH_SOURCE_CLUSTER_ALIAS | IDENTICAL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
