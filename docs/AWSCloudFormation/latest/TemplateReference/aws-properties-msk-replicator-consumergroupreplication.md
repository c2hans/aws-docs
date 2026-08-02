---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-consumergroupreplication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator ConsumerGroupReplication
<a name="aws-properties-msk-replicator-consumergroupreplication"></a>

Details about consumer group replication.

## Syntax
<a name="aws-properties-msk-replicator-consumergroupreplication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-consumergroupreplication-syntax.json"></a>

```
{
  "[ConsumerGroupOffsetSyncMode](#cfn-msk-replicator-consumergroupreplication-consumergroupoffsetsyncmode)" : {{String}},
  "[ConsumerGroupsToExclude](#cfn-msk-replicator-consumergroupreplication-consumergroupstoexclude)" : {{[ String, ... ]}},
  "[ConsumerGroupsToReplicate](#cfn-msk-replicator-consumergroupreplication-consumergroupstoreplicate)" : {{[ String, ... ]}},
  "[DetectAndCopyNewConsumerGroups](#cfn-msk-replicator-consumergroupreplication-detectandcopynewconsumergroups)" : {{Boolean}},
  "[SynchroniseConsumerGroupOffsets](#cfn-msk-replicator-consumergroupreplication-synchroniseconsumergroupoffsets)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-msk-replicator-consumergroupreplication-syntax.yaml"></a>

```
  [ConsumerGroupOffsetSyncMode](#cfn-msk-replicator-consumergroupreplication-consumergroupoffsetsyncmode): {{String}}
  [ConsumerGroupsToExclude](#cfn-msk-replicator-consumergroupreplication-consumergroupstoexclude): {{
    - String}}
  [ConsumerGroupsToReplicate](#cfn-msk-replicator-consumergroupreplication-consumergroupstoreplicate): {{
    - String}}
  [DetectAndCopyNewConsumerGroups](#cfn-msk-replicator-consumergroupreplication-detectandcopynewconsumergroups): {{Boolean}}
  [SynchroniseConsumerGroupOffsets](#cfn-msk-replicator-consumergroupreplication-synchroniseconsumergroupoffsets): {{Boolean}}
```

## Properties
<a name="aws-properties-msk-replicator-consumergroupreplication-properties"></a>

`ConsumerGroupOffsetSyncMode`  <a name="cfn-msk-replicator-consumergroupreplication-consumergroupoffsetsyncmode"></a>
The consumer group offset synchronization mode. With LEGACY, offsets are synchronized when producers write to the source cluster. With ENHANCED, consumer offsets are synchronized regardless of producer location. ENHANCED requires a corresponding replicator that replicates data from the target cluster to the source cluster.
*Required*: No
*Type*: String
*Allowed values*: `LEGACY | ENHANCED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConsumerGroupsToExclude`  <a name="cfn-msk-replicator-consumergroupreplication-consumergroupstoexclude"></a>
List of regular expression patterns indicating the consumer groups that should not be replicated.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `256 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConsumerGroupsToReplicate`  <a name="cfn-msk-replicator-consumergroupreplication-consumergroupstoreplicate"></a>
List of regular expression patterns indicating the consumer groups to copy.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `256 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DetectAndCopyNewConsumerGroups`  <a name="cfn-msk-replicator-consumergroupreplication-detectandcopynewconsumergroups"></a>
Enables synchronization of consumer groups to target cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SynchroniseConsumerGroupOffsets`  <a name="cfn-msk-replicator-consumergroupreplication-synchroniseconsumergroupoffsets"></a>
Enables synchronization of consumer group offsets to target cluster. The translated offsets will be written to topic \_\_consumer\_offsets.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
