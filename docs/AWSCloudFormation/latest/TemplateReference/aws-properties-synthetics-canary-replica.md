---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-synthetics-canary-replica.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Synthetics::Canary Replica
<a name="aws-properties-synthetics-canary-replica"></a>

A structure that contains information about a canary replica in a specific location.

## Syntax
<a name="aws-properties-synthetics-canary-replica-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-synthetics-canary-replica-syntax.json"></a>

```
{
  "[CanaryState](#cfn-synthetics-canary-replica-canarystate)" : {{String}},
  "[KmsKeyArn](#cfn-synthetics-canary-replica-kmskeyarn)" : {{String}},
  "[LastModified](#cfn-synthetics-canary-replica-lastmodified)" : {{Number}},
  "[Location](#cfn-synthetics-canary-replica-location)" : {{String}},
  "[ReplicationStatus](#cfn-synthetics-canary-replica-replicationstatus)" : {{ReplicaReplicationStatus}},
  "[ResourcesToReplicateTags](#cfn-synthetics-canary-replica-resourcestoreplicatetags)" : {{[ String, ... ]}},
  "[Tags](#cfn-synthetics-canary-replica-tags)" : {{[ Tag, ... ]}},
  "[VpcConfig](#cfn-synthetics-canary-replica-vpcconfig)" : {{VPCConfig}}
}
```

### YAML
<a name="aws-properties-synthetics-canary-replica-syntax.yaml"></a>

```
  [CanaryState](#cfn-synthetics-canary-replica-canarystate): {{String}}
  [KmsKeyArn](#cfn-synthetics-canary-replica-kmskeyarn): {{String}}
  [LastModified](#cfn-synthetics-canary-replica-lastmodified): {{Number}}
  [Location](#cfn-synthetics-canary-replica-location): {{String}}
  [ReplicationStatus](#cfn-synthetics-canary-replica-replicationstatus): {{
    ReplicaReplicationStatus}}
  [ResourcesToReplicateTags](#cfn-synthetics-canary-replica-resourcestoreplicatetags): {{
    - String}}
  [Tags](#cfn-synthetics-canary-replica-tags): {{
    - Tag}}
  [VpcConfig](#cfn-synthetics-canary-replica-vpcconfig): {{
    VPCConfig}}
```

## Properties
<a name="aws-properties-synthetics-canary-replica-properties"></a>

`CanaryState`  <a name="cfn-synthetics-canary-replica-canarystate"></a>
The current state of the canary in this replica location.
*Required*: No
*Type*: String
*Allowed values*: `CREATING | READY | STARTING | RUNNING | UPDATING | STOPPING | STOPPED | ERROR | DELETING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-synthetics-canary-replica-kmskeyarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z0-9-]+:kms:[a-z0-9-]+:[0-9]{12}:(key/([a-f0-9-]{36}|mrk-[a-f0-9]{32})|alias/[a-zA-Z0-9:/_.-]+)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastModified`  <a name="cfn-synthetics-canary-replica-lastmodified"></a>
The date and time that the replica was last modified.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Location`  <a name="cfn-synthetics-canary-replica-location"></a>
The Amazon Web Services Region where this replica is located.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-{0,1}[0-9]{0,1}$`
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicationStatus`  <a name="cfn-synthetics-canary-replica-replicationstatus"></a>
A structure that contains information about the replication status of this replica.
*Required*: No
*Type*: [ReplicaReplicationStatus](aws-properties-synthetics-canary-replicareplicationstatus.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourcesToReplicateTags`  <a name="cfn-synthetics-canary-replica-resourcestoreplicatetags"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-synthetics-canary-replica-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-synthetics-canary-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcConfig`  <a name="cfn-synthetics-canary-replica-vpcconfig"></a>
The VPC configuration for the canary replica in this location.
*Required*: No
*Type*: [VPCConfig](aws-properties-synthetics-canary-vpcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
