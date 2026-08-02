---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-topicreplication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator TopicReplication
<a name="aws-properties-msk-replicator-topicreplication"></a>

Details about topic replication.

## Syntax
<a name="aws-properties-msk-replicator-topicreplication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-topicreplication-syntax.json"></a>

```
{
  "[CopyAccessControlListsForTopics](#cfn-msk-replicator-topicreplication-copyaccesscontrollistsfortopics)" : {{Boolean}},
  "[CopyTopicConfigurations](#cfn-msk-replicator-topicreplication-copytopicconfigurations)" : {{Boolean}},
  "[DetectAndCopyNewTopics](#cfn-msk-replicator-topicreplication-detectandcopynewtopics)" : {{Boolean}},
  "[StartingPosition](#cfn-msk-replicator-topicreplication-startingposition)" : {{ReplicationStartingPosition}},
  "[TopicNameConfiguration](#cfn-msk-replicator-topicreplication-topicnameconfiguration)" : {{ReplicationTopicNameConfiguration}},
  "[TopicsToExclude](#cfn-msk-replicator-topicreplication-topicstoexclude)" : {{[ String, ... ]}},
  "[TopicsToReplicate](#cfn-msk-replicator-topicreplication-topicstoreplicate)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-msk-replicator-topicreplication-syntax.yaml"></a>

```
  [CopyAccessControlListsForTopics](#cfn-msk-replicator-topicreplication-copyaccesscontrollistsfortopics): {{Boolean}}
  [CopyTopicConfigurations](#cfn-msk-replicator-topicreplication-copytopicconfigurations): {{Boolean}}
  [DetectAndCopyNewTopics](#cfn-msk-replicator-topicreplication-detectandcopynewtopics): {{Boolean}}
  [StartingPosition](#cfn-msk-replicator-topicreplication-startingposition): {{
    ReplicationStartingPosition}}
  [TopicNameConfiguration](#cfn-msk-replicator-topicreplication-topicnameconfiguration): {{
    ReplicationTopicNameConfiguration}}
  [TopicsToExclude](#cfn-msk-replicator-topicreplication-topicstoexclude): {{
    - String}}
  [TopicsToReplicate](#cfn-msk-replicator-topicreplication-topicstoreplicate): {{
    - String}}
```

## Properties
<a name="aws-properties-msk-replicator-topicreplication-properties"></a>

`CopyAccessControlListsForTopics`  <a name="cfn-msk-replicator-topicreplication-copyaccesscontrollistsfortopics"></a>
Whether to periodically configure remote topic ACLs to match their corresponding upstream topics.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CopyTopicConfigurations`  <a name="cfn-msk-replicator-topicreplication-copytopicconfigurations"></a>
Whether to periodically configure remote topics to match their corresponding upstream topics.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DetectAndCopyNewTopics`  <a name="cfn-msk-replicator-topicreplication-detectandcopynewtopics"></a>
Whether to periodically check for new topics and partitions.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartingPosition`  <a name="cfn-msk-replicator-topicreplication-startingposition"></a>
Specifies the position in the topics to start replicating from.
*Required*: No
*Type*: [ReplicationStartingPosition](aws-properties-msk-replicator-replicationstartingposition.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TopicNameConfiguration`  <a name="cfn-msk-replicator-topicreplication-topicnameconfiguration"></a>
Configuration for specifying replicated topic names will be the same as their corresponding upstream topics or prefixed with source cluster alias.
*Required*: No
*Type*: [ReplicationTopicNameConfiguration](aws-properties-msk-replicator-replicationtopicnameconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TopicsToExclude`  <a name="cfn-msk-replicator-topicreplication-topicstoexclude"></a>
List of regular expression patterns indicating the topics that should not be replicated.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `249 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicsToReplicate`  <a name="cfn-msk-replicator-topicreplication-topicstoreplicate"></a>
List of regular expression patterns indicating the topics to copy.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `249 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
