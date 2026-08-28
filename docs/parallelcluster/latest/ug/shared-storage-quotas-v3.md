---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/shared-storage-quotas-v3.html
---

# Quotas for shared storage
<a name="shared-storage-quotas-v3"></a>

Configure cluster `SharedStorage` to mount existing shared file storage and create new shared file storage based on the quotas that are listed in the following table.

**The mounted file storage quotas for each cluster**

| File shared storage type | AWS ParallelCluster managed storage | External storage | Quota net total |
| --- | --- | --- | --- |
| Amazon EBS | 5 | 5 | 5 |
| RAID | 1 | 0 | 1 |
| Amazon EFS | 1 | 20 | 21 |
| Amazon FSx † | 1 FSx for Lustre | 20 | 21 |

**Note**
This table of quotas is added in AWS ParallelCluster version 3.2.0.

† AWS ParallelCluster only supports mounting existing Amazon FSx for NetApp ONTAP, Amazon FSx for OpenZFS, and File Cache systems. It doesn't support the creation of new FSx for ONTAP, FSx for OpenZFS, and File Cache systems.

**Note**
If you use AWS Batch as a scheduler, FSx for Lustre is only available on the cluster head node.
File Caches don't support AWS Batch schedulers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
