---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-perms-consumer-group-sync.html
---

# Consumer group offset sync permissions
<a name="msk-replicator-perms-consumer-group-sync"></a>

When `synchroniseConsumerGroupOffsets` is enabled (the default), the replicator translates consumer group offsets from the source cluster and writes them to the target cluster. With this feature enabled, consumers can resume from the correct position after failover.

Two sync modes are available: `LEGACY` (the default) and `ENHANCED`. In LEGACY mode, the replicator syncs offsets when producers write to the source cluster. In ENHANCED mode, the replicator syncs offsets regardless of where producers write. ENHANCED mode requires bidirectional replication. Both modes use the same IAM permissions.

**Note**
The internal topics that ENHANCED mode depends on (`mskr-offset-syncs.*` and `*.checkpoints.internal`) are already covered by the topic replication permissions on both clusters.

The following statements add permissions specifically for consumer group offset sync. Because offset syncing depends on data replication, some permissions overlap with the topic replication policy.

## Service execution role IAM policy (MSK clusters)
<a name="msk-replicator-perms-consumer-group-sync-iam"></a>

**Source cluster**
The service execution role must have permission to describe consumer groups and the topics they consume on the source.

```
[
    {
        "Sid": "SourceGroupPermissions",
        "Effect": "Allow",
        "Action": [
            "kafka-cluster:DescribeGroup"
        ],
        "Resource": [
            "arn:aws:kafka:${region}:${account}:group/${SourceClusterName}/${SourceClusterUUID}/${consumerGroupPattern}"
        ]
    },
    {
        "Sid": "SourceUserTopicPermissions",
        "Effect": "Allow",
        "Action": [
            "kafka-cluster:DescribeTopic"
        ],
        "Resource": [
            "arn:aws:kafka:${region}:${account}:topic/${SourceClusterName}/${SourceClusterUUID}/${topicsConsumedByGroup}"
        ]
    }
]
```

**Target cluster**
The service execution role must have permission to describe the replicated topics and alter consumer groups on the target so that translated offsets can be committed.

```
[
    {
        "Sid": "TargetCheckpointTopicPermissions",
        "Effect": "Allow",
        "Action": [
            "kafka-cluster:DescribeTopic"
        ],
        "Resource": [
            "arn:aws:kafka:${region}:${account}:topic/${TargetClusterName}/${TargetClusterUUID}/${replicatedTopicPattern}"
        ]
    },
    {
        "Sid": "TargetCheckpointGroupPermissions",
        "Effect": "Allow",
        "Action": [
            "kafka-cluster:AlterGroup",
            "kafka-cluster:DescribeGroup"
        ],
        "Resource": [
            "arn:aws:kafka:${region}:${account}:group/${TargetClusterName}/${TargetClusterUUID}/${consumerGroupPattern}"
        ]
    }
]
```

Replace the placeholders in the preceding statements as follows:
+ Replace `${consumerGroupPattern}` with the consumer group name or pattern configured for replication (for example, `my-app-group-*`).
+ Replace `${topicsConsumedByGroup}` with the topic pattern that the consumer groups read from on the source.
+ Replace `${replicatedTopicPattern}` with the corresponding replicated topic pattern on the target (`*.${topicPattern}` for PREFIXED naming, or `${topicPattern}` for IDENTICAL naming).

## Kafka ACLs (non-MSK clusters)
<a name="msk-replicator-perms-consumer-group-sync-acls"></a>

**Non-MSK as source**
When the source is a non-MSK cluster, consumer group offset sync requires the following ACLs.

| Resource | Type | Pattern type | Operation | Purpose |
| --- | --- | --- | --- | --- |
| `${consumerGroupPattern}` | Group | LITERAL or PREFIXED | Describe | Read committed offsets (OffsetFetch) |
| `${topicsConsumedByGroup}` | Topic | LITERAL or PREFIXED | Describe | Topic metadata for offset translation |

**Non-MSK as target**
When the target is a non-MSK cluster, consumer group offset sync requires the following ACLs.

| Resource | Type | Pattern type | Operation | Purpose |
| --- | --- | --- | --- | --- |
| `${replicatedTopicPattern}` | Topic | LITERAL or PREFIXED | Describe | Log end offset (ListOffsets) |
| `${consumerGroupPattern}` | Group | LITERAL or PREFIXED | Describe | FindCoordinator, DescribeGroup |
| `${consumerGroupPattern}` | Group | LITERAL or PREFIXED | Read | Commit translated offsets (OffsetCommit) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
