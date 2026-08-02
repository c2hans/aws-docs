---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/amazon-s3-replication-role-actions.html
---

# Amazon S3 replication role actions
<a name="amazon-s3-replication-role-actions"></a>

The IAM role used to perform the replication needs to have the following actions:

|  |
| --- |
| s3:ReplicateObject |
| s3:ReplicateDelete |
| s3:ReplicateTags |
| s3:ObjectOwnerOverrideToBucketOwner |
| s3:ListBucket |
| s3:GetReplicationConfiguration |
| s3:GetObjectVersionForReplication |
| s3:GetObjectVersionAcl |
| s3:GetObjectVersionTagging |
| s3:GetObjectRetention |
| s3:GetObjectLegalHold |

To verify the role has the replication role actions:

1. Copy the name of the role name in the [S3 Replication wizard](set-up-the-cost-feature.md).

1. Sign in to the [IAM Console](https://console.aws.amazon.com/iam) within the account you are setting up the replication in.

1. Paste the name of the role into the **Search IAM** box.

1. Select the top item from the list. This is the IAM role that will be used.

1. Under **Permissions policies**, expand the **Managed policy**.

1. Ensure that the policy has the actions detailed in the preceding table.
