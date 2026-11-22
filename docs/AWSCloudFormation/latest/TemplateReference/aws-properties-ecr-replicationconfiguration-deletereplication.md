---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecr-replicationconfiguration-deletereplication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::ReplicationConfiguration DeleteReplication

The delete replication configuration for a replication rule. When delete replication is enabled, the service replicates image deletions and image tag removals in the source registry to the replication destinations.

## Syntax
<a name="aws-properties-ecr-replicationconfiguration-deletereplication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecr-replicationconfiguration-deletereplication-syntax.json"></a>

```json
{
  "[Enabled](#cfn-ecr-replicationconfiguration-deletereplication-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ecr-replicationconfiguration-deletereplication-syntax.yaml"></a>

```yaml
  [Enabled](#cfn-ecr-replicationconfiguration-deletereplication-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-ecr-replicationconfiguration-deletereplication-properties"></a>

`Enabled`  <a name="cfn-ecr-replicationconfiguration-deletereplication-enabled"></a>
Specifies whether delete replication is enabled. If set to `true`, the service replicates image deletions and image tag removals from the source registry to each replication destination. If set to `false`, the service does not replicate image deletions or image tag removals.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
