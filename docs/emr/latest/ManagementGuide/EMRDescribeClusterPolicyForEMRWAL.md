---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/EMRDescribeClusterPolicyForEMRWAL.html
---

# AWS managed policy: EMRDescribeClusterPolicyForEMRWAL
<a name="EMRDescribeClusterPolicyForEMRWAL"></a>

You can't attach `EMRDescribeClusterPolicyForEMRWAL` to your IAM entities. This policy is attached to a service-linked role that allows Amazon EMR to perform actions on your behalf. For more information on this service-linked role, see [Using service-linked roles with Amazon EMR for write-ahead logging](using-service-linked-roles-wal.md).

This policy grants read-only permissions that allow the WAL service for Amazon EMR to find and return the status of a cluster. For more information about Amazon EMR WAL, see [Write-ahead logs (WAL) for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase-wal.html).

**Permissions details**

This policy includes the following permissions:
+ `emr` – Allows principals to describe cluster status from Amazon EMR. This is required so that Amazon EMR can confirm when a cluster has terminated and then, after thirty days, clean up any WAL logs left behind by the cluster.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "elasticmapreduce:DescribeCluster"
      ],
      "Resource": [
        "*"
      ],
      "Sid": "AllowELASTICMAPREDUCEDescribecluster"
    }
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
