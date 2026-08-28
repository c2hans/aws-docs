---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-perms-acl-replication.html
---

# ACL replication permissions
<a name="msk-replicator-perms-acl-replication"></a>

When `copyAccessControlListsForTopics` is enabled (the default), the replicator copies access control lists from the source cluster to the target cluster. Consumers on the target can then use the same authorization configuration.

## Service execution role IAM policy (MSK clusters)
<a name="msk-replicator-perms-acl-replication-iam"></a>

**Source cluster**
The service execution role must have permission to read ACLs from the source cluster.

```
{
    "Sid": "SourceAclReadPermissions",
    "Effect": "Allow",
    "Action": [
        "kafka-cluster:Connect",
        "kafka-cluster:DescribeCluster"
    ],
    "Resource": [
        "arn:aws:kafka:${region}:${account}:cluster/${SourceClusterName}/${SourceClusterUUID}"
    ]
}
```

**Target cluster**
The service execution role must have permission to write ACLs to the target cluster.

```
{
    "Sid": "TargetAclWritePermissions",
    "Effect": "Allow",
    "Action": [
        "kafka-cluster:Connect",
        "kafka-cluster:DescribeCluster",
        "kafka-cluster:AlterCluster"
    ],
    "Resource": [
        "arn:aws:kafka:${region}:${account}:cluster/${TargetClusterName}/${TargetClusterUUID}"
    ]
}
```

## Kafka ACLs (non-MSK clusters)
<a name="msk-replicator-perms-acl-replication-acls"></a>

**Non-MSK as source**
The replicator must have permission to describe ACLs on the source cluster.

| Resource type | Pattern | Operations |
| --- | --- | --- |
| Cluster | `kafka-cluster` (LITERAL) | Describe |

**Non-MSK as target**
The replicator must have permission to alter ACLs on the target cluster.

| Resource type | Pattern | Operations |
| --- | --- | --- |
| Cluster | `kafka-cluster` (LITERAL) | Alter |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
