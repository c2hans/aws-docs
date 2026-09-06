---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-replicationstartingposition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator ReplicationStartingPosition
<a name="aws-properties-msk-replicator-replicationstartingposition"></a>

Specifies the position in the topics to start replicating from.

## Syntax
<a name="aws-properties-msk-replicator-replicationstartingposition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-replicationstartingposition-syntax.json"></a>

```
{
  "[Type](#cfn-msk-replicator-replicationstartingposition-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-replicator-replicationstartingposition-syntax.yaml"></a>

```
  [Type](#cfn-msk-replicator-replicationstartingposition-type): {{String}}
```

## Properties
<a name="aws-properties-msk-replicator-replicationstartingposition-properties"></a>

`Type`  <a name="cfn-msk-replicator-replicationstartingposition-type"></a>
The type of replication starting position.
*Required*: No
*Type*: String
*Allowed values*: `LATEST | EARLIEST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
